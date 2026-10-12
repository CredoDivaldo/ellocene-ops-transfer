---
task: "Gerar Proposta"
responsavel: "@docs"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - conteúdo proposta + cliente + identidade
Saida: |
  - HTML → PDF WeasyPrint → Drive + Fibery Document (Tipo: Proposta Comercial)
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-proposta

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@docs
*gerar-proposta
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `conteúdo proposta + cliente + identidade` | string | Yes | conteúdo proposta + cliente + identidade |

## Output

- **HTML → PDF WeasyPrint → Drive + Fibery Document (Tipo: Proposta Comercial)**: HTML → PDF WeasyPrint → Drive + Fibery Document (Tipo: Proposta Comercial)

## Origin

Confidence: 93%
