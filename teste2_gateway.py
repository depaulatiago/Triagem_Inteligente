# -*- coding: utf-8 -*-
"""
Script de Teste de Integração para o Gateway do Sistema de Triagem Inteligente.

Este script simula um cliente fazendo requisições para o endpoint principal (/triagem)
do gateway e valida as respostas para diferentes cenários.

COMO USAR:
1. Certifique-se de que todo o sistema está em execução. Em um terminal, na pasta raiz
   do projeto, execute o comando:
   $ docker-compose up

2. Em OUTRO terminal, na mesma pasta raiz, execute este script:
   $ python test_gateway.py

O script irá imprimir os resultados de cada teste no console.
"""

# --- 1. Importação das Bibliotecas ---

# A biblioteca 'requests' é usada para fazer as chamadas HTTP para a nossa API.
import requests
# A biblioteca 'json' é usada aqui para formatar a saída da resposta, tornando-a mais legível.
import json

# --- 2. Configuração do Teste ---

# O endereço completo do nosso gateway, conforme definido no docker-compose.yml.
# O gateway está exposto na porta 5002 do nosso computador (localhost).
GATEWAY_URL = "http://localhost:5002/triagem"

# O cabeçalho da requisição, informando ao servidor que estamos enviando dados em formato JSON.
HEADERS = {"Content-Type": "application/json"}


# --- 3. Definição dos Cenários de Teste (Payloads) ---
# Cada 'payload' é um dicionário Python que simula os dados que um cliente enviaria.

# Cenário 1: Um caso claramente leve, com febre baixa e sem contexto psicossocial.
payload_cenario_leve = {
    "febre": 37.2,
    "dor": 0,
    "nausea": 0,
    "texto": "Estou me sentindo bem, apenas um pouco indisposto."
}

# Cenário 2: Um caso moderado, com febre e dor, e um texto indicando estresse.
payload_cenario_moderado_estresse = {
    "febre": 38.5,
    "dor": 1,
    "nausea": 0,
    "texto": "O trabalho tem sido uma loucura, estou muito estressado e sobrecarregado."
}

# Cenário 3: Um caso grave, com febre alta e todos os sintomas, e um texto indicando isolamento e ansiedade.
payload_cenario_grave_complexo = {
    "febre": 40.1,
    "dor": 1,
    "nausea": 1,
    "texto": "Moro sozinho e tenho medo de passar mal. Essa situação me deixa muito ansioso e me sinto isolado."
}

# Cenário 4: Um caso onde o paciente não informa o texto. O sistema deve lidar com isso sem quebrar.
payload_sem_texto = {
    "febre": 38.0,
    "dor": 1,
    "nausea": 1
    # A chave "texto" está ausente de propósito.
}


# --- 4. Função Auxiliar para Executar os Testes ---
# Criamos uma função para não repetir o mesmo código várias vezes.
def executar_teste(nome_cenario, payload):
    """Função que envia uma requisição para o gateway e imprime o resultado."""
    
    print("="*50)
    print(f"▶️  INICIANDO TESTE: {nome_cenario}")
    print("="*50)
    print("Enviando os seguintes dados para o Gateway:")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    try:
        # A linha principal: faz a requisição POST para a URL do gateway.
        # - headers=HEADERS: envia o cabeçalho que definimos.
        # - json=payload: converte nosso dicionário Python para JSON e o envia no corpo da requisição.
        # - timeout=10: define um tempo limite de 10 segundos para a resposta.
        response = requests.post(GATEWAY_URL, headers=HEADERS, json=payload, timeout=10)

        # Imprime o código de status da resposta (ex: 200 para sucesso, 500 para erro no servidor).
        print(f"\nStatus da Resposta Recebida: {response.status_code}")

        # Verifica se a requisição foi bem-sucedida.
        if response.status_code == 200:
            print("✅ SUCESSO: O Gateway processou a requisição e retornou uma resposta.")
            print("\n--- Resposta do Gateway ---")
            # Imprime a resposta JSON de forma formatada e legível, garantindo a exibição de acentos.
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print(f"❌ FALHA: O Gateway retornou um código de erro: {response.status_code}")
            print(f"Corpo da resposta (erro): {response.text}")

    except requests.exceptions.RequestException as e:
        # Este bloco é executado se houver um erro de rede (ex: o gateway não está de pé).
        print("\n❌ ERRO DE CONEXÃO!")
        print(f"Não foi possível conectar ao Gateway em {GATEWAY_URL}.")
        print("Verifique se você executou 'docker-compose up' e se todos os containers estão rodando sem erros.")
        print(f"Detalhe do erro de conexão: {e}")
    
    print("\n\n")


# --- 5. Execução Principal do Script ---
if __name__ == "__main__":
    print("### INICIANDO SUÍTE DE TESTES PARA O GATEWAY DA TRIAGEM INTELIGENTE ###\n")
    
    # Chama a função de teste para cada um dos cenários que definimos.
    executar_teste("Cenário de Paciente com Sintomas Leves", payload_cenario_leve)
    executar_teste("Cenário de Paciente com Sintomas Moderados e Estresse", payload_cenario_moderado_estresse)
    executar_teste("Cenário de Paciente com Sintomas Graves e Contexto Complexo", payload_cenario_grave_complexo)
    executar_teste("Cenário com Dados Incompletos (sem o campo 'texto')", payload_sem_texto)

    print("### SUÍTE DE TESTES CONCLUÍDA ###")