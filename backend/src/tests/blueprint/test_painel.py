#GET

def test_retornar_painel(client):
    resposta = client.get("/api/painel?id=2")

    assert "Nenhum painel com este ID foi encontrado" in resposta.text

def test_retorna_um_id_incorreto(client):
    resposta = client.get("/api/painel?id=9999999")
    assert "Nenhum painel com este ID foi encontrado." in resposta.text

#POST

def test_quando_enviar_sem_body(client):
    resposta = client.post("/api/painel")

    assert resposta.status_code == 400

def test_quando_envia_deve_retornar_sucesso(client):
    headers={'Content-Type': 'application/json'}
    dados = {
        "id_configuracao": 1,
        "id_secretaria": 2,
        "data_criado": "2023-09-30T14:00:00",
        "total_ativo": 50,
        "total_presentes": 30,
        "total_ausentes": 20,
        "total_presentes_curso": 25,
        "total_ativo_curso": 15,
        "total_ausente_curso": 10
    }
    resposta = client.post("/api/painel", headers=headers, json=dados)
    assert "Painel registrado com o ID" in resposta.text 

#DEL

def test_delete_painel_inexistente(client):
    resposta = client.delete("/api/painel?id=9999999")
    assert "Painel não encontrado." in resposta.text