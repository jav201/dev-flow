"""devflow-scan-spec.py -- the sensitive-pattern scan `/fast-dev-flow` Phase A step 6 owes.

    cd <this flow's root>                            # the gate command's own directory
    python scripts/devflow-scan-spec.py [SPEC]       # default: ./.fast-dev-flow/spec.md

Exit codes, and the middle one is a VERDICT and not a breakage:

    0   the scan ran, its four controls held, and NO pattern fired   -> security_required: false
    1   the scan ran, its four controls held, and a pattern FIRED    -> security_required: true
    2   the scan could NOT run, a control failed, or the spec carries none of the
        scanned sections: nothing is claimed about the spec

**THE PATTERN LIST IS NOT IN THIS FILE.** `commands/fast-dev-flow.md`
section *Patterns that trigger `security_required`* is that list's one home, and this script
READS it from there at every run (`C-50`). There is therefore no second inventory to drift:
delete a pattern from the command and this scanner stops matching it, which is exactly what a
reader auditing the command should be able to assume. The same section is the home of the
SCOPE (sections 1-4, with 3b and 3c excluded), of the MATCHING rule (case-insensitive, on word
boundaries, written as lookarounds so a pattern beginning with a non-word character can match)
and of the FOUR CONTROLS this script runs before it believes its own answer.

The placeholder vocabulary -- the `<...>` spans a scan must skip while they are still the
template's own words -- is read from `templates/fast-dev-flow/spec-template.md`, which is where
those words are shipped. A span the author has typed into is authored text and IS scanned.
"""
import os
import re
import sys

_SECTION = "### Patterns that trigger `security_required`"
# THE LIST'S OWN ANCHOR, and it is load-bearing. The section states its four CONTROLS in
# bullets of the same shape ABOVE the list, and each of them quotes example text in code
# spans -- `Information Flow Contract` among them. A parser that read every bullet of the
# section harvested the controls' examples as patterns, and the NEGATIVE control then fired
# on itself. The list begins at this line, so the parser begins there too.
_LIST_ANCHOR = "Patterns — case-insensitive, bounded:"
_BULLET = re.compile(r"^-\s+\*\*[^*]+:\*\*\s+(.+)$", re.M)
_SPAN = re.compile(r"<([^<>\n]{1,80})>")
_SCOPE = ("1.", "2.", "3.", "4.")
_SKIPPED = ("3b.", "3c.")


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def flow_home(start=None):
    """The flow root holding `commands/` and `templates/`, or None.

    TWO LAYOUTS, PROBED AND NOT ASSUMED. In the published bundle this file sits at
    `scripts/devflow-scan-spec.py` and the command is one directory up; the tree this bundle
    is generated from keeps it one level deeper, and the command is two up there. A
    hard-coded depth works in exactly one of the two and fails as *no such file* in the other.
    """
    here = os.path.dirname(os.path.abspath(start or __file__))
    for up in ("..", os.path.join("..", "..")):
        cand = os.path.normpath(os.path.join(here, up))
        if os.path.isfile(os.path.join(cand, "commands", "fast-dev-flow.md")):
            return cand
    return None


def patterns(command_text):
    """The command's pattern list -> an ordered list of patterns. PURE.

    Every bullet of the LIST is read, so a group added there is scanned without touching this
    file. An empty result is returned as such and the caller refuses to scan on it: a scanner
    that silently matched nothing would report `security_required: false` over every spec ever
    written, which is the vacuous check this control exists to refuse. The list is taken from
    `_LIST_ANCHOR` down, so the section's four control bullets -- which quote example text in
    code spans of exactly this shape -- are not harvested as patterns.
    """
    body = (command_text or "").split(_SECTION, 1)
    if len(body) != 2:
        return []
    body = re.split(r"(?m)^#{2,3} ", body[1], maxsplit=1)[0]
    if _LIST_ANCHOR not in body:
        return []
    body = body.split(_LIST_ANCHOR, 1)[1]
    out = []
    for line in _BULLET.findall(body):
        for tok in re.findall(r"`([^`]+)`", line):
            tok = tok.strip()
            if tok and tok not in out:
                out.append(tok)
    return out


def placeholders(template_text):
    """The `<...>` spans the template SHIPS -> a set of their inner words, case-folded."""
    return {s.strip().casefold() for s in _SPAN.findall(template_text or "") if s.strip()}


def in_scope(spec_text):
    """The spec's sections 1-4, 3b and 3c removed -> the text the scan reads. PURE."""
    parts, keep, take = re.split(r"(?m)^(##\s+\S+)", spec_text or ""), [], False
    for chunk in parts:
        m = re.match(r"^##\s+(\S+)", chunk)
        if m:
            num = m.group(1)
            # `_SKIPPED` IS DISJOINT FROM `_SCOPE`, so this conjunct can never be
            # False -- §3b and §3c are excluded by NOT BEING IN `_SCOPE`, and the
            # test is kept because the printed `scope:` line advertises `_SKIPPED`
            # as an active exclusion and a reader must be able to find the code
            # that performs it. It also holds the exclusion if `_SCOPE` ever
            # widens to a prefix test. (second review, `L3`)
            take = num in _SCOPE and num not in _SKIPPED
            continue
        if take:
            keep.append(chunk)
    return "\n".join(keep)


def strip_untouched(text, shipped):
    """Blank out every `<...>` span still carrying the template's own words. PURE.

    The span is REPLACED BY SPACES rather than deleted, so no two words are joined across the
    hole and an offset stays an offset. A span the author typed into is left exactly as it is.
    """
    def sub(m):
        return " " * len(m.group(0)) if m.group(1).strip().casefold() in shipped else m.group(0)
    return _SPAN.sub(sub, text or "")


