---
task: "Editar Processo"
responsavel: "@processos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - código PROC-… + delta (o que muda e porquê)
Saida: |
  - nova versão em rascunho; activo intocado
Checklist:
  - "[ ] Localizar spec actual (Fibery Document Runbook ou outbox)"
  - "[ ] Activo nunca é reescrito in-place — bump versao, estado rascunho"
  - "[ ] Changelog na prosa (versão, data, diff, motivo)"
  - "[ ] Revalidar schema e alinhamento YAML/prosa"
  - "[ ] Se o delta tocar comando inexistente ou gate jurídico, recusar ou handoff"
---

# *editar-processo

Kaizen do standard. Quem executa altera o standard; não improvisa em silêncio.

## Usage

```
@processos
*editar-processo {PROC-…} {delta}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `código` | string | Yes | `PROC-<FILHA\|HOL>-<slug>` |
| `delta` | string | Yes | O que muda e o motivo de negócio |

## Output

Spec vN+1 em rascunho. O Document activo permanece até `*promover-processo`.

## Não feito se

Patch no activo; prosa sem bump de versão; executar o processo.
