#!/usr/bin/env python3
"""Verify immutable raster sources against the on-repo source manifest.

Pending means not uploaded. Pending files may be absent; 'verified' files may not.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
manifest = ROOT / "assets/RASTER_MANIFEST.json"
errors = []
pending = 0
verified = 0

try:
    data = json.loads(manifest.read_text(encoding="utf-8"))
    entries = data["assets"]
except (OSError, ValueError, KeyError, TypeError) as e:
    print(f"FAIL: raster manifest cannot be read: {e}")
    sys.exit(1)

seen = set()
for x in entries:
    rel = x.get("path")
    if not isinstance(rel, str) or not rel.startswith("assets/") or ".." in Path(rel).parts:
        errors.append(f"Unsafe source path: {rel!r}")
        continue
    if rel in seen:
        errors.append(f"Duplicate source path: {rel}")
    seen.add(rel)
    expected = x.get("sha256", "")
    if not re.fullmatch("[a-fA-F0-9]{64}", expected):
        errors.append(f"Invalid SHA-256: {rel}")
        continue
    status = x.get("github_status")
    if status not in ("pending", "verified"):
        errors.append(f"Unknown GitHub status: {rel}")
        continue
    if status == "pending":
        pending += 1
    else:
        verified += 1
    f = ROOT / rel
    if not f.is_file():
        if status == "verified":
            errors.append(f"Marked verified but file missing: {rel}")
        continue
    if f.stat().st_size != x.get("bytes"):
        errors.append(f"Size mismatch: {rel}")
    digest = hashlib.sha256(f.read_bytes()).hexdigest()
    if digest.lower() != expected.lower():
        errors.append(f"SHA-256 mismatch: {rel}")
print(f"Tracked raster sources: {len(entries)}; pending: {pending}; verified: {verified}.")
for e in errors:
    print("FAIL:", e)
if errors:
    sys.exit(1)
print("PASS: Source-manifest integrity only. Pending files remain missing by design.")
