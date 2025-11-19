import json
from pathlib import Path

def leer_json_productos(ruta_archivo):
    ruta = Path(ruta_archivo)

    with ruta.open("r", encoding="utf-8") as archivo:
        producto = json.load(archivo)

    nombres = [producto.]