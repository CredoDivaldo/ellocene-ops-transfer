# Protocolo de Handoff

Handoffs preservam continuidade entre agentes. Usar `npm run handoff -- create --from <agente> --to <agente> --command <comando> --summary <contexto> --next <acção>`.

## Campos obrigatórios

`from_agent`, `to_agent`, `created_at`, `last_command`, `priority`, `summary`, `next_action` e `consumed`. Incluir `context_paths` quando houver material local relevante.

## Regras

1. Escrever handoff quando uma decisão altera a prioridade de outro agente, um bloqueio atravessa domínios ou trabalho crítico fica pendente.
2. Consumir apenas depois de incorporar o contexto no plano ou estado do destinatário.
3. `critical` requer acção no dia; `high`, na próxima sessão; `medium`, na semana; `low`, continuidade informativa.
4. Usar guardiao como destino quando não houver dono inequívoco.

## Triggers principais

- guardiao delega ou consolida dependências; actas entrega decisões a planos/registo; planos sinaliza métricas a kpis.
- legal e governanca encaminham versões aprováveis a docs; docs devolve falhas de conteúdo ao originador.
- conselheiros enviam recomendações executáveis a guardiao; cfo, cmo e cro cruzam métricas com kpis.
