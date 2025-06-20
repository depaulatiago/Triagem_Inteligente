from flask import Flask, request, jsonify
from analisador import analisar_contexto # Importa a nossa função de análise

app = Flask(__name__)

@app.route('/analisar_contexto', methods=['POST'])
def analisar_contexto_api():
    dados = request.json
    
    # Verifica se a chave 'texto' foi enviada no corpo da requisição
    if not dados or 'texto' not in dados:
        return jsonify({"erro": "O campo 'texto' é obrigatório."}), 400
        
    texto_paciente = dados['texto']
    
    # Chama a função de análise que criamos
    resultado_analise = analisar_contexto(texto_paciente)
    
    return jsonify(resultado_analise)

if __name__ == "__main__":
    # Roda na porta 5001 para não conflitar com o Agente 1
    app.run(host='0.0.0.0', port=5001)