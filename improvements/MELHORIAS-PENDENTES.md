# Melhorias Pendentes — Squad ellocene

> Problemas detectados em execução real. Cada item tem origem, impacto e acção correctiva proposta.
> Quando implementares uma melhoria, marca o item como **RESOLVIDO <data>** e descreve o que foi feito (padrão inspirado no squad ops-md).

---

## [IMP-001] guardiao *delegar — Relatórios devem usar SEMPRE o logo oficial SVG da marca

**RESOLVIDO 2026-08-24** — Modelo oficial (`ellocene-ops/tasks/gerar-relatorio.md` → reencaminhar para o template `EmpresasFilhas/Blimari/07-Operacoes/Processos/Modelos/Relatorio-Produtividade-Diario-Modelo.html`) agora exige logo oficial SVG embutido, ® incluído, fundo creme total, corpo ≥11pt, headings proeminentes e contactos no rodapé fixo. Ver `Registo-Operacional.md` (Blimari) para o padrão completo.

**Ficheiro:** `ellocene-ops/tasks/gerar-relatorio.md` (fluxo de relatórios); produção real em `EmpresasFilhas/Blimari/04-Clientes/<Cliente>/03-Comunicacoes/`
**Detectado em:** Execução de relatório de verificação Google — Colégio São Filipe Sermão (2026-08-24)
**Impacto:** ALTO — documento oficial saiu sem logo da marca (só texto "Blimari."); risco de imagem e inconsistência com o Design System v1.0 da Blimari

**Problema:**
O relatório gerado usava texto "Blimari." em vez do logo oficial (`05-Marketing/Assets_Marca/logo/signature/Blimari signarutre logo 5.svg`). Também: sem fundo creme total, sem ®, corpo pequeno e contactos fora do rodapé fixo.

**Acção correctiva:**
Sempre que um fluxo gerar relatórios oficiais, usar o modelo oficial com todas as regras:
- Logo oficial SVG embutido (nunca texto "Blimari."); nunca remover o ®
- Fundo creme `#FAF6F1` em TODA a página via `@page` (nunca borda branca)
- Corpo ≥11pt; headings 14.5pt+ uppercase com sublinhado laranja `#FF6A00`
- Contactos sempre no rodapé fixo (`@bottom-center`), nunca por baixo do texto
- Máximo 1 página A4; secções curtas "Feito hoje · Estado · Precisamos de si"; sem redundância

---

## [IMP-002] guardiao *delegar — Relatórios deviam ser concisos (1 página) por defeito

**RESOLVIDO 2026-08-24** — Template oficial impõe 1 página A4 e 3 secções curtas. Ficou no padrão de relatórios.

**Ficheiro:** `ellocene-ops/tasks/fluxo-completo-relatorio.md` / `ellocene-ops/tasks/relatorio-filha.md`
**Detectado em:** Relatório do Colégio (2026-08-24) — versão inicial tinha ~300 palavras em 4 secções; o dono do colégio não leria tudo
**Impacto:** MÉDIO — relatórios longos perdem o sentido; cliente atarefado abandona a leitura

**Problema:**
Relatório inicial: secção "valor do que foi feito" redundante com o "estado"; lista de configuração detalhada repetida.

**Acção correctiva:**
Relatórios de estado = máximo 1 página: "Feito hoje" (1–2 frases), "Estado" (callout com prazo/condição), "Precisamos de si" (pedidos ao cliente). Sem secção de valor repetida (o estado já comunica o que importa).

---

## [IMP-003] Melhorias do fluxo guardiao — guardar contexto de cliente/produtos para o catálogo Google

**PENDENTE** — a implementar quando se fizer o catálogo Google.

**Ficheiro:** `ellocene-ops/tasks/fluxo-completo-relatorio.md` (ou criar task dedicada) · `ellocene-ops/data/`
**Detectado em:** Relatório do Colégio (2026-08-24) — pedimos logótipo + produtos (propinas, inscrição/matrícula, uniformes) para criar catálogo
**Impacto:** MÉDIO — sem registo, o próximo passo (catálogo com preços) perde o contexto

