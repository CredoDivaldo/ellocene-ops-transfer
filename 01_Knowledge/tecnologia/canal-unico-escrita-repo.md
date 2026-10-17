> **⚠ REVOGADO pelo PIVOT de 17/10 (Credo).** Esta decisão (canal único = git da VM) foi substituída: o canal canónico de leitura/escrita da base passa a ser o **MCP** (conector GitHub + conector Fibery). A VM sai do caminho crítico. Mantém-se como registo histórico. Ver `05_Tasks/LER-PRIMEIRO-MCP.md`.

# Canal único de escrita do repo canónico — decisão de arquitectura

**Área:** tecnologia · **Dono:** CTO · **Estado:** v1.0 (2026-10-16) · **Tarefa:** TASK-2026-10-15-021
**Responde a:** SIG-2026-10-16-035 (Guardião)

---

## 1. Contexto (factos verificados, não hipóteses)

Dois canais escreveram no mesmo repo em paralelo:

| Canal | Estado | Autoria dos commits | Prova |
|---|---|---|---|
| Conector GitHub da plataforma | Funciona | `credolopes@icloud.com` (o Credo) | commits `ca104dc`, `28f225c`, `c72f9f8` |
| git da VM (`/workspace/ellocene-ops`) | Escrita local OK, **push bloqueado** | por Tiv (`@ellocene.local`) | 3+ commits locais, `origin` sem credencial |

Diagnóstico na VM (2026-10-16):
- `ssh -T git@github.com` → `Permission denied (publickey)` — deploy key **não registada**.
- `ellocene-ops-sync.service` → `failed (exit-code 2)`; log: «sem credencial GitHub. Sync impossivel.»
- Timer activo, dispara a cada 5 min e falha sempre.
- `origin` aponta para `git@github.com:Altars-Group/ellocene-ops.git` (nota: o repo foi movido de `CredoDivaldo/` para `Altars-Group/` — confirmar que é intencional).
- Identidade global do git na VM já corrigida: `DevOps (Tiv) <devops@ellocene.local>`.

**Consequência:** as duas árvores divergiram. O primeiro push da VM pode conflituar.

---

## 2. Decisão — canal único de escrita: **git da VM**

O conector GitHub **deixa de escrever** no `ellocene-ops`.

Razões:
1. O protocolo LER PRIMEIRO exige que a base funcione **sem a plataforma** — se só se escreve com a plataforma viva, o objectivo do projecto falha.
2. O conector publica **como o Credo**, apagando a autoria de cada Tiv; o git da VM assina por Tiv e mantém audit legível.
3. Escrever «por título» já provou hoje, no Fibery, que apanha a entidade errada — num repo isso vira ficheiros duplicados.
4. O timer de sync já está construído para o git da VM. Fecha-se o que já existe.

**Excepção — leitura:** o conector **continua autorizado a ler** o repo (é o caminho rápido para conferir conteúdo). Proibido é **escrever** por lá.

---

## 3. Procedimento de reconciliação (executar SÓ depois da deploy key entrar)

```bash
# 0. Pré-requisito: a chave está registada?
ssh -T git@github.com                      # deve responder: Hi <conta>!

cd /workspace/ellocene-ops

# 1. Ponto de retorno — nada se perde
git add -A && git commit -m "WIP: snapshot VM antes da reconciliacao" || true
git tag pre-reconciliacao-2026-10-16

# 2. Trazer o remoto e ligar o tracking
git fetch origin
git branch --set-upstream-to=origin/main main

# 3. Medir a divergência ANTES de mexer
git rev-list --left-right --count main...origin/main   # X  Y  = só-local  só-remoto

# 4. Rebase (nunca merge cego: mantém histórico linear e legível)
git pull --rebase origin main
# conflitos: resolver um a um -> git add <f> -> git rebase --continue

# 5. Publicar e confirmar
git push -u origin main
git fetch origin && git rev-list --left-right --count main...origin/main   # deve dar: 0  0
```

**Trava de segurança (obrigatória):** antes do `push`, o DevOps envia ao CTO a saída do `rev-list --left-right --count`. Se **não** der `0 0`, **parar** e resolver os conflitos com o CTO antes de rebasear. Ninguém faz `push` sem essa contagem.

---

## 4. Regra de desempate em conflito

**Pendente de decisão do Guardião** (política do squad, não arquitectura). Proposta do CTO:

- **Conhecimento e índices** (`01_Knowledge/`, `00_INDEX.md`): **vence a VM** — é onde o squad trabalhou e tem mais conteúdo.
- **Restantes ficheiros**: **vence o commit do Credo** — foi publicado pelo dono, tem precedência.

Enquanto não houver decisão, **não se empurra nada da VM**.

---

## 5. O que isto destranca

- **TASK-022** deixa de estar bloqueada por arquitectura — só falta a deploy key (APR-2026-10-16-005).
- **TASK-027** (prompts) continua válida: o método é exactamente este canal (clone git + pull na VM).
- **TASK-021** fecha com esta decisão registada.

---

## 6. Acções

1. ~~Registar esta decisão no repo~~ — este ficheiro.
2. Ligar ao índice-mestre (`00_INDEX.md`) e ao índice da área tecnologia.
3. Estender o doc 166 do Fibery com esta decisão.
4. Passar o procedimento ao DevOps + proibição de escrita pelo conector.
5. Confirmar com o Credo se a mudança de `CredoDivaldo/` para `Altars-Group/` é intencional.
