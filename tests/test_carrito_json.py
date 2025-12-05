
from tests.baseActions.inventory_page import InventoryPage
from tests.baseActions.usuario_acciones import AccionesUsuario
import pytest
from utils.lector_json import leer_json_productos
from utils.logger import logger


RUTA_JSON = "tests/objects/productos.json"

@pytest.mark.JSON
@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",leer_json_productos(RUTA_JSON))
def test_carrito_json(driver, usuario, password, nombre_producto ):
    """Caso de prueba: Verificar que el contador el carrito se incremente al
    agregar un producto. Navegar el carrito y verificar que el producto
    agregado sea el correcto - Utilizando JSON"""
    logger.info("--------------------------------------------")
    logger.info(f"Prueba para el producto {nombre_producto}")

    nombre = nombre_producto
    try:
        user = AccionesUsuario(driver)
        user.loguear_usuario(driver)
        inventory_page = InventoryPage(driver)

        # Agregar el producto al carrito
        inventory_page.agregar_producto_por_nombre(nombre_producto)

        # Abrir el carrito y validamos que el producto agregado sea el correcto
        nombre_producto_carrito = inventory_page.abrir_carrito_ver_elemento()
        assert nombre_producto == nombre_producto_carrito
        logger.info("Se agrego correctamente el producto")
        inventory_page.vaciar_elementos_carrito()  #Limpiamos el carrito para no dejar basura

    except Exception as e:
        logger.error(f"Error en test_carrito_json: {e}")
        raise
    finally:
        pass


