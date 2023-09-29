import requests, json

url = "http://localhost:5000/api/usuario"
headers = {'Content-Type': 'application/json'}

def test_deve_cadastrar_entao_retornar_mensagem():
    payload = {
        "login":"matheus",
        "senha":"senhaforte",
        "cargo":"Aluno"
    }

    payload = json.dumps(payload, indent=4)

    data = requests.post(url, payload, headers=headers)

    assert data.text == "Usuario criado com sucesso"