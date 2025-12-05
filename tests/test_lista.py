##import pytest
import pytest
from utils.logger import logger


@pytest.mark.Low
def test_lista_completa(lista_de_usuarios):
    """ SOLO VERIFICA QUE SE LEA BIEN LA LISTA DE USUARIOS y que no este vacia"""
    la_lista = lista_de_usuarios
    logger.info("--------------------------------------------")
    assert len(la_lista) > 1, logger.info("La lista de usuarios se leyó correctamente")

