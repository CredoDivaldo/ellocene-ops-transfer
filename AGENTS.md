# Ellocene Ops — instruções para Codex

## Âmbito e fontes de verdade

Este repositório é o squad operacional da holding Ellocene. `squad.yaml` é o manifesto; `agents/<nome>.md`, `tasks/` e `data/` são as fontes canónicas do domínio. As skills correspondentes vivem em `.agents/skills/`.

## Activação

Use primeiro `guardiao` para pedidos transversais, cockpit ou delegação. Para domínios inequívocos, use o subagente especializado em `.codex/agents/` e a skill homónima. Cada perfil deve ler a sua skill e agente canónico antes de agir. A lista e os exemplos de activação estão em `.codex/README.md`.

## Guardrails operacionais

- Consulte a configuração em `config/` e as normas documentais antes de criar ou publicar informação.
- O Fibery é a fonte primária para informação operacional. Ficheiros Markdown locais são contingência, salvo pedido explícito do operador.
- `docs` é o único agente que emite PDF/DOCX. Todo deliverable externo para cliente deve ser PDF e requer a identidade da empresa emitente.
- `legal` investiga e redige, mas não substitui a revisão humana nem autoriza assinatura. `governanca` não confirma deliberações sem o gate humano exigido.
- Não invente dados, decisões, cláusulas, métricas, ligações ou fontes. Registe bloqueios e encaminhe-os ao `guardiao`.

## Validação

Depois de alterar perfis, execute `npm run validate:codex-agents`.
