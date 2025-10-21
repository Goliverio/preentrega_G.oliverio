from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register


def test_carrito(driver):
    try:
        usuario = AccionesUsuario(driver)
        usuario.abrir_web(driver)
        usuario.validar_usuario()
        usuario.usuario_logged()


        productos = driver.find_elements(*Register.inventory_item)

        if len(productos)> 0:
            print(f'\nSe encontraron {len(productos)} productos. ')

    #   leer el nombre del último item de la lista y agregarlo al carrito

            nombre_producto = productos[len(productos)-1].find_element(*Register.inventory_name).text
            productos[len(productos)-1].find_element(*Register.inventory_add_button).click()

    #   Verificar que el contador del carrito se incremente

            badge = driver.find_element(*Register.carrito_icono).text
            assert badge == '1'
            print(f"El carrito tiene {badge} items. se incrementa correctamente!")


    #   navegar el carrito y ver que se agregó bien el producto seleccionado
            usuario.click_elemento(Register.carrito_add_item)

            assert nombre_producto == driver.find_element(*Register.inventory_name).text
            print("Se agrego correctamente ", nombre_producto)

        else:
            print("No se encontraron productos en el listado")

    except Exception as e:
        print(f"Error al agregar el producto: {e} \n")
        raise # RuntimeError("No se pudo cargar el inventario") from e
    finally:
        driver.quit()


