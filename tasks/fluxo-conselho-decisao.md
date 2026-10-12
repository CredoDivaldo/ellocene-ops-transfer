---
task: "Fluxo Conselho Decisao"
responsavel: "@guardiao"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - pedido de conselho (ex: 'devo criar empresa X?', 'como entrar no mercado Y?')
Saida: |
  - cadeia: @ceo (aconselhar) [+ @cfo se financeiro, @cmo se marketing, @cto se tech, @chro se pessoas, @cro se receita] → consolidação → gate Credo → @governanca (decisão formal) → @legal (se efeito legal) → @docs (memorando/acta PDF/DOCX) → Governança
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *fluxo-conselho-decisao

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@guardiao
*fluxo-conselho-decisao
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pedido de conselho (ex: 'devo criar empresa X?', 'como entrar no mercado Y?')` | string | Yes | pedido de conselho (ex: 'devo criar empresa X?', 'como entrar no mercado Y?') |

## Output

- **cadeia: @ceo (aconselhar) [+ @cfo se financeiro, @cmo se marketing, @cto se tech, @chro se pessoas, @cro se receita] → consolidação → gate Credo → @governanca (decisão formal) → @legal (se efeito legal) → @docs (memorando/acta PDF/DOCX) → Governança**: cadeia: @ceo (aconselhar) [+ @cfo se financeiro, @cmo se marketing, @cto se tech, @chro se pessoas, @cro se receita] → consolidação → gate Credo → @governanca (decisão formal) → @legal (se efeito legal) → @docs (memorando/acta PDF/DOCX) → Governança

## Origin

Confidence: 88%
