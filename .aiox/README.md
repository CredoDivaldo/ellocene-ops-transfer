# Runtime de Handoffs

Os handoffs são ficheiros YAML em `.aiox/handoffs/`. Criar com `npm run handoff -- create`, listar com `npm run handoff:list`, consumir com `npm run handoff -- consume` e validar com `npm run handoff:doctor`.

O handoff não substitui o estado do agente nem a fonte primária no Fibery; apenas torna explícita a continuidade entre sessões e domínios.
