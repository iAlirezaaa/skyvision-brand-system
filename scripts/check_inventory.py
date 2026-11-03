#!/usr/bin/env python3
"""Check that the Sky Vision visual backlog is internally consistent.

This does not assert design quality, ownership, rights, or owner approval.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
inventory_path = ROOT / "production/ASSET_INVENTORY.json"
backlog_path = ROOT / "production/ASSET_BACKLOG.md"
errors = []
try:
    data = json.loads(inventory_path.read_text(encoding="utf-8"))
    records = data["records"]
    statuses = set(data["allowed_status"])
    priorities = set(data["allowed_priority"])
except (OSError, ValueError, KeyError, TypeError) as error:
    print(f"FAIL: Inventory unavailable or invalid: {error}")
    sys.exit(1)

if not isinstance(records, list) or not records:
    errors.append("Inventory must contain at least one asset.")
ids = set()
paths = set()
for item in records:
    asset_id = item.get("id", "")
    match = re.fullmatch(r"([A-Z]{2})-(\d{2,3})", asset_id)
    if not match:
        errors.append(f"Bad asset ID: {asset_id!r}")
        continue
    if asset_id in ids:
        errors.append(f"Duplicate ID: {asset_id}")
    ids.add(asset_id)
    if item.get("status") not in statuses:
        errors.append(f"Invalid status: {asset_id}")
    if item.get("priority") not in priorities:
        errors.append(f"Invalid priority: {asset_id}")
    if item.get("review") not in ("not-approved", "approved"):
        errors.append(f"Invalid review flag: {asset_id}")
    if item.get("deliverable") != "exactly-one-image":
        errors.append(f"Each item needs exactly one image: {asset_id}")
    target = f"assets/production/{match.group(1)}/{asset_id}.png"
    if item.get("target") != target:
        errors.append(f"Nonstandard output path: {asset_id}")
    if target in paths:
        errors.append(f"Repeated output path: {target}")
    paths.add(target)
    if not item.get("title") or not item.get("category"):
        errors.append(f"Missing title or category: {asset_id}")
    if item.get("status") == "approved":
        if item.get("review") != "approved":
            errors.append(f"Unreviewed approved asset: {asset_id}")
        if not item.get("approval_ref"):
            errors.append(f"Approved asset missing approval reference: {asset_id}")
        if item.get("actual_repository_file") != target:
            errors.append(f"Approved asset missing exact repository path: {asset_id}")
        f = ROOT / target
        if not f.is_file():
            errors.append(f"Approved file not actually present: {asset_id}")
        elif not re.fullmatch(r"[0-9a-f]{64}", item.get("sha256", "")):
            errors.append(f"Approved asset missing SHA-256: {asset_id}")
        elif hashlib.sha256(f.read_bytes()).hexdigest() != item["sha256"]:
            errors.append(f"Approved asset hash mismatch: {asset_id}")
    if item.get("actual_repository_file") and not (ROOT / item["actual_repository_file"]).is_file():
        errors.append(f"Claimed GitHub file missing: {asset_id}")

try:
    human = backlog_path.read_text(encoding="utf-8")
    for asset_id in ids:
        if f"| {asset_id} |" not in human:
            errors.append(f"Backlog markdown omitted {asset_id}")
except OSError as error:
    errors.append(f"Missing readable backlog: {error}")

print(f"Sky Vision inventory: {len(records)} assets, {len(ids)} unique IDs; "
      f"{sum(x.get('status') == 'approved' for x in records)} approved.")
for error in errors:
    print("FAIL:", error)
if errors:
    sys.exit(1)
print("PASS: Inventory structure only; no claims about actual visual quality.")
