from tests.objects.register import Register
import time

def test_titulo(driver):
    """Caso de prueba: Verificar el título de la página de inicio sea correcto
    No es necesario loguear al usuario."""
    try:
        driver.get(Register.url_web)  # SOLO ABRIMOS LA WEB

        assert driver.title   == Register.pagina_titulo      #Comprobamos el título de la página.
        print("Titulo es correcto:", driver.title)
        time.sleep(2)

    finally:
        driver.quit()