# Triagem Inteligente com Múltiplos Agentes de IA

## 🎯 Objetivo

Desenvolver um sistema distribuído de triagem hospitalar utilizando dois agentes de IA que avaliam o estado clínico e o contexto social/psicológico do paciente.

## 🧠 Agentes

### Agente 1 – Classificador de Sintomas (ML supervisionado)

* Recebe sintomas clínicos estruturados (ex: febre, dor, náusea).
* Utiliza um modelo treinado com `scikit-learn` para classificar o nível de gravidade.

### Agente 2 – Avaliador de Contexto Psicológico e Social (NLP)

* Recebe descrição textual do paciente sobre seu bem-estar, estresse, acesso à saúde, etc.
* Usa NLP com modelo leve (ex: `distilbert`) para interpretar o texto e gerar recomendações.

## 🔁 Arquitetura Distribuída

* Cada IA roda como um microserviço independente.
* Um gateway central orquestra as chamadas e unifica a resposta.
* Comunicação via REST APIs com `Flask`.
* Infraestrutura com `Docker` e `docker-compose`.

## 🔒 Segurança

* A arquitetura será avaliada com modelagem de ameaças.
* A versão final implementará contramedidas básicas de segurança (ex: validação de entrada, autenticação leve).

## 📑 Documentação

* `docs/visao-inicial.pdf`: arquitetura antes das medidas de segurança.
* `docs/visao-final.pdf`: arquitetura final com mitigação de riscos.
* `docs/referencias.md`: justificativas e fontes acadêmicas sobre o problema.

## 🧪 Como Executar

1. Clonar o repositório
2. Executar `docker-compose up --build`
3. Testar o endpoint principal: `POST /avaliar` no gateway com JSON contendo:

```json
{
  "sintomas": {
    "febre": 38.5,
    "tosse": 1,
    "nausea": 0
  },
  "contexto": {
    "descricao": "Paciente vive sozinho, relata estresse intenso e mora longe do hospital."
  }
}
```

## ✅ Relevância do Problema

A triagem hospitalar muitas vezes ignora o contexto psicológico e regional do paciente. Este sistema busca fornecer uma análise mais holística, considerando tanto o quadro clínico imediato quanto fatores externos que impactam a saúde.

## 👥 Equipe

* Nome 1 (responsável pelo agente 1)
* Nome 2 (responsável pelo agente 2)
* Nome 3 (gateway, integração e documentação)

## 📘 Licença

Projeto acadêmico da disciplina de Sistemas Distribuídos - UFLA
