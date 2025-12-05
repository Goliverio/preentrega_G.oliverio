from tests.objects.register import Register
import pytest
from utils.logger import logger

@pytest.mark.Low
def test_titulo(driver):
    """Caso de prueba: Verificar el título de la página de inicio sea correcto
    No es necesario loguear al usuario."""
    logger.info("--------------------------------------------")
    logger.info(f"ABRIMOS LA WEB:  {Register.url_web}")
    try:
        driver.get(Register.url_web)  # SOLO ABRIMOS LA WEB

        # Comprobamos el título de la página.
        logger.info(f"COMPROBANDO QUE EL TITULO SEA {Register.pagina_titulo}")
        assert driver.title == Register.pagina_titulo, \
            logger.error("El titulo de la pagina no es correcto")
        logger.info(f"Titulo es correcto: {driver.title}")

    finally:
        pass
