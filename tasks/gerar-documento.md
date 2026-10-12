---
task: "Gerar Documento"
responsavel: "@docs"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - conteúdo + tipo + identidade (holding ou filha)
Saida: |
  - router para task específica ou documento genérico
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-documento

Task generated from squad design blueprint for ellocene-ops.

> **Regra inegociável:** todo e qualquer documento destinado a um CLIENTE é entregue em **PDF** (WeasyPrint). `.md` é rascunho interno — nunca vai para a pasta do cliente. Gravar `.pdf` (+ `.html` fonte) na pasta do cliente; nunca `.md`.

## Usage

```
@docs
*gerar-documento
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `conteúdo + tipo + identidade (holding ou filha)` | string | Yes | conteúdo + tipo + identidade (holding ou filha) |

## Output

- **router para task específica ou documento genérico**: router para task específica ou documento genérico

## Origin

Confidence: 94%
