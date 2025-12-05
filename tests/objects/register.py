from selenium.webdriver.common.by import By


class Register:
    url_web = "https://www.saucedemo.com"
    url_inventory = "/inventory.html"
    pagina_titulo = "Swag Labs"
    user_name = "standard_user"
    password = "secret_sauce"
    userInput = (By.ID, "user-name")
    passInput = (By.ID, "password")
    registerButton = (By.ID, "login-button")
    userRegisteredLanding = (By.CLASS_NAME, "inventory_item")
    msgError = (By.CSS_SELECTOR, ".error-message-container h3")
    logout_page = (By.ID, "logout_sidebar_link")

    ####  PARAR EL INVENTARIO

    inventory_title = (By.CSS_SELECTOR,'div.header_secondary_container .title')
    inventory_container = [By.CSS_SELECTOR, 'div.header_secondary_container .title']
    inventory_name = (By.CLASS_NAME, "inventory_item_name")
    inventory_price = (By.CLASS_NAME, "inventory_item_price")
    inventory_menu = (By.CLASS_NAME, "bm-menu")
    inventory_filter = (By.CLASS_NAME, "product_sort_container")


    ####### PARA EL CARRITO

    inventory_item = (By.CLASS_NAME, "inventory_item")
  #  inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
    inventory_add_button = (By.TAG_NAME, "button")
    inventory_add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
    carrito_icono = (By.CLASS_NAME, "shopping_cart_badge")
    carrito_add_item = (By.CLASS_NAME, "shopping_cart_link")
    carrito_item = (By.CLASS_NAME, "cart_item")
    carrito_reset = (By.ID, "reset_sidebar_link")
    carrito_menu = (By.ID, "react-burger-menu-btn")

    #################  Archivo de usuarios para login


    archivo_usuarios = "tests/objects/data_login.csv"
