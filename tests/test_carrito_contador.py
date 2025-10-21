from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register


def test_carrito_contador(driver):
    try:
        usuario = AccionesUsuario(driver)
        usuario.abrir_web(driver)
        usuario.validar_usuario()
        usuario.usuario_logged()

        productos = driver.find_elements(*Register.inventory_item)

        print(f'\nSe encontraron {len(productos)} productos.')

#   Agregamos al carrito el primer producto que encontramos
        productos[0].find_element(*Register.inventory_add_button).click()

#   Verificamos que el contador del carrito refleje el producto agregado.
        badge = driver.find_element(*Register.carrito_icono).text
        assert badge == '1'
        print(f"En el carrito hay {badge} producto")

    except Exception as e:
        print(f"Error en test_carrito_contador : {e} \n")
        raise
    finally:
        driver.quit()


