
#POST

def test_quando_envia_cadastro_correto_retorna_sucesso(client):
    headers={'Content-Type':'application/json'}
    chamada={"id_materia" : 2, "id_turma" : 2, "id_professor" : 2}
    resposta = client.post("/api/chamada", headers=headers, json=chamada)
    assert "Chamada registrada" in resposta.text

def test_quando_envia_cadastro_sem_body(client):
    headers={'Content-Type': 'application/json'}
    resposta = client.post("/api/chamada", headers=headers)
    assert resposta.status_code == 400

#GET

def test_quando_recebe_id_entao_retorna_turma(client):
    resposta = client.get("/api/chamada?id=3")
    assert "status" in resposta.text

def test_quando_recebe_id_incorreto_entao_retornar_error(client):
    resposta = client.get("/api/chamada?id=500000")
    assert "Chamada não encontrada" in resposta.text

def test_quando_recebe_id_invalido_entao_retornar_error(client):
    resposta = client.get("/api/chamada?id=aaaaaa")
    assert "Deve ser um número inteiro" in resposta.text

def test_quando_recebe_numero_negativo_entao_retorna_error(client):
    resposta = client.get("/api/chamada?id=-1")
    assert "ID inválido" in resposta.text

#DELETE

def test_quando_envia_delete_id_inexistente_deve_retornar_erro(client):
    resposta = client.delete("/api/chamada?id=500000")
    assert "Chamada não encontrada" in resposta.text