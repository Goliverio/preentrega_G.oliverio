from tests.baseActions.usuario_acciones import AccionesUsuario
import pytest
from tests.objects.register import Register
from faker import Faker


#inicializamos faker

faker =Faker()

@pytest.mark.parametrize("nom_u, pass_u,debe_funcionar",[
    (faker.user_name(), faker.password(), False),
    (faker.user_name(), faker.password(), False),
])

def test_login_faker(nom_u, pass_u, debe_funcionar, driver):
    """Caso de Prueba: Testeo de login de usuarios con credenciales inválidas."""
    usuario = AccionesUsuario(driver)
    Register.user_name = nom_u
    Register.password = pass_u

    if debe_funcionar:
        try:
            usuario.loguear_usuario(driver)
            assert Register.url_inventory in driver.current_url, "No fue redirigido a inventory.html"
            print("Podemos ver " + Register.url_inventory)

        except Exception as e:
            print(f"Error en test_login: {e}")
            raise
        finally:
            driver.quit()
    elif not debe_funcionar:
        usuario.abrir_web()
        usuario.validar_usuario()
        mensaje_error = usuario.obtener_error_login(Register.msgError)
        print(mensaje_error)
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"
