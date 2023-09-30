#GET

def test_retornar_lembrete(client):
    resposta = client.get("/api/lembrete?id=2")

    assert "Nenhum lembrete com este ID foi encontrado" in resposta.text

def test_retorna_um_id_incorreto(client):
    resposta = client.get("/api/lembrete?id=999999")
    assert "Nenhum lembrete com este ID foi encontrado" in resposta.text

#POST

def test_quando_enviar_sem_body(client):
    resposta = client.post("/api/lembrete")

    assert resposta.status_code == 400

def test_quando_envia_deve_retornar_sucesso(client):
    headers={'Content-Type': 'application/json'}
    dados = {
        "id_secretaria": 1,
        "destinatario_cargo": "Coordenador",
        "destinatario_id": 123,
        "titulo": "Lembrete importante",
        "mensagem": "Não se esqueça da reunião amanhã.",
        "criacao": "2023-09-29T12:00:00",
        "visualizacao": None
    }
    resposta = client.post("/api/lembrete", headers=headers, json=dados)

    assert "Lembrete registrado com sucesso" in resposta.text

#DEL

def test_delete_lembrete_inexistente(client):
    resposta = client.delete("/api/lembrete?id=9999999")
    assert "Lembrete não encontrado" in resposta.text