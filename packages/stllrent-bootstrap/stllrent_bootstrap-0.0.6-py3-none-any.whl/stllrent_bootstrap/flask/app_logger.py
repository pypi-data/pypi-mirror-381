import logging
import sys
from stllrent_bootstrap.flask.app_settings import BaseAppSettings
from pydantic_settings import BaseSettings
from pythonjsonlogger import jsonlogger

# Variável no escopo do módulo para armazenar o nome do logger principal.
_LOGGER_NAME = None

def configure_logging(settings_instance: BaseSettings):
    """
    Configures the main application logger with JSON output,
    separating logs to stdout and stderr.
    """
    global _LOGGER_NAME
    app_logger_name = settings_instance.API_PRIMARY_PATH.replace("/", "_")
    main_app_logger = logging.getLogger(app_logger_name)

    # Limpar handlers existentes para evitar duplicação
    if main_app_logger.handlers:
        for handler in list(main_app_logger.handlers):
            main_app_logger.removeHandler(handler)
            if hasattr(handler, 'close'):
                handler.close()

    main_app_logger.setLevel(settings_instance.APP_LOG_LEVEL)
    main_app_logger.propagate = False

    _LOGGER_NAME = app_logger_name

    # --- Configurar o JsonFormatter ---
    # Este formatador será usado para ambas as saídas (stdout e stderr)
    json_formatter = jsonlogger.JsonFormatter(
        '%(funcName)s %(lineno)d %(levelname)s %(name)s %(message)s'
    )
    
    # --- Configurar Handlers com separação de saída ---

    # 1. Handler para STDOUT (INFO e WARNING)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(settings_instance.APP_LOG_LEVEL)  # Nível mínimo
    stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
    stdout_handler.setFormatter(json_formatter)
    main_app_logger.addHandler(stdout_handler)

    # 2. Handler para STDERR (ERROR e CRITICAL)
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)  # Nível mínimo
    stderr_handler.addFilter(lambda record: record.levelno >= logging.ERROR)
    stderr_handler.setFormatter(json_formatter)
    main_app_logger.addHandler(stderr_handler)

    # Configurar loggers para bibliotecas de terceiros como 'requests'
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    
    urllib3_log = logging.getLogger("urllib3")
    urllib3_log.setLevel(logging.DEBUG)
    urllib3_log.propagate = True

    # Mensagem de configuração em JSON
    main_app_logger.info("Application logger successfully configured.", extra={
        "logger_name": app_logger_name,
        "log_level": settings_instance.APP_LOG_LEVEL,
        "status": "success"
    })

def get_logger():
    """ 
    Gera o logger já configurado para esta aplicação 
    """
    if _LOGGER_NAME is None:
        # Fallback de segurança: retorna um logger padrão se não configurado
        logging.basicConfig()
        return logging.getLogger("stllrent_bootstrap.unconfigured")

    return logging.getLogger(_LOGGER_NAME)