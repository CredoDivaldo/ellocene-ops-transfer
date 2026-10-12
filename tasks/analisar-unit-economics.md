---
task: "Analisar Unit Economics"
responsavel: "@cfo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - filha/projecto + custos + preço
Saida: |
  - unit economics + recomendação
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *analisar-unit-economics

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cfo
*analisar-unit-economics
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filha/projecto + custos + preço` | string | Yes | filha/projecto + custos + preço |

## Output

- **unit economics + recomendação**: unit economics + recomendação

## Origin

Confidence: 88%
