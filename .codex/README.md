# Agentes Codex — Ellocene Ops

Os 17 agentes do manifesto estão instalados como subagentes Codex em `.codex/agents/`; as respectivas skills estão em `.agents/skills/`.

## Uso

Num chat aberto nesta pasta, peça explicitamente a delegação, por exemplo:

```text
Use [@guardiao](subagent://guardiao) para montar o cockpit da holding.
Use [@legal](subagent://legal) para preparar uma minuta de NDA angolana.
```

Pode também pedir ao Codex para usar um agente pelo nome, por exemplo: `Delegue esta análise de unit economics ao agente cfo.` Para fluxos mistos, comece por `guardiao`.

| Camada | Agentes |
|---|---|
| Orquestração | guardiao |
| Operação | actas, planos, registo, relatorios, docs, processos, governanca, portfolio, kpis |
| Jurídico | legal |
| Conselho | ceo, cfo, cto, cmo, chro, cro |

Valide a instalação com `npm run validate:codex-agents`. Reinicie a sessão do Codex se os perfis tiverem sido adicionados enquanto ela já estava aberta.
