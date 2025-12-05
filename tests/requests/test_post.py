import requests
import pytest
from utils.logger import logger
from tests.objects.requests_data import DatosWebApi


@pytest.mark.Api
def test_post_users():
    url = DatosWebApi.url
    headers = DatosWebApi.headers
    payload = {"name": "Jose", "job": "Profesor"}

    response = requests.post(url, headers=headers, json=payload)
    logger.info("--------------------------------------------")

    # VERIFICAR QUE EL RECURSO SE HAYA CREADO
    logger.info("VERIFICANDO QUE EL RECURSO SE HAYA CREADO")
    assert response.status_code == 201, logger.error(f"Status code error:  {response.status_code}")
    logger.info(f"Status Code:  {response.status_code}")

    data = response.json()

    # VERIFICAR QUE EL NOMBRE DE LA RESPUESTA SEA EL MISMO QUE EL ENVIADO
    logger.info("VERIFICANDO EL NOMBRE DE LA RESPUESTA CON EL ENVIADO")
    assert data["name"] == payload["name"] , logger.error("Error al guardar los datos")
    logger.info("Datos correctos")

    # VERIFICAR QUE LA RESPUESTA TENGA UN ID
    logger.info("VERIFICANDO QUE QUE LA RESPUESTA TENGA UN ID")
    assert "id" in data, logger.error("ID no encontrado")
    logger.info("El ID es correcto")
