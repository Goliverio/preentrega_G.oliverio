import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_login_titulo.py",
    "tests/test_inventario_navegacion.py",
    "tests/test_inventario_titulo.py",
    "tests/test_carrito_contador.py", 
    "tests/test_carrito_add.py"
]

# Argumentos para ejectuar las pruebas: archivos  + reporte + oociones
pytest_args = test_files + ["-vs", "--html=report.html", "--self-contained-html"]
               #[" -vs --html=report.html", "--self-contained-html"])


#pytest_args = test_files + ["-vs"]

pytest.main(pytest_args)
