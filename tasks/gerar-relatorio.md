---
task: "Gerar Relatorio"
responsavel: "@docs"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - conteúdo estruturado de @relatorios + identidade
Saida: |
  - HTML → PDF WeasyPrint → Drive ELLOCENE + Fibery Document
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-relatorio

Task generated from squad design blueprint for ellocene-ops.

> **Regra inegociável:** todo e qualquer relatório destinado a um CLIENTE é entregue em **PDF** (WeasyPrint). `.md` é rascunho interno — nunca vai para a pasta do cliente. Gravar `.pdf` (+ `.html` fonte) na pasta do cliente; nunca `.md`.

## Usage

```
@docs
*gerar-relatorio
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `conteúdo estruturado de @relatorios + identidade` | string | Yes | conteúdo estruturado de @relatorios + identidade |

## Output

- **HTML → PDF WeasyPrint → Drive ELLOCENE + Fibery Document**: HTML → PDF WeasyPrint → Drive ELLOCENE + Fibery Document

## Origin

Confidence: 95%
