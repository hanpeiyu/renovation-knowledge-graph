#!/usr/bin/env python3
"""Validate YAML-front-matter nodes, vocabularies and cross references."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)

def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def main() -> int:
    errors = []
    types = {t["id"] for t in load_yaml(ROOT / "ontology/types.yaml")["types"]}
    relations = {r["id"] for r in load_yaml(ROOT / "ontology/relations.yaml")["relations"]}
    schema = json.loads((ROOT / "schemas/node.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    nodes = {}
    files = sorted((ROOT / "knowledge").rglob("*.md"))
    for path in files:
        content = path.read_text(encoding="utf-8")
        match = FRONT.match(content)
        if not match:
            errors.append(f"{path}: missing YAML front matter")
            continue
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{path}: invalid YAML: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path}: front matter must be a mapping")
            continue
        for issue in validator.iter_errors(data):
            errors.append(f"{path}: {issue.message}")
        ident = data.get("id")
        if ident in nodes:
            errors.append(f"{path}: duplicate ID {ident}")
        if ident:
            nodes[ident] = (path, data)
        if data.get("type") not in types:
            errors.append(f"{path}: unknown type {data.get('type')}")
        for rel in data.get("relations", []) if isinstance(data.get("relations"), list) else []:
            if not isinstance(rel, dict):
                errors.append(f"{path}: relation must be mapping")
            elif rel.get("kind") not in relations:
                errors.append(f"{path}: unknown relation {rel.get('kind')}")
        if data.get("type") == "claim" and data.get("status") == "reviewed":
            claims = data.get("claims", [])
            if not claims or any(not x.get("evidence_ids") for x in claims if isinstance(x, dict)):
                errors.append(f"{path}: reviewed claim requires evidence_ids per claim")
    for ident, (path, data) in nodes.items():
        for rel in data.get("relations", []) if isinstance(data.get("relations"), list) else []:
            if isinstance(rel, dict) and rel.get("target") not in nodes:
                errors.append(f"{path}: broken relation target {rel.get('target')}")
    if errors:
        print("\n".join("ERROR: " + item for item in errors))
        return 1
    print(f"PASS: {len(files)} Markdown files; {len(nodes)} nodes; {len(types)} types; {len(relations)} relation kinds")
    return 0

if __name__ == "__main__":
    sys.exit(main())