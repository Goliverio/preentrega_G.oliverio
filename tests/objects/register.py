from selenium.webdriver.common.by import By


class Register:
    url_web = "https://www.saucedemo.com"
    url_inventory = "/inventory.html"
    user_name = "standard_user"
    password = "secret_sauce"
    userInput = (By.ID, "user-name")
    passInput = (By.ID, "password")
    registerButton = (By.ID, "login-button")
    userRegisteredLanding = (By.CLASS_NAME, "inventory_item")


    ####  PARAR EL INVETARIO

    inventory_title = (By.CSS_SELECTOR,'div.header_secondary_container .title')
    inventory_container = [By.CSS_SELECTOR, 'div.header_secondary_container .title']
    inventory_name = (By.CLASS_NAME, "inventory_item_name")
    inventory_price = (By.CLASS_NAME, "inventory_item_price")
    inventory_menu = (By.CLASS_NAME, "bm-menu")
    inventory_filter = (By.CLASS_NAME, "product_sort_container")


    ####### PARA EL CARRITO

    inventory_item = (By.CLASS_NAME, "inventory_item")
    inventory_add_button = (By.TAG_NAME, "button")
    carrito_icono = (By.CLASS_NAME, "shopping_cart_badge")
    carrito_add_item = (By.CLASS_NAME, "shopping_cart_link")
