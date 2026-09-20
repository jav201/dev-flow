# -*- coding: utf-8 -*-
"""devflow-mutate — the flow's CANONICAL mutation harness.

    python devflow-mutate.py                     run every mutant of the default subject
    python devflow-mutate.py --list              print the registry, run nothing
    python devflow-mutate.py --select id,id      run a subset, by registry id
    python devflow-mutate.py --origin rev63      run one revision's migrated battery
    python devflow-mutate.py --subject NAME      a subject other than the validator
    python devflow-mutate.py --self-proof        the four planted mutants of C-57, on a
                                                 fixture subject this file writes itself

WHY THIS FILE IS PYTHON, said here so the flow's stack-agnostic rule is visibly respected
rather than quietly broken. `commands/dev-flow.md` binds every project to its OWN stack and
this repository ships no general-purpose tooling. The exception is argued, not assumed: this
harness's SUBJECT is `docs/tools/devflow-validate.py`, which is Python, and a harness that
mutates Python source has to read and rewrite Python source. It is not offered to projects --
`<project>/tools/mutation_harness.py` stays where it is and keeps mutating that project's code.
The operator's 2026-09-07 ruling (`Q1`) says exactly this in both halves.

WHAT A THROWAWAY HARNESS CANNOT DO, which is the whole reason this file exists: 42 named
mutants were written across rev52, rev54 and rev55, and not one of them can be re-run today.
Each battery re-learned the same four lessons and two of them re-shipped the same defects.
The registry beside this file (`devflow-mutants.json`) is the accumulation those batteries
never had, and every mutant in it carries the revision that first wrote it.

FIVE PROPERTIES, EACH PAID FOR BY A DEFECT THAT SHIPPED. They are the harness's contract and
each one has an arm in `devflow-validate.py --selftest`:

  1. THE VERDICT COMES FROM THE LAST LINE, BY EQUALITY.  rev49's own arm prints a child
     process's `SELFTEST PASSED` MID-RUN, so a harness searching for that substring scored
     ALL TWELVE applicable mutants SURVIVED at exit 1 -- a false-survivor sweep. The last
     non-blank line is stripped and compared for EQUALITY against the subject's declared
     verdict literals. `verdict_of` is pure and armed on that exact transcript.

  2. A CRASH IS NOT A SURVIVOR.  A mutant that dies at import emits no arm line at all, and a
     reader scoring only what was printed calls that silence a survival (`R-88-10`: 0 arm
     lines and no FAIL scored SURVIVED, against 299 when rebuilt; the shell's `$?` captured
     the pipeline, so the crash also reported exit 0). Anything that is not one of the two
     declared verdict lines is a CRASH, and CRASH is a verdict of its own.

  3. A MUTANT THAT DID NOT APPLY IS NOT A RESULT.  Two rev63 mutants matched their anchor
     ZERO times and one earlier battery split a path so its first two mutants never applied
     at all -- both render, to a careless reader, exactly like a survivor. An anchor must
     match EXACTLY ONCE, and a substitution whose bytes do not move the file is a no-op.
     Both are `BAD`, never `SURVIVED`, and `BAD` fails the run.

  4. THE VERDICT IS PER ARM, NEVER PER MUTANT.  A process exit code is a boolean over a map:
     one verdict per mutant over a set containing parametrized arms cannot say WHICH arms
     reddened, so an inert arm hides behind a sibling that failed and `3 passed` sits unread
     in the transcript. Four arms once survived a FULLY REMOVED gate that way. This harness
     reports the SET of newly-red arm labels per mutant and an inverse index per arm, and
     `--per-arm` prints the map the exit code cannot carry.

  5. AN UNMUTATED BASE RUNS FIRST, AND A RED BASE ABORTS.  Its failing-arm set is the NOISE
     FLOOR and is subtracted from every mutant's, so a kill can never be claimed off an arm
     that was already red. It happened twice in one batch, and both times the kills were
     discharged rather than reported. A base that reaches no verdict, or the failing one,
     ABORTS the run (exit 2) instead of scoring against it.

AND A SIXTH THIS HARNESS ADDS, because migrating rev63's battery exposed it. Some arms are
DERIVED: `ENC VERDICT-live` re-runs the whole selftest in a child, so it reddens whenever
ANYTHING else does -- and it also reddens when the child merely CRASHES, which no arm
detected. A kill resting only on a derived arm is not a detection, so derived arms are
subtracted before the KILLED decision and reported separately as `derived-only`.

THE NAMED-MUTATION MANDATE, MADE VERIFIABLE (`R-88-12`). `LLR-88.4` required every arm to
name, IN A COMMENT, the mutation that reddens it -- and nothing in a selftest can read a
comment, so an arm was audited as covering an axis it did not touch and the audit ticked the
box (623 of 1998 block lines, 31% of the scanned surface, unreached in silence). Here the
claim is a DECLARED FIELD, `expect_arms`, which this harness parses and CHECKS against the
arms the mutation actually reddened. A mutant whose named arm stays green is reported
`claim UNMET`, by name, and fails the run. That is the negative control the mandate never had.

NOTHING LIVE IS EVER MUTATED. Every run copies the subject -- and, when the subject declares
one, the flow home it reads through `DEVFLOW_HOME` -- into a scratch tree, and mutates the
copy. The live tree is opened for reading and never for writing.
"""
import argparse
import glob
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REGISTRY = os.path.join(HERE, "devflow-mutants.json")
DEFAULT_HOME = os.path.dirname(os.path.dirname(HERE))          # docs/tools -> ~/.claude
SCHEMA = 1

