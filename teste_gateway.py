import requests

# Dados de entrada de teste
data = {
    "sintomas": ["febre", "dor"],  # Use apenas sintomas esperados: "febre", "dor", "nausea"
    "contexto": "idoso, comorbidades"
}

try:
    response = requests.post("http://localhost:5000/triagem", json=data)
    print("Status:", response.status_code)
    print("Resposta do gateway:")
    print(response.json())
except Exception as e:
    print("Erro ao conectar ao gateway:", e)
