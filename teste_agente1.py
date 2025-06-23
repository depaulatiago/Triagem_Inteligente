import requests

data = {
    "sintomas": ["tosse", "febre"],
    "contexto": "idoso, comorbidades"
}

response = requests.post("http://localhost:5000/predict", json=data)
print("Status:", response.status_code)
print("Resposta:", response.text)
