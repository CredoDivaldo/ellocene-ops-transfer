# Orquestração de Fluxos

```text
pedido → guardiao → especialista → state → outbox → validação/gate → deliverable
                     ↘ handoff ↗
```

## Cadência

- Diário: planos actualiza prioridades; guardiao lê bloqueios; registo preserva eventos; kpis sinaliza risco.
- Semanal: agentes activos actualizam estado; guardiao produz síntese; planos promove o próximo plano accionável.
- Por incidente: criar registo em `04_Execution/03_Incidents/`, atribuir dono e recovery; não ocultar dependências.

## Hierarquia de estado

1. `02_Control/<agente>/state/`; 2. `03_Data/03_State/`; 3. fontes do squad; 4. histórico.

## Gates

Legal e societário requerem revisão humana. Processo só fica activo com gate do Credo. Entregável de cliente exige PDF produzido por docs e identidade da emitente.
