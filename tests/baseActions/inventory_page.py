import time

from tests.objects.register import Register
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import logger


class InventoryPage:
    def __init__(self, driver, ):
        self.wait = None
        self.driver = driver
        self.Register = Register
        self.wait = WebDriverWait(driver, 10)

    def agregar_producto_por_nombre( self, nombre_producto):
        productos = self.driver.find_elements(*self.Register.inventory_item)

        for producto in productos:
            nombre = producto.find_element(*self.Register.inventory_name).text
            if  nombre.strip() == nombre_producto.strip():
                boton = producto.find_element(*self.Register.inventory_add_button)
                boton.click()
                logger.info("Agregando al carrito a:")
                logger.info(f"{nombre} ")
                return self
        raise Exception(f"No se encontro el producto {nombre_producto}")



    def abrir_carrito_ver_elemento(self):
        self.wait.until(EC.element_to_be_clickable(self.Register.carrito_add_item)).click()
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self.Register.inventory_name))
        return nombre_producto.text



    def vaciar_elementos_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self.Register.carrito_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.Register.carrito_reset)).click()
        # time.sleep(2)
