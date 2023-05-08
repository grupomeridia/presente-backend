from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/cadastro', methods=['POST'])
def cadastrar_aluno():
    dados = request.get_json()
    nome = dados['nome']
    ra = dados['ra']
    return jsonify({'mensagem': 'Aluno cadastrado com sucesso! {} {}'.format(nome,ra)})

@app.route('/registra', methods=['POST'])
def registra_ponto():
    dados = request.get_json()
    ra = dados['ra']
    return jsonify({'mensagem': 'Aluno registrado com sucesso! {} {}'})


@app.route('/editAluno', methods=['PUT'])
def edita_aluno():
    dados = request.get_json()
    id = dados['id']
    nome = dados['nome']
    ra = dados['ra']
    return jsonify({'mensagem': 'Aluno editado com sucesso! {} {}'.format(nome,ra)})

@app.route('/getAlunos', methods=['GET'])
def busca_alunos():
    return jsonify({'mensagem': 'Alunos do banco!'})


@app.route('/getAluno', methods=['GET'])
def busca_alunos():
    return jsonify({'mensagem': 'Alunos do banco!'})

if __name__ == '__main__':
    app.run(debug=True)
