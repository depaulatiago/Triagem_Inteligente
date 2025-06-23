from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

AGENTE1_URL = "http://agente1:5000/classificar"   # Corrigido!
AGENTE2_URL = "http://localhost:5001/analisar_contexto"  # Também corrigido!

@app.route('/triagem', methods=['POST'])
def triagem():
    data = request.get_json()

    if not data or 'sintomas' not in data or 'contexto' not in data:
        return jsonify({"erro": "Campos 'sintomas' e 'contexto' são obrigatórios."}), 400

    try:
        # Transformar sintomas em entrada booleana para Agente 1
        sintomas_lista = data["sintomas"]
        entrada_agente1 = {
            "febre": int("febre" in sintomas_lista),
            "dor": int("dor" in sintomas_lista),
            "nausea": int("nausea" in sintomas_lista)
        }

        # Envia para o Agente 1
        resposta_agente1 = requests.post(AGENTE1_URL, json=entrada_agente1)
        resultado_agente1 = resposta_agente1.json()

        # Envia para o Agente 2
        entrada_agente2 = {"texto": data["contexto"]}
        resposta_agente2 = requests.post(AGENTE2_URL, json=entrada_agente2)
        resultado_agente2 = resposta_agente2.json()

        return jsonify({
            "resultado_agente1": resultado_agente1,
            "resultado_agente2": resultado_agente2,
            "triagem": "Com base nos dois agentes, recomenda-se avaliar os resultados combinados."
        }), 200

    except Exception as e:
        return jsonify({"erro": f"Erro na comunicação com os agentes: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
