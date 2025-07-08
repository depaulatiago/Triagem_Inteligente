### 4.3. Visão Final (Pós-Implementação das Mitigações)

Após a análise de ameaças, a arquitetura foi revisada para incorporar as medidas de mitigação. A principal mudança foi a introdução de um **Proxy Reverso (Nginx)** como ponto de entrada do sistema.

O Nginx é responsável por:
1.  **Terminação SSL/TLS:** Ele gerencia a criptografia HTTPS, descriptografando a requisição do cliente e a repassando para o Gateway via HTTP na rede interna segura do Docker.
2.  **Rate Limiting:** Aplica a política de limitação de requisições.
3.  **Gateway de API:** Atua como o único ponto de entrada, escondendo os detalhes da infraestrutura interna.

**Diagrama da Arquitetura Final:**

```mermaid
graph TD
    subgraph "Ambiente do Usuário"
        Cliente[<i class='fa fa-user'></i> Cliente]
    end

    subgraph "Perímetro Seguro do Servidor (Docker)"
        subgraph "Ponto de Entrada"
            Nginx[<i class='fa fa-shield-alt'></i> Proxy Reverso Nginx]
        end

        subgraph "Serviços da Aplicação"
            Gateway(Gateway API)
            Agente1(Agente 1 - Sintomas)
            Agente2(Agente 2 - Contexto)
            Logs[<i class='fa fa-file-alt'></i> Sistema de Logs]
        end
    end

    Cliente -- "<b>Requisição HTTPS</b><br/>+ Chave de API" --> Nginx
    Nginx -- "Aplica Rate Limit<br/>Repassa Requisição HTTP" --> Gateway
    Gateway -- "Requisição HTTP interna" --> Agente1
    Gateway -- "Requisição HTTP interna" --> Agente2
    Gateway -- "Registra atividade" --> Logs
    Agente1 -- "Resposta JSON" --> Gateway
    Agente2 -- "Resposta JSON" --> Gateway
    Gateway -- "Resposta agregada" --> Nginx
    Nginx -- "<b>Resposta HTTPS Criptografada</b>" --> Cliente

    linkStyle 0 stroke:#18a118,stroke-width:2.5px;
    linkStyle 1 stroke:#333,stroke-width:2px;
    linkStyle 2 stroke:#333,stroke-width:2px,stroke-dasharray: 5 5;
    linkStyle 3 stroke:#333,stroke-width:2px,stroke-dasharray: 5 5;
    linkStyle 4 stroke:#f66,stroke-width:1.5px,stroke-dasharray: 5 5;
    linkStyle 5 stroke:#333,stroke-width:1.5px,stroke-dasharray: 5 5;
    linkStyle 6 stroke:#333,stroke-width:1.5px,stroke-dasharray: 5 5;
    linkStyle 7 stroke:#333,stroke-width:2px;
    linkStyle 8 stroke:#18a118,stroke-width:2.5px;
```
**Observação:** Os diagramas acima utilizam a sintaxe Mermaid e podem ser renderizados diretamente pelo GitHub em arquivos `.md`. Eles usam ícones do Font Awesome, que também são suportados.