**Problema:**
O relatório pede ao cliente logótipo e produtos/preços, mas não há ficheiro padrão de recolha por cliente (o SOP P2 da Blimari prevê Anexo C/D). Ao chegar a altura de criar o catálogo Google (P3, passo 5), a informação pode falta.

**Acção correctiva:**
Criar um ficheiro de recolha de dados por cliente (ex.: `EmpresasFilhas/Blimari/04-Clientes/<Cliente>/99-Anexos/produtos-catalogo.md`) com campos: logótipo (ficheiro), produtos (nome, preço, categoria — propinas, inscrição/matrícula, uniformes, outros) e estado da recolha. Ligar ao fluxo de relatórios.

---

## [IMP-004] guardiao — Não verifica identidade visual por empresa antes de gerar documentos

**RESOLVIDO 2026-08-24** — a partir da correcção do relatório do colégio, o padrão de relatórios referencia a identidade por empresa (`ellocene-ops/data/identidades-empresas.yaml`) e o @docs usa o logo oficial por marca.

**Ficheiro:** `ellocene-ops/tasks/gerar-relatorio.md`
**Detectado em:** mesma execução do IMP-001
**Impacto:** MÉDIO — risco de documento de uma filha sair com a marca de outra (problema identificado no `identidades-empresas.yaml`: "um documento Blimari NUNCA deve parecer um documento Altars ou Tivra")

**Problema:**
O fluxo de relatório não obrigava a consultar `identidades-empresas.yaml` antes de gerar (logo, paleta, tipografia por empresa).

**Acção correctiva:**
Antes de gerar qualquer documento de filha, consultar `ellocene-ops/data/identidades-empresas.yaml` e usar a identidade da empresa (tokens/logo da pasta `05-Marketing/Brand-Book/`). Se não houver identidade definida → usar a da Holding; nunca inventar marca.

---

## [IMP-005] guardiao — Fluxo de relatório não registava rasto operacional por cliente

**RESOLVIDO 2026-08-24** — criado `EmpresasFilhas/Blimari/07-Operacoes/Registo-Operacional.md` com o padrão de relatórios e registo de acções por cliente (alinhado ao SOP P3 passo 7).

**Ficheiro:** `ellocene-ops/tasks/fluxo-completo-relatorio.md`
**Detectado em:** Execução de relatório do colégio (2026-08-24) — sem registo de acções
**Impacto:** MÉDIO — governança ("TUDO é auditável, deixa rasto") exigia registo; sem ele, perde-se histórico e pendências (videochamada no 4.º dia, recolha de produtos)

**Problema:**
Após gerar o relatório, não havia registo operacional (ex.: onde registar "no 4.º dia submeter videochamada" / "aguardando logótipo e produtos").

**Acção correctiva:**
Criar/actualizar um `Registo-Operacional.md` por empresa em `07-Operacoes/`, com: data, cliente, acção, estado, entregável. Registar pendências com datas-alvo (gatilhos futuros).

---

## [IMP-006] relatorios — Falta comando/tarefa para relatório de execução diário/semanal por cliente, para qualquer empresa do grupo

**PENDENTE** — a implementar.

**Ficheiro:** `ellocene-ops/agents/relatorios.md` + criar task dedicada em `ellocene-ops/tasks/` (ex.: `relatorio-execucao.md`)
**Detectado em:** Execução real 2026-08-25 — relatório de estado do Colégio São Filipe Sermão (BLI) gerado manualmente, sem comando dedicado
**Impacto:** MÉDIO-ALTO — cada relatório de execução é hoje montado caso a caso (copiando o modelo, recolhendo contexto manualmente); sem comando/task oficial, o fluxo é lento, depende de contexto do operador e não está padronizado para o grupo.

