import pytest
import sys

# Lista de archivos de pruebas a ejecutar
test_files = [
     "tests/test_login.py",
     "tests/test_login_titulo.py",
    "tests/test_lista.py",
    "tests/test_inventario_navegacion.py",
    "tests/test_inventario_titulo.py",
    "tests/test_carrito_contador.py",
    "tests/test_carrito_add.py",
    # TEST UTILIZANDO JSON
    "tests/test_carrito_json.py",
    # TEST FAKER
    "tests/test_login_faker.py",  # Se ejecuta por último porque buscamos que rechace el login
    # TEST DE APIS
    "tests/requests/test_delete.py",
    "tests/requests/test_get.py",
    "tests/requests/test_patch.py",
    "tests/requests/test_post.py",
    "tests/requests/test_put.py"
]

opciones = []
cantidad_argumentos = len(sys.argv)

def muestra_ayuda_sale():
    print("\nUsar: python run_test.py -m [marker a ejecutar]  [OTRAS OPCIONES]\n")
    print("""Los MARKERS disponibles son:
            Low: Test de baja prioridad
            Medium: Test de prioridad media
            High: Test de prioridad alta
            Api: Pruebas de APi
            JSON: Pruebas JSON
    Si no se especifica ningún MARKER se ejecutan todas las pruebas.
    """)
    sys.exit()

if cantidad_argumentos > 1:
    if sys.argv[1] == "--help":
        muestra_ayuda_sale()
    else:
        opciones = sys.argv[1:]

# Argumentos para ejecutar las pruebas: archivos + MARKS + reporte + opciones
pytest.main(test_files + opciones)

#pytest.main("tests",  opciones)
