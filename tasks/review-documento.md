---
task: "Review Documento"
responsavel: "@legal"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - documento redigido por outro agente
Saida: |
  - review jurídico + correcções propostas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *review-documento

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@legal
*review-documento
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `documento redigido por outro agente` | string | Yes | documento redigido por outro agente |

## Output

- **review jurídico + correcções propostas**: review jurídico + correcções propostas

## Origin

Confidence: 86%
