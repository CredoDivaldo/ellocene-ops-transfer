---
task: "Gerar Docx"
responsavel: "@docs"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - conteúdo + tipo + identidade (minutas, contratos, propostas editáveis)
Saida: |
  - DOCX via pandoc/python-docx com identidade configurada + Drive + Fibery
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-docx

Task generated from squad design blueprint for ellocene-ops.

> **Regra inegociável:** todo e qualquer documento destinado a um CLIENTE é entregue em **PDF** (o DOCX é para edição interna/minutas colaborativas). Para envio ao cliente, gerar também o `.pdf` via WeasyPrint. `.md` é rascunho interno — nunca vai para a pasta do cliente.

## Usage

```
@docs
*gerar-docx
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `conteúdo + tipo + identidade (minutas, contratos, propostas editáveis)` | string | Yes | conteúdo + tipo + identidade (minutas, contratos, propostas editáveis) |

## Output

- **DOCX via pandoc/python-docx com identidade configurada + Drive + Fibery**: DOCX via pandoc/python-docx com identidade configurada + Drive + Fibery

## Origin

Confidence: 93%
