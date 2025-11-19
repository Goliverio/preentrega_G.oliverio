import requests
#import pytest
#import json


def test_get_users():
    url = "https://reqres.in/api/users?page=2"  # Endpoint
    encabezado = {"x-api-key": "reqres-free-v1"}
    response = requests.get(url, headers=encabezado) #, verify=False)

    print(response.status_code)
    assert response.status_code == 200, "No es 200"

    # print(response.json())
    data = response.json()
    # print("########################################################")
    # print(data)


    # VERIFICAR QUE LA CLAVE "DATA" ESTA PRESENTE
    print("VERIFICAR QUE LA CLAVE 'DATA' ESTA PRESENTE")
    assert "data" in data

    # VERIFICAR QUE DATA ES UNA LISTA
    print("VERIFICAR QUE DATA ES UNA LISTA")
    assert isinstance(data["data"], list)

    # VERIFICAR QUE HAYA AL MENOS UN USUARIO EN LA LISTA
    print("VERIFICAR QUE HAYA AL MENOS UN USUARIO EN LA LISTA")
    print("En la lista hay", len(data), "usuarios" )
    print(data)
    assert len(data["data"]) > 0


