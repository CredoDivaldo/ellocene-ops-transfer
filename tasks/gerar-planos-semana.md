---
task: "Gerar Planos Semana"
responsavel: "@planos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - tarefas actas
  - carryover
  - estado Fibery Task
  - prioridades do Credo
Saida: |
  - plano semanal (por filha/projecto) → gate → publicação
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-planos-semana

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@planos
*gerar-planos-semana
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tarefas actas` | string | Yes | tarefas actas |
| `carryover` | string | Yes | carryover |
| `estado Fibery Task` | string | Yes | estado Fibery Task |
| `prioridades do Credo` | string | Yes | prioridades do Credo |

## Output

- **plano semanal (por filha/projecto) → gate → publicação**: plano semanal (por filha/projecto) → gate → publicação

## Origin

Confidence: 94%