**Problema:**
O agente `relatorios` tem comandos para relatório de holding, de filha, de investidor, listar fontes e state-of-the-union, mas **não tem um comando/tarefa para gerar relatórios de execução diários/semanais para clientes** — o tipo de relatório mais frequente na operação (ex.: relatório de estado de verificação Google enviado a um cliente). Não existe task `relatorio-execucao` (ou equivalente) que aceite:
- a **empresa do grupo** (ex.: Blimari),
- o **cliente** (ex.: Colégio São Filipe Sermão),
- o **período** (dia/semana),
- e o **que foi feito ao longo do período** — OU que **verifique automaticamente** os registos diários (`Registo-Operacional.md` de cada empresa em `07-Operacoes/`) e as **tarefas no Fibery** para compor o "Feito hoje/esta semana".

Hoje isso é feito manualmente: houve que localizar a pasta do cliente, ler a proforma, o relatório anterior e o registo operacional para reconstruir o contexto.

**Acção correctiva:**
1. Criar task `ellocene-ops/tasks/relatorio-execucao.md` (responsável: `@relatorios`) com entrada: `empresa + cliente + período [+ descrição do que foi feito]`.
2. No fluxo: se o operador fornecer o que foi feito, usar directamente; senão, **consultar automaticamente** o `Registo-Operacional.md` da empresa (em `EmpresasFilhas/<Empresa>/07-Operacoes/`) filtrando por cliente + período, e/ou as tarefas do Fibery (base `Ellocene/*`, campo cliente/empresa) para o mesmo período.
3. Adicionar o comando `*relatorio-execucao` a `ellocene-ops/agents/relatorios.md` e à listagem de comandos da skill `/relatorios`.
4. Reutilizar o padrão oficial de relatório (1 página A4, identidade da empresa via `ellocene-ops/data/identidades-empresas.yaml`, registo no `Registo-Operacional.md` da empresa).

---

## [IMP-007] docs — Todo e qualquer documento enviado a um CLIENTE deve ser SEMPRE PDF (nunca .md)

**PENDENTE** — a enraizar nos agentes e skills.

**Ficheiro:** `ellocene-ops/agents/docs.md` + `ellocene-ops/agents/relatorios.md` + skills `ellocene-ops/.agents/skills/docs/SKILL.md`, `ellocene-ops/.agents/skills/relatorios/SKILL.md` + router `ellocene-ops/.agents/skills/ellocene-ops/SKILL.md` + `ellocene-ops/tasks/gerar-relatorio.md` (e tasks de documentos em geral)
**Detectado em:** Execução real 2026-08-26 — relatório de implementação da Raquel Comercial gerado em `.md` e guardado em `03-Comunicacoes/`; o operador corrigiu: "De nada me serve um .md para enviar a um cliente."
**Impacto:** ALTO — um `.md` não é enviável a um cliente final; gera retrabalho (regenerar em PDF) e quebra a imagem profissional da filha.

**Problema:**
A regra de que deliverables para clientes são SEMPRE PDF existia apenas implicitamente (o template oficial de fatura/relatório é HTML→PDF via WeasyPrint), mas não estava enraizada como instrução explícita no agente `docs`, no agente `relatorios`, nem nas skills. Resultado: o fluxo produziu um `.md` para a pasta do cliente, quando o único artefacto útil é o `.pdf` (acompanhado, opcionalmente, do `.html` fonte para edição futura).

**Acção correctiva:**
1. Enraizar a regra no agente `docs` (produtor de artefactos visuais): **todo e qualquer documento destinado a um cliente é entregue em PDF**; `.md` é apenas rascunho interno, nunca vai para a pasta do cliente.
2. Enraizar a mesma regra no agente `relatorios` (que "NÃO produz PDFs — delega ao @docs"): ao delegar, instruir o `@docs` a entregar PDF.
3. Reforçar nas skills `docs`, `relatorios` e no router `ellocene-ops` (fila "PDF/DOCX, dossiê, proposta, SOP → docs").
4. Reforçar nas tasks `gerar-relatorio.md` / `gerar-documento.md` / `gerar-docx.md` o passo final: gerar PDF via WeasyPrint e gravar `.pdf` (+ `.html` fonte) na pasta do cliente; nunca gravar `.md` na pasta do cliente.
5. Regra de apoio (já registada em `CLAUDE.md` Governança): deliverables para clientes são SEMPRE PDF.
---

