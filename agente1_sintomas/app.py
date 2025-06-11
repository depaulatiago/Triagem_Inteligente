from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
modelo = joblib.load('modelo.pkl')

@app.route('/classificar', methods=['POST'])
def classificar_sintomas():
    dados = request.json
    entrada = [[dados.get('febre', 0), dados.get('dor', 0), dados.get('nausea', 0)]]
    predicao = modelo.predict(entrada)[0]

    return jsonify({'classificacao': predicao})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
