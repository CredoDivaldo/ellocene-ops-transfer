#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');

const root = process.cwd();
const directory = path.join(root, '.aiox', 'handoffs');
const required = ['from_agent', 'to_agent', 'created_at', 'last_command', 'summary'];

function ensureDirectory() {
  fs.mkdirSync(directory, { recursive: true });
}

function parse(argv) {
  const [command = 'list', ...tokens] = argv;
  const options = { _: [] };
  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index];
    if (!token.startsWith('--')) {
      options._.push(token);
      continue;
    }
    const key = token.slice(2);
    const next = tokens[index + 1];
    if (!next || next.startsWith('--')) options[key] = true;
    else {
      options[key] = next;
      index += 1;
    }
  }
  return { command, options };
}

function quote(value) {
  return JSON.stringify(String(value));
}

function serialise(data) {
  return Object.entries(data)
    .filter(([, value]) => value !== undefined && value !== '')
    .map(([key, value]) => `${key}: ${typeof value === 'boolean' ? value : quote(value)}`)
    .join('\n') + '\n';
}

function parseFile(file) {
  const result = {};
  for (const line of fs.readFileSync(file, 'utf8').split('\n')) {
    const match = line.match(/^([a-z_]+):\s*(.*)$/);
    if (!match) continue;
    const [, key, raw] = match;
    if (raw === 'true') result[key] = true;
    else if (raw === 'false') result[key] = false;
    else {
      try { result[key] = JSON.parse(raw); } catch { result[key] = raw; }
    }
  }
  return result;
}

function handoffs() {
  ensureDirectory();
  return fs.readdirSync(directory)
    .filter((name) => name.endsWith('.yaml'))
    .sort()
    .reverse()
    .map((name) => ({ name, file: path.join(directory, name), data: parseFile(path.join(directory, name)) }));
}

function slug(value) {
  return String(value).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60) || 'handoff';
}

function create(options) {
  if (!options.from) throw new Error('É obrigatório indicar --from AGENTE.');
  if (!options.summary) throw new Error('É obrigatório indicar --summary TEXTO.');
  const createdAt = new Date().toISOString();
  const id = `${createdAt.replace(/[-:.]/g, '').replace('Z', 'Z')}-${slug(options.from)}-${slug(options.to || 'global')}-${slug(options.command || 'handoff')}`;
  const payload = {
    id,
    from_agent: options.from,
    to_agent: options.to || 'global',
    created_at: createdAt,
    last_command: options.command || 'unknown',
    priority: options.priority || 'medium',
    status: 'open',
    summary: options.summary,
    next_action: options.next || '',
    consumed: false,
  };
  const file = path.join(directory, `${id}.yaml`);
  ensureDirectory();
  fs.writeFileSync(file, serialise(payload), 'utf8');
  console.log(`created ${path.relative(root, file)}`);
}

function list(options) {
  const items = handoffs().filter(({ data }) =>
    (!options.to || data.to_agent === options.to || data.to_agent === 'global') &&
    (!options.from || data.from_agent === options.from) &&
    (options.all || data.consumed !== true),
  );
  if (!items.length) return console.log('no handoffs found');
  console.log('file | from | to | priority | status | summary');
  for (const { name, data } of items) {
    console.log([name, data.from_agent || '-', data.to_agent || '-', data.priority || '-', data.consumed ? 'consumed' : 'open', data.summary || '-'].join(' | '));
  }
}

function consume(options) {
  const target = handoffs().find(({ name, data }) =>
    data.consumed !== true && (!options.file || name === options.file || data.id === options.file) &&
    (!options.to || data.to_agent === options.to || data.to_agent === 'global'),
  );
  if (!target) return console.log('no matching handoff found');
  target.data.consumed = true;
  target.data.status = 'consumed';
  target.data.consumed_at = new Date().toISOString();
  target.data.consumed_by = options.by || options.to || 'unknown';
  fs.writeFileSync(target.file, serialise(target.data), 'utf8');
  console.log(`consumed ${target.name}`);
}

function doctor() {
  const errors = [];
  for (const { name, data } of handoffs()) {
    for (const field of required) if (!data[field]) errors.push(`${name}: missing ${field}`);
    if (data.priority && !['low', 'medium', 'high', 'critical'].includes(data.priority)) errors.push(`${name}: invalid priority`);
  }
  if (errors.length) {
    console.error(errors.join('\n'));
    process.exitCode = 1;
  } else console.log(`ok: ${handoffs().length} handoff files validated`);
}

function help() {
  console.log('handoff commands:\n  create --from AGENT --to AGENT --command CMD --summary TEXT [--next TEXT] [--priority low|medium|high|critical]\n  list [--to AGENT] [--from AGENT] [--all]\n  consume [--to AGENT] [--file FILE_OR_ID] [--by AGENT]\n  doctor');
}

const { command, options } = parse(process.argv.slice(2));
try {
  if (command === 'create') create(options);
  else if (command === 'list') list(options);
  else if (command === 'consume') consume(options);
  else if (command === 'doctor') doctor();
  else help();
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
