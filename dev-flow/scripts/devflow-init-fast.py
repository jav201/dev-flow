"""devflow-init-fast.py — the fast flow's init, mechanically.

    cd <your project's root>                         # the batch is declared HERE
    python <this flow's root>/scripts/devflow-init-fast.py [PROJECT ROOT]

Contract: declare a `mode: fast` batch in the project root — the argument when
one is given, the CURRENT WORKING DIRECTORY when none is — exactly as
`commands/dev-flow-init.md` §*The `fast` declaration* specifies — the six keys,
`guided` seeded by measurement, `decisions_log: []` seeded when guided — create
the homes that declaration names (`03-increments/`, `evidence/`, the backlog
lane), mark the evidence home `-text` in `.gitattributes`, and copy
`templates/fast-dev-flow/spec-template.md` to `.fast-dev-flow/spec.md` with the
header fields filled. The FIRST line of output is the absolute root it resolved,
so a wrong root is visible before anything is written; a root that is a flow
INSTALLATION is refused outright. Idempotent: refuses to overwrite an existing
batch unless `--force`. Exit 0 done / 1 refused / 2 bad input.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# The batch-id grammar's one home is `_V28_BATCH` in `scripts/devflow-validate.py`;
# this is the same grammar, re-spelled here because a script in the hand cannot
# import the gate it feeds. Widening one without the other is a known defect class.
_BATCH = re.compile(r"^(\d{4}-\d{2}-\d{2})-(batch|fast)-(\d+)$")

_ROOT_SIGNALS = (".git", "package.json", "pyproject.toml", "README.md")
# The two witnesses of a flow INSTALLATION -- the manifest and the gate script, TOGETHER --
# named SEGMENT BY SEGMENT in each of the two layouts a flow is installed in. Either witness
# alone is common enough that a project could carry it; both together is what a flow home is.
# Spelled in both scripts because a script in the hand cannot import its sibling; widening one
# without the other is a known defect class, and this pair is the thing to widen.
_LAYOUTS = ((("FLOW-VERSION.md",), ("scripts", "devflow-validate.py")),
            (("docs", "FLOW-VERSION.md"), ("docs", "tools", "devflow-validate.py")))


def _flow_root() -> Path:
    """The flow home this script ships in — PROBED over both layouts, never assumed.

    In the published bundle this file sits at `scripts/devflow-init-fast.py` and the
    commands are one directory up; the tree the bundle is generated from keeps it one
    level deeper, and they are two up there. A hard-coded depth resolves in exactly one
    of the two and hands the other a template path that does not exist — measured while
    landing this script, where the fixed depth named the wrong directory and the spec
    template was reported unreadable. `devflow-scan-spec.py` probes the same anchor for
    the same reason; both scripts answer the question the same way, or one of them is
    looking somewhere else.
    """
    here = Path(__file__).resolve().parent
    for up in (here.parent, here.parent.parent):
        if (up / "commands" / "fast-dev-flow.md").is_file():
            return up
    return here.parent


def _spec_template(flow: Path) -> Path:
    """Where the fast spec template ships, under either layout's flow root."""
    return flow / "templates" / "fast-dev-flow" / "spec-template.md"


def _is_flow_installation(root: Path) -> bool:
    """Does `root` hold a flow INSTALLATION's own two witnesses, in either layout?"""
    return any(root.joinpath(*_man).is_file() and root.joinpath(*_tool).is_file()
               for _man, _tool in _LAYOUTS)


def _flow_version(flow: Path) -> str | None:
    """The revision `FLOW-VERSION.md` declares — canon keeps it under `docs/`."""
    for cand in (flow / "FLOW-VERSION.md", flow / "docs" / "FLOW-VERSION.md"):
        try:
            text = cand.read_text(encoding="utf-8")
        except OSError:
            continue
        m = re.search(r"(?m)^flow_version\s*:\s*(\S+)\s*$", text)
        if m:
            return m.group(1)
    return None


