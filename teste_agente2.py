import requests

data = {
    "texto": "idoso com comorbidades"
}

response = requests.post("http://localhost:5001/analisar_contexto", json=data)

print("Status:", response.status_code)
print("Resposta:", response.json())
