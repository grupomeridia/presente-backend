
import requests, json,re

url = "http://localhost:5000/api/aluno"
headers = {'Content-Type': 'application/json'}


def test_deve_criar_um_aluno():
    payload = {
        "id_usuario":1, 
        "nome":"Matheus Almeida",
        "ra":56526591
    }

    payload = json.dumps(payload, indent=4)
    data = requests.post(url, payload, headers=headers)

    assert "Aluno registrado com o ID" in data.text

def test_deve_retornar_um_aluno():
    data = requests.get(url, params={"id":2})
    data = data.json()   
    assert all(key in data for key in ["Ativo", "Ausente", "id", "Nome", "RA"])

def test_deve_atualizar_um_aluno():
    
    payload = {
        "id_usuario":1, 
        "nome":"Matheus Henrique",
        "ra":506060
    }
    payload = json.dumps(payload, indent=4)

    data = requests.put(url, data=payload, params={"id":2}, headers=headers)

    assert "Aluno ID " in data.text

def test_deve_deletar_um_aluno_entao_retornar_erro():
    data = requests.delete(url, params={"id":"abc"})
    assert "ID deve ser um número inteiro" in data.text

def test_deve_deletar_um_aluno_nao_encontrado():
    data = requests.delete(url, params={"id":999999999})
    assert "Aluno não encontrado" in data.text

def test_deve_deletar_um_aluno_sucesso():
    data = requests.delete(url, params={"id":2})
    assert "Aluno ID" in data.text

def test_retorna_200(client):
    assert client.get("api/aluno").status_code == 404

def test_cadastra_aluno(client):
    response = client.get("/api/aluno", data={"id_usuario":1,"nome":"Matheus Almeida","ra":56526591})
    assert "Aluno ID " in response.text

