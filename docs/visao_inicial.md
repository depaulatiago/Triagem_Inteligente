## 4. Documentação Arquitetônica

Esta seção detalha a evolução da arquitetura do sistema, desde sua concepção inicial até a versão final com medidas de segurança implementadas.

### 4.1. Visão Inicial (Pré-Modelagem de Ameaças)

A arquitetura inicial foi projetada para validar a funcionalidade principal do sistema: a orquestração de múltiplos agentes de IA através de um gateway central.

Nesta visão, os três microserviços (`agente1`, `agente2` e `gateway`) são orquestrados pelo Docker Compose. Um cliente (usuário final) faz uma requisição HTTP diretamente para o Gateway, que por sua vez consulta os dois agentes na rede interna do Docker e agrega as respostas.

**Diagrama da Arquitetura Inicial:**

```mermaid
graph TD
    subgraph "Ambiente do Usuário"
        Cliente[<i class='fa fa-user'></i> Cliente]
    end

    subgraph "Ambiente do Servidor (Docker)"
        Gateway(Gateway API)
        Agente1(Agente 1 - Sintomas)
        Agente2(Agente 2 - Contexto)
    end

    Cliente -- "Requisição HTTP com dados do paciente" --> Gateway
    Gateway -- "Requisição HTTP interna (porta 5000)" --> Agente1
    Gateway -- "Requisição HTTP interna (porta 5001)" --> Agente2
    Agente1 -- "Resposta JSON (classificação)" --> Gateway
    Agente2 -- "Resposta JSON (análise textual)" --> Gateway
    Gateway -- "Resposta JSON agregada" --> Cliente

    linkStyle 0 stroke:#333,stroke-width:2px;
    linkStyle 1 stroke:#333,stroke-width:2px;
    linkStyle 2 stroke:#333,stroke-width:2px;
    linkStyle 3 stroke:#f66,stroke-width:1.5px,stroke-dasharray: 5 5;
    linkStyle 4 stroke:#f66,stroke-width:1.5px,stroke-dasharray: 5 5;
    linkStyle 5 stroke:#333,stroke-width:2px;
```

**Pontos Fracos Identificados nesta Visão:**
* A comunicação é feita via HTTP, sem criptografia.
* Não há controle de acesso; qualquer um pode chamar a API.
* O sistema está vulnerável a ataques de negação de serviço (DoS).
* Não há registro de atividades para auditoria.