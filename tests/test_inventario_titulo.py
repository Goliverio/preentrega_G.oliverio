from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register


def test_inventario_titulo(driver):
    """   Caso de prueba: Verífica que el título de la página sea correcto
    """
    try:
        usuario = AccionesUsuario(driver)
        usuario.loguear_usuario(driver)

        titulo = usuario.ver_elemento(Register.inventory_title).text
        assert titulo == "Products"
        print("Titulo de sección OK   ", titulo)

    except Exception as e:
        print(f"Error en test_inventario_titulo: {e} \n")
        raise
    finally:
        driver.quit()


