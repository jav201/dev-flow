"""trace_check.py: checks the Records section of dev-flow v3 (SKILL.md). Run it from the repository root.

  US     every user story is named by an active requirement
  CASE   one or more 02-test-cases*.md (one per group allowed) sit beside each requirement file, and together hold a
         case `<id>/<n>` for every active requirement
  TEST   every active requirement, or a TC/AT id it lists, is named by a file under --tests
  SLICE  every source file changed since --base is named in a requirement file or a --fixes record
  EVID   a 04-validation.md sits beside each requirement file, and every evidence path it cites is committed
  CANON  every active requirement is in --canon (batch end)

Requirement ids are HLR-, LLR- or R-<AREA>-NNN. A requirement file defines an id where a heading, a bold lead or a table row starts with it; a definition that
says "— Withdrawn" makes the id inactive. Exit 0: no gap. 1: gaps, one line each. 2: nothing to check.

With --ids PATTERN ..., only CASE and TEST run, and only for the active requirements whose id matches a pattern
(fnmatch); no match exits 2. The summary line names the checks that ran.

  tester:    trace_check.py --req .dev-flow/<inc>/01-requirements.md --ids "LLR-3.*" "R-LOAD-*"
  increment: trace_check.py --req .dev-flow/<inc>/01-requirements.md --base <inc base> --src <pkg>
  batch end: trace_check.py --req <the 01-requirements.md of each increment of THIS batch> --base <batch base> --src <pkg>
                 --fixes <batch-end correction record> --canon REQUIREMENTS.md
"""
import argparse
import fnmatch
import glob
import os
import posixpath
import re
import subprocess
import sys

ID = r"(?:US|HLR|LLR|R|TC|AT)-[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*"
ID_RE = re.compile(r"(?<![A-Za-z0-9])" + ID)
DEF_RE = re.compile(r"^\s*(#{1,6}\s+|[-*]\s+\*\*|\*\*|\|\s*)(" + ID + ")")
HEAD_RE = re.compile(r"^#{1,6}\s")
GONE_RE = re.compile(r"(?:—|–|\s-)\s*\**\s*withdrawn\b", re.I)
REQ = ("HLR-", "LLR-", "R-")
EVID_RE = re.compile(r"`([^`\s]*evidence/[^`\s]*)`")
# Tests name ids in any spelling (`TC-B100-43`, `tc_b100_43`, `test_e4_llr_171_1m_...`): compare normalised forms.
TOKEN_RE = re.compile(r"(?<![a-z0-9])(?=((?:us|hlr|llr|r|tc|at)(?:_[a-z0-9]+){1,6}))")


def norm(s):
    return re.sub(r"[^a-z0-9]+", "_", s.lower())


def git(*args):
    out = subprocess.run(("git", "-c", "core.quotepath=off") + args, capture_output=True, text=True,
                         encoding="utf-8", errors="replace", check=True).stdout
    return [line for line in out.splitlines() if line]


def parse(paths):
    """-> {id: ids named in its block}, withdrawn ids, all text. A block runs from its definition to the next
    definition or heading; a table row defines only itself."""
    blocks, gone, text = {}, set(), []
    for path in paths:
        cur = None
        with open(path, encoding="utf-8") as f:
            for line in f:
                text.append(line)
                m = DEF_RE.match(line)
                if m:
                    cur = m.group(2)
                    blocks.setdefault(cur, set())
                    if GONE_RE.search(line):
                        gone.add(cur)
                elif HEAD_RE.match(line):
                    cur = None
                if cur:
                    blocks[cur].update(ID_RE.findall(line))
                if m and m.group(1).startswith("|"):
                    cur = None
    return blocks, gone, "".join(text)


def named_tokens(root):
    found = set()
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != "__pycache__" and not d.startswith(".")]
        for name in files:
            try:
                with open(os.path.join(dirpath, name), encoding="utf-8") as f:
                    text = norm(f.read())
            except (OSError, UnicodeDecodeError):
                continue
            for run in TOKEN_RE.findall(text):
                parts = run.split("_")
                found.update("_".join(parts[:k]) for k in range(2, len(parts) + 1))
    return found


def slice_gaps(base, src, tests, req_text):
    roots = [s.replace("\\", "/").strip("/") for s in src]
    tests = tests.replace("\\", "/").strip("/") + "/"
    changed = set(git("diff", "--name-only", base)) | set(git("ls-files", "--others", "--exclude-standard"))
    gaps = []
    for f in sorted(changed):
        if f.startswith(tests) or not any(f == r or f.startswith(r + "/") for r in roots):
            continue
        if not any(re.search(r"(?<![\w.-])" + re.escape(n) + r"(?![\w-])", req_text) for n in (f, posixpath.basename(f))):
            gaps.append(("SLICE", f"{f} changed since {base} and no requirement file names it"))
    return gaps


