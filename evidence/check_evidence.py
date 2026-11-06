#!/usr/bin/env python3
"""Check the claim and source registries against each other and the pages.

What this checks (structure only):
  - claim IDs are well formed and unique; source keys are unique
  - layer, status and access are in vocabulary
  - every claim's sources exist, and every source is used by some claim
  - a hypothesis is never 'supported'
  - an absence claim records what was 'searched'
  - a 'supported' claim has at least one source read at catalogue_record or
    deeper AND re-located by a second person (relocated: true)
  - every source says whether it has been re-located
  - every page a claim names exists, and its anchor phrase is on that page
    (whitespace and case ignored, nothing else)
  - every claim ID mentioned in a markdown file exists

What it cannot check: whether a sentence is faithful to its source. That is
the reviewer's job (docs/review-process.md). A clean run means the registry
is consistent, not that the history is right.

Each run states which files it read and reports, without failing, how many
sources lack a URL or archive (OF-1), so a clean exit never hides that gap.

Usage, from anywhere:  python evidence/check_evidence.py [repo_root]
Exit status 1 if anything is wrong.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml:  python -m pip install pyyaml")

LAYERS = {"documented", "recollection", "testimony", "interpretation",
          "hypothesis", "absence"}
STATUSES = {"supported", "partly_supported", "unverified", "unsupported", "open"}
ACCESS = ["primary_inspected", "indexed_text", "catalogue_record",
          "secondary_report", "user_screenshot", "not_located"]
SUPPORTING_ACCESS = set(ACCESS[:3])
CLAIM_ID_RE = re.compile(r"^claim\.[a-z0-9_]+(\.[a-z0-9_]+)+$")
CLAIM_MENTION_RE = re.compile(r"\bclaim\.[a-z0-9_]+(?:\.[a-z0-9_]+)+")
SKIP_DIRS = {".git", "__pycache__", "tests"}


def norm(text):
    return re.sub(r"\s+", " ", text).strip().casefold()


def load(path, errors):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{path.name}: cannot read: {exc}")
        return {}


def check(root):
    errors = []
    ev = root / "evidence"
    sources = load(ev / "sources.yml", errors).get("sources") or []
    claims = load(ev / "claims.yml", errors).get("claims") or []

    source_by_key = {}
    for i, s in enumerate(sources):
        key = s.get("key")
        where = f"sources.yml entry {i} ({key})"
        if not key:
            errors.append(f"{where}: no key")
            continue
        if key in source_by_key:
            errors.append(f"{where}: duplicate key")
        source_by_key[key] = s
        if s.get("access") not in ACCESS:
            errors.append(f"{where}: access {s.get('access')!r} not in {ACCESS}")
        if not isinstance(s.get("relocated"), bool):
            errors.append(f"{where}: relocated must be true or false")

    used = set()
    seen_ids = set()
    page_cache = {}
    for i, c in enumerate(claims):
        cid = c.get("id")
        where = f"claims.yml entry {i} ({cid})"
        if not cid or not CLAIM_ID_RE.match(str(cid)):
            errors.append(f"{where}: id must look like claim.area.name")
        elif cid in seen_ids:
            errors.append(f"{where}: duplicate id")
        seen_ids.add(cid)

        layer, status = c.get("layer"), c.get("status")
        if layer not in LAYERS:
            errors.append(f"{where}: layer {layer!r} not in {sorted(LAYERS)}")
        if status not in STATUSES:
            errors.append(f"{where}: status {status!r} not in {sorted(STATUSES)}")
        if not str(c.get("statement") or "").strip():
            errors.append(f"{where}: no statement")

        keys = c.get("sources") or []
        if not keys:
            errors.append(f"{where}: no sources")
        for k in keys:
            if k not in source_by_key:
                errors.append(f"{where}: unknown source {k!r}")
            used.add(k)

        if layer == "hypothesis" and status == "supported":
            errors.append(f"{where}: a hypothesis cannot be 'supported'; "
                          "re-layer it and say why")
        if layer == "absence" and not str(c.get("searched") or "").strip():
            errors.append(f"{where}: an absence claim must record what was searched")
        # r1/R1-12: a source read once and never found again cannot carry 'supported'.
        read_deep_enough = any(
            source_by_key.get(k, {}).get("access") in SUPPORTING_ACCESS
            and source_by_key.get(k, {}).get("relocated") is True for k in keys)
        if status == "supported" and not read_deep_enough:
            errors.append(f"{where}: 'supported' needs a source at "
                          f"{sorted(SUPPORTING_ACCESS)} with relocated: true")

        pages = c.get("pages") or []
        if not pages:
            errors.append(f"{where}: no pages")
        for p in pages:
            path, anchor = p.get("path"), p.get("anchor")
            if not path or not anchor:
                errors.append(f"{where}: page entry needs path and anchor")
                continue
            target = root / path
            if path not in page_cache:
                page_cache[path] = (norm(target.read_text(encoding="utf-8"))
                                    if target.is_file() else None)
            text = page_cache[path]
            if text is None:
                errors.append(f"{where}: page {path} does not exist")
            elif norm(str(anchor)) not in text:
                errors.append(f"{where}: anchor not found in {path}: {anchor!r}")

    for k in source_by_key:
        if k not in used:
            errors.append(f"sources.yml: {k!r} is not used by any claim")

    read = []
    for md in sorted(root.rglob("*.md")):
        if SKIP_DIRS & set(md.relative_to(root).parts):
            continue
        read.append(md.relative_to(root).as_posix())
        for m in CLAIM_MENTION_RE.findall(md.read_text(encoding="utf-8")):
            if m not in seen_ids:
                errors.append(f"{md.relative_to(root).as_posix()}: "
                              f"mentions unknown claim {m}")

    no_url = sum(1 for s in sources if not s.get("url"))
    no_archive = sum(1 for s in sources if not s.get("archived"))
    by_access = {a: sum(1 for s in sources if s.get("access") == a) for a in ACCESS}

    print(f"read: evidence/claims.yml, evidence/sources.yml, {len(read)} markdown files")
    print(f"{len(claims)} claims, {len(sources)} sources")
    print("access: " + ", ".join(f"{a} {n}" for a, n in by_access.items()))
    relocated = sum(1 for s in sources if s.get("relocated") is True)
    print(f"not yet re-findable (OF-1): {no_url} sources without url, "
          f"{no_archive} without archived snapshot, "
          f"{len(sources) - relocated} never re-located")
    for e in errors:
        print("ERROR " + e)
    print("FAILED" if errors else "all checked")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # Thai anchors on a cp949/cp1252 console
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    sys.exit(check(root))
