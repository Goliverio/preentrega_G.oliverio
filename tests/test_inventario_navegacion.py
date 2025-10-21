from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register


def test_inventario_navegacion(driver):
    try:

        usuario = AccionesUsuario(driver)
        usuario.abrir_web(driver)
        usuario.validar_usuario()
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        print("Login exitoso y validado correctamente!")


#   comprobamos el título
        titulo = driver.find_element(*Register.inventory_container).text
        assert titulo == "Products"
        print("Titulo de sección OK : ", titulo)


#   Nos fijamos que se muestre al menos 1 producto
        productos = driver.find_elements(*Register.userRegisteredLanding)
        assert 0 < len(productos)
        print(f'Se encontraron {len(productos)} productos.')

#   comprobamos que el nombre y el precio del primer producto no estén vacíos
        nombre_producto = productos[0].find_element(*Register.inventory_name).text
        precio_producto = productos[0].find_element(*Register.inventory_price).text
        assert nombre_producto and precio_producto
        print(f"Nombre del primer producto: {nombre_producto} \nSu precio es: {precio_producto}")


#   verificamos la existencia del menu principal
        assert driver.find_element(*Register.inventory_menu)
        print("se expande el menu principal")


#   verificamos que exista un filtro para ordenar los productos
        assert driver.find_element(*Register.inventory_filter)
        print("Existen filtros para el listado de productos")


    except Exception as e:
        print(f"Error en Test_login: {e} \n")
        raise # RuntimeError("No se pudo cargar el inventario") from e
    finally:
        driver.quit()

