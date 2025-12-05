from utils.logger import logger
from tests.objects.requests_data import DatosWebApi
import requests
import pytest

@pytest.mark.Api
def test_put_users():
    url = DatosWebApi.url
    headers = DatosWebApi.headers

    response = requests.put(url, headers=headers)
    logger.info("--------------------------------------------")

    logger.info("OBTENIENDO RESPUESTA DEL SERVIDOR")
    assert response.status_code == 200,  logger.error(f"Status code error:  {response.status_code}")
    logger.info(f"Status Code:  {response.status_code}")

    logger.info("VERIFICANDO EL TIEMPO DE RESPUESTA")
    assert  response.elapsed.seconds < 1 , logger.error(f"Supero el tiempo esperado:  {response.elapsed.seconds}")
    logger.info(f"Tiempo de respuesta:  {response.elapsed.seconds}")

    # Validación de datos
    body = response.json()

    logger.info("VALIDANDO ESTADO DE LOS DATOS")
    assert "updatedAt" in body,  logger.error(f"Los datos no se guardaron")
    logger.info("Registro guardado correctamente")


