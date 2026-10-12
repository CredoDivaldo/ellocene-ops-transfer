# Governança Documental — Documentos nascem no Fibery

> Política do squad ellocene-ops (prioridade máxima). Registada em **IMP-008** (2026-09-02) no `improvements/MELHORIAS-PENDENTES.md`.
> Actualizada em **2026-10-12**: links Google Drive obrigatórios + proibição de referências internas em documentos externos.

## Regra

1. **TODO e QUALQUER documento** de informação/registo/inteligência/planos — PRDs, estruturas de projecto, planos, SOPs, actas, notas, briefings, logs, guias, relatórios internos, memorandos, propostas de trabalho — é criado **directamente no Fibery** (`Ellocene/Document`), com o conteúdo no campo `Description` (e `Resumo Executivo`), ligado ao Project/Cliente/EmpresaFilha correcto.
2. `.md` local só como **fallback** quando o MCP Fibery está indisponível; nesse caso, registar o conteúdo no Fibery assim que o MCP voltar.
3. **Excepção — deliverables externos/clientes:** relatórios, facturas, contratos, cartas bancárias e documentos para partilhar com pessoas externas → **PDF ou DOCX** (identidade da filha via `identidades-empresas.yaml`), SEMPRE com **versão homóloga e idêntica** devidamente organizada no Fibery (Documento ligado ao projecto/cliente).
4. Ao trabalhar entidades no Fibery (Project, Client, Meeting, Task, Document…), **preencher os campos da entidade** (Descrição, Valores, Datas, Equipa, Sponsor, Links) — nunca deixar entidades vazias.
5. **Campos de link** (`Link Principal`, `Pasta Drive`, `Link`…) aceitam APENAS **URLs normais** (web / Google Drive / serviço). Nunca `file:///...` nem paths locais — se não houver URL válida, **deixar vazio** (IMP-009).
6. **Propostas comerciais** seguem **obrigatoriamente** `config/propostas-comerciais.md`: template oficial da emitente, identidade do design system, gate `tools/audit-tokens.sh`, PDF no Drive do cliente e registo no Fibery como "Proposta Comercial" com versão homóloga. Nenhuma proposta sai fora deste padrão.

## Documentos externos — regras adicionais (IMP-010, 2026-10-12)

7. **Sem referências internas em documentos externos.** Cartas, contratos, resoluções, facturas e qualquer PDF/DOCX destinado a bancos, clientes, notários ou terceiros **não podem** conter:
   - códigos internos (ex.: `HOL-CART-BAI-2026-001`);
   - menções a versão de rascunho / "pronta para assinatura" / "sujeita a revisão";
   - rodapés de controlo interno, paths de Drive, IDs Fibery ou notas de agentes.
   O controlo de versão e estado fica **só** no Fibery e nos metadados internos do squad.
8. **Links Google Drive obrigatórios.** Quando um deliverable for gravado no Drive, o agente deve:
   - obter o **link exacto** (`viewUrl` / `https://drive.google.com/file/d/.../view`) via ferramenta Google Drive (`search_files`, `create_file`, `get_file_metadata` ou `gdrive files upload/info`);
   - **nunca** devolver apenas o path local (`/Users/.../My Drive/...`);
   - preencher o campo `Link Principal` / `Pasta Drive` no Fibery com essa URL;
   - na resposta ao operador, listar sempre **Fibery + Google Drive (URL)**.

## Execução (fluxos)

1. Os agentes `guardiao` / `docs` / `legal` / `relatorios` / `planos` / `processos` e as tasks `gerar-documento` / `gerar-relatorio` / `gerar-sop` / `documentar-processo` / `fluxo-completo-*` / `minuta-deliberacao` / `redigir-contrato` executam por esta ordem:
   - **1º** criar o documento no Fibery (`create_entities` + `insert_document_blocks` no Description/Resumo Executivo);
   - **2º** só depois, se for um deliverable externo, gerar PDF/DOCX (via `@docs`/WeasyPrint ou reportlab) **sem referências internas**;
   - **3º** gravar no Google Drive e obter o **link exacto** (ferramenta Drive / `gdrive`);
   - **4º** actualizar Fibery (`Link Principal` = URL Drive) e responder com **Fibery + Drive**.
2. O `@guardiao`, ao delegar, reforça esta regra no pedido a cada agente.
3. Relatórios internos/finais a outro membro da equipa usam sempre o link Fibery, nunca o path de um ficheiro `.md` local.

## Registo de origem

- **Detectado em:** Sprint Sunel Têxtil (2026-09-02) — PRD e Estrutura do Projecto gerados em `.md` local com apenas `Link Principal` file:// no Fibery; Project com descrição/campos vazios.
- **Impacto:** ALTO — informação importante fora do workspace estruturado; invisível para a equipa e outras ferramentas (Codex, OpenClaw) sem path manual.
- **Actualização 2026-10-12:** Carta BAI — proibição de rodapés internos em documentos formais externos; obrigação de devolver link Drive (não path).
