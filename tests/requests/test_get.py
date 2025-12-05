import requests
import pytest
from utils.logger import logger
from tests.objects.requests_data import DatosWebApi

@pytest.mark.Api
def test_get_users():
    url = DatosWebApi.url
    headers = DatosWebApi.headers

    response = requests.get(url, headers=headers)

    logger.info("--------------------------------------------")
    logger.info("OBTENIENDO RESPUESTA DEL SERVIDOR")
    assert response.status_code == 200, logger.error(f"Status code error:  {response.status_code}")
    logger.info(f"Status Code:  {response.status_code}")

    data = response.json()

    # VERIFICAR QUE LA CLAVE "DATA" ESTA PRESENTE
    logger.info("VERIFICANDO QUE LA CLAVE 'DATA' ESTA PRESENTE")
    assert  data["data"]["id"] == 2, logger.error("La Clave Data fue encontrada")
    logger.info(f"Clave {data['data']['id']} se encontro")

    # VERIFICAR QUE HAYA AL MENOS UN USUARIO EN LA LISTA
    logger.info("VERIFICANDO SI HAY USUARIOS EN LA LISTA")
    assert len(data["data"]) > 0,  logger.error("La DATA no es una lista")
    logger.info(f"Se encontraron {len(data["data"])} usuarios")


