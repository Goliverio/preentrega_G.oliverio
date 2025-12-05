import logging
import pathlib

## Configuración de logs para los distintos tests.


audit_dir = pathlib.Path('reports')  # Carpeta donde se guardara el log
audit_dir.mkdir(exist_ok=True)
log_file = audit_dir/ 'suite.log'    # archivo que contiene los logs

logger = logging.getLogger("msg")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(log_file,mode='a', encoding="utf-8")

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s | %(funcName)s : %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
