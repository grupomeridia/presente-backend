#GET

def test_dado_id_inexiste_deve_retornar_erro(client):
    resposta = client.get("/api/presenca?id=2")
    assert "Nenhuma presença foi encontrada" in resposta.text

def test_dado_id_invalido_deve_retornar_erro(client):
    resposta = client.get("/api/presenca?id=foo")
    assert "Deve ser um número inteiro" in resposta.text


#POST

def test_quando_envia_post_sem_body_deve_retornar_erro(client):
    resposta = client.post("/api/presenca")
    assert resposta.status_code == 400

