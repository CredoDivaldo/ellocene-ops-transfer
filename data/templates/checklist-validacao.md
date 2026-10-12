# Checklist de validação — process-spec v1

Pass/fail binário. Qualquer FAIL bloqueia `*promover-processo`.

## Schema
- [ ] `id` no formato `PROC-<FILHA|HOL>-<slug>`
- [ ] `versao`, `estado`, `titulo`, `empresa_filha`
- [ ] `dono_humano` preenchido (humano, não agente)
- [ ] `trigger.tipo` + `trigger.descricao` testável
- [ ] `padrao` da lista fechada
- [ ] `entrada` e `saida` com artefactos nomeados
- [ ] `criterio_feito` do processo (não só dos passos)
- [ ] `gate_promocao` humano

## Passos
- [ ] Cada passo tem `id` (`P1`…), actor_tipo, actor, ferramenta, criterio_feito
- [ ] Cada passo tem teste embutido OU critério de feito observável (Spear-Bowen: o problema assinala-se sozinho)
- [ ] Ligação entre passos é sim/não (pedido e resposta sem ambiguidade)
- [ ] Passo `agente` tem `comando` que existe em `ellocene-ops/agents/<actor>.md`
- [ ] Exactamente um Accountable (A) no processo
- [ ] Agente não é A de gate jurídico/societário/assinatura/pagamento
- [ ] `seguinte` forma um grafo acíclico até FIM (salvo loop explícito justificado)
- [ ] `overreach: true` recusado
- [ ] 5–10 passos no núcleo (20/80); mais = partir o processo

## Alinhamento
- [ ] Cada id de passo na prosa existe no YAML e vice-versa
- [ ] Job aid tem 5–9 itens extraídos, não inventados — é o que o executor corre no pause point, não a folha TWI do instrutor
- [ ] Ramos têm default seguro
- [ ] Sem `file://` nem paths locais em campos de link

## Implementação
- [ ] Trigger vive no sítio do trabalho (comando, handoff, Fibery) — não só no Drive
- [ ] Caminho velho identificado (deprecar ou bloquear)
- [ ] PDF `@docs` NÃO é a fonte
- [ ] Estado ≠ `activo` até gate do Credo
