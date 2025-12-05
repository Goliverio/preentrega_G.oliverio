from tests.baseActions.usuario_acciones import AccionesUsuario
import pytest
from tests.baseActions.acciones_base import leer_csv_login
from tests.objects.register import Register
from utils.logger import logger


@pytest.mark.High
@pytest.mark.parametrize("nom_u, pass_u,debe_funcionar",leer_csv_login(Register.archivo_usuarios))
def test_login(nom_u, pass_u, debe_funcionar, driver):
    """Caso de Prueba: Testeo de login de usuarios.
        Los usuarios se leen desde un archivo CSV con el tipo de credencial que posee
    """
    usuario = AccionesUsuario(driver)
    Register.user_name = nom_u
    Register.password = pass_u

    logger.info("--------------------------------------------")

    if debe_funcionar:
        try:
            usuario.loguear_usuario(driver)
            assert Register.url_inventory in driver.current_url, \
                        logger.error("No fue redirigido a inventory.html")
            logger.info(f"Podemos ver {Register.url_inventory}")

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
            logger.error("El mensaje de error no se esta mostrando")
