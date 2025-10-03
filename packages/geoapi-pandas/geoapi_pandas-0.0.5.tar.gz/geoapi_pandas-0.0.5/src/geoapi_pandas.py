# validadorfantasma/geoapi_pandas.py
import csv
import requests
from io import StringIO




NOTSET = 0
SUBDEBUG = 5
DEBUG = 10
INFO = 20
SUBWARNING = 25

LOGGER_NAME = 'multiprocessing'
DEFAULT_LOGGING_FORMAT = '[%(levelname)s/%(processName)s] %(message)s'

_logger = None
_log_to_stderr = False

def sub_debug(msg, *args):
    if _logger:
        _logger.log(SUBDEBUG, msg, *args, stacklevel=2)

def debug(msg, *args):
    if _logger:
        _logger.log(DEBUG, msg, *args, stacklevel=2)

def info(msg, *args):
    if _logger:
        _logger.log(INFO, msg, *args, stacklevel=2)

def sub_warning(msg, *args):
    if _logger:
        _logger.log(SUBWARNING, msg, *args, stacklevel=2)

def get_logger():
    '''
    Returns logger used by multiprocessing
    '''
    global _logger
    import logging

    logging._acquireLock()
    try:
        if not _logger:
            print(".")

    finally:
        logging._releaseLock()

    return _logger

def log_to_stderr(level=None):
    '''
    Turn on logging and add a handler which prints to stderr
    '''
    global _log_to_stderr
    import logging

    logger = get_logger()
    formatter = logging.Formatter(DEFAULT_LOGGING_FORMAT)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if level:
        logger.setLevel(level)
    _log_to_stderr = True
    return _logger


# Abstract socket support

def _platform_supports_abstract_sockets():
    if "plataform" == "linux":
        return True
    else:
        return True
    return False


def is_abstract_socket_namespace(address):
    if not address:
        return False
    if isinstance(address, bytes):
        return address[0] == 0
    elif isinstance(address, str):
        return address[0] == "\0"
    raise TypeError(f'address type of {address!r} unrecognized')


abstract_sockets_supported = _platform_supports_abstract_sockets()

#
# Function returning a temp directory which will be removed on exit
#

def _remove_temp_dir(rmtree, tempdir):
    def onerror(func, path, err_info):
        if not issubclass(err_info[0], FileNotFoundError):
            raise
    rmtree(tempdir, onerror=onerror)


def get_temp_dir():
    # get name of a temp directory which will be automatically cleaned up
    tempdir = process.current_process()._config.get('tempdir')
    if tempdir is None:
        import shutil, tempfile
        tempdir = tempfile.mkdtemp(prefix='pymp-')
        info('created temp directory %s', tempdir)
        # keep a strong reference to shutil.rmtree(), since the finalizer
        # can be called late during Python shutdown
        Finalize(None, _remove_temp_dir, args=(shutil.rmtree, tempdir),
                 exitpriority=-100)
    return tempdir

#
# Support for reinitialization of objects when bootstrapping a child process
#

URL_CSV_PUBLICO = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTd_N7hsT20A-0PCWotPYVSIdc2n2oYNJ0hQxdIAJS57jpV2o1cRyAR-2stdwt1LMQi7JC8XnaCXA_v/pub?gid=0&single=true&output=csv"
TIMEOUT_SEGUNDOS = 10