## [IMP-008] Governança documental — TODO documento nasce no Fibery; .md local só como fallback

**PENDENTE — política a enraizar no squad** (prioridade máxima)

**Ficheiro:** `ellocene-ops/` (agentes `guardiao`, `docs`, `relatorios`, `planos`; tasks `gerar-documento`, `gerar-relatorio`, `gerar-sop`, `fluxo-completo-*`; skills + router) · `CLAUDE.md` Governança
**Detectado em:** Sprint Sunel Têxtil (2026-09-02) — PRD e Estrutura do Projecto gerados em `.md` local (`06-Empresas-Filhas/Altars/04-Clientes/Sunel_Textil/05-MVP/`) com apenas `Link Principal` file:// no Fibery; o Project no Fibery ficou com descrição e campos vazios.
**Impacto:** ALTO — informação importante vive fora do workspace estruturado (Fibery); outros membros da equipa e outras ferramentas (Codex, OpenClaw) não acedem como contexto sem path manual; quebra a governança "TUDO é auditável, deixa rasto".

**Problema:**
Os agentes geram documentos de informação/registo/inteligência/planos como `.md` local (artefacto primário), em vez de criar o conteúdo directamente em `Ellocene/Document` no Fibery. O Fibery é o workspace estruturado do squad — os ficheiros locais são invisíveis para a equipa.

**Acção correctiva (regra — prioridade máxima):**
1. **TODO e QUALQUER documento de informação/registo/inteligência/planos** (PRDs, estruturas de projecto, planos, SOPs, actas, notas, briefings, logs, guias, relatórios internos, memorandos, etc.) deve ser **gerado directamente no Fibery** (`Ellocene/Document`, conteúdo no campo Description/Resumo Executivo, ligado ao Project/Cliente/EmpresaFilha).
2. `.md` local **só como fallback** quando o MCP Fibery está indisponível; e, mesmo nesse caso, registar o conteúdo no Fibery assim que o MCP voltar.
3. **Excepção (deliverables externos):** relatórios, facturas, contratos e documentos **para partilhar com pessoas externas/clientes** → **PDF ou DOCX** (identidade da filha), mas **sempre com uma versão homóloga e idêntica devidamente organizada no Fibery** (Documento ligado ao projecto/cliente).
4. **Reestruturar o squad** para impor isto: actualizar agentes, tasks e skills para instruírem "criar conteúdo no Fibery (`create_entities` + `insert_document_blocks`)" como primeiro passo; `.md`/PDF apenas como saída final para externos.
5. Ao trabalhar um Project/Cliente no Fibery, **preencher os campos da entidade** (Descrição, Valores, Datas, Equipa, Sponsor, Links) — nunca deixar entidades vazias.

---

---

## [IMP-010] Processo Pacote Starter Blimari — pipeline + alertas + acções programáticas

**PROPOSTA — a planear e implementar**

**Ficheiro:** `ellocene-ops/` (agentes `guardiao`, `relatorios`, `docs`; tasks de fluxo Pacote Starter) · `Blimari/07-Operacoes/Processos/Processos-Pacote-Starter-v1.0.md`
**Detectado em:** Execução real Ve Palace (2026-09-03) — perfil Google Business rejeitado pela Google, resolução manual (email ao suporte, videochamada solicitada, relatório gerado) **sem qualquer automação**; cada passo exigiu explicação do operador.
**Impacto:** ALTO — cada perfil hoje é gerido manualmente, o que escala mal para dezenas de perfis; risco de perda de prazos (rejeições que expiram, videochamadas não agendadas); operador tem de re-explicar contexto a cada interacção.
**Origem no Fibery:** Task #55 "Melhorar processo/fluxo Pacote Starter Blimari (automação + alertas + pipeline)" (ligada à EmpresaFilha Blimari).

