---
task: "Auditar Processo"
responsavel: "@processos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - código PROC-… ou âmbito (filha / semana)
Saida: |
  - adesão, desvios, golden run, recomendações de kaizen (não aplica sozinho)
Checklist:
  - "[ ] Só processos activos ou piloto — rascunho não se audita como FBA"
  - "[ ] Cruzar spec com handoffs, Tasks Fibery, registo e golden run"
  - "[ ] ≥3 desvios iguais → recomendar *editar-processo"
  - "[ ] Caminho velho ainda mais fácil que o standard = FAIL de implementação"
  - "[ ] Handoff a kpis se a métrica não estiver a ser lida"
  - "[ ] Não reescrever o spec nesta task"
---

# *auditar-processo

Followed By All inclui agentes. Auditoria = o handbook é o que fazemos agora.

## Usage

```
@processos
*auditar-processo {PROC-…}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `código ou âmbito` | string | Yes | Processo ou `filha:BLI` / `semana` |

## Output

Relatório: corridas observadas, desvios, se o job aid está no ponto de uso, próxima acção (`editar` / `formar` / `ok`).
