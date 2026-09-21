"""devflow-evidence.py — the evidence row, mechanically.

    cd <your project's root>                         # the evidence lives HERE
    python <this flow's root>/scripts/devflow-evidence.py [--root R] FILE...

Contract: for each evidence file under the home `artifact_homes.evidence`
declares, print the SHA-256 of its bytes on disk, its size, and a packet-ready
`Evidence files` table row to paste (never retype); verify `.gitattributes`
marks the home `-text` (`--fix` adds the line). With `--check`, compare each
file's digest on disk against the git INDEX blob — which is what the packet says
to hash, and is not a commit — and against the digest the newest increment packet
records, printing MATCH / MISMATCH per file; where there is no repository the index
limb has no subject and says so. The project root is `--root` when given and the
CURRENT WORKING DIRECTORY when not; the FIRST line of output is the absolute root it
resolved, and a root that is a flow INSTALLATION is refused. Exit 0 all good / 1 a
check failed / 2 bad input or the check could not run.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_DIGEST = re.compile(r"\b([0-9a-fA-F]{64})\b")
_PACKET = re.compile(r"^increment-(\d+)\.md$")
# The two witnesses of a flow INSTALLATION -- the manifest and the gate script, TOGETHER --
# named SEGMENT BY SEGMENT in each of the two layouts a flow is installed in. Either witness
# alone is common enough that a project could carry it; both together is what a flow home is.
# Spelled in both scripts because a script in the hand cannot import its sibling; widening one
# without the other is a known defect class, and this pair is the thing to widen.
_LAYOUTS = ((("FLOW-VERSION.md",), ("scripts", "devflow-validate.py")),
            (("docs", "FLOW-VERSION.md"), ("docs", "tools", "devflow-validate.py")))


def _flow_root() -> Path:
    """The flow home this script ships in \u2014 PROBED over both layouts, never assumed.

    `scripts/` in a bundle, one level deeper in the tree the bundle is generated from:
    a hard-coded depth is right in exactly one of them. `devflow-init-fast.py` and
    `devflow-scan-spec.py` probe the same anchor, and all three answer the question the
    same way, or one of them is looking somewhere else.
    """
    here = Path(__file__).resolve().parent
    for up in (here.parent, here.parent.parent):
        if (up / "commands" / "fast-dev-flow.md").is_file():
            return up
    return here.parent


def _is_flow_installation(root: Path) -> bool:
    """Is `root` a flow INSTALLATION rather than a project, in either layout?

    The same predicate `devflow-init-fast.py` applies to its root, for the same reason:
    a script that silently accepts the flow's own folder as the project is the defect
    round 3's reader met.
    """
    flow = _flow_root()
    if root == flow or flow in root.parents:
        return True
    return any(root.joinpath(*_man).is_file() and root.joinpath(*_tool).is_file()
               for _man, _tool in _LAYOUTS)


def _git(root: Path, *args: str) -> tuple[int, bytes] | None:
    """(returncode, stdout bytes) of a read-only git call, or None when git is absent."""
    try:
        out = subprocess.run(["git", "-C", str(root), *args],
                             capture_output=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.returncode, out.stdout


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _state(root: Path) -> dict | None:
    """`.dev-flow/state.json` as a MAPPING, or None. Valid JSON of the wrong shape is None.

    A top-level array parses and then fails on the first `.get`, which reaches the operator
    as a traceback instead of the one-line refusal every other bad input gets.
    """
    try:
        doc = json.loads((root / ".dev-flow" / "state.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return doc if isinstance(doc, dict) else None


def _home_rel(state: dict, key: str, default: str) -> str | None:
    """A declared `repo:` home as a normalized repo-relative path, or None."""
    homes = state.get("artifact_homes")
    raw = homes.get(key) if isinstance(homes, dict) else None
    if raw is None:
        raw = default
    if not isinstance(raw, str) or not raw.startswith("repo:"):
        return None
    return os.path.normpath(raw[len("repo:"):].replace("\\", "/")).replace("\\", "/").rstrip("/")


def _rel_under(root: Path, file: Path, home: str) -> str | None:
    """file's repo-relative POSIX path when it resolves under home, else None."""
    try:
        rel = file.resolve().relative_to(root).as_posix()
    except ValueError:
        return None
    norm = os.path.normpath(rel).replace("\\", "/")
    return norm if norm == home or norm.startswith(home + "/") else None