KILLED, CRASH, SURVIVED, BAD = "KILLED", "CRASH", "SURVIVED", "BAD"
# A FIFTH OUTCOME, AND IT IS NOT A VERDICT. Some mutants only redden on some
# interpreters -- rev60's `M16` plants a bare escape that `-W error` reddens on 3.12 and
# not on 3.11. Running one where it cannot fire and calling the result SURVIVED reports
# the interpreter, not the code. It is REPORTED and COUNTED rather than skipped, because
# an arm that quietly excuses itself is the vacuous check one level out.
SKIPPED = "SKIPPED"


# ---------------------------------------------------------------- the pure core
#
# Everything below this line up to `load_registry` is PURE: text in, verdict out, no
# filesystem and no subprocess. That is deliberate and it is what lets the validator's own
# selftest drive the classifier directly on the transcripts that produced each historical
# defect, instead of re-deriving them from a live run. The plumbing -- does a mutant actually
# reach the file, does the subject actually start -- cannot be proved that way, which is why
# `--self-proof` exists beside it.

def read_text(path):
    """A file as text, LF-normalised, or None. BYTES in, str out -- never text mode.

    Not tidiness. Text-mode WRITING translates LF to CRLF on Windows, so a mutated copy
    written that way differs from its source on EVERY line and no byte comparison against it
    means anything; text-mode READING then hides the difference again. One project's harness
    failed its own SHA-256 restore check for exactly this, and the lesson is registered as
    "a harness that guarantees bytes must do its I/O in bytes". Reading and writing here are
    a matched pair: both in bytes, both LF.
    """
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError:
        return None
    return raw.decode("utf-8", "replace").replace("\r\n", "\n")


def write_text(path, text):
    """Text to a file as UTF-8 with LF endings, in bytes. See `read_text`."""
    with open(path, "wb") as fh:
        fh.write(text.replace("\r\n", "\n").encode("utf-8"))


def apply_mutation(src, old, new):
    """(source, anchor, replacement) -> (mutated source, status). PURE.

    THREE OUTCOMES AND NOT TWO. `ok` is the only one that produces a result; the other two
    are `BAD` and they are the reason this function returns a status instead of raising:
    a battery that stops at the first unappliable mutant reports nothing about the rest.

      `ok`             the anchor matched exactly once and the bytes moved.
      `anchor:<n>`     the anchor matched `n` times, n != 1. ZERO means the target is gone --
                       the code moved under the registry, which is the migration case this
                       harness was written to make visible. MORE THAN ONE means the mutation
                       is ambiguous: it would land somewhere the author did not name.
                       DISTINCT from `nofile` (see `one`), because "the code moved" and "the
                       file is not in the staged tree" have different fixes and one sentence
                       for both is how a staging bug reads as a migration.
      `noop`           the anchor matched once and the replacement left the file identical.
                       This is the case that reads exactly like a survivor and is not one:
                       nothing was tested, so there is nothing to have survived.
    """
    n = src.count(old)
    if n != 1:
        return src, "anchor:%d" % n
    out = src.replace(old, new, 1)
    if out == src:
        return src, "noop"
    return out, "ok"


def verdict_of(text, pass_line, fail_line):
    """The subject's verdict, from the LAST non-blank line, BY EQUALITY. PURE.

    -> `"PASS"`, `"FAIL"`, or None when the run reached no verdict at all.

    `in` IS THE DEFECT, NOT A SHORTHAND FOR IT. rev49's `ENC VERDICT-live` arm runs a CHILD
    `--selftest` and prints its output, so `SELFTEST PASSED` appears MID-RUN in a transcript
    whose own verdict is `SELFTEST FAILED`. A substring reader scored twelve applicable
    mutants SURVIVED against a process that exited 1. Reading the last line by equality is
    the whole repair, and it is why this function takes the text rather than an exit code.
    """
    lines = [ln.strip() for ln in (text or "").split("\n") if ln.strip()]
    if not lines:
        return None
    last = lines[-1]
    if last == pass_line:
        return "PASS"
    if last == fail_line:
        return "FAIL"
    return None


def failing_arms(text, arm_re, fail_re):
    """The set of arm labels this transcript reports as FAILING. PURE.

    An arm label is what `arm_re` captures -- for the validator, the rule id and the arm name,
    which together are the RESOLVED NODE ID of property 4. Returning a SET of labels rather
    than a count is the point: `len(fails) > 0` is the boolean that hid four inert arms behind
    a fifth that failed.
    """
    arm = re.compile(arm_re)
    bad = re.compile(fail_re)
    out = set()
    for line in (text or "").split("\n"):
        if not bad.search(line):
            continue
        m = arm.match(line)
        if m:
            out.add(" ".join(g for g in m.groups() if g))
    return out


