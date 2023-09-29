
import requests, json

url = "http://localhost:5000/api/aluno"

def test_deve_retornar_um_aluno():
    data = requests.get(url, params={"id":2})
    data = data.json()   
    assert all(key in data for key in ["Ativo", "Id", "Nome", "RA"])

