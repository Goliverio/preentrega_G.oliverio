from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register
import pytest
from utils.logger import logger



@pytest.mark.Medium
def test_carrito_contador(driver):
    """Caso de prueba: Verificar que el contador el carrito se incremente al
    agregar un producto"""
    usuario = AccionesUsuario(driver)
    usuario.loguear_usuario(driver)

    try:

        productos = driver.find_elements(*Register.inventory_item)
        logger.info("--------------------------------------------")
        logger.info(f"Se encontraron {len(productos)} productos.")

        #   Agregamos al carrito el primer producto que encontramos
        logger.info("AGREGANDO EL PRIMER PRODUCTO ENCONTRADO")
        productos[0].find_element(*Register.inventory_add_button).click()

#   Verificamos que el contador del carrito refleje el producto agregado.
        logger.info(f"VERIFICANDO QUE EL CONTADOR SUME EL PRODUCTO AGREGADO")
        badge = driver.find_element(*Register.carrito_icono).text
        assert badge == '1' , logger.error("No se incrementa el contador del carrito")
        logger.info(f"En el carrito hay {badge} producto")


        # Abrimos el menu, buscamos el botón reset y hacemos click.
        # Esto es para resetear el carrito en caso que se necesite hacer otras pruebas
        driver.find_element(*Register.carrito_menu).click()
        if usuario.se_muestra(Register.carrito_reset):
            driver.find_element(*Register.carrito_reset).click()
        else:
            logger.error("No se puedo borrar los elementos el carrito")
            usuario.logout_user() # Salimos de la página para no dejar basura en el carrito.

    except Exception as e:
        logger.error(f"Error en test_carrito_contador : {e} \n")
        usuario.logout_user()
        raise
    finally:
        #usuario.logout_user()
        pass


