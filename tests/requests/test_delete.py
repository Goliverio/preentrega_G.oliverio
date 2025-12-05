import requests
import pytest
from tests.objects.requests_data import DatosWebApi
from utils.logger import logger


@pytest.mark.Api
def test_delete():
    url = DatosWebApi.url
    headers = DatosWebApi.headers
    payload = {"id": 2}

    logger.info("--------------------------------------------")

    #response = requests.request("DELETE", url, headers=headers, data=payload)
    logger.info("BORRANDO EL USUARIO")
    response = requests.delete( url, headers=headers, data=payload)

    #COMPROBANDO LA RESPUESTA DEL SERVIDOR
    logger.info("OBTENIENDO RESPUESTA DEL SERVIDOR")
    assert  response.status_code == 204,  logger.error(f"Status code error:  {response.status_code}")
    logger.info(f"Status Code:  {response.status_code}. Eliminado correctamente")

    # COMPROBANDO EL TIEMPO DE RESPUESTA
    logger.info("COMPROBANDO TIEMPO DE RESPUESTA")
    assert response.elapsed.seconds < 2 ,  logger.error("El tiempo de respuesta fue muy largo")
    logger.info(f"El tiempo de respuesta fue {response.elapsed.seconds}")
