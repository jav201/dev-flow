"""trace_check.py enforces the Records section: the trace from story to test, the slice, the evidence and the
canon. Each test removes one link and expects that check to report it, because a check that cannot fail would let
a step be skipped silently."""
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trace_check  # noqa: E402

REQ = """\
# Requirements — demo, Inc 1

## 2. Source user story

**US-1.** As a user, I want B after A, so that C.

## 3. High-level requirements

### HLR-1 — B follows A
- **Traceability:** US-1
- **Acceptance test(s):** AT-1

## 4. Low-level requirements

- **LLR-1.1 — Event.** When A, the system shall show B. Threshold: 1/1.
- **LLR-1.2 — Unwanted.** If A fails, then the system shall say why. Verified by TC-12.
- **LLR-1.3 — Withdrawn** (merged into LLR-1.1).

## 5. Acceptance tests

- **AT-1** — press `a`; B shows.

## 6. Slice

| # | File | Unit | Change |
|---|---|---|---|
| 1 | core.py | `show` | changed |
"""
TESTS = '''\
def test_shows_b():
    """TC-11 (LLR-1.1)."""

def test_tc_12_says_why():
    pass

def test_at_1():
    pass
'''
CASES = """\n| Case | Class | Objective | Preconditions | Inputs | Expected | Verified by |
|---|---|---|---|---|---|---|
| HLR-1/1 | normal | Verify that B follows A | none | press `a` | B | test_at_1 (full) |
| LLR-1.1/1 | normal | Verify that B shows | none | A | B | test_shows_b (full) |
| LLR-1.2/1 | robustness | Verify that a failure says why | none | A fails | the reason | test_tc_12_says_why (full) |
"""
VALIDATION = "# Inc 1 — validation\n\n| GREEN | `evidence/green.txt` |\n"
CANON = "| Id | Statement |\n|---|---|\n| HLR-1 | B follows A |\n| LLR-1.1 | shows B |\n| LLR-1.2 | says why |\n"
INC = ".dev-flow/inc-1/"
ARGS = ["--req", INC + "01-requirements.md", "--base", "base", "--src", "pkg", "--canon", "REQUIREMENTS.md"]


def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def git(root, *args):
    subprocess.run(("git", "-c", "user.name=toy", "-c", "user.email=toy@example.invalid") + args, cwd=root,
                   check=True, capture_output=True)


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """A batch whose every link holds: base commit, then the increment's change, all committed."""
    git(tmp_path, "init", "-q")
    write(tmp_path, "pkg/core.py", "def show():\n    pass\n")
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-qm", "base")
    git(tmp_path, "tag", "base")
    write(tmp_path, "pkg/core.py", "def show():\n    return 'B'\n")
    write(tmp_path, INC + "01-requirements.md", REQ)
    write(tmp_path, INC + "02-test-cases.md", CASES)
    write(tmp_path, INC + "04-validation.md", VALIDATION)
    write(tmp_path, INC + "evidence/green.txt", "1 passed\n")
    write(tmp_path, "tests/test_core.py", TESTS)
    write(tmp_path, "REQUIREMENTS.md", CANON)
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-qm", "inc 1")
    monkeypatch.chdir(tmp_path)
    return tmp_path


def check(capsys, args=ARGS):
    rc = trace_check.main(args)
    return rc, capsys.readouterr().out


def test_a_batch_with_every_link_passes(repo, capsys):
    rc, out = check(capsys)
    assert rc == 0, out
    assert "LLR-1.3" not in out  # withdrawn: owes no test and no canon row


def test_a_story_no_requirement_names_is_a_gap(repo, capsys):
    write(repo, INC + "01-requirements.md", REQ.replace("## 3.", "**US-2.** As a user, I want D.\n\n## 3."))
    rc, out = check(capsys)
    assert rc == 1 and "US     US-2 is named by no active requirement" in out


def test_a_requirement_no_test_names_is_a_gap(repo, capsys):
    write(repo, "tests/test_core.py", TESTS.replace("TC-11 (LLR-1.1)", "LLR-1.10"))
    rc, out = check(capsys)
    assert rc == 1 and "TEST   LLR-1.1 is named by no file" in out  # LLR-1.10 is not LLR-1.1


def test_a_requirement_with_no_test_case_is_a_gap(repo, capsys):
    write(repo, INC + "02-test-cases.md", CASES.replace("| LLR-1.2/1 |", "| LLR-1.20/1 |"))
    rc, out = check(capsys)
    assert rc == 1 and "CASE   LLR-1.2 has no test case" in out
    os.remove(repo / INC / "02-test-cases.md")
    rc, out = check(capsys)
    assert rc == 1 and "CASE   no 02-test-cases.md beside" in out


def split_cases(repo, second):
    """Testers split the cases by file group; the checker must read the group files as one record."""
    os.remove(repo / INC / "02-test-cases.md")
    rows = CASES.splitlines(keepends=True)
    write(repo, INC + "02-test-cases-G1.md", "".join(rows[:5]))  # header, HLR-1/1, LLR-1.1/1
    write(repo, INC + "02-test-cases-G2.md", second)


