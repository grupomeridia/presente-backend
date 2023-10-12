#GET

def test_retornar_secretaria(client):
    resposta = client.get("/api/secretaria?id=500")

    assert "Nenhum ID encontrado" in resposta.text

def test_retorna_um_id_incorreto(client):
    resposta = client.get("/api/secretaria?id=9999999")

    assert "Nenhum ID encontrado" in resposta.text

def test_retorna_id_invalido(client):
    resposta = client.get("/api/secretaria?id=oie")

    assert "ID deve ser um número inteiro." in resposta.text

def test_retorna_um_id_negativo(client):
    resposta = client.get("/api/secretaria?id=-1")
    assert "ID inválido." in resposta.text

#POST

def test_quando_enviar_sem_body(client):
    resposta = client.post("/api/secretaria")

    assert resposta.status_code == 400

def test_quando_envia_retorna_sucesso(client):
    headers={'Content-Type': 'application/json'}
    dados = {
        "id_usuario": 1,
        "status": True,
        "nome": "Luiz"
    }
    resposta = client.post("/api/secretaria", headers=headers, json=dados)
    
    assert "Secretaria registrado com o ID" in resposta.text

#DEL

def test_delete_painel_inexistente(client):
    resposta = client.delete("/api/secretaria?id=9999999")
    assert "Secretaria não encontrada" in resposta.text

def test_delete_painel_invalido(client):
    resposta = client.delete("/api/secretaria?id=eyu")
    assert "ID deve ser um número inteiro." in resposta.text

def test_delete_painel_sucesso(client):
    resposta = client.delete("/api/secretaria?id=1")
    assert "Secretaria ID" in resposta.text