**Problema:**
O ciclo de vida de um perfil Google Business no Pacote Starter é hoje manual do início ao fim:
1. Criação do perfil — feita manualmente no business.google.com
2. Verificação (vídeo/correio/videochamada) — acompanhada manualmente, sem alertas de prazo
3. Rejeição automática (muito comum em Angola) — detectada manualmente no email; recurso enviado à mão
4. Videochamada — agendamento manual, sem lembrete
5. Verificado → optimização → manutenção — sem pipeline de estado

Cada passo requer que o operador re-explique o contexto. A experiência Ve Palace de hoje (2026-09-03) é exemplar: email de rejeição detectado → contexto explicado do zero → email de videochamada escrito manualmente → relatório gerado → operação registada. Nada disto deveria exigir intervenção humana além de aprovação.

**Acção correctiva (proposta):**
1. **Pipeline de estado por perfil** — cada perfil Google de cada cliente Blimari tem um estado (Criado → A Verificar → Videochamada Solicitada → Videochamada Agendada → Verificado → Optimizado → Mantido) visível num dashboard/report.
2. **Alertas automáticos** — notificações (no Fibery e/ou WhatsApp/email) para cada etapa:
   - "Perfil criado — iniciar verificação dentro de 24h"
   - "Verificação pendente há X dias — acção necessária"
   - "Rejeição detectada — disparar recurso (com aprovação humana)"
   - "Videochamada marcada para amanhã — preparar guião"
3. **Acções programáticas com templates** — rejeição da Google dispara um template de email de videochamada pré-aprovado (apenas confirmação humana); alertas de prazo enviam notificações preparadas; pipeline actualiza-se automaticamente.
4. **Integração Fibery como source of truth** — o estado de cada perfil vive no Fibery (Task ou nova entidade); agentes consultam e actuam sobre ele; operador aprova, não explica.
5. **Comando dedicado** — criar comando no agente `relatorios` (ex.: `*pipeline-pacote-starter`) que mostra o estado de todos os perfis e permite activar acções.

**Decisão de direcção (Credo, 2026-09-04):** o estado de cada perfil deve viver numa **nova entidade "Perfil Google" no Fibery** (uma por perfil — ex.: Ve Palace, ABDG, Colégio) com campo de estado/verificação, ligada ao Cliente e à EmpresaFilha. NÃO reutilizar Ellocene/Task para este fim. (Registo da melhoria apenas — implementação fica para sessão dedicada.)

**Critérios de sucesso:**
- Novo perfil adicionado → pipeline mostra "Criado" e alerta "iniciar verificação" automático
- Rejeição Google → sistema sugere email de videochamada (operador só aprova)
- Videochamada agendada → alerta 24h antes com guião pronto
- Todos os perfis visíveis num dashboard consolidado

## [IMP-009] Campos de Link no Fibery — nunca colar paths de ficheiros locais

**PENDENTE — regra**

**Ficheiro:** `ellocene-ops/config/governanca-documentos.md` + agentes/tasks que usam `Ellocene/Link Principal`, `Ellocene/Pasta Drive`
**Detectado em:** Sprint Sunel (2026-09-02) — documentos criados com `Link Principal: file:///Users/.../Proposta.pdf` no Fibery
**Impacto:** MÉDIO — um `file://` local não é navegável por outros membros nem por outras ferramentas; polui o campo e engana.

**Acção correctiva (regra):**
1. Campos de link (`Ellocene/Link Principal`, `Ellocene/Pasta Drive`, `Ellocene/Link`, etc.) aceitam APENAS **URLs normais**: página web ou serviço (Google Drive, website, app).
2. Se não houver uma URL válida → **deixar vazio**. Nunca colar `file:///...` nem paths locais.
3. Actualizar a nota dos agentes + `governanca-documentos.md`.
