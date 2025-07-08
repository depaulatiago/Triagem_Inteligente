# gateway/gateway.py

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Agente 1 dentro do Docker
AGENTE1_URL = "http://agente1:5000/classificar"

# Agente 2 fora do Docker
AGENTE2_URL = "http://host.docker.internal:5001/analisar_contexto"

@app.route('/')
def home():
    return "Gateway da Triagem Inteligente - Sistema Distribuído"

@app.route('/triagem', methods=['POST'])
def triagem():
    data = request.get_json()

    if not data:
        return jsonify({"erro": "Nenhum dado recebido."}), 400

    try:
        resposta_agente1 = requests.post(AGENTE1_URL, json=data)
        resultado_agente1 = resposta_agente1.json()

        resposta_agente2 = requests.post(AGENTE2_URL, json={"texto": data.get("texto", "")})
        resultado_agente2 = resposta_agente2.json()

        resposta_final = {
            "resultado_agente1": resultado_agente1,
            "resultado_agente2": resultado_agente2,
            "triagem": "Com base nos dois agentes, recomenda-se avaliar os resultados combinados."
        }

        return jsonify(resposta_final), 200

    except Exception as e:
        return jsonify({"erro": f"Erro na comunicação com os agentes: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
