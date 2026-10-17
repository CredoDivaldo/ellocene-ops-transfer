# Skill: consultar-base-canonica

## Quem é?
- **Tiv:** Guardião
- **Propósito:** Garante que cada Tiv lê a base canónica antes de agir, conforme o protocolo LER PRIMEIRO.

## Quando usar esta skill?
- Antes de agir em qualquer tarefa relacionada com a operação do squad.
- Quando o Tiv precisa de referência sobre processos, áreas ou áreas de conhecimento.
- Quando o Tiv não tem certeza sobre o que está escrito na base canónica (GitHub).

## Como usar (passos)

### 1. Ler o protocolo LER PRIMEIRO (obrigatório) — versão MCP 2.0
```
connector_call github get_file_contents {"owner":"Altars-Group","repo":"ellocene-ops","path":"00_INDEX.md"}
```
(Não uses `git pull` na VM: o canal canónico é o conector GitHub.)

### 2. Identificar a área do Tiv
Consulte a tabela de áreas no `00_INDEX.md` (seção 2). O dono de cada área é o Tiv responsável.

### 3. Ler o índice da área
```
connector_call github get_file_contents {"owner":"Altars-Group","repo":"ellocene-ops","path":"01_Knowledge/<area>/00_INDEX.md"}
```

### 4. Ler a referência específica (se aplicável)
- Para agentes: `04_Agents/<tiv-slug>.md` (conector GitHub)
- Para processos/registos/decisões/governança: **conector Fibery** (`connector_call fibery`)
- Para tarefas: fila de tarefas da equipa (`tivra-team tasks`)

### 5. Agir só depois de ter lido
- Nunca agir de memória.
- Se o conector falhar, reporta com o **erro cru** ao Guardião. Via de recurso: clone local `/workspace/ellocene-ops` só como leitura de emergência (pode estar desactualizado). **Nunca pares por causa de um `git pull`.**

## Exemplo de uso

Suponha que estás a trabalhar na área de **Negócios** (CEO).

1. `connector_call github get_file_contents {"owner":"Altars-Group","repo":"ellocene-ops","path":"00_INDEX.md"}` — lê o protocolo e a tabela de áreas.
2. `connector_call github get_file_contents {"owner":"Altars-Group","repo":"ellocene-ops","path":"01_Knowledge/negocios/00_INDEX.md"}` — lê o índice de negócios.
3. Agora que sabes o que está escrito, prossegue com a tarefa.

## Regras de erro
- **Sem ler a base pelo conector antes de agir:** erro — o conhecimento pode estar desactualizado.
- **Não ler o `00_INDEX.md` antes de agir:** erro — o protocolo LER PRIMEIRO não foi seguido.
- **Conector a falhar sem reportar o erro cru:** erro — reporta o erro exacto; não improvises de memória.

## Prova de funcionamento
- `connector_call github get_file_contents {"owner":"Altars-Group","repo":"ellocene-ops","path":"00_INDEX.md"}` → devolve o índice
- `connector_call github get_file_contents {"owner":"Altars-Group","repo":"ellocene-ops","path":"04_Agents"}` → devolve a lista de agentes

---

**Versão:** 2.0 · **Data:** 2026-10-17 · **Dono:** Guardião · **Substitui:** v1.0 (git pull na VM)