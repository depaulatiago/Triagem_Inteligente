# Dicionário com palavras-chave para cada fator de risco
PALAVRAS_CHAVE = {
    "estresse": [
        "estresse", "estressado", "estressada", "pressão", "pressionado", 
        "sobrecarregado", "sobrecarregada", "exausto", "exausta"
    ],
    "ansiedade": [
        "ansiedade", "ansioso", "ansiosa", "preocupado", "preocupada", 
        "nervoso", "nervosa", "medo", "pânico"
    ],
    "isolamento": [
        "sozinho", "sozinha", "isolado", "isolada", "sem amigos", 
        "solitário", "solitária", "ninguém"
    ],
    "vulnerabilidade_social": [
        "sem apoio", "desempregado", "desempregada", "dificuldade financeira", 
        "sem dinheiro", "problema em casa"
    ]
}

RECOMENDACOES = {
    "estresse": "Foi identificado um possível quadro de estresse. É importante buscar atividades relaxantes e, se possível, conversar com um profissional sobre a pressão que está sentindo.",
    "ansiedade": "Sinais de ansiedade foram detectados. Práticas como meditação e exercícios de respiração podem ajudar. Considere buscar apoio psicológico para lidar com essas preocupações.",
    "isolamento": "A análise sugere um sentimento de isolamento. Manter contato com amigos e familiares, ou buscar grupos com interesses em comum, pode ser benéfico para o bem-estar social.",
    "vulnerabilidade_social": "Foram mencionados fatores que indicam vulnerabilidade social. É crucial buscar redes de apoio na sua comunidade, como serviços sociais ou ONGs, que podem oferecer auxílio."
}

def analisar_contexto(texto: str) -> dict:
    """
    Analisa o texto do paciente em busca de fatores de risco psicossociais.
    """
    texto = texto.lower() # Converte o texto para minúsculas para facilitar a busca
    fatores_identificados = []
    
    # Procura as palavras-chave no texto
    for fator, palavras in PALAVRAS_CHAVE.items():
        if any(palavra in texto for palavra in palavras):
            fatores_identificados.append(fator)
            
    # Monta a análise final
    if not fatores_identificados:
        analise_final = {
            "fatores_identificados": ["Nenhum fator de risco psicossocial proeminente identificado."],
            "recomendacao": "A análise textual não levantou pontos de atenção imediatos, mas é sempre válido manter o autocuidado e o acompanhamento clínico."
        }
    else:
        recomendacao_texto = "Análise complementar ao diagnóstico clínico:\n"
        for fator in fatores_identificados:
            recomendacao_texto += f"- {RECOMENDACOES[fator]}\n"
            
        analise_final = {
            "fatores_identificados": fatores_identificados,
            "recomendacao": recomendacao_texto
        }
        
    return analise_final