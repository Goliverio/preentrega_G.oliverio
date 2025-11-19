import requests


def test_post():
    url = "https://reqres.in/api/users"
    encabezado = {"x-api-key": "reqres-free-v1"}
    payload = {"name": "Jose", "job": "Profesor"}

    response = requests.post(url, headers=encabezado, json=payload)

    # VERIFICAR QUE EL RECURSO SE HAYA CREADO
    print("VERIFICAR QUE EL RECURSO SE HAYA CREADO")
    print(response.json())
    assert response.status_code == 201

    data = response.json()

    # VERIFICAR QUE EL NOMBRE DE LA RESPUESTA SEA EL MISMO QUE EL ENVIADO
    print("VERIFICAR QUE EL NOMBRE DE LA RESPUESTA SEA EL MISMO QUE EL ENVIADO")
    assert data["name"] == payload["name"]

    # VERIFICAR QUE LA RESPUESTA TENGA UN ID
    print("VERIFICAR QUE LA RESPUESTA TENGA UN ID")
    assert "id" in data