def test_test_cases_split_by_group_are_read_together(repo, capsys):
    split_cases(repo, CASES.splitlines(keepends=True)[-1])  # LLR-1.2/1
    rc, out = check(capsys)
    assert rc == 0, out


def test_a_case_missing_from_every_group_file_is_a_gap(repo, capsys):
    split_cases(repo, "| LLR-1.20/1 | robustness |\n")
    rc, out = check(capsys)
    assert rc == 1 and "CASE   LLR-1.2 has no test case" in out


def test_ids_checks_only_the_testers_own_requirements(repo, capsys):
    """A tester runs it before the other groups' tests exist: another group's gap must not show, its own must."""
    write(repo, INC + "02-test-cases.md", CASES.replace("| LLR-1.1/1 |", "| LLR-1.10/1 |"))  # other group's gap
    write(repo, "tests/test_core.py", TESTS.replace("test_tc_12_says_why", "test_says_why"))  # own gap
    os.remove(repo / INC / "04-validation.md")  # EVID is not the tester's check
    rc, out = check(capsys, ARGS + ["--ids", "LLR-1.2*"])
    assert rc == 1 and "TEST   LLR-1.2 is named by no file" in out, out
    assert "LLR-1.1 " not in out and "EVID" not in out
    assert out.splitlines()[-1] == "trace_check: 1 active requirements match --ids, checks run: CASE, TEST, 1 gap(s)"


def test_ids_that_match_no_requirement_is_nothing_to_check(repo, capsys):
    rc, out = check(capsys, ARGS + ["--ids", "LLR-9.*"])
    assert rc == 2 and "no active requirement matches --ids LLR-9.*" in out


def test_the_rewrite_ids_are_traced_like_hlr_and_llr(repo, capsys):
    write(repo, INC + "01-requirements.md", (
        "## Rows\n\n**US-1.** As a user, I want B.\n\n"
        "| R-LOAD-001 | When A, the system shall show B. US-1 |\n"
        "| R-LOAD-002 | If A fails, then the system shall say why. US-1 |\n\nSlice: `core.py`\n"))
    write(repo, INC + "02-test-cases.md", "| R-LOAD-001/1 | normal |\n| R-LOAD-002/1 | robustness |\n")
    write(repo, "tests/test_core.py", 'def test_shows_b():\n    """R-LOAD-001/1."""\n')
    rc, out = check(capsys, ARGS[:6])
    assert rc == 1 and "TEST   R-LOAD-002 is named by no file" in out and "R-LOAD-001 " not in out


def test_a_tc_id_in_the_requirement_counts_as_its_link(repo, capsys):
    write(repo, "tests/test_core.py", TESTS.replace("test_tc_12_says_why", "test_says_why"))
    rc, out = check(capsys)
    assert rc == 1 and "TEST   LLR-1.2 is named by no file" in out


def test_a_changed_source_file_outside_the_slice_is_a_gap(repo, capsys):
    write(repo, "pkg/extra.py", "x = 1\n")  # untracked counts as changed
    rc, out = check(capsys)
    assert rc == 1 and "SLICE  pkg/extra.py changed since base" in out


def test_a_batch_end_fix_is_traced_through_its_correction_record(repo, capsys):
    write(repo, "pkg/extra.py", "x = 1\n")
    write(repo, "fixes.md", "| F-1 | law guard | HLR-1 | `pkg/extra.py` |\n")
    rc, out = check(capsys, ARGS + ["--fixes", "fixes.md"])
    assert rc == 0, out


def test_uncommitted_or_unlisted_evidence_is_a_gap(repo, capsys):
    write(repo, INC + "04-validation.md", VALIDATION + "| RED | `evidence/red.txt` |\n")
    write(repo, INC + "evidence/red.txt", "1 failed\n")  # on disk, never committed
    rc, out = check(capsys)
    assert rc == 1 and "cites evidence/red.txt, which is not committed" in out
    os.remove(repo / INC / "04-validation.md")
    rc, out = check(capsys)
    assert rc == 1 and "EVID   no 04-validation.md beside .dev-flow/inc-1/01-requirements.md" in out


def test_a_requirement_missing_from_the_canon_is_a_gap(repo, capsys):
    write(repo, "REQUIREMENTS.md", CANON.replace("| LLR-1.1 |", "| LLR-1.10 |"))
    rc, out = check(capsys)
    assert rc == 1 and "CANON  LLR-1.1 is not in REQUIREMENTS.md" in out


def test_a_file_with_no_requirement_is_nothing_to_check(repo, capsys):
    write(repo, INC + "01-requirements.md", "# empty\n")
    rc, out = check(capsys)
    assert rc == 2 and "no requirement (HLR, LLR or R-) defined" in out
