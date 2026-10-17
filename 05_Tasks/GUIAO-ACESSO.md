# Guião de Acesso — Base Canónica ellocene-ops (VM)

**Tarefa:** TASK-2026-10-15-022 (P0) · **Dono:** DevOps · **Data:** 2026-10-16 00:52 UTC

## 1. Caminho na VM

- **Raiz:** `/workspace/ellocene-ops`
- **Dono:** DevOps (infraestrutura)
- **Grupo:** user (acesso comum)

## 2. Estrutura Canónica

| Pasta | Conteúdo |
|---|---|
| `00_INDEX.md` | Índice-mestre (protocolo LER PRIMEIRO) |
| `01_Knowledge/` | Base de conhecimento por área (`negocios/`, `financas/`, `tecnologia/`, `marketing/`, `governanca/`, `legal/`, `clientes/`, `_logs/`, `_scripts/`, `_staging/`) |
| `02_Processes/` | Processos repetíveis (registados no Fibery) |
| `03_Workflows/` | Fluxos de trabalho específicos |
| `04_Agents/` | System prompts de cada Tiv (18 prompts) |
| `05_Tasks/` | Estado da fila de tarefas (inclui `GUIAO-ACESSO.md`) |
| `06_Governance/` | Governança e decisões da holding |
| `07_Outputs/` | Entregáveis finais (PDFs, planos) |
| `scripts/` | Scripts de sincronização (`sync.sh`, `INSTALAR-SYNC.md`) |
| `backup/` | Reserva de conhecimento local (preservado) |

## 3. Protocolo LER PRIMEIRO (versão MCP 2.0)

> Decisão do Credo (17/10): o canal canónico é o **MCP** — conector GitHub (operação) + conector Fibery (registo). A VM saiu do caminho crítico.

Para qualquer ação do squad, cada Tiv deve:

1. **Pré-leitura pelo conector GitHub:**
   ```
   connector_call github get_file_contents {"owner":"Altars-Group","repo":"ellocene-ops","path":"00_INDEX.md"}
   ```

2. **Ler a área aplicável** (mesmo conector):
   - CMO: `01_Knowledge/marketing/00_INDEX.md`
   - CFO: `01_Knowledge/financas/00_INDEX.md`
   - CTO: `01_Knowledge/tecnologia/00_INDEX.md`
   - ...etc.

3. **Ler o prompt do seu role:** `04_Agents/<tiv-slug>.md` (conector GitHub).

4. **Processos/registos/decisões:** conector Fibery.

5. **Se o conector falhar:** reportar com o **erro cru** ao Guardião. **Nunca parar por causa de um `git pull`.**

## 4. Como Escrever na Base

**Canal canónico (MCP):**
```
connector_call github create_or_update_file {"owner":"Altars-Group","repo":"ellocene-ops","path":"<path>","content":"<conteúdo>","message":"<descrição>","branch":"main"}
```
Para vários ficheiros de uma vez: `connector_call github push_files`.

**Via de recurso (VM, P3 — fora do caminho crítico):** `git add` + `git commit` + `git push` em `/workspace/ellocene-ops`, só quando o MCP não servir e houver credencial.
- **Deploy key SSH (P3, bloqueada pela org):** `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKLf1zceHIJb92oCh/6r/EN3SEjQKNbi6puUyu/e3IL7 devops-vm-ellocene-ops` — registo devolve HTTP 422 «Deploy keys are disabled for this repository».

## 5. Sincronização Automática

O script `scripts/sync.sh` mantém a VM alinhada com o GitHub (5 minutos):

```bash
# Instalar via systemd (recomendado):
sudo cp /workspace/ellocene-ops/scripts/sync.sh /usr/local/bin/ellocene-ops-sync.sh
sudo chmod +x /usr/local/bin/ellocene-ops-sync.sh
sudo cp /tmp/ellocene-ops-sync.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now ellocene-ops-sync.timer

# Ver logs:
tail -n 40 /var/log/ellocene-ops-sync.log

# Testar manualmente:
/workspace/ellocene-ops/scripts/sync.sh
```

**Estado atual (2026-10-16 00:52 UTC):**
- `sync.sh` instalado e testado.
- systemd timer **instalado** (ficheiro pronto, mas serviço não ativado devido à credencial GitHub).
- Logs em `/var/log/ellocene-ops-sync.log` mostram: "ERRO: sem credencial GitHub".

## 6. Diagnóstico de Bloqueio

Se `git push` falhar com `Permission denied (publickey)` ou `fatal: could not read Username`, a causa é:

1. **Deploy key SSH não registada no GitHub** (`CredoDivaldo/ellocene-ops` → Settings → Deploy keys).
2. **Token HTTPS não configurado** no ambiente da VM.

**Prova:**
```bash
ssh -T git@github.com
# Resultado: Permission denied (publickey)

git ls-remote origin
# Resultado: fatal: could not read Username for 'https://github.com'
```

## 7. Recuperação

Se a VM ficar desalinhada com o GitHub:

1. **Canal canónico:** usar o conector GitHub (`tivra-team connector-call github push_files`) para ler/escrever no repo remoto.
2. **Via de recurso:** com credencial, `git pull --rebase origin main` → `git push origin main` (P3).

## 8. Prova de Funcionamento

```bash
cd /workspace/ellocene-ops
git rev-parse --abbrev-ref HEAD           # main
ls -d 0*_*                                 # 7 pastas principais
test -f 00_INDEX.md && echo OK            # OK
git remote -v                             # origin  https://github.com/...
find . -maxdepth 2 -type f | wc -l        # ~200 ficheiros
```

---

**Versão:** 1.0 · **Registado no:** `/workspace/ellocene-ops/05_Tasks/GUIAO-ACESSO.md`