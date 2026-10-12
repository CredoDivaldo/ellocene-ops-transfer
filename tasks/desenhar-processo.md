---
task: "Desenhar Processo"
responsavel: "@processos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - objectivo + gatilho + filha (ou candidato vindo de *detectar)
Saida: |
  - process-spec YAML v0.1 + prosa canónica alinhada; estado rascunho
Checklist:
  - "[ ] Objectivo numa frase (resultado de cliente)"
  - "[ ] Trigger testável"
  - "[ ] DRI humano + papéis H/A/S com exactamente um A"
  - "[ ] 5–10 passos: verbo + objecto + ferramenta + critério de feito + seguinte"
  - "[ ] Comandos de agente existem no squad"
  - "[ ] Padrão de orquestração escolhido (um, ou misto justificado)"
  - "[ ] Excepções com default seguro; job aid 5–9 itens"
  - "[ ] Máximo 5 perguntas fechadas se faltar dado; senão recusar"
---

# *desenhar-processo

Cria o spec. Não documenta no Fibery (isso é `*documentar-processo`). Não promove.

Templates: `ellocene-ops/data/templates/processo-spec.yaml` e `processo-prosa.md`. Schema: `ellocene-ops/data/processo-schema.yaml`.

## Usage

```
@processos
*desenhar-processo {objectivo + gatilho + filha}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `objectivo + gatilho + filha` | string | Yes | O que muda no mundo, o que dispara, HOL/ALT/BLI/PYR/TIV |

## Output

YAML + prosa com ids `P1`… no outbox e, se MCP disponível, já pronto para `*documentar-processo`.

## Não feito se

Ensaio sem YAML; passo com comando inexistente; executar o processo; PDF.
