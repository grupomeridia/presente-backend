from flask import jsonify

#GET

def test_quando_informado_id_correto_deve_retornar_usuario(client):
    resposta = client.get("/api/usuario?id=1")
    assert "Login" in resposta.text

#POST

def test_quando_envia_post_sem_body_deve_retornar_erro(client):
    resposta = client.post("/api/usuario")
    assert resposta.status_code == 400

def test_quando_envia_cadastro_correto_deve_retornar_sucesso(client):
    headers={'Content-Type': 'application/json'}
    usuario = {"login":"teste2","senha":"teste","cargo":"Aluno"}
    resposta = client.post("/api/usuario", headers=headers, json=usuario)
    assert "Usuario criado com sucesso" in resposta.text 

def test_quando_envia_cadastro_correto_deve_retornar_erro(client):
    headers={'Content-Type': 'application/json'}
    usuario = {"login":"teste","senha":"teste","cargo":"Aluno"}
    resposta = client.post("/api/usuario", headers=headers, json=usuario)
    assert "Esse login já está sendo usado" in resposta.text 

#DELETE

#def test_quando_envia_delete_id_inexistente_deve_retornar_erro(client):
#    resposta = client.delete("/api/usuario?id=99999")
#    assert 1==1


