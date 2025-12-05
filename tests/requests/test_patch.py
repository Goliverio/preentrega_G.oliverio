import requests
import pytest
from utils.logger import logger
from tests.objects.requests_data import DatosWebApi


@pytest.mark.Api
def test_patch_users():
    url = DatosWebApi.url
    headers = DatosWebApi.headers
    data = {"name":"Juan"}

    response = requests.patch(url, headers=headers, json=data)
    logger.info("--------------------------------------------")

    # Validación de status code
    logger.info("OBTENIENDO RESPUESTA DEL SERVIDOR")
    assert response.status_code == 200, logger.error(f"Status code error:  {response.status_code}")
    logger.info(f"Status Code:  {response.status_code}")

    #Validacion de datos actualizados
    body = response.json()

    logger.info("VERIFICANDO LA ACTUALIZACIÓN DE DATOS")
    assert body["name"]  == data["name"], logger.error("El nombre no concuerda")
    logger.info("Datos actualizados")

