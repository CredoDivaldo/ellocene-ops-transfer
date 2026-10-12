---
task: "Listar Fontes"
responsavel: "@relatorios"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - tipo de relatório
Saida: |
  - inventário de dados disponíveis + lacunas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *listar-fontes

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@relatorios
*listar-fontes
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tipo de relatório` | string | Yes | tipo de relatório |

## Output

- **inventário de dados disponíveis + lacunas**: inventário de dados disponíveis + lacunas

## Origin

Confidence: 94%
