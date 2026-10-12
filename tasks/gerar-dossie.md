---
task: "Gerar Dossie"
responsavel: "@docs"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - conteúdo dossiê de filha/constituição + identidade
Saida: |
  - HTML → PDF WeasyPrint → Drive + Fibery
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-dossie

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@docs
*gerar-dossie
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `conteúdo dossiê de filha/constituição + identidade` | string | Yes | conteúdo dossiê de filha/constituição + identidade |

## Output

- **HTML → PDF WeasyPrint → Drive + Fibery**: HTML → PDF WeasyPrint → Drive + Fibery

## Origin

Confidence: 92%
