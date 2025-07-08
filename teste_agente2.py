import requests

data = {
    "texto": "O trabalho tem sido uma loucura, estou muito estressado e sobrecarregado."
}

response = requests.post("http://localhost:5001/analisar_contexto", json=data)

print("Status:", response.status_code)
print("Resposta:", response.json())