def fired(text, pats):
    """The patterns matching `text` -> an ordered list. PURE.

    `(?<!\\w)...(?!\\w)` and never `\\b...\\b`: there is no word boundary before a `.` that
    follows whitespace, so `\\b\\.env\\b` matches nothing and `.env` is on the list. The
    lookaround behaves like `\\b` for a word-initial pattern and still matches the others.
    """
    hits = []
    for p in pats:
        if re.search(r"(?<!\w)" + re.escape(p) + r"(?!\w)", text or "", re.I):
            hits.append(p)
    return hits


def scan(spec_text, command_text, template_text):
    """(fired patterns, the text actually read) for one spec. PURE."""
    pats = patterns(command_text)
    body = strip_untouched(in_scope(spec_text), placeholders(template_text))
    return fired(body, pats), body


CONTROLS = (
    ("positive", "## 3.\n- When `a session token` expires, it is re-issued.\n", True),
    ("negative", "## 3.\n- The Information Flow Contract is declared by the author.\n", False),
    ("placeholder", "## 2.\n- As a <role>, I want <goal>, so that <benefit>.\n", False),
    ("placeholder-unbracketed", "## 2.\n- As a role, I want a goal, so that a benefit.\n", True),
    ("authored-in-brackets",
     "## 3.\n- When <a session token expires>, the system shall <re-issue it>.\n", True),
)


def controls(command_text, template_text):
    """Run the four controls -> [(name, expected, got)]. The verdict is believed only on all.

    The placeholder control is a PAIR and is counted as one: the template's own words must not
    fire and the same line with the brackets removed must, which is what makes the skip a rule
    rather than an off switch an author can leave two characters in place to reach.
    """
    out = []
    for name, text, want in CONTROLS:
        hits, _ = scan(text, command_text, template_text)
        out.append((name, want, bool(hits)))
    return out


def main(argv):
    home = flow_home()
    if not home:
        print("BLOCKED: no `commands/fast-dev-flow.md` above this script, so the pattern "
              "list's one home could not be read and NOTHING was scanned.")
        return 2
    command_text = _read(os.path.join(home, "commands", "fast-dev-flow.md"))
    template_text = _read(os.path.join(home, "templates", "fast-dev-flow",
                                       "spec-template.md"))
    pats = patterns(command_text)
    if not pats:
        print("BLOCKED: `commands/fast-dev-flow.md` %s holds no pattern bullets, so this run "
              "would report a clean spec without having looked at one." % _SECTION)
        return 2
    spec = argv[1] if len(argv) > 1 else os.path.join(".fast-dev-flow", "spec.md")
    spec_text = _read(spec)
    if spec_text is None:
        print("BLOCKED: no spec at `%s`, so nothing was scanned." % spec)
        return 2

    # THE SCOPE IS MEASURED BEFORE ANY VERDICT IS PUBLISHED, and this is the control the
    # first cut did not have. `in_scope` keys on the heading token `## <N>.` the template
    # ships; a spec whose headings are spelled any other way -- `## 1 Objective`, `##3.`,
    # a setext underline, no `##` at all -- yields an EMPTY body, and every one of the four
    # controls still passes, because the controls run on synthetic conformant text and never
    # touch the spec. The result was `security_required: false` over a spec holding ten
    # patterns and read zero bytes of, under a `scope:` line claiming to have read four
    # sections. That is the same vacuous-scan defect this file already refuses for the
    # PATTERN LIST, one argument over, and `C-40` asks it of every green: what would this
    # look like if the repair had been made by removal? `in_scope` returning `""` is that
    # removal, and it was invisible. The scan now REFUSES rather than reporting.
    body = in_scope(spec_text)
    if not body.strip():
        seen = re.findall(r"(?m)^#{1,6}\s+(\S+)", spec_text) or ["(none)"]
        print("BLOCKED: none of sections %s was found in `%s`, so the scan read NOTHING and "
              "claims nothing about it. The headings this file carries are: %s. The scan "
              "reads `## <n>.` exactly as `templates/fast-dev-flow/spec-template.md` writes "
              "them -- the number, then a period."
              % (" ".join(_SCOPE), spec, " ".join(seen[:12])))
        return 2

    checks = controls(command_text, template_text)
    print("scanner  : reads its %d pattern(s) from `commands/fast-dev-flow.md` %s"
          % (len(pats), _SECTION))
    print("scope    : sections %s of `%s`, with %s excluded -- %d byte(s) read"
          % (" ".join(_SCOPE), spec, " ".join(_SKIPPED), len(body)))
    # FIVE ROWS, FOUR CONTROLS: the placeholder control is a PAIR -- the template's own
    # words must not fire and the same line unbracketed must -- and a reader counting
    # rows against the command's "four controls" needs that said where they are printed.
    print("controls : %d row(s) for the %d control(s) the command defines — the "
          "placeholder control is a PAIR (the template's own words must NOT fire, "
          "and the same line unbracketed MUST), so it prints two rows"
          % (len(checks), len(checks) - 1))
    for name, want, got in checks:
        print("control  : %-24s expected %-5s got %-5s %s"
              % (name, str(want).lower(), str(got).lower(),
                 "ok" if want == got else "FAILED"))
    if any(want != got for _n, want, got in checks):
        print("BLOCKED: a control failed, so this scan's own answer is not believed and "
              "nothing is claimed about `%s`." % spec)
        return 2

    hits, _body = scan(spec_text, command_text, template_text)
    if hits:
        print("flags    : %s" % ", ".join("`%s`" % h for h in hits))
        print("security_required: true")
        print("Answer Phase B step 1's four questions and record them in the spec's section 6.")
        return 1
    print("flags    : none")
    print("security_required: false")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
