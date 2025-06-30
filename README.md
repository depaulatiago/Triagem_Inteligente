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

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/Triagem_Inteligente.git
cd Triagem_Inteligente
```

### 2. Subir os serviços Docker (Agente 1 e Gateway)

No diretório raiz do projeto (onde está o `docker-compose.yml`):

```bash
docker-compose up --build
```

Isso iniciará os serviços do `gateway` e do `agente1_sintomas`.

### 3. Executar o Agente 2 (não containerizado)

Em outro terminal, acesse a pasta `agente2_contexto`:

```bash
cd agente2_contexto
python -m venv venv
./venv/Scripts/activate  # Windows
pip install -r requirements.txt
python app.py
```

Verifique se está rodando em `http://127.0.0.1:5001`.

### 4. Testar o Sistema

Com todos os serviços rodando, execute o script de teste no diretório raiz:

```bash
python teste_gateway.py
```

Exemplo de resposta esperada:

```json
{
  "resultado_agente1": { "classificacao": "leve" },
  "resultado_agente2": { 
    "fatores_identificados": [...],
    "recomendacao": "..."
  },
  "triagem": "Com base nos dois agentes, recomenda-se avaliar os resultados combinados."
}
```

## ✅ Relevância do Problema

A triagem hospitalar tradicional costuma focar apenas nos sintomas físicos imediatos, muitas vezes ignorando o contexto psicológico, social e regional do paciente. Além disso, em muitos cenários, a alta demanda e a escassez de profissionais geram **demoras no atendimento**, o que pode comprometer o cuidado eficaz, especialmente em casos mais graves.

Este sistema busca atuar como uma **ferramenta de apoio à decisão clínica**, oferecendo uma análise automatizada e rápida dos sintomas e do contexto do paciente. A proposta **não é substituir o médico**, mas **auxiliá-lo** com informações consolidadas e inteligências especializadas que ajudem a:

- Priorizar atendimentos com base em gravidade e risco social;
- Oferecer uma visão mais completa do paciente;
- Aumentar a eficiência na tomada de decisão sobre encaminhamentos, diagnósticos e prescrições.

Assim, o sistema contribui para uma triagem mais **ágil**, **contextualizada** e **assertiva**, beneficiando tanto os profissionais de saúde quanto os pacientes.

## 👥 Equipe

* Nome 1 (responsável pelo agente 1)
* Nome 2 (responsável pelo agente 2)
* Nome 3 (gateway, integração e documentação)

## 📘 Licença

Projeto acadêmico da disciplina de Sistemas Distribuídos - UFLA
