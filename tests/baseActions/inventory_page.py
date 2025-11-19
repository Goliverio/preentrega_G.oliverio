from tests.objects.register import Register
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest



class InventoryPage:
    def __init__(self, driver,):
        self.driver = driver
        self.Register = Register
        self.wait = WebDriverWait(driver, 10)

    def agregar_primer_producto(self):
        productos = self.wait.until(EC.visibility_of_element_located(self.Register.inventory_item))
        productos = self.driver

    def agregar_producto_por_nombre(self, nombre_producto):
        productos = self.obtener_todos_los_procutos()

        for producto in productos:
            nombre = producto.find_element(*self.Register.inventory_item)

            if nombre.strip().lower() == nombre.strip().lower()


    def abrir_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self.Register.inventory_add_to_cart_button))


    def obtener_conteo_carrito(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.Register.carrito_icono))
            contador_carrito = self.driver.find_element(self.Register.carrito_icono)
            return int(contador_carrito.text)
        except Exception as e:
            return 0

    def obtener_todos_los_procutos(self):
        pass