def classify(status, verdict, grew):
    """(apply status, verdict, newly-red arm labels) -> (verdict word, reason). PURE.

    THE WHOLE TAXONOMY IN ONE PLACE, so it can be armed without running anything. Every row
    is a defect that shipped, and the table is ordered by which mistake is cheapest to make:

      status != ok      -> BAD       the mutation never happened. Not a result.
      verdict is None   -> CRASH     no declared verdict line was reached. A file that dies
                                     at import prints no arm line, and silence is not a pass.
      verdict == PASS   -> SURVIVED  the subject ran clean under the mutation. A real finding.
      FAIL, grew empty  -> SURVIVED  the failures are the BASE's, not this mutant's. Scoring
                                     these KILLED is how a red baseline manufactures kills.
      FAIL, grew        -> KILLED    an arm that was green before this mutation is red now.
    """
    if status.startswith("nofile:"):
        return BAD, ("the mutant's target file is not in the staged tree (%s) -- a staging "
                     "fault, NOT a drifted anchor" % status.split(":", 1)[1])
    if status.startswith("anchor:"):
        return BAD, "mutation did not apply (%s)" % status
    if status == "noop":
        return BAD, "mutation applied as a no-op -- the bytes did not move"
    if status != "ok":
        # NOT A CATCH-ALL WITH A SPECIFIC SENTENCE. The first cut ended with the no-op
        # sentence for every status it did not recognise, so a `nofile:` fault -- and any
        # status a later revision mints -- was reported as "the bytes did not move", sending
        # the next reader to retire a mutant that is perfectly good. A fourth status was
        # minted in this rev alone; there will be a fifth.
        return BAD, "unrecognised apply status %r -- this harness does not know what happened" % status
    if verdict is None:
        return CRASH, "no declared verdict line was reached -- the subject died, it did not pass"
    if verdict == "PASS":
        return SURVIVED, "the subject passed under the mutation"
    if not grew:
        return SURVIVED, "the subject failed, but on the BASE's own arms -- nothing new reddened"
    return KILLED, "%d arm(s) went red that the BASE did not have red" % len(grew)


def claim_check(expect_arms, grew):
    """(the mutant's DECLARED arms, the arms that actually reddened) -> (met, missing). PURE.

    `R-88-12` made executable. A declaration of `[]` is `unclaimed`, not `met`: a mutant that
    names no arm has made no claim, and reporting that as a satisfied claim is the free pass
    the mandate had for a year.
    """
    if not expect_arms:
        return "unclaimed", []
    missing = [a for a in expect_arms if a not in grew]
    return ("met" if not missing else "UNMET"), missing


# ---------------------------------------------------------------- the registry

def load_registry(path):
    """The mutant registry, validated enough that a typo is a message and not a traceback."""
    text = read_text(path)
    if text is None:
        sys.exit("registry not found: %s" % path)
    try:
        reg = json.loads(text)
    except ValueError as exc:
        sys.exit("registry is not valid JSON: %s" % exc)
    if reg.get("schema") != SCHEMA:
        sys.exit("registry schema %r, this harness speaks %d" % (reg.get("schema"), SCHEMA))
    ids = [m["id"] for m in reg["mutants"]]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        sys.exit("duplicate mutant id(s): %s" % ", ".join(dupes))
    for m in reg["mutants"]:
        if m["subject"] not in reg["subjects"]:
            sys.exit("mutant %s names unknown subject %r" % (m["id"], m["subject"]))
    return reg


def select(reg, ids=None, origin=None, subject=None, include_retired=False):
    """The mutants this run will apply, in registry order."""
    out = []
    for m in reg["mutants"]:
        if m.get("retired") and not include_retired:
            continue
        if ids and m["id"] not in ids:
            continue
        if origin and m.get("origin") != origin:
            continue
        if subject and m["subject"] != subject:
            continue
        out.append(m)
    return out


# ---------------------------------------------------------------- the runner

