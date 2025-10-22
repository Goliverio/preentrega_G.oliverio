from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
            print("No se encontró el elemento")
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
            print("No se encontró el elemento")
            return None
