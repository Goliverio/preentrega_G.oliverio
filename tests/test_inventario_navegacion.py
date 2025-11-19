import pytest

from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register

#@pytest.mark.parametrize("usuario, contrasena")
def test_inventario_navegacion(driver):
    """Caso de prueba: Una vez realizado el login comprobamos la existencia ve
    varios elementos en la sección del inventario:
    1. Que se muestre algun producto.
    2. Que el nombre y precio del producto no este vacío.
    3. Que el menu principal sea visible.
    4. Que exista un filtro para ordenar los productos"""
    try:

        usuario = AccionesUsuario(driver)
        usuario.loguear_usuario(driver)

#   Nos fijamos que se muestre al menos 1 producto
        productos = driver.find_elements(*Register.userRegisteredLanding)
        assert 0 < len(productos)
        print(f'Se encontraron {len(productos)} productos.')

#   comprobamos que el nombre y el precio del primer producto no estén vacíos
        nombre_producto = productos[0].find_element(*Register.inventory_name).text
        precio_producto = productos[0].find_element(*Register.inventory_price).text
        assert nombre_producto and precio_producto, "Los datos de los artículos no están completos"
        print(f"Nombre del primer producto: {nombre_producto} \nSu precio es: {precio_producto}")

#   verificamos la existencia del menu principal
        assert usuario.ver_elemento(Register.inventory_menu), "No se muestra el menu principal"
        print("se expande el menu principal")

#   verificamos que exista un filtro para ordenar los productos
        assert usuario.ver_elemento(Register.inventory_filter), "No se encuentra ningún filtro para ordenar los artículos"
        print("Existen filtros para el listado de productos")

    except Exception as e:
        print(f"Error en test_inventory_navegacion: {e} \n")
        raise  RuntimeError("No se pudo cargar el inventario") from e
    finally:
        driver.quit()

