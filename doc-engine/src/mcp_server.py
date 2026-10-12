#!/usr/bin/env python3
"""
mcp_server.py — Servidor MCP do doc-engine
Expõe a ferramenta `generate_document` e `list_templates` via protocolo MCP (stdio).

Qualquer agente do Claude Code, Cursor, ou ChatGPT (via bridge) pode invocar:
  generate_document(company="altars", document_type="proposal", variables={...})
"""

import sys
import json
import asyncio
from pathlib import Path

# Adiciona src ao path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generator import generate_document
from registry import TEMPLATE_MAP, TEMPLATES_DIR, extract_placeholders, get_template_path

TOOLS = [
    {
        "name": "generate_document",
        "description": "Gera um documento PDF/HTML determinístico a partir de template e tokens oficiais de uma empresa do grupo Ellocene.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "company": {
                    "type": "string",
                    "enum": ["holding", "blimari", "altars", "tivra", "piramyd", "aicos"],
                    "description": "Empresa emitente do documento (determina tokens de design e identidade visual)"
                },
                "document_type": {
                    "type": "string",
                    "enum": ["proposal", "scp", "contract", "report", "sop", "acta", "dossier"],
                    "description": "Tipo de documento a gerar"
                },
                "variables": {
                    "type": "object",
                    "description": "Dicionário de variáveis a preencher no template (ex: {'CLIENTE-NAME': '...', ...})"
                },
                "output_dir": {
                    "type": "string",
                    "description": "Directório de destino para os ficheiros (opcional; default: /tmp/doc-engine-output)"
                },
                "output_basename": {
                    "type": "string",
                    "description": "Nome base dos ficheiros gerados sem extensão (opcional)"
                }
            },
            "required": ["company", "document_type", "variables"]
        }
    },
    {
        "name": "list_templates",
        "description": "Lista os templates disponíveis por empresa e tipo, com os placeholders que cada um exige.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "company": {
                    "type": "string",
                    "description": "Filtrar por empresa (opcional)"
                }
            }
        }
    }
]

def handle_list_templates(args):
    target_company = args.get("company")
    results = []

    for (comp, dtype), fname in TEMPLATE_MAP.items():
        if target_company and comp != target_company.lower():
            continue
        tpl_path = TEMPLATES_DIR / fname
        if not tpl_path.exists():
            continue

        raw = tpl_path.read_text(encoding="utf-8")
        phs = extract_placeholders(raw)

        results.append({
            "company": comp,
            "document_type": dtype,
            "template_file": fname,
            "required_placeholders": phs,
            "placeholder_count": len(phs)
        })

    return {"templates": results}

def handle_generate_document(args):
    company = args["company"]
    doc_type = args["document_type"]
    variables = args["variables"]
    output_dir = Path(args["output_dir"]) if "output_dir" in args else None
    output_basename = args.get("output_basename")

    result = generate_document(
        company=company,
        doc_type=doc_type,
        variables=variables,
        output_dir=output_dir,
        output_basename=output_basename,
    )
    return result

def main():
    """Loop simples JSON-RPC sobre stdio (protocolo MCP v1)."""
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue

        msg_id = req.get("id")
        method = req.get("method")

        if method == "tools/list":
            resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})

            try:
                if tool_name == "generate_document":
                    res = handle_generate_document(tool_args)
                elif tool_name == "list_templates":
                    res = handle_list_templates(tool_args)
                else:
                    raise ValueError(f"Ferramenta desconhecida: {tool_name}")

                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(res, indent=2, ensure_ascii=False)}]
                    }
                }
            except Exception as e:
                resp = {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32000, "message": str(e)}
                }

            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()

        elif method == "initialize":
            resp = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {"name": "ellocene-doc-engine", "version": "1.0.0"},
                    "capabilities": {"tools": {}}
                }
            }
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
