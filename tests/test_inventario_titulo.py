from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register
import pytest
from utils.logger import logger


@pytest.mark.Low
def test_inventario_titulo(driver):
    """   Caso de prueba: Verífica que el título de la página sea correcto
    """
    try:
        usuario = AccionesUsuario(driver)
        usuario.loguear_usuario(driver)

        logger.info("--------------------------------------------")

        titulo = usuario.ver_elemento(Register.inventory_title).text
        assert titulo == "Products", logger.error("EL TITULO DE LA PAGINA INVENTARIO NO ES CORRECTO")
        logger.info(f"Titulo de sección OK:  {titulo}")

    except Exception as e:
        logger.error(f"Error en test_inventario_titulo: {e} \n")
        raise
    finally:
        pass


