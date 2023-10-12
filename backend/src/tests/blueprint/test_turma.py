
#POST
def test_quando_envia_cadastro_correto_retorna_sucesso(client):
    headers={'Content-Type': 'application/json'}
    turma={"nome" : "turma2", "ano" : 2023, "semestre" : 2, "turno" :  "Noturno", "modalidade" : "Presencial", "curso" : "Engenharia de Software"}
    resposta = client.post("/api/turma", headers=headers, json=turma)
    assert "Turma Cadastrada com o ID" in resposta.text

def test_quando_envia_cadastro_sem_body(client):
    headers={'Content-Type': 'application/json'}
    resposta = client.post("/api/turma", headers=headers)
    assert resposta.status_code == 400

def test_quando_cadastrar_professor_sucesso(client):
    headers={'Content-Type': 'application/json'}
    turma={"id_turma":1, "id_professor":1}
    resposta = client.post("/api/turma/cadastrarProfessor", headers=headers, json=turma)
    assert "Professor cadastrado" in resposta.text

def test_quando_cadastrar_aluno_sucesso(client):
    headers={'Content-Type': 'application/json'}
    turma={"id_turma":1, "id_aluno":1}
    resposta = client.post("/api/turma/cadastrarAluno", headers=headers, json=turma)
    assert "Aluno cadastrado" in resposta.text

#GET

def test_quando_recebe_id_entao_retorna_turma(client):
    resposta = client.get("/api/turma?id=1")
    assert "status" in resposta.text

def test_quando_recebe_id_incorreto_entao_retornar_error(client):
    resposta = client.get("/api/turma?id=4300")
    assert "Nenhuma turma com o ID" in resposta.text

def test_quando_recebe_id_invalido_entao_retornar_error(client):
    resposta = client.get("/api/turma?id=aaaaa")
    assert "O ID deve ser um número inteiro" in resposta.text

def test_quando_recebe_numero_negativo_entao_retorna_error(client):
    resposta = client.get("/api/turma?id=-1")
    assert "ID inválido" in resposta.text

#PUT

def test_quando_edita_retorna_sucesso(client):
    headers={'Content-Type':'application/json'}
    turma={"nome" : "turma2", "ano" : 2023, "semestre" : 2, "turno" :  "Noturno", "modalidade" : "Presencial", "curso" : "Engenharia de Software"}
    resposta = client.put("/api/turma?id=1", headers=headers, json=turma)
    assert "sucesso" in resposta.text

#DELETE

def test_quando_envia_delete_id_inexistente_deve_retorna_erro(client):
    resposta = client.delete("/api/turma?id=90000")
    assert "Turma não encontrada" in resposta.text