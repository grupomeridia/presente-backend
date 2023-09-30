
#POST
def test_quando_envia_cadastro_correto_retorna_sucesso(client):
    headers={'Content-Type':'application/json'}
    materia={"nome":"materia3"}
    resposta = client.post("/api/materia", headers=headers, json=materia)
    assert "Projeto cadastrado com o ID" in resposta.text

def test_quando_envia_cadastro_sem_body(client):
    headers={'Content-Type':'application/json'}
    resposta = client.post("/api/materia", headers=headers)
    assert resposta.status_code == 400

#GET

def test_quando_recebe_id_entao_retorna_materia(client):
    resposta = client.get("/api/materia?id=1")
    assert "Ativo" in resposta.text

def test_quando_recebe_id_incorreto_entao_retornar_error(client):
    resposta = client.get("/api/materia?id=490903")
    assert "Nenhuma materia com o ID" in resposta.text

def test_quando_recebe_id_invalido_entao_retornar_error(client):
    resposta = client.get("/api/materia?id=aaaaaaaa")
    assert "O ID deve ser um número inteiro" in resposta.text

def test_quando_recebe_numero_negativo_entao_retorna_error(client):
    resposta = client.get("/api/materia?id=-1")
    assert "ID inválido" in resposta.text

#DELETE

def test_quando_envia_delete_id_inexistente_deve_retornar_error(client):
    resposta = client.delete("/api/materia?id=84398492")
    assert "Matéria não encontrada." in resposta.text