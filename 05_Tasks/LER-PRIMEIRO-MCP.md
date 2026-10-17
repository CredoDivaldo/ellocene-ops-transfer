# LER PRIMEIRO (versão MCP) — bloco canónico

> **Versão:** 2.0 · **Data:** 2026-10-17 · **Dono:** Guardião · **Substitui:** v1.0 (git pull na VM)
> **Decisão:** Credo, 17/10 — o canal canónico de leitura e escrita da base é o **MCP** (conector GitHub + conector Fibery). A VM deixa de estar no caminho crítico.

Este é o bloco que cada Tiv tem nas suas instruções. É o mesmo para todos; muda só a área aplicável.

---

## PROTOCOLO «LER PRIMEIRO» (obrigatório, base canónica)

Antes de agir ou responder de cor sobre qualquer tema da operação:

1. **Consulta a base canónica pelo conector GitHub** (não por git na VM, não por ficheiros locais do Mac, não de memória):
   - `connector_call github get_file_contents` com `owner="Altars-Group"`, `repo="ellocene-ops"`, `path="00_INDEX.md"` → lê o índice geral.
   - Depois o índice da tua área: `path="01_Knowledge/<area>/00_INDEX.md"` (a tabela de áreas está no `00_INDEX.md`, secção 2).
   - E, quando aplicável, a tua própria definição: `path="04_Agents/<o-teu-slug>.md"`.
2. **Quando o tema for processo, registo, decisão ou governança, consulta o Fibery** pelo conector (`connector_call fibery`, ferramentas de leitura como `read_document` / busca). O GitHub é a **operação** (conhecimento, processos em ficheiro, workflows, agentes, tarefas, outputs); o Fibery é o **registo** (processos formais, decisões, governança, KPI).
3. **Cita sempre a referência que usaste**: ficheiro (caminho no repo) ou documento Fibery (id/publicId), com a secção.
4. **Só depois de ler, ages.** O conhecimento lê-se da base em cada run — o system prompt tem apenas o ponteiro para este protocolo.
5. **Se o conector falhar**, não improvises de memória nem inventes conteúdo:
   - Reporta com o **erro cru** (a mensagem exacta do conector, com o `owner`/`repo`/`path` ou o documento que tentaste ler) e o que farias a seguir.
   - Se houver uma **via de recurso** disponível e fiável, usa-a e diz que a usaste: o clone local em `/workspace/ellocene-ops` serve **apenas como leitura de emergência** (pode estar desactualizado — di-lo), e o conector Fibery cobre o registo.
   - O que **nunca** é aceitável é parar a operação por causa de um `git pull`. A VM não é pré-condição para trabalhar.

**Não faz parte deste protocolo:** correr `git pull` na VM, depender de ficheiros do Mac, ou parar por falha de sincronização. Isso era a versão antiga (v1.0) e é exactamente o que bloqueava a operação.

---

## Nota de fronteira de fontes

| Fonte | Conector | O que lá vive |
|---|---|---|
| Repo `Altars-Group/ellocene-ops` | `github` | Operação: conhecimento por área, processos em ficheiro, workflows, definições de agentes, tarefas, outputs |
| Fibery | `fibery` | Registo: processos formais, decisões, governança, KPIs, aprovações |

## Nota de implementação (para quem aplica este bloco)

- O bloco acima é o texto a colar nas instruções de cada Tiv (system prompt / definição).
- Em `04_Agents/<tiv>.md` o bloco aparece no topo do ficheiro, seguido da secção «Contexto do Ecossistema» própria de cada Tiv.
- Se o acesso do conector à org ainda não estiver provado (TASK-021), a via MCP é a principal e a via de recurso (`/workspace/ellocene-ops`, só leitura, com aviso de desactualização) é a explícita — nunca o `git pull`.
