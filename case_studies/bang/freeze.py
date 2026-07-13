#!/usr/bin/env python3
"""Generate a DRAFT SHA-256 freeze manifest of the Bang campaign corpus.

Read-only. Produces case_studies/bang/CORPUS_FREEZE.manifest.json.

This makes the freeze plan (00_FIRST_RESPONSE.md §8) concrete rather than
aspirational. It is v0/DRAFT: the exact file boundary is blocking decision
B-freeze, and poison-flagged items (contamination controls, §6) are recorded
but NOT excluded, so a rediscovery run that "confirms" them can be scored as a
failure.

Usage:  python case_studies/bang/freeze.py
"""
from __future__ import annotations
import hashlib
import json
import subprocess
from pathlib import Path

BANG = Path("/home/maxim/PycharmProjects/bang-plank-euler-jacobi")

# --- Include list: the campaign knowledge record (§8) -----------------------
INCLUDE_FILES = [
    "00-research-dossier.md", "03-work-plan.md", "README.md",
    "pinasco-outreach-draft-y-research.md",
    "instrucciones-modificaciones-paper-aims.md",
    "AUDITORIA_CLAUDE_30Jn.md",
]
INCLUDE_DIRS = [
    "drafts", "experiments", "notes", "auditorias", "paper-ready", "kimi",
]

# --- Exclusions (§8): abandoned / unrelated / copyright ---------------------
EXCLUDE_SUBPATHS = [
    "drafts/obsolete",              # abandoned Euler-Jacobi approach; do not cite
    "drafts/hamilton-jacobi",       # unrelated Hamilton-Jacobi note
    "refs",                         # copyright-excluded third-party PDFs
    ".git", "target", "__pycache__",
]
EXCLUDE_SUFFIXES = [".log", ".aux", ".out", ".blg", ".pyc"]

# --- Poison flags (§6): frozen WITH a warning, not excluded -----------------
POISON = {
    "notes/09-fibonacci-bootstrap.md": "unretracted but mathematically UNSOUND",
    "paper-ready/00-INDEX.ms": "asserts since-corrected triangle=>planar (Ambrus) claim",
    # notes 05..21 are early refuted 'victory' drafts (range-flagged below)
}
POISON_RANGE_NOTE = "notes/05..21 are early refuted 'victory' drafts (AUDITORIA_CLAUDE_30Jn.md)"


def excluded(rel: str) -> bool:
    if any(rel == e or rel.startswith(e + "/") or f"/{e}/" in f"/{rel}" for e in EXCLUDE_SUBPATHS):
        return True
    if "obsolete" in rel or "hamilton-jacobi" in rel:
        return True
    return any(rel.endswith(s) for s in EXCLUDE_SUFFIXES)


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def collect() -> list[Path]:
    out: list[Path] = []
    for f in INCLUDE_FILES:
        p = BANG / f
        if p.is_file() and not excluded(f):
            out.append(p)
    for d in INCLUDE_DIRS:
        base = BANG / d
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file():
                rel = str(p.relative_to(BANG))
                if not excluded(rel):
                    out.append(p)
    return sorted(set(out))


def git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=BANG, text=True
        ).strip()
    except Exception:
        return "UNKNOWN"


def main() -> None:
    files = collect()
    entries = []
    for p in files:
        rel = str(p.relative_to(BANG))
        entry = {"path": rel, "bytes": p.stat().st_size, "sha256": sha256(p)}
        if rel in POISON:
            entry["poison_flag"] = POISON[rel]
        entries.append(entry)

    # A manifest-of-manifests hash: deterministic over (path, sha256) pairs.
    roll = hashlib.sha256()
    for e in entries:
        roll.update(f"{e['path']}:{e['sha256']}".encode())

    manifest = {
        "schema_version": "theoryforge-freeze/0.1-draft",
        "status": "DRAFT_UNFROZEN",
        "source_repo": "https://github.com/maximilianolucius/bang-plank-affine-triangle.git",
        "git_commit": git_commit(),
        "n_files": len(entries),
        "total_bytes": sum(e["bytes"] for e in entries),
        "manifest_hash": "sha256:" + roll.hexdigest(),
        "exclusions": EXCLUDE_SUBPATHS + [f"*{s}" for s in EXCLUDE_SUFFIXES],
        "poison_range_note": POISON_RANGE_NOTE,
        "note": "B-freeze is unresolved: the file boundary and poison policy require PI sign-off before this becomes bang-freeze-v0.",
        "files": entries,
    }
    out = Path(__file__).with_name("CORPUS_FREEZE.manifest.json")
    out.write_text(json.dumps(manifest, indent=2, sort_keys=False))
    print(f"wrote {out}")
    print(f"  files={manifest['n_files']}  bytes={manifest['total_bytes']}")
    print(f"  git_commit={manifest['git_commit']}")
    print(f"  manifest_hash={manifest['manifest_hash']}")
    poisoned = [e for e in entries if 'poison_flag' in e]
    print(f"  poison-flagged files present: {len(poisoned)}")
    for e in poisoned:
        print(f"    - {e['path']}: {e['poison_flag']}")


if __name__ == "__main__":
    main()
