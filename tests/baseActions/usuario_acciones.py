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

    def abrir_web(self):
        self.load(Register.url_web)
        print("Cargamos la web")

    def loguear_usuario(self, driver):
        try:
            self.abrir_web()
            self.validar_usuario()

            assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
            print("Login exitoso y validado correctamente!")

        except Exception as e:
            print(f"Error en Test_login: {e} \n")
            raise   RuntimeError("No se pudo cargar el inventario") from e
        finally:
            pass
#            driver.quit()