def case_gaps(paths, active):
    gaps, text = [], ""
    for p in paths:
        files = sorted(glob.glob(posixpath.join(glob.escape(posixpath.dirname(p) or "."), "02-test-cases*.md")))
        if not files:
            gaps.append(("CASE", f"no 02-test-cases*.md beside {p}"))
            continue
        for cases in files:
            with open(cases, encoding="utf-8") as f:
                text += f.read() + "\n"
    if text:
        gaps += [("CASE", f"{r} has no test case {r}/<n>") for r in active
                 if not re.search(r"(?<![A-Za-z0-9.-])" + re.escape(r) + r"/\d", text)]
    return gaps


def committed(path, tracked):
    if any(c in path for c in "*?["):
        return any(fnmatch.fnmatchcase(t, path) for t in tracked)
    return path in tracked or any(t.startswith(path + "/") for t in tracked)


def evid_gaps(paths, tracked):
    gaps = []
    for p in paths:
        folder = posixpath.dirname(p)
        record = posixpath.join(folder, "04-validation.md")
        if not os.path.isfile(record):
            gaps.append(("EVID", f"no 04-validation.md beside {p}"))
            continue
        with open(record, encoding="utf-8") as f:
            cited = sorted(set(EVID_RE.findall(f.read())))
        if not cited:
            gaps.append(("EVID", f"{record} cites no evidence path"))
        for c in cited:
            where = (posixpath.normpath(posixpath.join(folder, c)), posixpath.normpath(c))
            if not any(committed(w, tracked) for w in where):
                gaps.append(("EVID", f"{record} cites {c}, which is not committed"))
    return gaps


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    head, rest = __doc__.split("\n", 1)
    ap = argparse.ArgumentParser(description=head, epilog=rest, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--req", nargs="+", required=True, help="the requirement files (globs allowed)")
    ap.add_argument("--tests", default="tests", help="the tests folder (default: tests)")
    ap.add_argument("--base", help="the commit the change started from; turns SLICE on")
    ap.add_argument("--src", nargs="+", default=[], help="the source folders SLICE looks at")
    ap.add_argument("--fixes", nargs="+", default=[], help="batch-end correction records; the files they name count for SLICE")
    ap.add_argument("--canon", help="the requirements canon; turns CANON on")
    ap.add_argument("--ids", nargs="+", metavar="PATTERN",
                    help="requirement id patterns (fnmatch); run only CASE and TEST, only for the matching requirements")
    a = ap.parse_args(argv)
    paths = sorted({os.path.relpath(p).replace("\\", "/") for g in a.req for p in (glob.glob(g) or [g])})
    if a.base and not a.src:
        ap.error("--base needs --src")
    if not os.path.isdir(a.tests):
        print(f"trace_check: no tests folder {a.tests}")
        return 2
    blocks, gone, text = parse(paths)
    reqs = sorted(i for i in blocks if i.startswith(REQ))
    if not reqs:
        print("trace_check: no requirement (HLR, LLR or R-) defined in " + ", ".join(paths))
        return 2
    active = [r for r in reqs if r not in gone]
    stories = sorted(i for i in blocks if i.startswith("US-"))
    gaps, ran = [], ["CASE", "TEST"]
    if a.ids:
        active = [r for r in active if any(fnmatch.fnmatchcase(r, p) for p in a.ids)]
        if not active:
            print("trace_check: no active requirement matches --ids " + " ".join(a.ids))
            return 2
    else:
        ran = ["US"] + ran
        for us in stories:
            if not any(us in blocks[r] for r in active):
                gaps.append(("US", f"{us} is named by no active requirement"))
    found = named_tokens(a.tests)
    gaps += case_gaps(paths, active)
    for r in active:
        ids = {r} | {i for i in blocks[r]
                     if i.startswith(("TC-", "AT-")) or (r.startswith("HLR-") and i.startswith("LLR-"))}
        if not any(norm(i) in found for i in ids):
            gaps.append(("TEST", f"{r} is named by no file under {a.tests}, and neither is a TC/AT id it lists"))
    if a.base and not a.ids:
        ran.append("SLICE")
        for fix in a.fixes:
            with open(fix, encoding="utf-8") as f:
                text += f.read()
        gaps += slice_gaps(a.base, a.src, a.tests, text)
    if not a.ids:
        ran.append("EVID")
        gaps += evid_gaps(paths, set(git("ls-files")))
    if a.canon and not a.ids:
        ran.append("CANON")
        with open(a.canon, encoding="utf-8") as f:
            have = set(ID_RE.findall(f.read()))
        gaps += [("CANON", f"{r} is not in {a.canon}") for r in active if r not in have]
    for check, msg in gaps:
        print(f"{check:<6} {msg}")
    if a.ids:
        scope = f"{len(active)} active requirements match --ids"
    else:
        scope = f"{len(stories)} US, {len(active)} active requirements ({len(reqs) - len(active)} withdrawn)"
    print(f"trace_check: {scope}, checks run: {', '.join(ran)}, {len(gaps)} gap(s)")
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
