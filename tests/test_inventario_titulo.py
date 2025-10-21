from tests.baseActions.usuario_acciones import AccionesUsuario
from tests.objects.register import Register



def test_inventario_titulo(driver):
    try:
        usuario = AccionesUsuario(driver)
        usuario.abrir_web(driver)
        usuario.validar_usuario()

        titulo = usuario.ver_elemento(Register.inventory_title).text
        assert titulo == "Products"
        print("Titulo de sección OK   ", titulo)

    except Exception as e:
        print(f"Error en test_inventario_titulo: {e} \n")
        raise
    finally:
        driver.quit()