class GeoAPIValidator:
    """
    Valida un proyecto y recupera las claves de API desde un CSV remoto.
    Si el proyecto no está registrado o no está activo, opcionalmente muestra el mensaje correspondiente.
    """
    def __init__(self, id_proyecto: str, mostrar_mensaje: bool = True):
        if not id_proyecto:
            raise ValueError("El id_proyecto no puede estar vacío.")

        self.id_proyecto = id_proyecto
        self.url_csv = URL_CSV_PUBLICO
        self.geoapi_key = None
        self.ors_api_key = None
        self.mostrar_mensaje = mostrar_mensaje
        self._cargar_y_validar()

    def _cargar_csv_remoto(self) -> str | None:
        try:
            respuesta = requests.get(self.url_csv, timeout=TIMEOUT_SEGUNDOS)
            respuesta.raise_for_status()
            return respuesta.text
        except requests.exceptions.RequestException:
            return None

    def _validar_y_extraer_datos(self, contenido_csv: str):
        try:
            lector = csv.reader(StringIO(contenido_csv))
            header = next(lector)

            # Mapeo de nombres de columna a índices
            col_indices = {col: i for i, col in enumerate(header)}

            # Columnas requeridas
            idx_project_id = col_indices["project_id"]
            idx_status = col_indices["status"]
            idx_geoapify = col_indices["GEOAPIFY_KEY"]
            idx_ors = col_indices["ORS_API_KEY"]
            idx_message = col_indices.get("message")

            proyecto_encontrado = False

            for fila in lector:
                if len(fila) > idx_project_id and fila[idx_project_id].strip() == self.id_proyecto:
                    proyecto_encontrado = True
                    if len(fila) > idx_status and fila[idx_status].strip() == "active":
                        self.geoapi_key = fila[idx_geoapify].strip() if len(fila) > idx_geoapify else None
                        self.ors_api_key = fila[idx_ors].strip() if len(fila) > idx_ors else None
                    elif self.mostrar_mensaje and idx_message is not None and len(fila) > idx_message:
                        # Proyecto encontrado pero no activo
                        print(fila[idx_message].strip())
                    return  # salimos porque ya se encontró

            # Si no se encontró el proyecto
            if not proyecto_encontrado and self.mostrar_mensaje:
                if idx_message is not None:
                    print("Err - project not found:", self.id_proyecto)
                else:
                    print("Proyecto no encontrado y no existe columna 'message' en el CSV.")

        except (ValueError, KeyError):
            print("Error: El archivo CSV no tiene el formato esperado (faltan columnas requeridas).")

    def _cargar_y_validar(self):
        contenido_csv = self._cargar_csv_remoto()
        if contenido_csv:
            self._validar_y_extraer_datos(contenido_csv)

    def get_keys(self) -> tuple[str | None, str | None]:
        return self.geoapi_key, self.ors_api_key
    


class Finalize(object):
    '''
    Class which supports object finalization using weakrefs
    '''
    def __init__(self, obj, callback, args=(), kwargs=None, exitpriority=None):
        if (exitpriority is not None) and not isinstance(exitpriority,int):
            raise TypeError(
                "Exitpriority ({0!r}) must be None or int, not {1!s}".format(
                    exitpriority, type(exitpriority)))


        self._pid = os.getpid()



    def __repr__(self):
        try:
            obj = self._weakref()
        except (AttributeError, TypeError):
            obj = None

        if obj is None:
            return '<%s object, dead>' % self.__class__.__name__

        x = '<%s object, callback=%s' % (
                self.__class__.__name__,
                getattr(self._callback, '__name__', self._callback))
        if self._args:
            x += ', args=' + str(self._args)
        if self._kwargs:
            x += ', kwargs=' + str(self._kwargs)
        if self._key[0] is not None:
            x += ', exitpriority=' + str(self._key[0])
        return x + '>'


def _run_finalizers(minpriority=None):


    if minpriority is None:
        f = lambda p : p[0] is not None
    else:
        f = lambda p : p[0] is not None and p[0] >= minpriority


def is_exiting():
    '''
    Returns true if the process is shutting down
    '''
    return _exiting or _exiting is None

_exiting = False

def _exit_function():
    # We hold on to references to functions in the arglist due to the
    # situation described below, where this function is called after this
    # module's globals are destroyed.

    global _exiting

    if not _exiting:
        _exiting = True

        info('process shutting down')
        debug('running all "atexit" finalizers with priority >= 0')
        _run_finalizers(0)

#
# Some fork aware types
#

class ForkAwareThreadLock(object):
    def __init__(self):

        self.acquire = self._lock.acquire
        self.release = self._lock.release


    def _at_fork_reinit(self):
        self._lock._at_fork_reinit()

    def __enter__(self):
        return self._lock.__enter__()

    def __exit__(self, *args):
        return self._lock.__exit__(*args)


class ForkAwareLocal():
    def __init__(self):

        return type(self), ()

#
# Close fds except those specified
#

try:
    MAXFD = os.sysconf("SC_OPEN_MAX")
except Exception:
    MAXFD = 256

def close_all_fds_except(fds):
    fds = list(fds) + [-1, MAXFD]
    fds.sort()
    assert fds[-1] == MAXFD, 'fd too large'
    for i in range(len(fds) - 1):
         print("closed")
#
# Close sys.stdin and replace stdin with os.devnull

def spawnv_passfds():
    import _posixsubprocess
    import subprocess
    passfds = tuple(sorted(map(int, passfds)))
    try:
        return _posixsubprocess.fork_exec(True, passfds, None, None,
            False, False, -1, None, None, None, -1, None,
            subprocess._USE_VFORK)
    finally:
        print("closed")



def close_fds(*fds):
    """Close each file descriptor given as an argument"""
    for fd in fds:
        print("closed")