def _text_marked(gitattributes: Path, home: str) -> bool:
    """Does `.gitattributes` carry a line marking the evidence home `-text`?"""
    try:
        lines = gitattributes.read_text(encoding="utf-8").splitlines()
    except OSError:
        return False
    accepted = {home, home + "/", home + "*", home + "/*", home + "/**"}
    for ln in lines:
        parts = ln.split()
        if len(parts) >= 2 and parts[0].rstrip("/") in {a.rstrip("/") for a in accepted} \
                and "-text" in parts[1:]:
            return True
    return False


def _packet_digests(packet: Path) -> dict[str, str]:
    """The newest packet's `Evidence files` section -> {normalized cited path: digest}.

    Cell-wise, like the rule that reads it: the digest is a 64-hex cell and the
    path is its neighbour, whichever side it stands on.
    """
    try:
        text = packet.read_text(encoding="utf-8")
    except OSError:
        return {}
    m = re.search(r"(?ms)^#+\s*Evidence files\s*$(.*?)(?=^#|\Z)", text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if line.count("|") < 2:
            continue
        cells = [c.replace("`", "").replace("**", "").strip()
                 for c in line.split("|")]
        for i, c in enumerate(cells):
            if not _DIGEST.fullmatch(c):
                continue
            near = [cells[j] for j in (i - 1, i + 1)
                    if 0 <= j < len(cells) and "/" in cells[j]]
            if near:
                out[os.path.normpath(near[0]).replace("\\", "/")] = c.lower()
            break
    return out


def _newest_packet(root: Path, increments: str) -> Path | None:
    try:
        names = os.listdir(root / increments)
    except OSError:
        return None
    # NO WALRUS HERE, and the reason is the manifest's: `python-api` is DECLARED 3.7 and
    # `V30` DERIVES that floor from the constructs the tabled Python files actually use, so
    # one `:=` in a shipped script silently raises the file set's floor to 3.8 and BLOCKs the
    # gate against a row nobody changed. Measured at landing.
    matched = [(_PACKET.match(n), n) for n in names]
    packets = sorted(((int(m.group(1)), n) for m, n in matched if m), reverse=True)
    return root / increments / packets[0][1] if packets else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="devflow-evidence.py",
        description="Digest evidence files under the declared home and print "
                    "packet-ready rows; --check compares disk, git index blob and "
                    "the newest packet's recorded digest. "
                    "Exit 0 all good / 1 a check failed / 2 bad input.")
    ap.add_argument("--root", default=None,
                    help="the project root; default: the current working directory")
    ap.add_argument("files", nargs="+", help="evidence file(s) under the declared home")
    ap.add_argument("--check", action="store_true",
                    help="compare disk vs committed blob vs the packet's recorded digest")
    ap.add_argument("--fix", action="store_true",
                    help="add the `-text` mark for the evidence home to .gitattributes")
    args = ap.parse_args(argv)

    # THE RESOLVED ROOT IS THE FIRST LINE, before any read and before any --fix write,
    # for the reason its sibling states: a wrong root accepted silently is the defect.
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    print(f"devflow-evidence · project root {root.as_posix()}"
          + ("" if args.root else "  (no --root given — the current directory)"))
    if not root.is_dir():
        print(f"bad input: `{root.as_posix()}` is not a directory on disk")
        return 2
    if _is_flow_installation(root):
        print(f"bad input: `{root.as_posix()}` is the flow's own tree — a flow "
              f"INSTALLATION, not a project; run this from your project's root, or name "
              f"that root with --root")
        return 2
    state = _state(root)
    if state is None:
        print("bad input: no readable `.dev-flow/state.json` — run "
              "scripts/devflow-init-fast.py first")
        return 2
    home = _home_rel(state, "evidence",
                     f".dev-flow/{state.get('batch_id') or '<batch_id>'}/evidence")
    if home is None or "<" in home:
        print("bad input: `artifact_homes.evidence` is not a filled `repo:` home; "
              "a `vault:` home is verified by nothing this script can read")
        return 2

    rows: list[tuple[str, str, str, int]] = []  # name, rel, digest, size
    for arg in args.files:
        file = Path(arg)
        if not file.is_absolute():
            file = root / file
        rel = _rel_under(root, file, home)
        if rel is None:
            print(f"bad input: `{arg}` does not resolve under the declared home "
                  f"`{home}/` — cite each path from the repository root")
            return 2
        try:
            data = file.read_bytes()
        except OSError:
            print(f"bad input: `{rel}` is not a readable file on disk")
            return 2
        rows.append((file.name, rel, _sha256(data), len(data)))

    ga = root / ".gitattributes"
    marked = _text_marked(ga, home)
    if not marked and args.fix:
        line = f"{home}/** -text"
        try:
            text = ga.read_text(encoding="utf-8")
        except OSError:
            text = ""
        sep = "" if not text or text.endswith("\n") else "\n"
        ga.write_text(text + sep + line + "\n", encoding="utf-8")
        print(f"fixed .gitattributes — added `{line}`")
        marked = True
    if not marked:
        print(f"FAILED .gitattributes — no line marks `{home}/` -text; a normalising "
              f"git stores bytes that do not hash to what you record. Re-run with "
              f"--fix to add `{home}/** -text`")

    print(f"evidence home: {home}/")
    for name, rel, digest, size in rows:
        print(f"  {rel}  sha256 {digest}  {size} bytes")
    print("packet rows (paste into the packet's `Evidence files` table):")
    for name, rel, digest, _size in rows:
        print(f"| {name} | {rel} | {digest} |")
    if marked:
        print(f"field value: `{len(rows)} artifact(s), each at the declared home"
              + (" and cited with the digest of its stored bytes`" if args.check
                 else ", with the digest of its bytes on disk`"))

    if not args.check:
        return 0 if marked else 1

    increments = _home_rel(state, "increments",
                           f".dev-flow/{state.get('batch_id') or '<batch_id>'}/03-increments")
    packet = _newest_packet(root, increments) if increments else None
    if packet is None:
        print("cannot check: no increment packet on disk records a digest — "
              "write the packet row first")
        return 2                    # could not run, which is not the same as a failed check
    cited = _packet_digests(packet)
    _gd = _git(root, "rev-parse", "--git-dir")
    versioned = _gd is not None and _gd[0] == 0
    if not versioned:
        print(f"n/a: no git repository at `{root.as_posix()}`, so the INDEX comparison has "
              f"no subject here; the packet's recorded digests are still compared")
    print(f"checking against packet {packet.relative_to(root).as_posix()}:")

    all_match = True
    for _name, rel, digest, _size in rows:
        blob = _git(root, "cat-file", "-p", f":{rel}") if versioned else None
        if versioned and blob is None:
            print("cannot check: git could not be asked — no verdict claimed")
            return 2
        blob_digest = _sha256(blob[1]) if blob and blob[0] == 0 else None
        packet_digest = cited.get(rel)
        ok = packet_digest == digest and (blob_digest == digest or not versioned)
        all_match &= ok
        detail = []
        if versioned and blob_digest != digest:
            # NOT "committed": `:path` reads the INDEX, so a file that was only `git add`ed
            # matches here. The behaviour is what the packet asks for; the word was not.
            detail.append("index blob " +
                          (f"hashes to {blob_digest}" if blob_digest
                           else "— not staged (nothing in the index at that path)"))
        if packet_digest != digest:
            detail.append("packet records " +
                          (packet_digest if packet_digest else "no digest for this path"))
        print(f"  {'MATCH' if ok else 'MISMATCH'} {rel}"
              + ("" if ok else " — " + "; ".join(detail)))
    return 0 if (all_match and marked) else 1


if __name__ == "__main__":
    sys.exit(main())
