

#POST

def test_quando_envia_cadastro_sem_body_entao_retorna_erro(client):
    headers={'Content-Type': 'application/json'}
    resposta = client.post("/api/aluno", headers=headers)
    assert resposta.status_code == 400

    #GET

def test_quando_recebe_id_entao_retorna_aluno(client):
    resposta = client.get("/api/aluno?id=1")
    assert "Ativo" in resposta.text

def test_quando_recebe_id_incorreto_entao_retorna_erro(client):
    resposta = client.get("/api/aluno?id=9999999")
    assert "Nenhum aluno com este ID foi encontrado" in resposta.text

def test_quando_recebe_id_invalido_entao_retorna_erro(client):
    resposta = client.get("/api/aluno?id=abc")
    assert "Deve ser um número inteiro" in resposta.text

def test_dado_ra_retorna_aluno(client):
    resposta = client.get("/api/aluno/findByRa?ra=504083")
    assert "Ativo" in resposta.text

#PUT

def test_quando_envia_put_sem_id_entao_retorna_erro(client):
    resposta = client.put("/api/aluno")
    assert resposta.status_code == 400

def test_quando_envia_put_sem_body_retorna_erro(client):
    resposta = client.put("/api/aluno?id=2")
    assert resposta.status_code == 400

#DELETE

def test_quando_envia_delete_com_id_invalido(client):
    resposta = client.delete("/api/aluno?id=foo")
    assert "ID deve ser um número inteiro" in resposta.text

def test_quando_envia_delete_com_id_inexistente(client):
    resposta = client.delete("/api/aluno?id=9999999")
    assert "Aluno não encontrado" in resposta.text