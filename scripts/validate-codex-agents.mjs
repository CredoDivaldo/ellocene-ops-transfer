import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();
const expected = [
  "guardiao", "legal", "governanca", "actas", "planos", "registo",
  "portfolio", "kpis", "relatorios", "docs", "processos", "ceo", "cfo",
  "cto", "cmo", "chro", "cro",
];
const failures = [];
const controls = [
  ["01_Guardiao", "cockpit"], ["02_Legal", "legal"], ["03_Governanca", "governanca"],
  ["04_Actas", "actas"], ["05_Planos", "planos"], ["06_Registo", "registo"],
  ["07_Portfolio", "portfolio"], ["08_KPIs", "kpis"], ["09_Relatorios", "relatorios"],
  ["10_Docs", "docs"], ["11_Processos", "processos"], ["12_CEO", "ceo"],
  ["13_CFO", "cfo"], ["14_CTO", "cto"], ["15_CMO", "cmo"], ["16_CHRO", "chro"],
  ["17_CRO", "cro"],
];

for (const name of expected) {
  const profile = join(root, ".codex", "agents", `${name}.toml`);
  const skill = join(root, ".agents", "skills", name, "SKILL.md");
  const source = join(root, "agents", `${name}.md`);

  if (!existsSync(profile)) {
    failures.push(`Perfil em falta: ${profile}`);
    continue;
  }

  const content = readFileSync(profile, "utf8");
  for (const field of [
    `name = \"${name}\"`,
    "description = ",
    "developer_instructions = \"\"\"",
  ]) {
    if (!content.includes(field)) failures.push(`${name}: campo obrigatório em falta (${field})`);
  }
  if (!existsSync(skill)) failures.push(`${name}: skill em falta (${skill})`);
  if (!existsSync(source)) failures.push(`${name}: fonte canónica em falta (${source})`);
}

const actual = existsSync(join(root, ".codex", "agents"))
  ? readdirSync(join(root, ".codex", "agents")).filter((file) => file.endsWith(".toml"))
  : [];
const unexpected = actual.filter((file) => !expected.includes(file.replace(/\.toml$/, "")));
if (unexpected.length) failures.push(`Perfis não declarados no manifesto: ${unexpected.join(", ")}`);

for (const required of ["AGENTS.md", ".codex/config.toml", ".codex/README.md", "squad.yaml"]) {
  if (!existsSync(join(root, required))) failures.push(`Ficheiro obrigatório em falta: ${required}`);
}

for (const document of [
  "AGENT-OPERATING-MODEL.md", "AGENT-IO-MATRIX.md", "HANDOFF-PROTOCOL.md",
  "HANDOFF-MATRIX.md", "WORKFLOW-ORCHESTRATION.md", "RISK-REGISTER.md",
  "GATE-LOG.md", "UNKNOWNS-REGISTER.md",
]) {
  if (!existsSync(join(root, "01_Governance", document))) failures.push(`Governação em falta: ${document}`);
}

for (const [directory, domain] of controls) {
  for (const required of ["README.md", "inbox", "outbox", join("state", `${domain}-current.md`)]) {
    if (!existsSync(join(root, "02_Control", directory, required))) {
      failures.push(`Superfície de controlo em falta: 02_Control/${directory}/${required}`);
    }
  }
}

for (const required of [".aiox/README.md", "scripts/handoff.js", "03_Data/03_State/README.md"]) {
  if (!existsSync(join(root, required))) failures.push(`Runtime em falta: ${required}`);
}

if (failures.length) {
  console.error("Instalação Codex inválida:\n- " + failures.join("\n- "));
  process.exit(1);
}

console.log(`Instalação válida: ${expected.length} agentes Codex, ${expected.length} skills, ${controls.length} superfícies de controlo e governação AIOX disponíveis.`);
