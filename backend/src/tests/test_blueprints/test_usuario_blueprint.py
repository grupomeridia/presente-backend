import requests, json, re

url = "http://localhost:5000/api/usuario"
headers = {'Content-Type': 'application/json'}

id = 0

""" def test_deve_cadastrar_entao_retornar_mensagem():
    payload = {
        "login":"matheuz",
        "senha":"senhaforte",
        "cargo":"Aluno"
    }

    payload = json.dumps(payload, indent=4)

    data = requests.post(url, payload, headers=headers)
s
    
    assert data.text == "Usuario criado com sucesso"
 """


