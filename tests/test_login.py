from tests.baseActions.usuario_acciones import AccionesUsuario
import time

def test_loging(driver):
    try:
        usuario = AccionesUsuario(driver)
        usuario.abrir_web(driver)
        usuario.validar_usuario()
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        print("Ingresamos correctamente!!")
        print("Podemos ver /inventory.html")
        time.sleep(4)

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        
        driver.quit()          # si esto se cierra me cierra el driver para siempre?