def _git(root: Path, *args: str) -> str | None:
    """Stdout of a read-only git call, or None when git cannot answer."""
    try:
        out = subprocess.run(["git", "-C", str(root), *args],
                             capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def _existing_batches(devflow: Path) -> list[str]:
    """Directory names under `.dev-flow/` that parse as batch records."""
    try:
        names = os.listdir(devflow)
    except OSError:
        return []
    return sorted(n for n in names
                  if _BATCH.match(n) and (devflow / n).is_dir())


def _next_batch_id(devflow: Path, today: str) -> str:
    """Today's date, suffix auto-incremented over same-date batches of either family."""
    high = 0
    for name in _existing_batches(devflow):
        m = _BATCH.match(name)
        if m and m.group(1) == today:
            high = max(high, int(m.group(3)))
    return f"{today}-fast-{high + 1:02d}"


def _fill_spec(template: str, project: str, batch_id: str, revision: str,
               base_ref: str | None, started: str, objective: str | None) -> str:
    """The template with the fields this script can fill filled; the rest ships as-is."""
    text = template.replace("<PROJECT>", project)
    # THE REPLACEMENT IS A LAMBDA, never an f-string: `re.sub` reads `\\g`, `\\1` and a
    # lone backslash out of the REPLACEMENT, and a base ref or a revision is caller data.
    def _row(name: str, value: str) -> None:
        nonlocal text
        text = re.sub(r"(?m)^\| " + re.escape(name) + r" \|.*\|$",
                      lambda _m: "| %s | `%s` |" % (name, value), text)

    _row("Batch", batch_id)
    _row("Flow revision", revision)
    if base_ref:
        _row("Base ref", base_ref)
    _row("Started", started)
    if objective:
        text = text.replace("`<what this batch solves, in one sentence>`",
                            objective, 1)
    return text


def _mark_text(gitattributes: Path, line: str) -> str:
    """Ensure the evidence home is marked `-text`; returns what happened."""
    try:
        text = gitattributes.read_text(encoding="utf-8")
    except OSError:
        text = ""
    if line in [ln.strip() for ln in text.splitlines()]:
        return "already marked"
    sep = "" if not text or text.endswith("\n") else "\n"
    gitattributes.write_text(text + sep + line + "\n", encoding="utf-8")
    return "written"


_BACKLOG = """# Backlog — {project}

The cross-batch queue, shared by `/dev-flow` and `/fast-dev-flow`. Every open item lives
in exactly ONE canonical file; a project MAY partition it into lanes declared in its
`docs/engineering-rules.md`, which is a split and never a copy.

Base ref: {base_ref}
Last refresh: {today}

## Open
## Done
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="devflow-init-fast.py",
        description="Declare a `mode: fast` batch: state.json, the homes it names, "
                    "the backlog lane, the `-text` mark and a header-filled spec. "
                    "Exit 0 done / 1 refused (existing batch; use --force) / 2 bad input.")
    ap.add_argument("root", nargs="?", default=None,
                    help="the project root (the repository the batch works in); "
                         "default: the current working directory")
    ap.add_argument("--objective", default=None,
                    help="one sentence; fills the spec's section 1")
    ap.add_argument("--lang", choices=("en", "es"), default="en",
                    help="language the spec's prose will be authored in (default en)")
    ap.add_argument("--force", action="store_true",
                    help="overwrite an existing batch declaration, archiving what it replaces")
    ap.add_argument("--root-anyway", action="store_true",
                    help="this directory IS the project root although it carries none of the "
                         "usual signals (--force does NOT imply this)")
    args = ap.parse_args(argv)

    # THE RESOLVED ROOT IS THE FIRST LINE THIS SCRIPT PRINTS, before any guard and
    # before any write. Round 3's reader scaffolded the flow's own installation because
    # the root it passed was never echoed back: a script that accepts a wrong root
    # silently is the same defect as prose that never says which path to type.
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    print(f"devflow-init-fast · project root {root.as_posix()}"
          + ("" if args.root else "  (no argument given — the current directory)"))
    if not root.is_dir():
        print(f"bad input: `{root.as_posix()}` is not a directory on disk — nothing written")
        return 2
    flow = _flow_root()
    if root == flow or flow in root.parents or _is_flow_installation(root):
        print(f"bad input: `{root.as_posix()}` is the flow's own tree — a flow "
              f"INSTALLATION, not a project; run this from your project's root, or name "
              f"that root as the argument — nothing written")
        return 2
    # THE ROOT-SIGNAL OVERRIDE IS ITS OWN FLAG. Until the landing review it rode on
    # `--force`, which pre-check 2 recommends for a different purpose entirely, so the one
    # command the page tells you to reach for turned the project-root guard off as a side
    # effect -- round 3's defect, re-opened through the repair for it.
    if not any((root / s).exists() for s in _ROOT_SIGNALS) and not args.root_anyway:
        print(f"bad input: none of the project-root signals "
              f"({', '.join(_ROOT_SIGNALS)}) exist under `{root.as_posix()}` — "
              f"pre-check 1's one home is `commands/dev-flow-init.md` §Pre-checks, "
              f"and a script cannot ask; pass --root-anyway only if this really is the "
              f"project root — nothing written")
        return 2

    revision = _flow_version(flow)
    if revision is None:
        print("bad input: no `flow_version :` line readable in FLOW-VERSION.md "
              "beside this script (or under its `docs/`) — nothing written")
        return 2
    template_path = _spec_template(flow)
    try:
        template = template_path.read_text(encoding="utf-8")
    except OSError:
        print(f"bad input: `{template_path.as_posix()}` is not readable — "
              f"this script must run from the flow's own `scripts/` — nothing written")
        return 2

    devflow = root / ".dev-flow"
    fastdir = root / ".fast-dev-flow"
    state_path = devflow / "state.json"
    spec_path = fastdir / "spec.md"

    if (state_path.exists() or spec_path.exists()) and not args.force:
        found = " and ".join(p.relative_to(root).as_posix()
                              for p in (state_path, spec_path) if p.exists())
        print(f"refused: this project already declares a batch ({found}). Re-run with "
              f"--force to start a new one; the spec and the declaration it replaces are "
              f"archived under `.fast-dev-flow/archive/` and `.dev-flow/archive/`, ledger "
              f"included — nothing written")
        return 1

    today = datetime.now().strftime("%Y-%m-%d")
    started = datetime.now().strftime("%Y-%m-%d %H:%M")
    batch_id = _next_batch_id(devflow, today)
    guided = not _existing_batches(devflow)  # first batch is seeded by measurement
    base_ref = _git(root, "rev-parse", "HEAD")
    project = root.name

    written: list[str] = []

    # --force ARCHIVES BOTH RECORDS, and the second one is the point: `state.json` is the
    # single slot that holds `decisions_log`, so archiving the spec while overwriting the
    # declaration beside it destroys the guided ledger and keeps the prose. Found at the
    # landing review, on a batch whose `A` decision had been recorded.
    #
    # THE NAME IS MADE UNIQUE, and the second review is why: the stamp is second-resolution
    # and `Path.replace` overwrites silently, so six `--force` runs inside two seconds
    # archived six records into two files and printed six lines saying they were kept. Four
    # of those lines were false, which is worse than the loss.
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    def _archive(path: Path, home: Path, suffix: str) -> str:
        home.mkdir(parents=True, exist_ok=True)
        target, n = home / f"{stamp}-{suffix}", 0
        while target.exists():
            n += 1
            target = home / f"{stamp}-{n:02d}-{suffix}"
        path.replace(target)
        return target.relative_to(root).as_posix()

    state: dict = {
        "mode": "fast",
        "batch_id": batch_id,
        "flow_version": revision,
        "stations_active": ["P1", "P3"],
        "guided": guided,
    }
    if guided:
        # The one key that asks this flow to write the ledger back gets its ledger
        # seeded EMPTY: at birth the batch has genuinely recorded no decision, and
        # the first gate appends to a home that exists rather than inventing one.
        state["decisions_log"] = []
    state["artifact_homes"] = {
        "spec": "repo:.fast-dev-flow/spec.md",
        "increments": f"repo:.dev-flow/{batch_id}/03-increments/",
        "evidence": f"repo:.dev-flow/{batch_id}/evidence/",
        "backlog": "repo:.dev-flow/BACKLOG.md",
    }

    # A HOME'S NAME MAY ALREADY BE TAKEN BY A FILE, and `mkdir` raises an OSError whose
    # traceback is not a contract. Every refusal this script makes is one line and an exit
    # code; an unexpected one is no different.
    try:
        devflow.mkdir(exist_ok=True)
        (devflow / batch_id / "03-increments").mkdir(parents=True, exist_ok=True)
        (devflow / batch_id / "evidence").mkdir(parents=True, exist_ok=True)
        fastdir.mkdir(exist_ok=True)
    except OSError as exc:
        print(f"bad input: the homes this declaration names could not be created under "
              f"`{root.as_posix()}` ({exc.__class__.__name__}) — nothing written")
        return 2
    written.append(f".dev-flow/{batch_id}/03-increments/ and .dev-flow/{batch_id}/evidence/ "
                   f"(empty — git meets them with their first content; no .gitkeep)")

    # NOTHING IS MOVED UNTIL EVERY REFUSAL IS BEHIND US. The archive used to run above the
    # guard, so a run that then refused had already emptied both homes and printed
    # *nothing written* over a project that now declared no batch at all -- a state no
    # documented step produces and none describes how to leave. Second review, `N1`.
    if spec_path.exists():
        written.append("archived the previous spec -> "
                       + _archive(spec_path, fastdir / "archive", "spec.md"))
    if state_path.exists():
        written.append("archived the previous declaration, ledger included -> "
                       + _archive(state_path, devflow / "archive", "state.json"))

    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    written.append(f".dev-flow/state.json — batch `{batch_id}`, flow {revision}, "
                   f"guided: {'true' if guided else 'false'}"
                   + (", decisions_log seeded []" if guided else ""))

    backlog_path = devflow / "BACKLOG.md"
    if backlog_path.exists():
        written.append(".dev-flow/BACKLOG.md — already on disk, left untouched")
    else:
        backlog_path.write_text(
            _BACKLOG.format(project=project,
                            base_ref=base_ref or "(no commit yet — fill at first reconciliation)",
                            today=today),
            encoding="utf-8")
        written.append(".dev-flow/BACKLOG.md — the empty queue, base ref "
                       + (base_ref or "unfilled (no commit yet)"))

    ga_result = _mark_text(root / ".gitattributes",
                           f".dev-flow/{batch_id}/evidence/** -text")
    written.append(f".gitattributes — evidence home marked -text ({ga_result})")

    spec_path.write_text(
        _fill_spec(template, project, batch_id, revision, base_ref, started,
                   args.objective),
        encoding="utf-8")
    filled = "Batch, Flow revision, Started" + (", Base ref" if base_ref else "")
    written.append(f".fast-dev-flow/spec.md — from the template, filled: {filled}"
                   + (", section 1" if args.objective else "")
                   + (" — Base ref left as the placeholder (no commit yet)"
                      if not base_ref else ""))

    print(f"declared · batch {batch_id} · flow {revision}")
    for w in written:
        print(f"  wrote {w}")
    if args.lang == "es":
        print("  note: --lang es — write the spec's prose in Spanish; this script "
              "fills fields, not prose")
    print("")
    # THE NEXT COMMANDS ARE PRINTED AS ABSOLUTE PATHS, both sides. This script sits at
    # `scripts/` in a bundle and one level deeper in the tree it is generated from, and a
    # relative spelling is true in one of those and a dead path in the other -- the same
    # defect class as the root that was never echoed.
    _here = Path(__file__).resolve().parent
    # ⚠ THIS HINT USED TO PUBLISH AN ORDER, AND THE ORDER IT PUBLISHED WAS WRONG.
    # It read *fill the spec's sections 1-4 ... then the scanner and the gate*, while
    # `commands/fast-dev-flow.md` pre-check 6 -- the step that comes next, and that page's
    # own numbering -- says to run the gate BEFORE Phase A, which is before any of those
    # sections exist. Two documents ordering the same four acts differently, and a reader
    # who trusted this one skipped a refusal. The page is the order's ONE home, so this
    # script names the page and states no order at all; the two commands stay, because a
    # reader still needs their absolute spelling on this machine. (flow rev94, benchmark
    # round 1, `init-fast-next-hint-contradicts-gate-order`.)
    print("next: open `commands/fast-dev-flow.md` §Pre-checks and continue from there; "
          "it is the one home for what comes next and in what order. The two commands it "
          "names run from anywhere:")
    print(f"  python {(_here / 'devflow-scan-spec.py').as_posix()} "
          f"{(root / '.fast-dev-flow' / 'spec.md').as_posix()}")
    print(f"  python {(_here / 'devflow-validate.py').as_posix()} {root.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
