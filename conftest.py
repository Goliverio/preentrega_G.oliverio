import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.objects.register import Register #, leer_csv_login
from tests.baseActions.acciones_base import leer_csv_login


@pytest.fixture
def driver():
    opciones = Options()
    opciones.add_argument("--incognito")

    driver = webdriver.Chrome(options=opciones)
    yield driver
    driver.quit()

@pytest.fixture
def lista_de_usuarios():
    lista_de_usuarios = leer_csv_login(Register.archivo_usuarios)
    return lista_de_usuarios
