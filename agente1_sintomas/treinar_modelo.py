# -*- coding: utf-8 -*-
"""
Script de Treinamento do Modelo de Machine Learning (Versão Simples) para o Agente 1.

Este script é responsável por:
1. Definir um conjunto de dados fictício, porém lógico e coerente, para a triagem de pacientes.
2. Manter a estrutura original de 3 características (features) para compatibilidade.
3. Treinar um modelo de classificação (DecisionTreeClassifier).
4. Salvar o modelo treinado no arquivo 'modelo.pkl' para ser utilizado pelo Agente 1.

Este script deve ser executado uma única vez para gerar o arquivo do modelo.
"""

# --- 1. Importação das Bibliotecas ---

# DecisionTreeClassifier é o nosso algoritmo de Machine Learning.
from sklearn.tree import DecisionTreeClassifier
# joblib é usado para salvar nosso modelo treinado em um arquivo.
import joblib

print("--- Iniciando o script de treinamento do modelo (versão simples e robusta) ---")

# --- 2. Definição das Características (Features) ---

# O modelo será treinado com base em 3 informações, nesta ordem exata:
# Característica 1: 'febre' (float) - A temperatura corporal do paciente em graus Celsius.
# Característica 2: 'dor'   (int)   - Um valor binário (0 ou 1) indicando a presença de dor significativa (ex: dor de cabeça, dor no corpo). 1 para 'sim', 0 para 'não'.
# Característica 3: 'nausea'(int)   - Um valor binário (0 ou 1) indicando se o paciente sente náuseas. 1 para 'sim', 0 para 'não'.

# --- 3. Geração dos Dados de Treinamento ---
# Os dados foram criados seguindo regras lógicas para cada nível de gravidade.

# REGRAS PARA CASOS 'LEVE':
# - Febre baixa ou ausente (36.5 a 37.7°C).
# - Dor é pouco comum.
# - Náusea é muito rara.
dados_leves = [
    # [febre, dor, nausea]
    [36.8, 0, 0], [37.1, 0, 0], [37.3, 1, 0], [36.9, 0, 0], [37.0, 1, 0],
    [37.2, 0, 0], [36.7, 0, 0], [37.4, 0, 0], [37.5, 1, 0], [37.1, 0, 0],
    [36.6, 1, 0], [37.6, 0, 0], [37.7, 1, 0], [37.0, 0, 0], [36.9, 1, 0]
]
# Total de 15 amostras leves.

# REGRAS PARA CASOS 'MODERADO':
# - Febre moderada (37.8 a 38.9°C).
# - Dor é comum.
# - Náusea pode ou não estar presente.
dados_moderados = [
    # [febre, dor, nausea]
    [37.9, 1, 0], [38.1, 0, 1], [38.3, 1, 1], [38.0, 1, 0], [38.5, 0, 1],
    [38.2, 1, 0], [37.8, 0, 0], [38.4, 1, 1], [38.6, 1, 0], [38.8, 0, 1],
    [37.9, 1, 1], [38.7, 1, 0], [38.9, 1, 1], [38.0, 0, 1], [38.2, 1, 1],
    [38.5, 1, 0], [38.1, 1, 1], [37.8, 1, 0], [38.3, 0, 1], [38.6, 1, 1]
]
# Total de 20 amostras moderadas.

# REGRAS PARA CASOS 'GRAVE':
# - Febre alta (39.0 a 40.5°C).
# - Dor é quase sempre presente.
# - Náusea é comum.
dados_graves = [
    # [febre, dor, nausea]
    [39.1, 1, 1], [39.5, 1, 0], [40.0, 1, 1], [39.3, 0, 1], [39.8, 1, 1],
    [39.0, 1, 0], [40.2, 1, 1], [39.6, 1, 1], [40.5, 1, 1], [39.4, 1, 0],
    [39.9, 1, 1], [40.1, 1, 0], [39.2, 1, 1], [39.7, 0, 1], [40.3, 1, 1]
]
# Total de 15 amostras graves.

# Juntando todos os dados em duas listas principais: X (características) e y (rótulos/respostas)
X = dados_leves + dados_moderados + dados_graves

y = (['leve'] * len(dados_leves)) + \
    (['moderado'] * len(dados_moderados)) + \
    (['grave'] * len(dados_graves))

print(f"\n--- Total de {len(X)} amostras de dados geradas para o treinamento. ---")
print(f"Exemplos de X (características): {X[:3]}")
print(f"Exemplos de y (rótulos): {y[:3]}")


# --- 4. Treinamento do Modelo ---
print("\n--- Iniciando o treinamento do modelo DecisionTreeClassifier ---")

# Cria uma instância do classificador (o "cérebro" em branco).
# random_state=42 garante que a "árvore" seja construída da mesma forma toda vez, para resultados consistentes.
modelo = DecisionTreeClassifier(random_state=42)

# O método .fit() realiza o treinamento, ensinando o modelo a mapear os sintomas em X para a gravidade em y.
modelo.fit(X, y)

print("--- Treinamento concluído com sucesso! ---")


# --- 5. Salvando o Modelo Treinado ---
nome_arquivo_modelo = 'modelo.pkl'

# Usa a função dump do joblib para salvar o objeto do modelo treinado no arquivo.
joblib.dump(modelo, nome_arquivo_modelo)

print(f"\n--- Modelo salvo com sucesso no arquivo: '{nome_arquivo_modelo}' ---")
print("Este arquivo agora pode ser usado pelo Agente 1.")