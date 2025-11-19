from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.objects.register import Register



class CartPage:
    def __init__(self, driver, ):
        self.driver = driver
        self.Register = Register
        self.wait = WebDriverWait(driver, 10)

    def obtener_nombre_carrito(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self.Register.inventory_item))
    #    productos = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator)
        return  productos

    def algo(self):
        pass





