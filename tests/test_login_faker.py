from tests.baseActions.usuario_acciones import AccionesUsuario
import pytest
from tests.objects.register import Register
from faker import Faker
from utils.logger import logger


#inicializamos faker

faker =Faker()

@pytest.mark.parametrize("nom_u, pass_u,debe_funcionar",[
    (faker.user_name(), faker.password(), False),
    (faker.user_name(), faker.password(), False),
])
@pytest.mark.Medium
def test_login_faker(nom_u, pass_u, debe_funcionar, driver):
    """Caso de Prueba: Testeo de login de usuarios con credenciales inválidas utilizando FAKER."""
    usuario = AccionesUsuario(driver)
    Register.user_name = nom_u
    Register.password = pass_u

    logger.info("--------------------------------------------")
    logger.info(f"[{nom_u} - {pass_u}]")

    if debe_funcionar:
        try:
            logger.info("VERIFICANDO QUE EL USUARIO SEA REDIRIGIDO CORRECTAMENTE")

            usuario.loguear_usuario(driver)
            assert Register.url_inventory in driver.current_url, \
                    logger.error(f"No fue redirigido a {Register.url_inventory}")
            logger.info("Podemos ver " + Register.url_inventory)

        except Exception as e:
            logger.error(f"Error en test_login: {e}")
            raise
        finally:
            pass
    elif not debe_funcionar:
        usuario.abrir_web()
        usuario.validar_usuario()
        mensaje_error = usuario.obtener_error_login(Register.msgError)
        logger.info(mensaje_error)
        assert "Epic sadface" in mensaje_error, \
            logger.error("El mensaje de error no se muestra")

