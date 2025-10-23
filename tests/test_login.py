from tests.baseActions.usuario_acciones import AccionesUsuario
import time

def test_login(driver):
    """Caso de prueba: Login exitoso con credenciales válidas.
    Verífica que el usuario pueda iniciar sesión y sea redirigido a la página de inventario.
    """
    try:
        usuario = AccionesUsuario(driver)
        usuario.loguear_usuario(driver)
        assert "/inventory.html" in driver.current_url, "No fue redirigido a inventory.html"
        print("Podemos ver /inventory.html")

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()
