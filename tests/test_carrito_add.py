from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register
import pytest
from utils.logger import logger

from tests.baseActions.inventory_page import InventoryPage


@pytest.mark.Medium
def test_carrito(driver):
    """Caso de prueba: Verificar que el contador el carrito se incremente al
    agregar un producto. Navegar el carrito y verificar que el producto
    agregado sea el correcto"""

    inventory_page = InventoryPage(driver)

    try:
        usuario = AccionesUsuario(driver)
        usuario.logout_user()
        logger.info("hicimos el logout para limpiar la sesión")
        usuario.loguear_usuario(driver)

        productos = driver.find_elements(*Register.inventory_item)

        if len(productos)> 0:

            logger.info("--------------------------------------------")
            logger.info(f"Se encontraron {len(productos)} productos")

    #   leer el nombre del último item de la lista y agregarlo al carrito

            nombre_producto = productos[len(productos)-1].find_element(*Register.inventory_name).text
            inventory_page.agregar_producto_por_nombre(nombre_producto)

    #   Verificar que el contador del carrito se incremente
            logger.info("COMPROBANDO El CONTADOR DEL CARRITO")
            badge = driver.find_element(*Register.carrito_icono).text
            assert badge == '1' , logger.error("El contador no muestra los datos")
            logger.info(f"El carrito tiene {badge} items. se actualizo correctamente!")

    #   navegar el carrito y ver que se agregó bien el producto seleccionado
            logger.info("VERIFICANDO QUE LOS DATOS DEL CARRITO SEAN CORRECTOS")
            logger.info(nombre_producto)
            nombre_producto_carrito = inventory_page.abrir_carrito_ver_elemento()
            logger.info(nombre_producto_carrito)

            assert nombre_producto == nombre_producto_carrito, \
                logger.error("El nombre del producto no se corresponde")

            logger.info(f"Se agrego correctamente  {nombre_producto}")

        else:
            logger.error("No se encontraron productos en el listado")

    except Exception as e:
        logger.error(f"Error al agregar el producto: ")
        raise  RuntimeError("No se pudo cargar el inventario") from e
    finally:
        inventory_page.vaciar_elementos_carrito()    #limpiamos el carrito de basura


