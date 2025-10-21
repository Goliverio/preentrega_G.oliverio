from tests.baseActions.usuario_acciones import AccionesUsuario
import time


def test_titulo(driver):
    try:
        usuario = AccionesUsuario(driver)
        usuario.abrir_web(driver)

        assert driver.title == "Swag Labs"
        print("Titulo es correcto:", driver.title)
        time.sleep(2)

    finally:
        driver.quit()