import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.objects.register import Register
from tests.baseActions.acciones_base import leer_csv_login
from utils.logger import logger
import os
import pathlib
import time


# Define la ruta donde guardar la captura (crea la carpeta 'screens' si no existe)
target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True)



@pytest.fixture(scope='session')
def driver():
    opciones = Options()
    opciones.add_argument("--incognito")

    #######################   Para GitHub   #####################
    opciones.add_argument("--no-sandbox")  #  github
    opciones.add_argument("--disable-gpu")
    #opciones.add_argument("--window-size=1920,1080")
    opciones.add_argument("--headless=new")   # github

    #############################################################

    driver = webdriver.Chrome(options=opciones)
    yield driver
    driver.quit()


@pytest.fixture
def lista_de_usuarios():
    lista_de_usuarios = leer_csv_login(Register.archivo_usuarios)
    return lista_de_usuarios


def pytest_configure(config):
    """
    Configuración que se ejecuta al iniciar pytest.
    """
    # Para que no de warning el marker JSON
    config.addinivalue_line("markers", "JSON: Test de relacionados a JSON.")

    # Crea el directorio para capturas de pantalla si no existe.
    if not os.path.exists(target):
        os.makedirs(target)
        logger.info(f"Directorio {target} creado.")



#    Hook wrapper para procesar el resultado de la prueba y tomar una captura si falla.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call ):
    # Ejecuta el resto de los hooks pytest_runtest_makereport
    outcome = yield
    report = outcome.get_result()

    # Verifica si la fase de 'call' (ejecución de la prueba) falló
    if report.when in ("setup", "call") and report.failed:
        # Intenta obtener la instancia del driver web del item de la prueba
        try:
            driver = item.funcargs.get("driver", None)

            if driver:
                # Crea un nombre de archivo único con la hora y el nombre de la prueba
                timestamp = time.strftime("%Y-%m-%d-%H_%M_%S")
                screenshot_path = target
                screenshot_filename = f"{item.name}_{timestamp}.png"
                driver.save_screenshot(f"{screenshot_path}/{screenshot_filename}")
                logger.info(f"Captura de pantalla guardada en: ")
                logger.info(f"{screenshot_path}/{screenshot_filename}")
            else:
                logger.error("Imposible conectarse con el WebDriver")

        except Exception as e:
            logger.error(f"Error al intentar tomar la captura de pantalla: {e}")
