from tests.baseActions.acciones_base import AccionesBase
from tests.objects.register import Register
from utils.logger import logger


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
        logger.info(f"Validando usuario")
        self.click_para_ingresar()

    def abrir_web(self):
        self.load(Register.url_web)
        logger.info("Cargando la WEB")

    def loguear_usuario(self, driver):
        try:
            self.abrir_web()
            self.validar_usuario()
        except Exception as e:
            logger.error(f"Error en login: {e} \n")
            raise   RuntimeError("No se pudo loguear al usuario") from e
        finally:
            pass

    def logout_user(self):
        try:
            #self._esperar_por_elemento(Register.carrito_menu)
            self.ver_elemento(Register.inventory_menu)
            self.click_elemento(Register.logout_page)
        except Exception as e:
            logger.error(f"No se puede hacer el logout {e}")
            raise RuntimeError("No se puede hacer el logout") from e
        finally:
            pass
