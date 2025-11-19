import requests
def test_delete():
    url = "https://reqres.in/api/users/2"

    payload = {"id": 8}
    headers = {
      'x-api-key': 'reqres-free-v1'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)
    print("Imprimiendo detalles")
    print(response.status_code)
    print(response.elapsed.seconds)
    assert  response.status_code == 204 and  response.elapsed.seconds < 1 , "No se puedo borrar o Muy lento"