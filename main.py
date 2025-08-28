import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para lidar com as requisições do webhook
@app.route('/', methods=['GET',"POST"])
def home():
    return "OK", 200

@app.route('/listar', methods=["GET"])
def listar():
    return jsonify({"mensagem": "Listar OK"}), 200

@app.route('/criar', methods=["POST"])
def criar():
    data = request.get_json()  # Recebe JSON enviado no corpo do POST
    nome = data.get('nome')
    print(nome)
    return "Criar OK", 200

if __name__ == '__main__':
     # Pegar a porta da variável de ambiente ou usar 5000 como padrão
    port = int(os.environ.get('PORT', 5000))
    # Iniciar o servidor Flask
    app.run(host='0.0.0.0', port=port)