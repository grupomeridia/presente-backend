#GET

def test_retornar_professor(client):
    resposta = client.get("/api/professor?id=100")

    assert "Nenhum professor com este ID foi encontrado" in resposta.text

def test_retorna_um_id_incorreto(client):
    resposta = client.get("/api/professor?id=9999999")
    assert "Nenhum professor com este ID foi encontrado." in resposta.text

#POST

def test_quando_enviar_sem_body(client):
    resposta = client.post("/api/professor")

    assert resposta.status_code == 400

def test_quando_envia_deve_retornar_sucesso(client):
    headers={'Content-Type': 'application/json'}
    dados = {
        "id_usuario": 1,
        "nome": "Luiz",
        "status": True
    }
    resposta = client.post("/api/professor", headers=headers, json=dados)

    assert "Professor cadastrado com o id" in resposta.text

#DEL

def test_delete_painel_inexistente(client):
    resposta = client.delete("/api/professor?id=9999999")
    assert "Professor não encontrado" in resposta.text