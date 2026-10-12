---
task: "Promover Processo"
responsavel: "@processos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - código PROC-… + evidência de aprovação do Credo
Saida: |
  - estado activo + handoff ao guardiao para executar daqui em diante
Checklist:
  - "[ ] *validar-processo PASS"
  - "[ ] Evidência explícita do Credo (mensagem desta sessão, GATE-LOG, ou Fibery Aprovado por)"
  - "[ ] Sem evidência: parar e pedir o gate — nunca auto-promover"
  - "[ ] Workflow Document → Activo; Versao Principal = true nesta versão"
  - "[ ] Handoff guardiao: spec activo, passos, comando de orquestração"
  - "[ ] Handoff docs só se o Credo quiser PDF SOP"
  - "[ ] Não alterar ellocene-ops/ sem pedido explícito — wiring em spec, não em patch"
---

# *promover-processo

Único caminho rascunho → activo. Gate humano obrigatório.

## Usage

```
@processos
*promover-processo {PROC-…} {evidência Credo}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `código` | string | Yes | `PROC-…` |
| `evidência Credo` | string | Yes | Aprovação explícita |

## Output

Document Activo + handoff `processos → guardiao`.

## Não feito se

Auto-promover; PDF no lugar da promoção; patch silencioso da fonte do squad.