def stage(work, subj, home_root):
    """A scratch copy of the subject -- and of the flow home when the subject declares one.

    The validator's `--selftest` reads templates and commands through `_flow_home()`, which
    honours `DEVFLOW_HOME`. Mutating a TEMPLATE is therefore as real a mutation as mutating
    the source, and half the migrated registry does exactly that -- so the home is copied
    whole and the copy is what the run reads.
    """
    root = os.path.join(work, "tree")
    os.makedirs(root, exist_ok=True)
    if subj.get("home_copy"):
        # A `home_copy` ENTRY MAY BE A GLOB, and rev67 is why. An arm that walks
        # `skills/*/SKILL.md` must meet every one of them in the staged tree or the BASE run
        # measures a DIFFERENT population from the live one and fails before a single mutant
        # is scored -- which is exactly what happened. Naming the four skills the arm used to
        # read by hand would re-create the second inventory the arm was widened to abolish,
        # and copying `skills/` whole is not an option either: it is 419 MB, 388 of them one
        # vendorized skill, per mutant. The glob copies the 35 files the arm actually reads.
        rels = []
        for rel in subj["home_copy"]:
            if "*" in rel:
                hits = sorted(glob.glob(os.path.join(home_root, rel.replace("/", os.sep))))
                # A PATTERN THAT MATCHES NOTHING IS A HARNESS FAULT, not an empty population.
                # Silently contributing zero files stages a tree the arms then measure as a
                # smaller corpus, and the failure surfaces two layers from its cause -- as a
                # BASE vector mismatch nobody would trace back to a typo in this list.
                if not hits:
                    raise RuntimeError(
                        "home_copy pattern %r matched nothing under %s" % (rel, home_root))
                rels += [os.path.relpath(h, home_root).replace(os.sep, "/") for h in hits]
            else:
                rels.append(rel)
        for rel in rels:
            src = os.path.join(home_root, rel.replace("/", os.sep))
            dst = os.path.join(root, rel.replace("/", os.sep))
            if os.path.isdir(src):
                # `__pycache__` is EXCLUDED, and it is not housekeeping: `copy2` preserves
                # mtime, so a stale `.pyc` copied beside its source satisfies the interpreter's
                # freshness check and the BASE run executes bytecode nobody wrote. That is
                # `C-46` planted by the harness itself, in the one run whose job is to be
                # trustworthy.
                shutil.copytree(src, dst,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            elif os.path.isfile(src):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
        subject_path = os.path.join(root, subj["path"].replace("/", os.sep))
        if not os.path.isfile(subject_path):
            os.makedirs(os.path.dirname(subject_path), exist_ok=True)
            shutil.copy2(os.path.join(home_root, subj["path"].replace("/", os.sep)),
                         subject_path)
        return root, subject_path
    subject_path = os.path.join(root, os.path.basename(subj["path"]))
    shutil.copy2(os.path.join(home_root, subj["path"].replace("/", os.sep)), subject_path)
    return root, subject_path


def interpreter_version(interpreter):
    """(major, minor) of an interpreter, ASKED rather than assumed. -> tuple or None."""
    try:
        p = subprocess.run([interpreter, "-c",
                            "import sys;print('%d.%d' % sys.version_info[:2])"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    out = p.stdout.decode("utf-8", "replace").strip().split(".")
    return tuple(int(x) for x in out) if len(out) == 2 and all(
        x.isdigit() for x in out) else None


def run_once(interpreter, root, subject_path, subj, timeout):
    """Execute the staged subject and return its combined transcript."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    if subj.get("home_copy"):
        env["DEVFLOW_HOME"] = root
    argv = [interpreter, subject_path] + list(subj.get("argv", []))
    # `stdout=PIPE` and not `capture_output=`: this file is canon, and every canon `.py` is
    # scanned by `V30` to DERIVE the flow's declared Python API floor. `capture_output=` is a
    # 3.7 construct and would make this harness -- a script with no need of it -- one of the
    # sites that binds the floor, and the first one cited. The floor stays where it is
    # measured: `devflow-validate.py:41`.
    try:
        proc = subprocess.run(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              env=env, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        # A HANG IS A CRASH, NOT AN ABORT. Letting this propagate would throw away every
        # result already computed -- ninety minutes of them -- over the one mutant the
        # timeout exists for. The partial output is kept and no verdict line follows it,
        # which is precisely what `verdict_of` reads as CRASH.
        # WHATEVER WAS FLUSHED, which in practice is usually NOTHING: a piped child's
        # stdout is block-buffered and the buffer dies with the process. The classification
        # does not depend on it -- no verdict line was reached, which is CRASH either way --
        # and the sentence says "whatever was flushed" rather than promising output the
        # mechanism cannot deliver.
        part = b"".join(x for x in (exc.stdout, exc.stderr) if x)
        return (part.decode("utf-8", "replace").replace("\r\n", "\n")
                + "\nTIMEOUT after %ss -- the subject never reached a verdict\n" % timeout)
    return (proc.stdout.decode("utf-8", "replace") + "\n"
            + proc.stderr.decode("utf-8", "replace")).replace("\r\n", "\n")


def one_mutant(mutant, subj, home_root, interpreter, work, timeout, keep):
    """Apply one mutant to a fresh staged copy and score it. -> a result dict."""
    d = os.path.join(work, mutant["id"])
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    root, subject_path = stage(d, subj, home_root)
    target = subject_path if mutant.get("file") is None else \
        os.path.join(root, mutant["file"].replace("/", os.sep))
    src = read_text(target)
    if src is None:
        # NOT `anchor:0`. The mutant names a file the staged tree does not hold -- a subject
        # whose `home_copy` does not reach it, or a path typo -- which is a HARNESS fault and
        # not a drifted registry entry. Reporting it as a missing anchor would send the next
        # reader to retire a mutant that is perfectly good.
        status = "nofile:%s" % (mutant.get("file") or subj["path"])
        text = ""
    else:
        mutated, status = apply_mutation(src, mutant["old"], mutant["new"])
        if status == "ok":
            write_text(target, mutated)
            text = run_once(interpreter, root, subject_path, subj, timeout)
        else:
            text = ""
    if text:
        write_text(os.path.join(d, "transcript.txt"), text)
    res = {"id": mutant["id"], "origin": mutant.get("origin"), "target": mutant.get("target"),
           "status": status, "text": text}
    if not keep and status != "ok":
        shutil.rmtree(d, ignore_errors=True)
    return res


def score(res, subj, floor, expect_arms):
    """Turn a raw run into a per-arm verdict. The BASE floor is subtracted HERE, once."""
    if res.get("skipped"):
        res.update(verdict=None, arms=[], derived=[], word=SKIPPED, why=res["skipped"],
                   claim="unclaimed", missing=[])
        return res
    verdict = verdict_of(res["text"], subj["pass_line"], subj["fail_line"])
    fails = failing_arms(res["text"], subj["arm_re"], subj["fail_re"])
    derived = set(subj.get("derived_arms", ()))
    grew_all = fails - floor
    grew = grew_all - derived
    word, why = classify(res["status"], verdict, grew)
    if word == SURVIVED and res["status"] == "ok" and verdict == "FAIL" and grew_all:
        why = ("the subject failed only on DERIVED arm(s) %s -- a re-run of the whole "
               "selftest reddens whenever anything does, so this is not a detection"
               % ", ".join(sorted(grew_all)))
    claim, missing = claim_check(expect_arms, grew)
    res.update(verdict=verdict, arms=sorted(grew), derived=sorted(grew_all & derived),
               word=word, why=why, claim=claim, missing=missing)
    return res


def base_run(subj, home_root, interpreter, work, timeout):
    """The unmutated copy, run FIRST. -> (floor, transcript, verdict)."""
    d = os.path.join(work, "BASE")
    # CLEARED, exactly as `one_mutant` clears its own. `--work` is the documented scratch flag
    # and `--keep` exists to preserve it for inspection, so re-running into the same directory
    # is the EXPECTED workflow -- and with `exist_ok=True` alone it died in `copytree` with a
    # bare `FileExistsError` before a single thing was measured.
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    root, subject_path = stage(d, subj, home_root)
    text = run_once(interpreter, root, subject_path, subj, timeout)
    write_text(os.path.join(d, "transcript.txt"), text)
    verdict = verdict_of(text, subj["pass_line"], subj["fail_line"])
    return failing_arms(text, subj["arm_re"], subj["fail_re"]), text, verdict


# ---------------------------------------------------------------- the self-proof
#
# `C-57`: an instrument is blind until it has reported a FAILURE. This harness is an
# instrument, so it owes its own known-bad inputs -- and they must corrupt its MECHANISM, not
# its verdict. Four are planted against a FIXTURE subject written here, twenty lines that
# imitate the validator's transcript grammar and nothing else. The fixture is the point: the
# real validator takes minutes per mutant, and a proof nobody can afford to run is a proof
# nobody runs. FIVE cases over the FOUR verdicts, and the ordering is deliberate: `SURVIVED` is
# planted LAST because it is the one a mutation harness exists to emit -- `KILLED` is the good
# news -- and the one every broken reader has produced by accident instead of on purpose. An
# instrument that has never reported its own failure mode is blind, `C-57`, and a self-proof
# missing `SURVIVED` proves only that the harness can agree with itself.

FIXTURE = '''# a fixture subject for devflow-mutate --self-proof. Not a validator.
import sys
GREETING = "hello"
LIMIT = 3
LINES = 41


def check_greeting():
    return GREETING == "hello"


def check_limit():
    return LIMIT == 3


def check_lines():
    """A deliberately LINE-KEYED arm: it reads the file's length and nothing else.

    Its whole purpose is to be DERIVED -- it reddens when a blank line is inserted anywhere,
    which is not a change in behaviour. The real validator has four arms of this shape (the
    `V30` family, keyed on the canon table's line counts and on a cited line number), and the
    census exists to find them. A fixture with no such arm could not tell a working census
    from one that returns the empty set.
    """
    with open(__file__, "rb") as fh:
        return len(fh.read().decode("utf-8").splitlines()) == LINES


def main():
    ok = True
    for name, fn in (("greeting", check_greeting), ("limit", check_limit),
                     ("lines", check_lines)):
        good = fn()
        ok = ok and good
        print("  FIX %-12s expected the fixture to hold %s" % (name, "ok" if good else "FAIL"))
    print("FIXTURE PASSED" if ok else "FIXTURE FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
'''

SELF_PROOF_SUBJECT = {
    "path": "fixture_subject.py",
    # The fixture's own behaviour-free probe: a blank line before a constant changes every
    # line number below it and no semantics at all. `FIX lines` must show up in the census
    # and `FIX greeting` must not.
    "derived_probes": [["insert-blank-line", 'GREETING = "hello"',
                        '\nGREETING = "hello"']],
    "argv": [],
    "pass_line": "FIXTURE PASSED",
    "fail_line": "FIXTURE FAILED",
    "arm_re": r"^\s{2}(\S+)\s+(\S+)\s",
    "fail_re": r"FAIL$",
    "derived_arms": [],
}

SELF_PROOF_MUTANTS = [
    {"id": "proof-killable", "subject": "fixture", "origin": "rev64", "file": None,
     "target": "GREETING", "old": 'GREETING = "hello"', "new": 'GREETING = "goodbye"',
     "expect": KILLED, "expect_arms": ["FIX greeting"],
     "why": "a mutation an arm sees -- the ONLY case a two-verdict harness reads correctly"},
    {"id": "proof-crash", "subject": "fixture", "origin": "rev64", "file": None,
     "target": "import sys", "old": "import sys",
     "new": "import sys\nraise RuntimeError('planted import-time death')",
     "expect": CRASH, "expect_arms": [],
     "why": "dies before printing one arm line -- scored SURVIVED by every stdout-only reader"},
    {"id": "proof-noop", "subject": "fixture", "origin": "rev64", "file": None,
     "target": "LIMIT", "old": "LIMIT = 3", "new": "LIMIT = 3",
     "expect": BAD, "expect_arms": [],
     "why": "the anchor matches and the bytes do not move -- nothing was tested"},
    {"id": "proof-gone", "subject": "fixture", "origin": "rev64", "file": None,
     "target": "a symbol that is not there", "old": "NO_SUCH_SYMBOL = 1", "new": "x",
     "expect": BAD, "expect_arms": [],
     "why": "the anchor matches ZERO times -- the code moved under the registry"},
    {"id": "proof-survivor", "subject": "fixture", "origin": "rev64", "file": None,
     "target": "LIMIT (a change no arm reads)",
     "old": "LIMIT = 3", "new": "LIMIT = 3  # applied, and inert",
     "expect": SURVIVED, "expect_arms": [],
     "why": "the mutation APPLIED, the subject ran, and no arm moved -- the FINDING this "
            "instrument exists to emit, and the verdict no earlier battery ever proved"},
]


# THE DERIVED-ARM CENSUS. A `derived_arms` list maintained by hand is a list beside the
# thing it describes, which is this project's most-recorded defect -- and it failed here
# exactly that way: the first cut declared the two arms a reviewer happened to trip over and
# missed four more. So the question is asked MECHANICALLY instead.
#
# A BEHAVIOUR-FREE MUTATION IS THE PROBE, and two of them, because one is not a domain. A
# blank line inserted near the top changes every line number below it and no semantics at all;
# reordering the operands of an `or` changes the source bytes and no semantics at all. An arm
# that reddens under either is keyed on something other than the subject's behaviour -- a line
# number, a line count, a byte layout -- and is DERIVED by definition, whatever anyone
# remembered to write down.
#
# THE PROBES MUST STAY BEHAVIOUR-FREE OR THE CENSUS IS A LIE, which is why they are not
# configurable: `insert-blank-line` is anchored on a comment line so it cannot land inside a
# string or a continuation, and `swap-or-operands` is anchored on one commutative expression
# whose two operands are pure calls on the same argument.
DERIVED_PROBES = [
    # ANCHORED IN THE SUBJECT AND AT THE TOP OF IT, because the point is to move every line
    # number BELOW the anchor. `import warnings` is one line, at module level, in the
    # validator, and a blank line after an import is a no-op in every sense the language has.
    # ABOVE the future import, which is the FIRST statement -- so every line number in
    # the file moves, the citation `devflow-validate.py:41` included. Anchoring BELOW it
    # moved the line COUNT only and surfaced ONE arm of four: a probe that reaches less
    # than the class it is censusing reports a smaller class, which is the census's own
    # version of the defect it exists to find. Blank lines before a `__future__` import
    # are legal (PEP 236) and mean nothing.
    ("insert-blank-line",
     "from __future__ import annotations\nimport ast, builtins, hashlib,",
     "\nfrom __future__ import annotations\nimport ast, builtins, hashlib,"),
    # And one that moves BYTES without moving line numbers, so the two probes cannot both be
    # answering the same question: `or` is commutative over two pure calls on one argument.
    ("swap-or-operands",
     "    return bool(_V64_ACC_ID.search(block) or _V64_ACC_BULLET.search(block))",
     "    return bool(_V64_ACC_BULLET.search(block) or _V64_ACC_ID.search(block))"),
]


def derived_census(subj, home_root, interpreter, work, timeout):
    """-> (arms reddened by a behaviour-free mutation, floor, per-probe detail).

    The probes come from the SUBJECT (`derived_probes`), because an anchor is a fact about the
    file being censused and nothing else. A probe whose anchor is not there is REPORTED, never
    skipped: a census that silently drops a probe measures less than it says, which is the
    defect this whole revision is about -- and it happened on this function's FIRST run, when
    the probe was still anchored in the harness instead of the subject.
    """
    floor, _text, verdict = base_run(subj, home_root, interpreter, work, timeout)
    if verdict != "PASS":
        return None, floor, [("BASE", "did not reach %r" % subj["pass_line"], [])]
    probes = subj.get("derived_probes") or DERIVED_PROBES
    detail, seen = [], set()
    for name, old, new in probes:
        m = {"id": "census-" + name, "subject": None, "file": None, "old": old, "new": new}
        res = one_mutant(m, subj, home_root, interpreter, work, timeout, keep=False)
        if res["status"] != "ok":
            detail.append((name, "PROBE DID NOT APPLY (%s)" % res["status"], []))
            continue
        fails = failing_arms(res["text"], subj["arm_re"], subj["fail_re"])
        grew = sorted(fails - floor)
        seen |= set(grew)
        detail.append((name, "applied", grew))
    return seen, floor, detail


def self_proof(interpreter, work, timeout):
    """-> (rows, ok). Runs the four planted mutants and BASE against the fixture subject."""
    home = os.path.join(work, "fixture-home")
    os.makedirs(home, exist_ok=True)
    write_text(os.path.join(home, "fixture_subject.py"), FIXTURE)
    subj = dict(SELF_PROOF_SUBJECT)
    floor, base_text, base_verdict = base_run(subj, home, interpreter, work, timeout)
    rows = [("BASE", "PASS" if base_verdict == "PASS" else str(base_verdict),
             base_verdict == "PASS" and not floor,
             "an unmutated copy reaches the pass line and reddens %d arm(s)" % len(floor))]
    all_ok = rows[0][2]
    for m in SELF_PROOF_MUTANTS:
        res = score(one_mutant(m, subj, home, interpreter, work, timeout, keep=False),
                    subj, floor, m["expect_arms"])
        good = res["word"] == m["expect"] and res["claim"] != "UNMET"
        all_ok = all_ok and good
        rows.append((m["id"], res["word"], good, m["why"]))
    return rows, all_ok


# ---------------------------------------------------------------- reporting

def report(rows, floor, per_arm, out=sys.stdout):
    """Per mutant, then PER ARM, then the machine-readable last line."""
    tally = {KILLED: 0, CRASH: 0, SURVIVED: 0, BAD: 0, SKIPPED: 0}
    unmet = []
    for r in rows:
        tally[r["word"]] += 1
        if r["claim"] == "UNMET":
            unmet.append(r)
        # The COUNT is printed beside the sample, never the sample alone: this harness's
        # fourth declared property is that the verdict is per ARM, and a truncated list
        # with no total is the aggregate it refuses, one layer up in the reporting.
        out.write("%-42s %-9s %-9s %3d arm(s)  %s\n"
                  % (r["id"], r["word"], r["claim"], len(r["arms"]),
                     ", ".join(r["arms"][:4])
                     + (" …" if len(r["arms"]) > 4 else "")))
        if r["word"] in (SURVIVED, CRASH, BAD) or r["claim"] == "UNMET":
            out.write("      %s\n" % r["why"])
        if r["claim"] == "UNMET":
            out.write("      CLAIM UNMET -- declared but stayed GREEN: %s\n"
                      % ", ".join(r["missing"]))
    if per_arm:
        index = {}
        for r in rows:
            for a in r["arms"]:
                index.setdefault(a, []).append(r["id"])
        out.write("\nPER ARM -- %d arm(s) reddened by at least one mutant\n" % len(index))
        for a in sorted(index):
            out.write("  %-44s %s\n" % (a, ", ".join(index[a])))
    out.write("\nnoise floor: %d arm(s)%s\n"
              % (len(floor), (" -- " + ", ".join(sorted(floor))) if floor else ""))
    out.write("MUTATION SUMMARY total=%d killed=%d crash=%d survived=%d bad=%d "
              "skipped=%d claims_unmet=%d unclaimed=%d floor=%d\n"
              % (len(rows), tally[KILLED], tally[CRASH], tally[SURVIVED], tally[BAD],
                 tally[SKIPPED], len(unmet),
                 sum(1 for r in rows if r["claim"] == "unclaimed"), len(floor)))
    return tally, unmet


def main(argv=None):
    p = argparse.ArgumentParser(description="the flow's canonical mutation harness")
    p.add_argument("--registry", default=DEFAULT_REGISTRY)
    p.add_argument("--home", default=DEFAULT_HOME,
                   help="the flow home the subject path is relative to")
    p.add_argument("--subject", default=None)
    p.add_argument("--select", default=None, help="comma-separated registry ids")
    p.add_argument("--origin", default=None, help="only mutants first written at this rev")
    p.add_argument("--interpreter", default=sys.executable)
    p.add_argument("--work", default=None, help="scratch dir; a temp dir when omitted")
    p.add_argument("--timeout", type=int, default=1800)
    p.add_argument("--json", default=None, help="write the result matrix here")
    p.add_argument("--per-arm", action="store_true", help="print the arm -> mutants index")
    p.add_argument("--keep", action="store_true", help="keep the trees of BAD mutants too")
    p.add_argument("--list", action="store_true")
    p.add_argument("--retired", action="store_true", help="include retired mutants")
    p.add_argument("--self-proof", action="store_true",
                   help="run this harness's own C-57 proof and nothing else")
    p.add_argument("--derived-census", action="store_true",
                   help="report which arms redden under a BEHAVIOUR-FREE mutation; those are "
                        "the derived arms, and the answer should equal `derived_arms`")
    a = p.parse_args(argv)

    tmp = None
    work = a.work
    if work is None:
        tmp = tempfile.mkdtemp(prefix="devflow-mutate-")
        work = tmp
    os.makedirs(work, exist_ok=True)
    try:
        if a.self_proof:
            rows, ok = self_proof(a.interpreter, work, a.timeout)
            for name, word, good, why in rows:
                print("%-20s %-9s %-4s %s" % (name, word, "ok" if good else "FAIL", why))
            print("SELF-PROOF %s -- %d case(s)" % ("PASSED" if ok else "FAILED", len(rows)))
            return 0 if ok else 1

        reg = load_registry(a.registry)
        if a.derived_census:
            subj = reg["subjects"][a.subject or sorted(reg["subjects"])[0]]
            seen, floor, detail = derived_census(
                subj, a.home, a.interpreter, work, a.timeout)
            declared = set(subj.get("derived_arms", ()))
            for name, status, grew in detail:
                print("%-20s %-28s %s" % (name, status, ", ".join(grew) or "-"))
            print("\nfloor      : %d arm(s)" % len(floor))
            print("declared   : %s" % ", ".join(sorted(declared)))
            print("observed   : %s" % (", ".join(sorted(seen)) if seen is not None else "-"))
            miss = sorted((seen or set()) - declared)
            extra = sorted(declared - (seen or set()))
            print("DERIVED CENSUS observed=%d declared=%d undeclared=%d declared-but-unseen=%d"
                  % (len(seen or ()), len(declared), len(miss), len(extra)))
            if miss:
                print("  UNDECLARED: %s" % ", ".join(miss))
            if extra:
                print("  DECLARED BUT NOT OBSERVED (may still be derived for another "
                      "reason): %s" % ", ".join(extra))
            return 1 if miss else 0
        ids = set(a.select.split(",")) if a.select else None
        if ids:
            # A TYPO IN `--select` MUST NOT RUN SILENTLY SMALLER. Asking for four mutants and
            # measuring three, with no line saying so, is the exact shape this whole revision
            # exists to refuse -- and the retired ones are named separately, because "you
            # spelled it wrong" and "it was retired" are different answers.
            known = {m["id"]: m for m in reg["mutants"]}
            unknown = sorted(i for i in ids if i not in known)
            gated = sorted(i for i in ids
                           if i in known and known[i].get("retired") and not a.retired)
            if unknown:
                sys.exit("no such mutant id: %s" % ", ".join(unknown))
            if gated:
                sys.exit("selected mutant(s) are RETIRED; pass --retired to run them anyway: "
                         "%s" % ", ".join(gated))
        chosen = select(reg, ids=ids, origin=a.origin, subject=a.subject,
                        include_retired=a.retired)
        if a.list:
            for m in reg["mutants"]:
                print("%-42s %-7s %-9s %-28s %s"
                      % (m["id"], m.get("origin", "?"), m.get("expect", "?"),
                         m.get("target", "?"),
                         "RETIRED: " + m["retired"] if m.get("retired") else m.get("why", "")))
            print("REGISTRY %d mutant(s), %d retired, %d selectable"
                  % (len(reg["mutants"]),
                     sum(1 for m in reg["mutants"] if m.get("retired")), len(chosen)))
            return 0
        if not chosen:
            sys.exit("no mutant selected")
        names = sorted({m["subject"] for m in chosen})
        if len(names) != 1:
            sys.exit("one subject per run; selected %s" % ", ".join(names))
        subj = reg["subjects"][names[0]]

        floor, base_text, base_verdict = base_run(subj, a.home, a.interpreter, work, a.timeout)
        print("BASE  verdict=%s  floor=%d arm(s)  %s"
              % (base_verdict, len(floor), ", ".join(sorted(floor)) or "-"))
        if base_verdict != "PASS":
            sys.stderr.write(
                "BASE did not reach %r -- a run scored against a red or crashed baseline "
                "reports the baseline, not the mutants. Nothing was scored.\n"
                % subj["pass_line"])
            return 2
        print()
        _ver = interpreter_version(a.interpreter)
        rows = []
        for m in chosen:
            need = m.get("requires_python")
            if need and _ver and tuple(need) > _ver:
                rows.append(score(
                    {"id": m["id"], "origin": m.get("origin"), "target": m.get("target"),
                     "status": "skipped", "text": "",
                     "skipped": "declares requires_python %s and this run is on %s -- NOT a "
                                "verdict, and not silently dropped"
                                % (".".join(str(x) for x in need),
                                   ".".join(str(x) for x in _ver))},
                    subj, floor, m.get("expect_arms", [])))
                continue
            rows.append(score(one_mutant(m, subj, a.home, a.interpreter, work, a.timeout,
                                         a.keep),
                              subj, floor, m.get("expect_arms", [])))
        for r, m in zip(rows, chosen):
            r["expected"] = m.get("expect")
            r["why_mutant"] = m.get("why")
        tally, unmet = report(rows, floor, a.per_arm)
        if a.json:
            write_text(a.json, json.dumps(
                [{k: v for k, v in r.items() if k != "text"} for r in rows],
                indent=1, ensure_ascii=False) + "\n")
        surprises = [r for r in rows if r.get("expected") and r["word"] != r["expected"]
                     and r["word"] != SKIPPED]
        if surprises:
            print("\nDECLARED OUTCOME NOT MET -- %d mutant(s):" % len(surprises))
            for r in surprises:
                print("  %-42s declared %-9s got %s" % (r["id"], r["expected"], r["word"]))
        return 1 if (unmet or surprises or tally[BAD]) else 0
    finally:
        if tmp is not None and not a.keep:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
