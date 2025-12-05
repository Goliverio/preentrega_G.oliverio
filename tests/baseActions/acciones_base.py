from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import pathlib
from utils.logger import logger



class AccionesBase:

    def __init__(self, driver):
        self.driver = driver
        pass

    def load(self, url):
        self.driver.get(url)

    def _esperar_por_elemento(self, by_locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(by_locator)
            )
            return self.driver.find_element(*by_locator)

        except TimeoutException:
            logger.info("No se encontró el elemento")
            return None

    def click_elemento(self, by_locator):
        usuario = self._esperar_por_elemento(by_locator)
        if usuario:
            usuario.click()
        else:
            raise Exception("No se puede hacer click en el elemento")

    def escribir_dato(self, by_locator, keyword):
        usuario = self._esperar_por_elemento(by_locator)
        if usuario:
            usuario.send_keys(keyword)
        else:
            raise Exception("No se puede encontrar en el elemento")

    def se_muestra(self, by_locator, ) -> bool:
        usuario = self._esperar_por_elemento(by_locator)
        if usuario:
            usuario.is_displayed()
            return True
        else:
            raise Exception("No se puede encontrar en el elemento")

    def es_activo(self, by_locator, ) -> bool:
        usuario = self._esperar_por_elemento(by_locator)
        if usuario:
            usuario.is_enabled()
            return  True
        else:
            raise Exception("No es accesible")


    def ver_elemento(self, by_locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(by_locator)
            )
            return self.driver.find_element(*by_locator)

        except TimeoutException:
            logger.info("No se encontró el elemento")
            return None

    def obtener_error_login(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(by_locator)
            )
            elemento = self.driver.find_element(*by_locator)
            return elemento.text
        except TimeoutException:
            logger.info("No se encontró el elemento. Pero para nada, nada!")
            return None


#
# Lee el archivo CVS con la lista de usuario
#
def leer_csv_login(ruta_archivo):
    """Lee el archivo CVS y devuelve los datos de cada usuario para tester

    Usage: leer_csv_login('Ruta_del_archivo')"""

    ruta = pathlib.Path(ruta_archivo)
    datos = []
    with open(ruta,newline='',encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            debe_funcionar = fila["debe_funcionar"].lower() == "true"
            datos.append((fila["usuario"], fila["password"], debe_funcionar))
    return datos
