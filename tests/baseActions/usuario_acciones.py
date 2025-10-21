from tests.baseActions.acciones_base import AccionesBase
from tests.objects.register import Register


class AccionesUsuario(AccionesBase):

    def __init__(self, driver):
        super().__init__(driver)

    def escribir_user(self, user: str):
        self.escribir_dato(Register.userInput, user)

    def escribir_pass(self, password: str):
        self.escribir_dato(Register.passInput, password)


    def click_para_ingresar(self):
        self.click_elemento(Register.registerButton)

    def usuario_logged(self) -> bool:
        return self.se_muestra(Register.userRegisteredLanding)


    def validar_usuario(self):
        self.escribir_user(Register.user_name)
        self.escribir_pass(Register.password)
        print("Ya escribimos usuario y pass. Ahora seguimos con el click para ingresar")
        self.click_para_ingresar()


    @staticmethod
    def abrir_web(driver):
        usuario = AccionesUsuario(driver)
        usuario.load(Register.url_web)
        print("Cargamos la web")

########## orueba prar carrito
    #@staticmethod
    def ver_productos(self):
#        productos = self.ver_elemento(Register.inventory_item)
#        productos = se.find_elements(Register.inventory_item)
        print(self.ver_elemento(Register.inventory_item))

      #  return productos




