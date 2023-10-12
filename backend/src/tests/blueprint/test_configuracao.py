
#POST
def test_quando_envia_cadastro_correto_retorna_sucesso(client):
    headers={'Content-Type':'application/json'}
    configuracao={ "aluno_ausente": 5, "inicio_aula": "2000-01-01T19:00:00", "fim_aula": "2000-01-01T22:00:00"}
    resposta = client.post("/api/configuracao", headers=headers, json=configuracao)
    assert "Configuracao criada com sucesso" in resposta.text

def test_quando_envia_cadastro_sem_body(client):
    headers={'Content-Type': 'application/json'}
    resposta = client.post("/api/configuracao", headers=headers)
    assert resposta.status_code == 400

#GET

def test_quando_recebe_id_entao_retorna_configuracao(client):
    resposta = client.get("/api/configuracao?id=1")
    assert "Alunos" in resposta.text

def test_quando_recebe_id_incorreto_entao_retornar_error(client):
    resposta = client.get("/api/configuracao?id=50000")
    assert "Configuracao não encontrada" in resposta.text

def test_quando_recebe_id_invalido_entao_retornar_error(client):
    resposta = client.get("/api/configuracao?id=aaaaaa")
    assert "Deve ser um número inteiro" in resposta.text

def test_quando_recebe_numero_negativo_entao_retorna_error(client):
    resposta = client.get("/api/configuracao?id=-1")
    assert "ID inválido" in resposta.text

#PUT

def test_quando_edita_deve_retornar_sucesso(client):
    headers={'Content-Type':'application/json'}
    configuracao={ "aluno_ausente": 5, "inicio_aula": "2000-01-01T19:00:00", "fim_aula": "2000-01-01T22:00:00"}
    resposta = client.put("/api/configuracao?id=1", headers=headers, json=configuracao)
    assert "sucesso" in resposta.text

#DELETE

def test_quando_envia_delete_id_inexistente_deve_retorna_erro(client):
    resposta = client.delete("/api/configuracao?id=94309")
    assert "Configuracao não encontrada" in resposta.text