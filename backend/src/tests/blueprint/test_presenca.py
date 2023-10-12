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

def test_faz_presenca(client):
    headers={'Content-Type':'application/json'}
    payload = {"id_aluno":1, "id_chamada":3,"tipo_presenca":"Regular"}
    resposta = client.post("/api/presenca", headers=headers, json=payload)
    assert "realizada" in resposta.text

#PUT
def test_envia_payload_errado_retorna_erro(client):
    resposta = client.put("/api/presenca")
    assert resposta.status_code == 400


#DELETE
def test_envia_id_errado_deleta_erro(client):
    resposta = client.delete("/api/presenca?id=foo")
    assert "Deve ser um número inteiro" in resposta.text

def test_quando_envia_delete_com_id_correto_retorna_ok(client):
    resposta = client.delete("/api/presenca?id=5")
    assert "sucesso" in resposta.text

def test_quando_envia_delete_com_id_inexistente(client):
    resposta = client.delete("/api/presenca?id=9999999")
    assert "Presenca não encontrada" in resposta.text

