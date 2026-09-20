# dev-flow-lessons — REFERENCE.md (origins, forensics, candidate history)

**The forensic half of the catalog, and the half a reader consults only when the question is
*how do we know that?*** `SKILL.md` beside it holds the controls, their rules, their stated
limits and their readers. **A content line lives in exactly ONE of the two files** (`C-50`);
headings live in both on purpose, because that is the id the link crosses by. The census that
holds the split is an arm, `CAT SPLIT-census`, not a claim in this paragraph.

This file is in the manifest's hashed file table from flow rev80, so it cannot drift silently
the way an unhashed second copy does — which was `C-58` wearing a file name.

**How to read a control section here.** Each one opens with
`↪ *Excerpts — the rule is in `SKILL.md` under this heading.*` and then carries ONLY the lines the
fold moved, verbatim and out of context, in the source's own order. **`…` marks each place a line was
lifted**, so a paragraph that starts mid-clause starts there rather than having been corrupted. A
section with nothing but its opening line is one the fold moved nothing for: its whole text is in
`SKILL.md` and this file does not repeat it.

---
## Locator map — every heading of `SKILL.md`, and what this file keeps for it

One row per `##`/`###` heading of the consultable half. `—` in the last column means the
fold moved nothing for that control: its whole text is in `SKILL.md` and nothing here
repeats it. The map is compared to both files BOTH WAYS by `CAT LOCATOR-both-ways`, so a
heading added on either side without its row reddens.

| Id | `SKILL.md` heading | Kept here |
|---|---|---|
| `How to use this mid-flow` | How to use this mid-flow | — |
| `The meta-rule (everything below is a special case of this)` | The meta-rule (everything below is a special case of this) | yes |
| `Index — all controls, by phase` | Index — all controls, by phase | — |
| `⏸ Candidates — observed, transcribed, NOT controls` | ⏸ Candidates — observed, transcribed, NOT controls | yes |
| `Phase 1-2 · Requirements, spec & review — designing oracles that can fail` | Phase 1-2 · Requirements, spec & review — designing oracles that can fail | yes |
| `C-10` | C-10 · Acceptance test exercises the shipped surface off a NON-DEFAULT value | yes |
| `C-12` | C-12 · Output-then-consume chains through the written artifact | — |
| `C-13` | C-13 · Measure rendered geometry at DRAFT time (+ C-13.1 deficit-matched fallback) | yes |
| `C-15` | C-15 / C-15.1 · Probe a framework symbol's runtime identity; grep its assignment sites | yes |
| `C-31` | C-31 · Input-set-as-oracle | yes |
| `C-40` | C-40 · Falsifiability BEFORE correctness — "can it go RED?" is a separate question | yes |
| `C-59` | C-59 · Evidence bytes live at a declared home, verbatim, and the store is verified | yes |
| `C-58` | C-58 · A mandate nothing reads is a paragraph | yes |
| `C-57` | C-57 · An instrument is blind until it has reported a failure | yes |
| `C-60` | C-60 · The harness that proves a check must not share a fixture with it | yes |
| `C-43` | C-43 · Premise evaluation — verifying work against a spec never verifies the SPEC's claims about the world | yes |
| `C-55` | C-55 · An emptiness is doing work — say which kind | yes |
| `C-56` | C-56 · An evidence transcript is corpus input | yes |
| `C-42` | C-42 · assert the EMITTED form, never the rendered one | yes |
| `reader-as-oracle (+ a MANDATORY corrupted negative control)` | reader-as-oracle (+ a MANDATORY corrupted negative control) | — |
| `KAT anchor — pin at least one externally-published known answer` | KAT anchor — pin at least one externally-published known answer | — |
| `assert-the-discriminating-negative` | assert-the-discriminating-negative | yes |
| `The coincidence oracle` | The coincidence oracle | yes |
| `Spec-side census rules (from §3)` | Spec-side census rules (from §3) | yes |
| `Phase 3 · Implementation — census, blast-radius & test hygiene` | Phase 3 · Implementation — census, blast-radius & test hygiene | — |
| `C-53` | C-53 · A rule that false-fails correct work is as expensive as one that passes wrong work | yes |
| `C-52` | C-52 · The four conditions that make a fork safe — and the one that changes category | yes |
| `C-51` | C-51 · Layer 0 — the unit that both existing layers look past | yes |
| `C-50` | C-50 · One home per artifact — and the link crosses by ID, never by content | yes |
| `C-49` | C-49 · Forward applicability — every output of a design review must be someone's declared input | yes |
| `C-48` | C-48 · A trigger's NON-activation is evidence, and is recorded with its probe | yes |
| `C-47` | C-47 · The increment budget counts SOURCE files, not the total | yes |
| `C-14` | C-14 · A move OR a correction greps its whole population (census the readers, and the claims) | yes |
| `Census & blast-radius principles (§3)` | Census & blast-radius principles (§3) | yes |
| `Test hygiene & environment (§5)` | Test hygiene & environment (§5) | yes |
| `Phase 4 · Validation & gates — evidence that cannot be faked` | Phase 4 · Validation & gates — evidence that cannot be faked | yes |
| `C-18` | C-18 · Every acceptance test = exactly ONE distinct on-disk node driving the full chain | yes |
| `C-25` | C-25 · Gate evidence = one complete run owned by the orchestrator | — |
| `C-32` | C-32 · Assert-the-painted-result | — |
| `freeze-then-measure — a figure is admissible only if it names what it measured` | freeze-then-measure — a figure is admissible only if it names what it measured | yes |
| `C-66` | C-66 · Flaky is a CLASS with a measured rate, never a name on a list | yes |
| `Gates & evidence rules (§4)` | Gates & evidence rules (§4) | yes |
| `Cross-phase · Multi-agent orchestration (§6)` | Cross-phase · Multi-agent orchestration (§6) | yes |
| `Cross-phase · The security lens on "just text" (§7)` | Cross-phase · The security lens on "just text" (§7) | yes |
| `C-44` | Cross-phase · C-44 — work that never landed | yes |
| `C-45` | Cross-phase · C-45 — the flow is a shared asset, and changes flow BOTH ways | yes |
| `C-62` | Cross-phase · C-62 — a rewrite converts prescriptions into permissions | yes |
| `C-65` | Cross-phase · C-65 — a ruling is applied as a CENSUS over its axis, never as the instance | yes |
| `C-46` | Implementation/Validation · C-46 — a hash-verified restore does not restore the CACHE | yes |
| `Phase 5 · Postmortem — honesty note, the scope of these claims (§8)` | Phase 5 · Postmortem — honesty note, the scope of these claims (§8) | yes |
| `Origin-only ids — headings the control census deliberately scores 0` | Origin-only ids — headings the control census deliberately scores 0 | — |
| `Writing canon — a parenthetical may carry provenance, NEVER a definition` | Writing canon — a parenthetical may carry provenance, NEVER a definition | yes |
| `Provenance (short)` | Provenance (short) | — |

---
## ORIGINAL META-RULE (pre-pruning, verbatim)

## The meta-rule (everything below is a special case of this)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

code.** A green suite full of vacuous checks is not evidence of anything — it is theater. Across
the corpus these checks did not cluster in implementation; they clustered **one level up, in the
SPECS and BRIEFS** — the artifacts that define what "correct" means. One batch shipped **9 vacuous
checks into review, most authored by the spec/brief layer**, every one caught only because Phase-3
hunted for them.

…

> worthless — in the corpus, **3-of-5 and 4-of-7 agent RED-predictions were wrong** when finally
> run ("the run won every time it was executed"). So: for every assertion, construct the mutation
> it should catch and confirm the assertion goes RED under it; for every RED, run it and watch it
> fail before you trust it.

**Why vacuous checks concentrate in specs, not code.** A wrong line of code fails a decent test. A
wrong *definition of correct* — a fixture that is a palindrome so reversal can't disturb it, a
universal claim whose hand-listed input set omits the one failing case, an assertion of
`spans == []` that is constant-true on safe input, unsafe input, and unwritten code alike —
produces a check that is **structurally incapable of failing**. No amount of implementation
testing finds it, because the check passes exactly as designed. You find it only by attacking the
check itself with the mutation it purports to guard against.

…

|---|---|---|---|

…

**A fourth place it hides: the oracle's source.** Measured 2026-08-18 across the 14 harnesses of
the `docker/` course. Each one compared a data block against the page it verified — but read the
*expected* value out of that same page:

```js
const ANAT = M.ANAT;                       // from a <script> IN THE PAGE
const SPAN = {};                           // from <span data-ann> IN THE PAGE
ok(SPAN[a].indexOf(L.t) >= 0, 'el texto del dato no coincide...');
```

Change the datum in the HTML and **both sides move together**, so the assertion passes while its own
message claims it compared. **13 of 14 harnesses had it**, green for months. Mutation is what
exposed it: 97 deliberate edits to page data, **76 survived before the fix and 12 after** — and the
12 are data nothing ever promised to assert, which is a different thing and worth separating.

…

- **A mutation that never applied reads as a survivor.** The first driver called `python3`, which
  did not exist on that machine, so the `sed` never ran and every mutant "survived". Fixed by
  counting the substitutions actually made and aborting on zero — *and by a negative control that
  must die.* A mutation harness needs its own mutation test.

…

  print "FAILURES" as green reports 14/14 while all 14 are crashing — a crash prints no failures
  either.

Note where the vacuousness lives: in the first two it hides in the **fixture** (the input set); in
the third it hides in the **assertion**. Both are spec-level defects — exactly why the corpus
found them above the code. The lesson is not "write more tests"; it is "a test that does not
separate correct from broken is a comment with a green checkmark."

---

## ORIGINAL CONTROL ENTRIES (pre-pruning, verbatim, in source order)

## Phase 1-2 · Requirements, spec & review — designing oracles that can fail

The V-model writes acceptance tests at spec time, so oracle-design controls belong here. This is
where the corpus's vacuous checks were authored — apply the meta-rule to every AT you spec.

### C-10 · Acceptance test exercises the shipped surface off a NON-DEFAULT value

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

test. If a feature has a policy branch (say, "verbose mode reformats the output"), a test run with
verbose left at its default *off* value exercises the un-branched path and asserts nothing about
the branch that shipped.

…

the result is non-empty passes whether precision is honored or ignored. Set `precision=5`, assert
the exact string `"3.14159"` — now the assertion moves iff the branch works, and you write **one
AT per policy branch**.

…

### C-12 · Output-then-consume chains through the written artifact

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

### C-13 · Measure rendered geometry at DRAFT time (+ C-13.1 deficit-matched fallback)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

contradicts. Row and column budgets computed from ratios were measured up to **4.5x off** the
truth; a fallback rung chosen for cheapness (trim 3 label columns) cannot close an actual 67-85
column deficit.

**Example.** Before calling a geometry story done, drive the real layout engine (a headless UI-driver harness) at each target size and **measure width AND height** of the rendered panes. Pick
a fallback by the **measured deficit**, not by which fallback is easiest.

…

### C-15 / C-15.1 · Probe a framework symbol's runtime identity; grep its assignment sites

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

dead code. In the corpus a sentinel `Select.BLANK` resolved at runtime to an inherited
`Widget.BLANK` whose value was the boolean `False` — so a spec-conformant filter against it was
**always false and shipped dead, twice**. `hasattr` and behavior-claims do not catch this; only
`repr()`/`type()` against the pinned version does.

…

### C-31 · Input-set-as-oracle

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

**Failure closed.** A test that certifies a **universal** ("every hue is distinguishable", "all
inputs round-trip") is only as strong as its input set — and a hand-listed input set is a spec
artifact that can omit the one failing member. Code mutation cannot find this, because the code is
correct; the *oracle's input list* is wrong. This is a defect **one level above the code**.

**Example.** A census asserted every hue in a palette was distinguishable. The per-hue arithmetic
was exact — but the hand-listed set of hues **omitted 38.44°**, the single hue that failed. The
fix: the test must **derive or guard its input set** (enumerate the real domain, or assert the
set's completeness), never trust a hand-typed list to be exhaustive.

…

### C-40 · Falsifiability BEFORE correctness — "can it go RED?" is a separate question
*(batch 64 — **corrected 2026-09-07**: this entry named batch 63 as its corpus and **batch-63 cites
`C-40` zero times**. The 93 lines a naive grep returns there are the unrelated `C-400`…`C-409` id
family, and a word-boundary sweep of all 67 batch directories puts **503 of the 774** real citations
in **batch-64**, the batch that minted it.)*

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

the change it gates**. One batch produced **five** such acceptances for a single defect, three of them
written *after* vacuity was already that batch's identified theme.

…

of the same input — while the **file writer**, the actual subject of the fix, never appeared in the
expression at all. Every one was arithmetically exact. The executed counterfactual read
`RED cases against the WRONG implementation: 0`.

…

1. **The declared subject must be IN the expression.** Name the subject the predicate *itself declares*
   it certifies, then confirm that subject appears in its own expression. *Corollary:* when the declared
   subject is not the subject of the change, the predicate is a **regression PIN, not a gate** — keep it
   and label it so.
2. **A quantified set must come from the RULE, not the implementation.** A set drawn from what the code
   currently handles certifies a completeness the code does not have.

**Rider — the verdict is PER RESOLVED ARM, never the process exit code** *(b76, re-committed b84)*.
A runner exits non-zero if ANY node fails, so one verdict per mutant over a node set containing
*parametrized* tests cannot say **which** arms reddened: an inert arm hides behind a sibling that
failed, and `3 passed` sits unread in the transcript. Record one verdict per resolved node id and
NAME the arms that stayed green. Assert the expected **arm count** first — a harness whose baseline
resolves ZERO arms makes its own all-green check compare `0 == 0` and pass, and a
whitespace-delimited node pattern silently drops every parametrized arm. **An arm the harness
cannot see is an arm it cannot report inert.** One project built this harness after four arms
survived a fully removed gate; the identical error was re-committed eight batches later — which is
the argument for the catalog rather than one project's scripts.

**Discharge:** name the mutation, **execute it**, paste the transcript — and run it where no other
session is reading, then **restore it, confirmed by hash**. `git status` is *vacuous for an untracked
file*: it reports identically whether or not the mutation was reverted.

**The measurement that makes this operable.** Encoded one-limb the rule flags **4 of 6**
known-vacuous predicates; both limbs flag **9 of 9**, with **0** false positives over sound controls.
That was a *laboratory* corpus, and this entry carried its own indictment for a year — *"nobody has
yet measured whether it fires in a live batch"*.

**MEASURED 2026-09-07, AND IT FIRES: 12 times, in six live batches — 72, 75, 77, 78, 79, 87.** Every
instance is a named predicate consequently **rejected, replaced, re-authored, re-labelled, or
blocking a gate**, each quoted in
`~/.claude/docs/analysis/briefs-2026-09-03/BRIEF-Q4-c40-c42-fire.md`; the detectors were proved on
planted good and bad cases before any count was believed. Sharpest three: a charter acceptance
**replaced** at batch-77 because it measured GREEN on the pre-change tree; six ATs rewritten at
batch-78; and at batch-77 a **claimed `C-40` discharge rejected** — §9's checklist marked both limbs
✓ over mutations of *code that did not exist yet*. The control turned on its own checklist.

**But the fire count is a LOWER BOUND, and what it cannot see is the more useful finding.** The
dominant live use is not rejection at a gate — it is **authoring-time shaping**: **23 `⚠️ C-40:`
advisories written into acceptance criteria before any AT existed**, where no rejection occurs

…

**A RULE READS THIS OBLIGATION FROM FLOW rev63, AND IT IS ATTRIBUTED HERE FROM rev64.**
`V33`/`Negative control` (`~/.claude/docs/tools/devflow-validate.py`, `req-template.md`) requires
every acceptance-bearing requirement to declare *the executed input on which the verification GOES
RED* — limb 1, as a field a rule reads. The attribution is not bookkeeping: **the obligation is
being honoured while the citation dies.** batch-89 and batch-90 discharge it in **16 of 16** and
**9 of 9** requirement blocks and name `C-40` **once between them**. At rev64 `V33`'s scope was
widened from `test`/`analysis` requirements to every **acceptance-bearing** one, because `C-40` binds
the second and read only the first — measured: **50** requirements across the 67 contracts were out
of reach, and **0** on either live active batch.

…

batch-90's `LLR-90.1.3` writes its negative control in the future tense (*"must make the check RED"*)
and passes, while two siblings in the same contract paste real transcripts. The difference visible to
any mechanism is prose tense. The execution is owed in the increment packet, per arm, under
**`Mutation verdicts`** (`V37`) — with the harness's registry ids, so the claim is re-runnable.

**The DISCHARGE clause got its own reader at flow rev68, and the reason it is not `V37`'s second limb
is measured, not preferred.** `C-40`'s discharge is three things — name the mutation, execute it and
paste the transcript, and **restore it, confirming the restore by the file's hash returning to its
pre-mutation value** — and the increment packet's `**RED counterfactual**` row (`V44`, NOTICE) is what
now reads it. **Fourteen** packets carry this obligation as a checklist row and **eight** carry
both it and `V37`'s, and the correspondence between the row's LABEL and its VALUE is exact: the **2**
whose text still read *"RED counterfactual captured **and restored by hash**"* both named a restore
digest (`sha256 177b9311… restored`; `sha256 ca1b6f7a… restored, CRLF intact`) while their mutation row
named arms — **no overlap**; the **12** that had dropped the clause named **no digest at all**, and ten
of them wrote a mutant TALLY in its place (*"34 scored, 34 reddened, 0 survivors"*), which is `V37`'s
subject. **The restore half disappeared from all twelve.** So the observed failure IS the
fold, and a folded rule would score a packet that ran a battery and never proved its tree came back
exactly as one that did both. `C-20`'s move-aside is the same row's other half — for a NET-NEW file the
RED is captured by moving the file aside, never by `git stash`, and the restore is proven by the file
existing again.

**TWO RIDERS ADDED AT FLOW rev75, AND THEY ARE ONE EDIT ON PURPOSE.** The operator's `C-45` sitting
of 2026-09-11 ruled `BRIEF-7` rows 1 and 11 **together** (rev70's own battery, and batch-76's
undischarged three-point proposal of 2026-07-31): both ask *does this mutation actually corrupt what
it claims to*, and housing them as two entries would be `C-50`'s two-inventories-of-one-class defect
committed in the catalog that names it. Both are **authoring-side** — neither implies a rule, and
the sitting said so explicitly: enforcing rider 1 in `devflow-mutate.py` is a separate revision's
work and is not claimed here.

…

SUBJECT the guard reads.** Three registered mutants were retired at flow rev70 for deleting the arm
that would have caught them rather than corrupting the thing that arm watches. **Both shapes score
KILLED, and only one of them is evidence:** deleting a guard proves the guard runs, which nobody
doubted. **The figure is a PROXY, is labelled one, and carries the predicate that produced it** — at flow
rev74 (`29da5f6`, the sitting's own tree) the registry holds **398 live** mutants, of which **14**
carry `new == ""` (pure deletion) and **24** more satisfy *`\bif\b` matches `old` and not `new`*
(the guard dropped, a substitute left behind): **38 of 398 — 9.5%** — are guard-removal-SHAPED.
That is an argument for the rule and not a count of defects: it cannot separate a legitimate
deliberate-emptiness mutant (`r65-M11-fold-never-applied`, correctly named for what it tests) from
a vacuous one, and **no hand pass over the 38 has been run** — said here so the number is never
cited as a defect count. ⚠ **`BRIEF-7` published this as *12 / 24 / 36 of 350*, and re-derived at
three registry snapshots it reproduces at EXACTLY ONE, rev72 (`730e63e`) — and only under a reading
of *empty* that admits whitespace, `r69-M15`'s `new` being a space.** Its real defect is the
DENOMINATOR: `350` is the registry TOTAL at that snapshot, where `live` is **334**, so the figure
was published against a population that includes retired mutants. **Only the `24` was stable across
all three snapshots**, which is the tell that the other two were counted once and then carried — the defect
`C-57` names, in a figure rather than in an instrument. **Discharge, one question at authoring time:**
*name what this mutant makes WRONG*, not what it removes. A mutant whose `why` can only be written
as “the check is gone” is the vacuous shape. Adjacent to `C-60`'s limb 3 and folded into
neither it nor `C-57`, because those are about the harness's INPUTS and this is about the mutation's
TARGET.

**Rider — “it applied” is not “it landed where it matters”: the anchor matches

…

READS** *(batch-76, 2026-07-31 — proposed with its three-point discharge and never folded in,
still open at the sitting **six weeks** later — 42 days, re-derived from the two dates in this
sentence rather than carried from `BRIEF-7`, which said seven)*. Bytes moving is not evidence. This limb is mechanical
where the two above are semantic: **(i)** a second anchor match means the harness mutated a site
nobody chose; **(ii)** an unreachable region cannot be observed by any arm; **(iii)** an expression
the asserting node never reads cannot change that node's verdict. The canonical harness already
enforces (i) — a non-unique anchor and a byte-identical substitution are both `BAD`, never
`SURVIVED`, and `BAD` fails the run — so **(ii) and (iii) are the authoring half and are performed
by a reader**, which is where they stay until somebody builds the call-graph check `C-51` also wants.

### C-59 · Evidence bytes live at a declared home, verbatim, and the store is verified

*(batch-66, and the same class again on 2026-09-07; flow rev66, `Q5` + `Q19` ruled as ONE control)*

**Failure closed.** An artifact is committed as PROOF — a transcript, a capture, a snapshot, a
`.PRE` copy of a file that lives outside version control — and the hash recorded beside it *is*
the contract. Two things then go wrong independently, and either one voids the proof while every
gate stays green: the STORE rewrites the bytes on the way in, so the digest no longer describes
what is stored; or the bytes are put somewhere that does not survive, so there is nothing left to
compare a digest against. **They are one control and not two**, because a store that verifies
bytes nobody can find and a store that keeps bytes nobody verified fail the same obligation from
opposite ends — and two controls would let a batch discharge one and cite it for both.

**Rule.** An evidence artifact is written to the home `artifact_homes.evidence` declares (a
`repo:` or `vault:` location — durable, named at the batch, **never a session-scoped `Temp`
path**), stored **byte for byte**, and cited in the packet with the **SHA-256 of the bytes at
that path**. The digest is re-derived from where the artifact LANDED, not from the file that was

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

**Exhibit 1 — the store rewrote the bytes and the commit looked healthy.** batch-66 committed
`.PRE` copies of four out-of-VCS files whose recorded SHA-256 was the entire rollback contract.
`core.autocrlf=true` normalised them on the way in: one was stored as `d46bb314…` against a
recorded `e103af29…`. A rollback from that commit would have restored bytes that do not hash to
the original. It was caught only because the ledger was re-checked against the **index blob**
rather than the working copy. **Two traps travel with it.** The corruption is **bidirectional and
half of it is invisible at commit time** — a CRLF file normalises to LF going in, while an LF file
converts to CRLF coming out at the next checkout, so its blob matches and its checkout does not.
And **`text eol=lf` is the WRONG fix**, even where a repository already uses it for snapshots and
goldens: evidence carries mixed line endings by nature, so only `-text` is correct.

**Exhibit 2 — the bytes were verified and then kept somewhere that disappears.** The same batch's
three destinations outside version control had no git history, so their `.PRE` copies WERE the
rollback — and they sat in the agent session's scratchpad, which does not survive the session.
All four matched their recorded hashes, so the rollback worked *that* time. Nothing made it work
the next time.

**The general form, and it is why this is not a git lesson.** *Whenever a hash is the contract,

…

handed to the store. Same family as `C-42` (*assert the EMITTED form of the producer*) with the
store as the producer — and the class recurs one layer in: a mutation harness in this project
failed its own SHA-256 restore check because text-mode I/O rewrote an LF file as CRLF, which is
content-equal and **not** byte-equal.

**Mechanism (flow rev66).** `artifact_homes` gains `evidence`, seeded by `/dev-flow-init` step 3.
`increment-template.md` gains the **`Evidence files`** section — a table of *artifact · path ·
SHA-256* and a declared field with a wording for having nothing to say — and gate row 16.
**`V41`** reads all three clauses: it NOTICEs a batch declaring no evidence home and a packet that
answers the field with nothing, and it **BLOCKs** a cited digest that disagrees with the bytes on
disk. That last severity costs nothing retroactively and the figure is the argument: measured
2026-09-10 over all **246** increment packets of this project's record, **none carries an
`Evidence files` section**, so the BLOCK branch fires on no document that exists — while a digest
that does not match its own bytes is not an omission a reader may weigh, it is a false claim.

> ⚠ **That figure was published WRONG first, and the correction is worth more than the number.**
> The claim shipped as *zero packets cite an artifact with a digest*, derived by a reader that
> scanned the WHOLE packet for a table row holding a 64-hex. Re-derived by the independent review
> with the same reader, it found **two** rows — in `2026-07-30-batch-72`'s fourth increment, a
> `git show …:… (blob)` restore ledger, which is a **correct** packet doing exactly what this
> control recommends. So the instrument was over-broad in both directions at once: it would have
> raised *does not sit under the declared home* on correct work (`C-53`), and it produced the very
> figure the severity argument rested on. The reader is now scoped to the section the template
> mints, and the figure above is what that reader measures. **`C-57` inside `C-59`'s own
> evidence** — a published instrument believed before it was shown to discriminate.

**What the rule cannot reach, declared rather than discovered.** A `vault:` home resolves against a
per-installation `vault_root`, so digests under it are **reported and never verified** from the
repository — the rule says how many rows it could not reach, in a sentence of its own. And it reads
whether a digest AGREES; it cannot know whether the artifact is the one the packet meant.

### C-58 · A mandate nothing reads is a paragraph
*(batches 88-89; flow rev63, 2026-09-07)*

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

`C-40` asks whether an acceptance predicate can go RED; this asks the question one level out,
of an obligation that has **no predicate at all**.

…

that reads it** or **a written exemption saying why not**. A mandate with neither is prose, and
it should be written as prose so nobody mistakes it for a control.

**The corollary that makes it operable, and it is where the mechanism usually goes wrong.**
The reader must be keyed on a **declared field**, never on a phrase. A corpus states the same
obligation in as many wordings as it has sites — measured on `<project>/.dev-flow/**.md`:
**19 sites, 19 distinct phrasings** for one obligation — so a rule grepping any one wording
catches 1 of 19, and a template that keeps its GUIDANCE in the value position makes every
unfilled slot read as answered. Key the slot; put the guidance beside it, not in it.

**And the second corollary, about what "empty" means.** The declared-empty wording is part of
the mandate. Where an absence is legitimate the template must say what to write (`none — <the
reason>`), so an absence DECLARED and an absence OMITTED do not render alike. Where the
absence is NOT legitimate, the template must say that too: for the independent-review pass,
`ABSENT` is the **empty** state and not a value, because the flow mandates the pass.

**Example (three, dated, measured).** (i) `R-89-8` — the 2026-08-28 ruling made `Negative
control`, `Boundary catalog` and `Acceptance test(s)` mandatory in `req-template.md`; measured
on 2026-09-07 against the shipped validator, `Negative control` returned 6 hits and `Boundary
catalog` 3, **every one a comment about the validator's own arms**, and `Acceptance test(s)`
returned **0**. Three mandatory fields, zero readers. (ii) `code-reviewer-absent` — the flow's
own `commands/dev-flow.md` mandates an independent `code-reviewer` pass at every increment
gate and says a HIGH blocks. batch-88 ran it at **7 of 7** increments; batch-89 ran it at
**0 of 6**, wrote `ABSENT` in all six packets, shipped **five flow revisions**, and **every
gate passed**. The absence cost nothing, which is the definition of a paragraph. (iii) The
exhibit that is not a failure: two batch-89 packets **performed** the instrument-RED-proof law
in a hand-written checklist row **that exists in no template**, in two different wordings — so
even where the obligation is honoured, an unminted row leaves the record unreadable.

**Discharge.** Not in a packet field — in the flow's own tooling. At every revision that mints
or amends a MANDATORY field, name the rule that reads it in the same increment, and prove the
reader RED on a document with the field deleted and on one holding the template's own
placeholder. Flow rev63 discharges the three `R-89-8` fields as `V33`/`V34`/`V35` and the
review pass as `V36`, all four `V9`-shaped NOTICEs keyed on declared fields.

**The open question this control does NOT close, stated so nobody reads it as closed.** The
same argument applies to the CONTROLS in this catalog: `C-40`/`C-42`-fire is an open `P1`
asking whether those two controls fire at all or should be demoted to paragraphs. `C-58` is
the general form of that question and it does not answer it; it says only that the question is
the right one, and that a control which cannot be shown to have fired is in exactly the
position `R-89-8`'s three fields were in.

**Rider — a fix can be correct, LAND, and be held by nothing** *(flow rev70's `⏸ Candidates`
battery; ruled onto this control at the `C-45` sitting of 2026-09-11, `BRIEF-7` row 2)*. This
control's subject is a MANDATE nothing reads; the same mechanism applies one step later to a
**REPAIR**. A fix can be right, land, and carry **no arm that would redden if it were reverted** —
so it survives exactly as long as nobody edits near it, and its correctness is a fact about the day
it shipped rather than a property of the tree. **Distinct from `C-57`**, which asks whether an
instrument can report failure: this asks whether any instrument is POINTED AT THE FIX AT ALL.
**Measured — and the measurement went wrong TWICE before it came out right, which is the most
useful thing this rider has to say.** The question the rider asks is *name the arm that reddens if
this diff is reverted*, and asking it of the flow's own canon needs the registry read correctly.
**`BRIEF-7` answered *12 of 12* from a hand list** (4 commands + 7 templates + 1 catalog) — a
population that does not exist: the template directory holds **fourteen** files and the **nine
`agents/*.md`** entered the manifest at rev73. **The first fold answered *33 of 34* from the
registry's `subjects` key** — also wrong, and wrong in the more instructive way: `subjects` is the
harness's RUN CONFIGURATION (which program is executed, its argv, its arm regex), while the file a
mutation is APPLIED TO is each mutant's own `file` key, which `devflow-mutate.py` resolves as
`subject_path if mutant.get("file") is None else join(root, mutant["file"])`.

**Derived from the `file` key, over the manifest's 34 tabled files, at rev75's registry (406 live
mutants, 29 distinct target files): 27 of the 34 are REACHED and 7 are not — and of the 28 prose
files, 24 are reached and only FOUR are not**: `templates/dev-flow/architecture-template.md`,
`design-proposal-template.md`, `executive-summary-template.md`, `agents/presentation-builder.md`.
`commands/dev-flow.md` alone carries **28** live mutants and this catalog carries **2**.

⚠ **And the unit is still not the rider's unit, which is the third way this one figure has been
counted wrong and the last.** *A file being REACHED says an arm exists somewhere in it, never that a
GIVEN FIX in it is held.* One mutant pins one sentence: of the 24 reached prose files **12 carry two
or fewer live mutants and four carry exactly one** (`commands/dev-flow-init.md`, `dev-flow-sync.md`,
`fast-dev-flow.md`, `templates/dev-flow/design-review-template.md`), and this census scores those
identically with `commands/dev-flow.md` at 28. **The first two answers erred toward alarm; this one
errs toward claimed coverage, inside a rider whose whole subject is fixes nobody holds.** So: the
file-level census bounds this rider's scope **from below** — four prose files, two hooks and the
CI workflow are reached by nothing at all — and **the per-fix question stays a question at the
gate**, which is where the rider puts it.

⚠ **Both wrong answers were larger than the truth and both read as closed censuses**; the first
fold even called its figure *nearly three times worse than the one almost shipped*, and it is three
times BETTER. **A rider about repairs that nothing holds was twice held by nothing itself**, and
what caught it both times was a reader asking the rider's own question of the rider's own evidence. **Discharge, one question at the gate:** *name the arm that
reddens if this diff is reverted.* When the honest answer is “none”, that answer is written
down — `C-55`'s declared emptiness — and it is not a reason to skip the question, because an
unheld fix that is KNOWN to be unheld is a different object from one nobody asked about.

### C-57 · An instrument is blind until it has reported a failure
*(batch 89; flow rev59-60, 2026-09-06)*

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

the **measuring apparatus** — the substring reader, the AST walk, the regex, the stdlib call, the
self-comparing arm, the grep that produced a census — and that is where every instrument defect of
2026-08 lived. None of those carries an `AT`/`TC` id; none sits under any gate; `C-40` never reaches
them.

…

**mechanism**, not merely its **verdict**.

**The corollary that makes it operable, and it is the expensive half.** A negative control that
replaces the whole probe with a constant is not a mechanism test: `N7-case-probe-is-assumed` replaced
an entire case-fold probe with `return True, None` and **survived twelve mutants**, because this
machine really does fold case — so the verdict was armed and the mechanism was not.

**And the second corollary, which is about the READER of the instrument.** A harness that scores its
mutants from stdout alone calls an import-time death a SURVIVOR, because a file that dies at import
emits no arm line at all. Three verdicts, never two: **KILLED / CRASH / SURVIVED**. *(Flow rev64
adds a fourth, and it is the same lesson one step earlier: a mutant that never **applied** — its
anchor matched zero times, or its replacement moved no bytes — is **BAD**, not SURVIVED. Two rev63
mutants matched nothing and one earlier battery split a path so its first two mutants never ran; all
of them read, to a careless reader, exactly like survivals. The flow's canonical harness is
`~/.claude/docs/tools/devflow-mutate.py`, its mutants are named data in `devflow-mutants.json`, and
its own four verdicts are proved on four planted known-bad inputs before any verdict of its is
believed.)*

**The FIXTURE sub-case — the predicate is fine and the DATA cannot tell the difference.**
*(batch 74; folded in at flow rev64 by the 2026-09-07 ruling `Q16`, as a named sub-case rather than
a second control: the catalog already sweeps this corpus, and two inventories of one class is the
defect `C-45`'s currency check exists to catch.)*
A predicate can be correctly written, correctly scoped, and quote exactly the right formula, and
still be unable to fail — because the **fixture's own symmetry** collapses the distinction the
predicate tests. **Executed:** every `Address` fixture was all-`F`, and on an all-`F` value rendering
the trailing K hex digits is byte-identical to rendering the leading K, *and* `bit_length() // 4` is
byte-identical to `(bit_length() + 3) // 4` — the `+3` is a no-op whenever the top nibble is ≥ 8,
which every `F`-leading value satisfies. The node that could not discriminate was the one **whose own
assertion quotes that ceiling formula**. Both defects survived a 29-node suite and were found by the
independent reviewer, not by the author's `C-40` pass, because **the mutation changes no output on
that fixture**. A second exhibit, one batch on: a batch-89 constant satisfied by **case-folding
alone** — the machine really does fold case, so the verdict was armed and the mechanism was not; and
a third, flow rev63's `M10`, a mutant whose replacement left the file byte-identical and was scored
as a run.
**A fourth exhibit, and it is the one that names the axis a fixture has to vary along.** `V25`
printed a ref count drawn from `ls-remote origin` beside an age drawn from **every** remote on the
machine — a typed sentence that **pins its WORDING and never its REFERENT**. Nine typed-sentence arms
and six registered-rule E2E arms all passed, because **every fixture had exactly one remote**, so the
sentence's referent and the oracle's domain were the same set; the same fixture let
`committerdate` → `authordate` survive for the identical reason. *The detector is not a better
sentence arm — it is a fixture whose domain has TWO elements that disagree, and each axis needs its
own second element.* One fixture with two remotes kills both mutants; no amount of re-reading the
sentence does.

**Ask of every fixture: *what does this make indistinguishable?*** For any predicate over a
positional, digit-wise or order-dependent property, add one **deliberately non-uniform** arm with its
discriminating precondition ASSERTED — batch-74's arm asserts `bit_length() % 4 != 0` and
`total == len(raw) - 2` *before* it asserts the behaviour, so a fixture that stops discriminating
fails loudly instead of passing quietly. **`C-40` asks whether the PREDICATE can go red; this asks
whether the FIXTURE lets it.**

**The INTER-TOOL sub-case — the tool that ran the step is not allowed to be the oracle that it ran.**
*(corpus: a commercial calibration-data tool, 2026-09-09, outside the record; folded in at flow rev71
by the operator's `Q23` ruling as the THIRD sub-case of this control rather than a fourth control —
the intra-suite case and the fixture case are already here, and this is the same class one tool
further out.)*
A step can **report success and have done nothing**, which is strictly worse than a crash: a crash
stops the line and costs nothing, a silent no-op propagates. **Executed:** a proprietary wizard run on
a 64-bit host completed **without error** and did not update its target datasets, while the same run
on a 32-bit host worked. A dataset left holding stale values is visually indistinguishable from a
correct one, and the defect surfaced only at a downstream generation step, and only because somebody
checked.

| A visible error | This |
|---|---|
| the process stops | it reports success |
| you know to redo it | it looks like it worked |
| damage is zero | stale data moves downstream |

**Rule.** When a step's success signal is produced by **the tool that executed the step**, that signal
is not the gate. The gate is an **observable delta measured by something that did not run the step**.
Two independent derivations of one fact that agree is evidence; one tool's exit code is an assertion
about itself. **Same shape as `C-60` one abstraction up:** `C-60` is the intra-suite case — the
harness and the check sharing an input — and this is the inter-tool case, the verifier and the thing
verified sharing a *provenance*.

**Example (five, dated, all from one batch).** (i) A mutation verdict read by substring reported 6 of
6 kills as survivors. (ii) An AST walk on the running interpreter reported a Python floor of 3.7 when
it was 3.12. (iii) A detector with a backwards regex under colour reported `0 killed / 12 survived`
when 12 were killed. (iv) `ast.parse(feature_version=)` was read as "3.7 accepts this" when it returns
the *running* interpreter's own verdict. (v) An arm comparing a constant to itself was green and
blind, and its sentinel SURVIVED the first battery — correctly. **The law is one control, not five
fixes.**

**Two more, from the flow's own machinery, because the pattern did not stop at that batch.** At flow
rev59 a mutation harness's first cut scored an alias mutant SURVIVED for exactly the reason above, and
was repaired before its verdicts were believed. At flow rev60 a `SyntaxWarning` shipped since rev59 —
`TC-B\d+-` inside a non-raw docstring — was emitted at compile time on **stderr** under Python 3.12
and **interleaved mid-line into the arm transcript**, so a reader counting arm lines got 591 where
3.11 printed 592. **The instrument was not wrong about the rules; its own transcript was corrupted by
the interpreter running it**, which is a failure mode no rule-level check can see.

**The PARTITIONED-INSTRUMENT sub-case — an `any` over an instrument that reports a VECTOR
passes on the instrument's own good half** *(flow rev74; folded in at rev75 as the fourth sub-case of
this class — the shape of the three above, one level up)*. The cases above ask whether an
instrument has been shown a known-bad input. This one asks the sharper question **of the arm that
does the showing**: when the instrument reports per field, per rule, per file, an arm written
`any(field == BAD)` is satisfied by a **single** bad field, so a defect corrupting the instrument's
OTHER fields leaves it green — an instrument RED-proved on one component and believed on all of
them. **The exhibit is rev74's own, and the battery found it after two review passes had not.**
`FV SEVERITY-census` parses five figures and two id lists out of a published paragraph; its first
ambiguity arm asked `any(... == AMBIGUOUS)`, and `r74-M14` — which strips the guard from the five
FIGURES and leaves it on the two id LISTS — **SURVIVED**. The arm now asserts **all seven fields**.
**Rule: an arm over a partitioned instrument asserts the WHOLE partition, by name and by count**;
`any` is admissible only where the instrument returns one thing. The neighbouring shape is `C-40`'s
arm-count limb — *an arm the harness cannot see is an arm it cannot report inert* — and the
difference is the sharp part: **here the arm sees every member and is satisfied by one.**

…

input fed to it and the FAILURE it returned, before any PASS from it was believed. Write
`none — no instrument beyond the suite` when there is nothing to declare — an absence declared is a
declaration, an absence omitted is a gap, and a rule cannot tell them apart otherwise.

**Why a FIELD and not a phrase, measured rather than argued.** The two packets in the corpus that
ever carried this obligation carried it as hand-written prose in a checklist row that exists in no
template, in two different sentences, and a third site (`04-validation.md`) wrote it a third way.
**Three sites, three sentences, one law, zero templates.** Any phrase-matching rule is structurally
blind to the fourth wording, so `V31` reads a declared field and nothing else.

**Honest limit.** `V31` reads whether the question was ANSWERED, never whether the answer is true or
complete: a partially filled cell reads as declared. Quality stays with the reviewer. And the
counterfactual "would the field have surfaced any of the five earlier" is **unmeasurable** from the
record — every one was found by an author looking twice or by a sentinel already in flight.

### C-60 · The harness that proves a check must not share a fixture with it
*(corpus: an outside course-verification harness, 2026-09-10, outside the record — the first outside
evidence this catalog has ever been offered; minted at flow rev71 by the operator's `Q23` ruling,
with two IN-HOUSE exhibits the proposal did not know about)*

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

remedy fails silently when the mutation harness resolves its target through the same constant, path,
or discovery helper as the assertion under test.** One root cause then disables both the check and
its detector, and nothing can go red. It is the regress `C-57` terminates at, reached from the other
side: not *who checks the checker*, but *what do the checker and its checker share*.

…

1. **The harness resolves its inputs independently of the artifact under test, and relative to its own
   location** (`__dirname`, `Path(__file__).parent`) so the harness and its material cannot be
   separated by a move, a rename or a consolidation. A shared absolute path, a shared config constant
   and a shared discovery helper are the same defect wearing different clothes.
2. **A mutation run that cannot resolve its target is a hard RED, never a pass.** Assert the expected
   mutant count *before* running. `total=0` is failure, not success.

…

**Example (the external corpus).** A verifier declared `SIBDIR` as an absolute path to a directory
that no longer existed. Fifteen assertions filtered that set through `fs.existsSync`, got `[]`, and
reported green. Both mutation harnesses carried the **same dead constant**: one printed
`BASELINE rc=0 green` and then crashed on `FileNotFoundError` opening the file it was supposed to
mutate. The instrument that would have exposed the vacuity was broken by the identical cause, so the
defect was undiscoverable from inside the suite. Measured, before → after resolving all three
constants from the harness's own location:

```
verify-course.js      16 failures / 530 asserts  ->  NO FAILURES / 584 asserts   (+54 never evaluated)
mutate-course-md.py   could not open its target  ->  killed=22 survived=0 anchor-miss=0
mutate-course-ter.py  same dead constant         ->  killed=5  survived=0 anchor-miss=0
```

**Two IN-HOUSE exhibits, and they are why the proposal's note that this had no local validation is out
of date.** (i) **Flow rev65's `F1`:** `Q18 TRACKED-foreign-root` was keyed on the ambient fact that
`~/.claude` happens to be a git repository, so the plain harness command scored **nothing** against a
red baseline — *and the mutant written to RECORD `F1` was keyed on the same ambient fact*, which is
limb 1 arriving by itself. (ii) **Flow rev67's `DEVFLOW_HOME` pop:** `V30`'s E2E fixture **POPPED**
the override in its `finally` instead of RESTORING it, and that variable is how the canonical harness
points a staged run at its scratch tree. Every arm after that block re-read the operator's live
`~/.claude` while claiming to read the copy under mutation, and **five mutants scored SURVIVED
falsely** — a staged run reading an unstaged tree does not report a weaker finding, it reports a false
one, in the safe direction, which is the only direction nobody checks.

**Rider.** Extends `C-40`'s rider (*assert the expected arm COUNT first*) one level up: assert the
harness's own **input resolution**, not only its arm count. An arm count is meaningless if the set
being armed is empty — which is **`C-55`** exactly, and the two controls meet here.

### C-43 · Premise evaluation — verifying work against a spec never verifies the SPEC's claims about the world

**Failure closed.** Every control above asks whether a *predicate* is sound, executable or falsifiable.
None asks whether the **claim the predicate rests on** is true. A stage can be fully compliant with a
requirement whose premise is false — and the gate passes, because the gate was checking conformance.

**Example.** A design batch wrote that a module's `variant_id=None` line was *"the single-variant
assumption, explicit in the code"*, and concluded the feature was *"mostly threading an existing
dimension, not building one"*. The line was real and at exactly the cited address — but sat inside a
**different block handler's** operation input, whose `variant_id` is the operations kernel's reporting
metadata. The module had **no such dimension at all**: three occurrences of the word across 531 lines,
none of them a seam. An implementer trusting it would have wired the new dimension into the wrong
object and believed the increment closed. Ten premises were executed; **eight held exactly — including
two line-counts and a cited line ADDRESS**, which is why "it looked verified" is not a defence.

**Rule — three verdicts, three tiers.** Verdicts: ✅ **TRUE** (an *executed* probe — command output, a
`file:line`; **citing another document is not evidence**) · ❌ **FALSE** (blocks) · ❓ **UNDECIDABLE**
(missing verification, or an ambiguous/incomplete requirement — blocks until decided or declared out
of scope **in writing**). Tiers: **axioms** (validated AND verified — law by default) · **hypotheses**
(*whatever this batch introduces, including everything inherited from a prior design batch — written
down is not verified*) · **premises** (claims about the world: symbols, line numbers, sizes, "X already
exists" — executed against disk, never trusted).

**An axiom is re-litigable, but only CONSTRUCTIVELY.** It re-opens on an executed counterexample or a
logical invalidation — which in practice is almost always **INCOMPLETENESS**, not falsehood. **The
disposition ENLARGES the requirement; it never deletes it.** Worked example: a spec's security section
declared a constraint mandatory while none of its six acceptance criteria observed it. Folding the
missing case into the nearest criterion was **rejected** — a two-subject acceptance is where an earlier
batch lost a threshold — and a **seventh** criterion was added, consuming an existing completeness
census rather than building a new oracle. The requirement set came out larger. That is the point.

**Reader: `V45`, flow rev69 — and this control had none for twenty-six revisions.** The per-batch
half is recorded in the requirements document's `**Premise evaluation**` field, in `req-template.md`
§2.7 beside the table it rolls up: the count, and the verdict, leading the cell with one of the three
tokens above or the legal empty `none — <why no premise applies>`. A cell reading `done` or `see the
table` scores **unidentified**, because the gate rule turns on the token and nothing else. **Measured
2026-09-10 over the 66 live `01-requirements.md` of the the origin project record, case-sensitively because the
reader is: a heading NAMING `Premise evaluation` is present in 10, the exact literal
`### 2.7 Premise evaluation` in 6, and the KEYED FIELD in 0 of 66**, including 0 of the 2 in the
active pair — both of which carry a heading. That is what *the most-cited
control in the flow, called mandatory at every gate* had bought: eleven command citations, three
template citations, and no mechanism. ⚠ `BRIEF-6` published *69 of 81 absent*; the 81 counted
`-architect` variants, `-DRAFT`s, `-rescoped` forks and a ledger, none of which is a contract any rule
reads. The population a rule can have is 66, and the FIELD figure — 0 of 66 — is the stronger claim.
**Severity NOTICE, three-batch convention:** carried by batches 90, 91 and 92, it BLOCKs or it is
retired.

### C-55 · An emptiness is doing work — say which kind

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

case**. It is the quietest defect here because nothing is wrong today: the claim is true, the suite is
green, and the change that will falsify both is one nobody will connect to either. C-40 asks whether a
predicate *can* go red; C-43 asks whether a premise is *true*. C-55 asks a third question both pass
over — **what is this resting on that is only accidentally the case right now?**

**Limb 1 — the emptiness is the FINDING.** When the result is an *absence* ("no X exists in the tree",
"the blind spot is empty"), the property that made the search wide enough is **part of the result**. A
negative result is only sound if the search was too **WIDE**; narrow it later and every derived claim
weakens while every guard stays green. Guard the over-breadth, and **say in the guard's own docstring
that it protects a CONCLUSION, not a behaviour** — otherwise the next reader files it as an
implementation detail and improves it away.

…

Run the same probe, unmodified, over a case known to be present. **Uniformity over heterogeneous inputs is the TRIGGER for
that control, never the verdict** — the correct answer can be uniform too, and in the origin below it
*was*: all 35 files really were present. A clean tree greps zero everywhere. Treating uniformity as a
verdict false-fails correct work, which **C-53** prices as high as passing wrong work. A *plausible*
zero reads as data; only an *impossible* value betrays itself, and that is luck, not detection. **If no
known-present case can be constructed, say so and downgrade the claim from a finding to an unverified
observation** — a control that cannot be paid is one that gets skipped in silence. This is **C-53's own
habits 1 and 3** (*lights up everywhere ⇒ probably mis-scoped*; *pair every rule with a positive AND a
negative control*) plus reader-as-oracle, applied to
**diagnostic probes** rather than to checkers and tests — and the gap is real, because nobody treats a probe as
code to be verified: *"I am only looking."* Measured: one cleanup session produced three broken
probes in a row with the identical signature — a `grep` flag supporting only unibyte and UTF-8 locales (27 of 27
branches reported "no PR", merged ones included), and a shell rewriting `rev:path` into `rev\path`
twice (**35 of 35 files reported ABSENT** when all 35 were present). The second was one sentence from
being reported as 35 files of lost work; what caught it was contradicting an earlier probe, not any
guard. The only trustworthy measurement in that session was the one probe carrying a positive control.

**Limb 2 — the emptiness is an ACCIDENT of today's data.** A guard clause that is a **no-op on the
current tree** is untested however green the suite, and the tell is mechanical: **mutating it changes
nothing today.** Two consequences: **a conjunctive criterion needs one mutation per conjunct**, and

…

**Example.** A batch's entire result was that no widget address in its tree is assembled from parts —
sound only because the binding walk deliberately **over-collects**, reporting bindings from unrelated
functions in the same file. One guard, explicitly labelled as protecting the conclusion, is all that
stops a later scope-precise "fix" from weakening every such claim with the suite green. In the same
batch a criterion read *"emit it under its own outcome and **never drop it**"*; only the classifier half
was mutated. Filtering unresolved rows out of the resolver's return passed **all sixteen** guards — it
dropped nothing, because the tree holds **zero** instances of the unresolvable case.

**Discharge:** construct the case the tree lacks — a fixture tree, an in-memory module, a synthetic
input — and assert the property against it. *"There are none today"* is the reason the guard is needed,
never a reason to skip it.

**An EXTERNAL corpus reproduced this control, which is evidence of its generality and not a new
control.** *(outside verification harness, 2026-09-10; assessed at flow rev71 under `Q23` as a
restatement of this entry and of its rider, and deliberately NOT minted as `C-61`.)* A suite ran
`set.filter(exists).forEach(assert)` over a set that resolved to empty: six sibling files behind a
stale absolute path, `existsSync` false six times, `filter` → `[]`, `forEach` over nothing — **fifteen
checks reporting green for an unknown number of runs, zero assertions executed.** The proposal framed
it as a new law (*assert a discovered set's cardinality before iterating it*); measured against this
entry it is limb 1 with the emptiness arriving from a **missing input** rather than from a true
absence, and the discharge is the rider already written above — *an absence is admissible only if the
probe that produced it CAN produce a non-absence*. **The mechanical form is worth stating because the
external corpus states it better than the origin did:** where a set is DISCOVERED at run time, assert
its expected cardinality first — *the discovery is part of the check* — because a control whose input
set is empty **did not pass, it did not run**, and a boolean green collapses those two verdicts into
one. The corpus's own rider (*resolve harness inputs relative to the harness's own location*) is not
here: it belongs to the harness rather than to the emptiness, and it joins **`C-60`'s limb 1**.

### C-56 · An evidence transcript is corpus input

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

**Failure closed.** An artifact written to PROVE something is read by the same scanners as the work
it describes. `.dev-flow/**` feeds the Atlas id-scanner and V13's tree grep, so an increment packet,
a review finding and a close record are corpus on the same terms as a spec — and no scanner
distinguishes a token being *reported* from one being *declared*.

**Consequence 1 — a mutation reverted in its target file but SPELLED verbatim in a transcript is not
reverted.** C-40's restore obligation covers the file that was mutated; it says nothing about the
packet quoting the mutation, so a sha256-proven revert can verify the wrong plane — source clean,
defect relocated into the evidence. **Describe mutations by position and operation** ("the id's fourth
character, digit → letter"); never paste the mangled token.

**Consequence 2 — dotted-range id shorthand is forbidden wherever an id-scanner reads.**
`AT-020..024` is not a range to a tokenizer. Enumerate, or write `AT-020` through `AT-024`.

**Consequence 3, added at flow rev75 — AN ARM'S OWN NAME IS CORPUS TOO, and it can be a member of
the set that arm refuses.** `V51`'s lineage-strike arm asserts that its id scores zero across six
canon documents; its own name contains that id, so citing the arm BY NAME in any of the six turns
the selftest red and blames the id rather than the citation. rev75 did exactly that and found it

…

size is a different object from a surprise*, which is the posture `ATL WILDCARD-known-cost` takes in
*The WILDCARD-STEM sub-case* below.

**Example** (Consequences 1 and 2)**.** An Inc-1 packet quoted the RED arm's corrupted id and two range tokens; the Atlas adopted
**three phantom ids**, one `--atlas --write` from the committed derived plane. Twice more the same day:
the orchestrator nearly re-committed the defect into the close record, and a zero-padded dotted range
in a batch-51 matrix proved **pre-existing**. The tokenizer half is closed at flow rev45 (a token whose
continuation is not registry grammar is refused whole, not truncated to a stem) — but hardening the
scanner does not make a mangled token in the corpus true.

**The WILDCARD-STEM sub-case, and its residual** *(batch-87 `increment-001.md` §6; folded in at the
`C-45` sitting of 2026-09-11, `BRIEF-7` row 10 — the same fold-with-band-marker move `Q16` made for
`C-57`, because a scanner that mints ids the corpus never declared **manufactures its own corpus**,
which is this control's subject read from the other end)*.

**What closed, at flow rev74.** `_ATLAS_ID_ATTC` now refuses the family-wildcard forms — `AT-057.*`,
`AT-057*`, `AT-057\*` — and the code-span dot, the two of six planted known-bad forms that still
minted a phantom stem after rev45's range fix. **The Atlas MOVED and the diff is the evidence:**
`ATLAS-TRACE.md` 4531 → 4521 lines as rev74 recorded them, twelve ids losing their batch-realm
mark and ten leaving the corpus entirely — and all ten are `BURNED`, `origin: seed`, nodeless, each carrying a registry
`provenance` that points at the very line the scanner harvested it from. **The registry had been
seeded FROM the phantom**, which is Consequence 1 with the direction reversed. ⚠ **Re-measured at
rev75 the file is 4520 lines** (164 866 bytes; `wc -l` and `splitlines()` agree), one short of
rev74's figure — either the Atlas moved again after that measurement or the number was off by one,
and this rev does not re-run the scan to find out because the corpus is a read-only repository. **The
one-line discrepancy is recorded rather than smoothed**: the evidence did not
merely record a corrupted token, it CREATED the id.

**The residual, declared rather than left open.** A single-asterisk markdown **emphasis** close is
indistinguishable from a family marker to a lookahead, because emphasis is decided by what comes
BEFORE the id and the scanner is looking rightward. Two independent approximations of emphasis scope
count **3 and 4** such sites among the 84 refused, disagree on which, and agree that exactly **one**
departing id — `TC-5xx`, itself a nodeless `BURNED` placeholder — leaves through that door
rather than through the wildcard. `ATL WILDCARD-known-cost` pins it, and **asserts that the refusal
EXISTS rather than that it is desirable**: a known cost with a named size is a different object from
a surprise. It is recorded at the control instead of in a backlog, where it would read as owed work.

### C-42 · assert the EMITTED form, never the rendered one

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

**Failure closed.** Executing the producer is **not enough** if the assertion is then written against
the form a *human reads*. Producers escape, encode, wrap and substitute, so confirming a named output
*exists* passes while a search for its readable form **false-fails a correct implementation**.

**Example.** A heading emitted as a code span was unfindable by its bare text — the probe returned an
impossible `-1`, which is the only reason it was caught. A snapshot export emits `&#160;` entities for
spaces, so a literal search for a visible label returns **0 matches** while the label is plainly on
screen; the emitted form returns **29/29**.

…

actual output, assert against that. Prefer the producer's own structured output (its parser's token
stream, a language-aware source parse) to a substring search over serialized text: a substring search
cannot tell a value from its own encoding.

**MEASURED 2026-09-07: it fires — twice, in two live batches, and both fires refute a MEASUREMENT
METHOD rather than a single predicate.** batch-75 `00-measurements.md`: *"any byte bound written
against `REPORT_CELL_CHARS`/`limit=` arithmetic is wrong by up to 2.03× unless it measures the
emitted form"* (transcript: `md_safe("'"*600, limit=500) -> len(emitted) = 1013`) — a charter premise
refuted at Phase 0, and every byte-bound predicate re-based. batch-77 `02-review-security.md` M-2, a
**MAJOR**: the spec's own grep census returned **0 hits** on a seventh site *"in a file absent from
the whole document — a textbook `C-42` miss, the pattern was written against the readable form"*.

**A FIELD AND A RULE FROM FLOW rev64, and a dissent recorded rather than averaged.** The obligation
is now `**Emitted-form assertion**` in `increment-template.md` — per artifact the increment emits,
the assertion executed against the emitted form and what it returned — read by `V38`. Until rev64
this control had **no rule, no field, and zero citations in `commands/dev-flow.md` or
`fast-dev-flow.md`**: it lived here alone, which is why one sentence now names it at Phase 3.
⚠ **`BRIEF-Q4` §5 recommended against the field** — on its reading, two fires against measurement
*methods* give no per-predicate slot to key on, and the remedy was catalog prose plus the missing
command citation. The operator ruled field + rule; the dissent is why `V38` is keyed on the
**increment packet**, where an artifact is actually emitted, and not on the requirement.

### reader-as-oracle (+ a MANDATORY corrupted negative control)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

### KAT anchor — pin at least one externally-published known answer

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

### assert-the-discriminating-negative

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

**Example.** Assert the file that must **NOT** exist does not exist; assert the bytes that must
**NOT** be written are absent. The negative is often the discriminating half of the oracle.

…

### The coincidence oracle
*(ui-design session, 2026-08)*

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

count by measuring the whole source `dict`. They agreed only because that fixture's window happened
to be the same size as the dict. When the window bug was **fixed**, the test went red — and the red
looked exactly like a regression introduced by the fix.

…

the discriminating-check test. What is broken is not falsifiability, it is **referent**: the oracle
measures a different quantity that currently has the same value. This is a third failure mode
alongside the fixture (C-31) and the assertion.

…

where the dict and the window are provably different sizes. If you cannot construct such a fixture,
the two are not independently verified; you have one measurement written twice.

…

### Spec-side census rules (from §3)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

  it is a blocker. Cite the consumer's real **input type** before binding a producer to it — a
  report bound to a service that consumes a different type had to be withdrawn. (b05,06,08,12)
- **Cross-cutting contracts go stale on any edit.** A contract that spans artifacts is invalidated
  the moment any cited low-level requirement is edited — especially gate-decision field
  insertions. Re-derive it, don't trust the cached version. (b07,08,09)

---

## Phase 3 · Implementation — census, blast-radius & test hygiene

### C-53 · A rule that false-fails correct work is as expensive as one that passes wrong work

Automating a control feels like pure gain, so the failure mode nobody budgets for is the **false block**:
a checker scoped to the wrong unit, flagging artifacts that were correct all along. It is worse than a
missing check, because a checker that cries wolf gets routed around — and once people learn to ignore its
output, the checks that *were* sound go with it.

**Measured while writing this flow's own validator (2026-08-10.)** The template's rule reads: *a `test` or
`analysis` LLR owes an executed verification and a numeric pass threshold.* Implemented **line-scoped**, it
produced **44 blocks** across the historical corpus. Every one was false: the convention puts those two
fields on their own lines *beneath* the method label, so the rule was demanding that a whole requirement
block fit on one line. Re-scoped to the **requirement block**, and narrowed to `LLR` blocks — which is what
the rule actually says — the same corpus yields **14**, concentrated in the earliest batches, which genuinely
predate the rule. The defect was not the rule; it was the unit the rule was evaluated over.

Three habits that catch this before it ships:

- **Run a new rule over a corpus you believe is CORRECT.** A rule that lights up everywhere is far more
  likely to be mis-scoped than to have discovered a systemic defect. Assume the corpus is right until the
  rule proves otherwise, not the reverse.
- **Scope to the unit the convention uses** — block, section, file — not to the unit that is easiest to
  iterate. Line-scoping is the default temptation because a line is easy to loop over.
- **Pair every rule with a positive AND a negative control** (the RED and the GREEN fixture) and keep them
  in the tool itself, so the pair runs on every change to the checker. Sibling to C-40: *can it go RED?* is
  one question, and *does it stay GREEN on correct work?* is a different one. Passing only the first is how
  a false-failing rule ships looking rigorous.

**Corollary for any generated check:** the same reasoning applies to a probe written into a spec. A
predicate written from the requirement's *wording* rather than from the artifact's actual *shape* fails in
exactly this direction — see the C-35 rider on the emitted form.

### C-52 · The four conditions that make a fork safe — and the one that changes category

Splitting a batch into parallel lanes is not made safe by good intentions; it is made safe by four
conditions checked **before** forking. If one is missing you do not fork — because *(b) without a frozen
contract* is not parallelism, it is **a collision with a delay**: both lanes advance happily and discover
the conflict at integration, which is the most expensive moment to discover it.

1. **Frozen contract.** No shared interface is touched inside a lane. If one must change, the work returns
   to the trunk — that is the interface trigger, already in the family.
2. **Disjoint FILE sets, not just modules.** Two lanes may not edit the same file, not even different
   regions of it. Checkable against the module map and the plan, before forking.
3. **Crossed reverse census.** The shared-surface family is run per lane and shared *before* starting: a
   symbol lane A touches may carry tests lane B also touches. **This is the only check that structurally
   cannot be performed from inside a lane** — which is precisely why it gets forgotten.
4. **One owner of the trunk.** Requirements, traceability, backlog and spec are never written from a lane.
   Lanes propose; the trunk integrates. Two writers on the same index is how it rots.

**Reader: `V46`, flow rev69 — and it is the CROSSED census's reader too, which is a ruling and not a
convenience.** The four conditions are declared in the requirements document's `**Fork preconditions**`
field, in `req-template.md` §2.8 beside a four-row table, one row per condition with a verdict and its
executed evidence; `none — this batch runs one lane` is the legal empty and MUST be written, because an
absence declared is a declaration and an absence omitted is a gap. **The field lives on the TRUNK's
document by construction:** condition 3 is the one this entry says *structurally cannot be performed
from inside a lane*, so a lane's own increment packet cannot answer for it — `V43` reads the per-lane
`Reverse census` in each packet, `V46` reads the crossed one once, where the fork was decided.
**Measured 2026-09-10 over the 66 live `01-requirements.md` of the the origin project record: 17 carry lane/fork
language and 0 declare the block; the field reads 0 of 66.** ⚠ **rev68 routed six remaining crossed-census
mandate sites here undecided — whether they were this control's third condition or an obligation of their
own. Enumerated by CATEGORY, all six sit inside a fork** (`/dev-flow` PDR condition 3 and DDR review
bullet · `design-review-template.md` PDR row 8 and DDR row 3 · `phase-checklists.md` DDR row 3 · this
entry), **every one of them names the lanes as its subject**, not one states the obligation outside
these four, and two of the six sit under a heading that names the fork in so many words
(`design-review-template.md` §B and `/dev-flow` §DDR, both *"the JOIN point when the batch forked"*).
A separate rule would carry the same trigger, author and artifact
and differ only in its name, which is `C-50`. **So: condition 3, reader `V46`.** Severity NOTICE,
three-batch convention.

**And the condition that changes category under parallelism:** C-40 asks that the RED counterfactual be
captured *where no other session is reading*. With a single agent that was a precaution. **With N lanes it
is a correctness condition** — mutating the shared tree contaminates a neighbour's measurement, silently.
That is why each lane needs its own worktree: not convenience, **evidence isolation**.

What is deliberately *not* parallelised: the complete validation run (it is one, owned by the orchestrator —
stitched across lanes it stops being evidence), the close and the backlog (one writer), and the requirements
(defined before the fork; a lane needing them changed raises the refine edge back to the trunk).

**The honest economics:** a fork buys **wall-clock, not work**. The batch ends when the longest lane ends,
so two very unequal lanes buy almost nothing while the coordination overhead is paid in full. It pays when
the lanes are comparable and there are genuinely independent modules or layers.

### C-51 · Layer 0 — the unit that both existing layers look past

White-box tests sit over the low-level requirement; black-box acceptance sits over the user's story. Both
look *past* the unit, so a bug inside a single function is visible to neither — and it accumulates as debt
that a green two-layer suite cannot see.

**Layer 0 is additive: it replaces nothing.** Layer 0 says "the piece works", layer A says "the mechanism
satisfies the requirement", layer B says "the user gets the outcome".

**The threshold must be operable, or it degrades into taste.** Two criteria, either one sufficient, both
checkable before the test is written:

- **decision** — the unit has 2+ paths (`if`/`elif`/`for`/`while`/`except`/a conditional comprehension),
  i.e. **cyclomatic complexity ≥ 3**, measurable with a standard AST walk and nothing installed;
- **boundary** — the unit **transforms data crossing a declared module boundary**: parses, serialises,
  computes an offset, validates, converts. It applies even with a single path, because that is exactly
  where the invisible bugs live.

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

branchless functions. Without that exclusion list the rule silently becomes "test everything".

**Anti-theatre clause:** layer 0 is measured by **mutation**, never by line coverage. High coverage made of
vacuous assertions is the dominant defect of this entire catalog — adding a layer measured by coverage
would industrialise it.

**READER, since flow `rev70`: `V49`.** Until then this control was cited by nothing in the flow and
invoked **once** in the whole `the record` record, while `validation-template.md` minted `### Layer 0 — unit`
and `increment-template.md` gate row 3 named the obligation — a mandate with no reader, which is `C-58`.
`V49` reads the keyed `**Layer 0:**` roll-up in the ACTIVE batch's `04-validation.md` (NOTICE, `S1`): the
count of units that met either criterion and how many carry a named reddening mutation, or the legal empty
**`none — no unit met the decision or boundary criterion`**, which the exclusion list above is what makes
legitimate. Measured case-sensitively on 2026-09-10 before the rule was written: the FIELD absent in **65
of 65** validation records, the section heading present in **2**. ⚠ **What `V49` cannot do, and no
field-keyed rule can:** it reads whether the question was ANSWERED, never whether the count is true or the
mutation real — the anti-theatre clause above stays the reviewer's job.

**Rider — an arm over a HELPER is not an arm over the RULE; an arm over the CORE is not an arm
over the LOADER** *(batch-89 portable lesson 2, 2026-08-28; ruled onto this control at the `C-45`
sitting of 2026-09-11, `BRIEF-7` row 5)*. Same blind-spot family, a different axis: the two layers
above look past the unit by **scope**, this rider looks past it by **call depth**. An arm that drives
the private helper a rule calls internally certifies the helper — the rule's own entry point, the
one a real gate invokes with its argument marshalling, its defaults and its guards, is never
executed. The same gap sits one level out between a core and the loader that resolves its inputs, and
a suite full of helper-level arms reports a coverage it does not have. **No cheap mechanical check
exists, and that is measured rather than assumed:** telling *the arm calls the helper* from *the arm
calls the rule* per registered arm needs a per-arm call graph — this control's own uncharted
territory, and the reason the sitting ruled a rider rather than a rule. **The authoring question is
which SYMBOL the arm names**, and it is answered by reading the arm, never by running it: a
helper-level arm and a rule-level arm are both green.

### C-50 · One home per artifact — and the link crosses by ID, never by content

Once a flow produces both *code-bound* artifacts (requirements, tests, traceability) and *deliberation*
artifacts (design proposals, review records), the pull to store them in different places is correct:
one kind must be readable by mechanical checks, the other is read by humans to decide. **The dividing
line is exactly that: if a mechanical check needs to READ it, it goes in the repo; if a human reads it
to decide, it goes in the document store.** A useful side-effect is that the automation frontier stops
needing an argument per control — it is decided by the artifact's home.

The split rots in two specific ways, and both are cheap to prevent:

- **Copying instead of routing.** Two copies means one is false and nobody knows which. This is not
  hypothetical: it is exactly how a canonical backlog went ~10 batches stale while every phase kept
  reading it. **And this invariant is STRUCTURAL, so no assertion over output can guard it**
  *(b84)*: collapsing two copies of a predicate into one call site is behaviour-preserving **by
  construction** — the two expressions agree on every possible input, which is exactly why the
  duplication was invisible. Restore the copy and every behavioural test stays green. Guard it by
  **parsing the artifact and asserting the shape** (the predicate is called from exactly the one
  function that owns it), never by comparing what the two produce. An adversarial review proposed a
  printed-output assertion for precisely this; **it was written, executed, and stayed green** — a
  reviewer's remedy is a hypothesis, and C-43 already says a hypothesis is not verified by having
  been written down. **One home per artifact, declared in configuration, and no command may write a path that
  is not declared there** — if something needs a new location, it is declared first.
- **Linking by content instead of by id.** The requirement in the repo cites `PDR-<batch>#D3`; the record
  in the store cites `R-014 v3`. **The ids are the glue.** Without them, separating the homes destroys
  the traceability the separation was supposed to organise.

**And the rule that keeps the deliberation store from becoming a shadow source of truth: what decides
code lands in the repo.** A design decision that fixes an interface is reflected in the requirement or
in the module map, both versioned beside the code. The store keeps the deliberation; the repo keeps the
commitment.

**State the cost rather than discovering it.** A record in a document store has no diff, no PR, no CI,
and cannot be grepped from a hook. Compensate by **sealing** it (date · verdict · participants · approved
ids) and citing it by id; a change after the seal is a new version with a new id, so the requirement that
cited the old one keeps pointing at the old one — which is the signal you want. What is *not* compensated:
no CI will ever verify a design record. That is a real boundary, and naming it is what keeps it from
being mistaken for an oversight later.

### C-49 · Forward applicability — every output of a design review must be someone's declared input

Adding a design phase is the easiest way to add cost that *looks* like rigour. The failure mode is not
that the review is skipped; it is that it produces a document nobody downstream ever opens, and nobody
notices because a thick artifact reads as diligence.

**The rule, distilled from ISO/IEC/IEEE 15288.** The standard separates *Architecture Definition* from
*Design Definition*, and defines the latter's outputs as **"design characteristics and design enablers
necessary for implementation"**, traceable to the architecture. Necessary *for implementation* — that is
the whole test. So: **everything a design review produces must be NAMED as the input of a later
activity. If an artifact is nobody's input, it does not belong in the review.**

Make it an artifact, not an intention: the proposal carries a **forward-applicability table** — one row
per output, with its named consumer and where that consumer will read it. **A row with an empty consumer
column means delete the output or justify it.** Without the table the rule degrades into "we thought
about it", which is this project's oldest failure mode.

**The corollary that answers "how big should a design review be?"** A review may legitimately cost half
the batch *provided that half is the literal input of the other half*. Cost is not the measure; consumption
is. And it is measurable: at close, count how many of the review's outputs were actually consumed. If the
answer is low, the review is mis-defined — and you learn it by measurement rather than by feeling.

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

**READER, since flow `rev77`: `V52`.** For seventy revisions this control was cited by NO rule while being realised in FOUR places — the design-proposal template §7, the design-review gate row 3, `phase-checklists.md` row 3 and `/dev-flow` §THE FORWARD-APPLICABILITY RULE — which is `C-58`’s mandate-with-no-reader at four sites at once. Measured read-only over the whole record before the rule was written: **0 of 949** files contain the string at all, against **109** design/review artifacts that were each subject to it — zero filled tables across 67 batches, and the sweep was shown discriminating first (a positive control returned 12 files, a planted near-spelling 0). `V52` reads the staged design proposal(s) of the ACTIVE batch (NOTICE, `S1`) and asks TWO questions, because the shipped template PRE-FILLS the consumer column and a reader keyed on this entry’s literal sentence alone would pass the untouched template: every row must NAME a consumer, and at least one row must say WHERE that consumer will read the output. It is scoped by `stations_active` naming `PDR`, never by mode — a batch that owes no design proposal is a SKIP with its reason (`C-53`). ⚠ **What it cannot do:** it reads the LOCAL STAGING under `.dev-flow/<batch_id>/design/`, because the sealed vault copy is out of every rule’s reach; and it reads whether the rows were ANSWERED, never whether the named consumer consumes anything — the corollary above, counting at close how many outputs were really consumed, stays a human measurement.

### C-48 · A trigger's NON-activation is evidence, and is recorded with its probe

Once rigour is decided by triggers — conditions verifiable before code, each with an executable probe —
the tempting failure is to record only the ones that fired. **Do not.** `"B1 did not fire"` with no
probe output beside it is textually indistinguishable from `"B1 was never evaluated"`, and the second
is what actually happens under time pressure. Record **id · verdict · probe output** for every trigger,
fired or not.

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

**The reader is `V43`, from flow rev68, and until then this control's largest instance was a
paragraph.** The increment packet's `### Reverse census` section is where the family-B probes are
recorded for the touched-symbol census `C-26` mandates, and it is where the ones that did NOT fire
belong. Measured 2026-09-10 over `<project>/.dev-flow/**` — 246 packets, 949 `.md` files —
**case-SENSITIVELY, because the reader is** (planted control `zzreversecensus` = 0 files; positive
control `Reverse census` = 14 of the 949): the keyed ROW is absent from **246 of 246** packets and the
`### Reverse census` heading is present in **2**, none of them in the active batch. ⚠ A first draft of
this paragraph published 7 / 239 / 46, every one of them measured with `.lower()` on both sides and
`re.I`, against a rule whose pattern carries neither — the independent review caught it, and the
numbers above are the re-run. `V43` reads the keyed
`**Reverse census**` row of the active batch's packets, NOTICE, and accepts the declared empty
`none — this increment touches no code symbol or shared surface`. It is keyed on the FIELD and never on
the row number: the sibling obligation in the same checklist sits at row 4 in **nine** packets and at
**row 3 in five**, across checklists shipped at four different lengths, so the ordinal is a spelling
this corpus actually varies.

### C-47 · The increment budget counts SOURCE files, not the total

**A cap on the TOTAL files per increment measures the wrong variable, and the direction of the error
is the expensive one: it penalises writing tests.** Under a flat "≤5 files", an increment of 3 source
+ 3 tests — well-cut, well-covered, with its AT and its TCs — is a violation, while 5 source + 0 tests
complies. The cap was invented to bound the *blast radius of the code change*; counting tests inside it
inverts the incentive precisely where you least want it inverted.

**The rule.** Cap **SOURCE** files (default: ≤4). Leave tests **uncapped** — each still has to map to

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

artifacts outside the count. **Do not add a total ceiling to compensate**: any total cap re-introduces
the defect. Reaching the cap is a **⚠ notice** (declare why the increment could not be cut smaller),
not a block; exceeding it is declared and reviewed, not auto-rejected — auto-blocking teaches people
to route around the rule instead of discussing it.

…

**Two honest limits, stated because the number will be quoted.** (i) It is ONE project — a Python the terminal UI
with a frozen engine; a backend with migrations or a component-heavy frontend will have a different
shape. (ii) Increments that were cut *in order not to break the old cap* do not appear as breaches:

…

### C-14 · A move OR a correction greps its whole population (census the readers, and the claims)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

**Failure closed — the extension, and why the old trigger could not close it.** *A correction has a
population, and until 2026-09-06 nothing in this flow enumerated it.* Batch-88 landed **8+**
corrections at one site of several — a pip-warning refinement that had 2 sites and landed at 1,
leaving *the site the gate reads*; an `EDITS` disambiguation with 5 sites landed at 1; an
operator-ruled guard line while 4 further documents kept quoting the old one; an ambiguous
"exactly 5 changed lines" threshold corrected in all five **only after an independent review named
them**. **Every one of them was found by a lens and none by a rule.** `C-14`'s trigger was *a path
MOVE*, and a corrected sentence is not a path move — **so this control fired on none of them**, which
is why the trigger is widened rather than a new control minted. Its sibling, the §3 census bullet
below, had been in this catalog since batches 09-10 and produced the same nil.

…

every reader of that artifact; **count a net-zero in-place rewrite as a touched file** that must
be re-verified, not as untouched. And: you correct a sentence a design review quotes. Enumerate every
artifact asserting that claim — **by the assertion category, not by the marker** — before editing the
first one. Measured at flow rev57: a marker-keyed census said 65 sites in 3 files; the population was
**72 in 6**, and 11 of the extra carried no marker at all, 2 of them in a file whose marker count was
zero. **A census keyed on a marker cannot see what carries no marker.**

…

the first site is edited**, and record the method with the count; net-0 in-place rewrites still count
as touched, and sites left unedited are named with their reason. The `P4`
supersession-completeness inspection is this census's executed form and **moved to `P3` at flow rev60**
for the same reason: run after every site is edited, it measures damage rather than risk.

**Why a FIELD and not a phrase.** Sweeping `.dev-flow/**.md` on 2026-09-06 for the enumeration marker
returned **19 sites and 19 distinct phrasings** — *"THE POPULATION WAS ENUMERATED BEFORE ANY REPAIR
WAS PROPOSED"*, *"population enumerated at 6 sites before any repair was proposed"*, *"Population
enumerated first"*, *"population is enumerated rather than merely swept"*, and fifteen more. **The
flow's own best instance of this rule has a population of nineteen and no two members agree**, so a
rule grepping any one of them catches 1 of 19. `V32` therefore reads the declared
`**Correction population**` field and never a sentence. *The defect regenerating inside its own remedy
is the strongest argument this corpus offers for a machine-readable field.*

**SECOND READER, since flow `rev78`: `V53`, and it reads the CLAIMS limb rather than the readers
limb.** A correction's population is not only the files that must change — it is every SENTENCE that
cites the thing being moved, and a citation is a claim that can be executed. The exhibit: one batch
replaced six stale `file.py:NNN` citations with symbol names; **five named the wrong symbol and one
named a symbol that had never existed in the repository**, while the comment carrying it read *"surface
fact, verified against …"*. The root cause is mechanical and reproducible — the anchors were derived by
taking the nearest preceding `def` to each stale line number, which is *guaranteed* wrong precisely
when the line number is the thing that drifted. ⚠ **And the replacement is worse than what it replaced:**
a stale LINE number fails visibly (the reader lands past end-of-file or on obvious nonsense), while a
wrong SYMBOL lands them inside a real, plausible method. **Temporarily wrong becomes permanently
wrong.** `V53` resolves every `path::symbol` anchor in `.dev-flow/**/*.md` against the working tree —
the file must exist and the symbol must be BOUND in it, by an AST binding walk for Python and a
word-boundary search otherwise, with every finding naming the resolver it used. It shares that
resolver with `V14` rather than minting a second one (`C-50`), and the adoption was measured before it
landed: over the record `V14` resolves 251 declared consumers, 95 carrying a `::symbol`, and **0
verdicts change**. **Severity is split by corpus, and the split is the design:** a wrong anchor in the
ACTIVE batch is a BLOCK — a false assertion at the station that wrote it — while the CLOSED record is a
census, a count and never a block, because those batches are sealed and re-anchoring them to satisfy a
rule written afterwards is editing the past. ⚠ **Line anchors are deliberately OUT and that is the
ruling, not an omission:** of 9079 in the record only 1815 resolve unambiguously and **0 of those 1815**
point past their file's end, which is the weakest possible staleness test — a line can be in range and
still wrong, so the check cannot be written honestly. ⚠ **What `V53` cannot do:** it asserts the symbol
is bound in the file, never that the sentence around the anchor is true about it.

### Census & blast-radius principles (§3)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

  category** (what kind of thing must be true everywhere), not on a frozen list of sites. (b09,10)
  **This bullet is `C-14`'s rule stated without a trigger, and for fifteen batches that is exactly
  what it cost** — batch-88 produced 8+ instances of the failure it describes while it sat green in
  the index. It now has a trigger and a rule: see `C-14` (widened 2026-09-06) and `V32`.

…

### Test hygiene & environment (§5)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

- **Signed-balance test ledger:** `post = base - D + A` on **collected** counts, where: `base` =
  test count before the change; `D` = tests deleted; `A` = tests added; `post` = the count you
  should observe after. A constant offset between expected and observed post-count is the
  signature of a units bug — a passed-vs-collected mismatch in the corpus was missed by exactly
  32. (b07-12)

…

  the lint became decorative. Pre-provision the toolchain as a hard entry gate; a recommendation
  that recurs unactioned across batches (ruff absent 3 batches running) is itself a process
  failure. (b32,02,03,04)

…

  transcodes what the child process prints, and one non-cp1252 byte can destroy a whole run's
  evidence. **The transcript IS the deliverable** — `C-25` requires one complete run owned by the
  orchestrator, and a corrupted transcript voids it whatever the exit code says, which is the failure
  mode no rule-level check can see (`C-57`'s own rev60 exhibit, one layer out). Invoke the
  interpreter directly — `<env>/python.exe -m pytest` — with `PYTHONIOENCODING=utf-8` set.
  **This is `C-19`'s family** (*test-run evidence discipline*, batch-35), and it is written HERE
  rather than under that origin heading because `C-19` exists in this catalog only as a `####`
  provenance stub and **a parenthetical may carry provenance, never a definition** (§*Writing
  canon*). Ruled at the `C-45` sitting of 2026-09-11, `BRIEF-7` row 8, **global half**; the project
  half — naming the working invocation in that project's own rules doc — is stack-specific by
  `C-45`'s placement test and is chartered to `the record` batch-91. **Both homes measured EMPTY on the
  day of the sitting** — **eighteen days** after the lesson was written, not the seven weeks
  `BRIEF-7` carried. (b87 `G4-03`)

---

## Phase 4 · Validation & gates — evidence that cannot be faked

A gate is only as good as the evidence it reads, and the most common failure is a gate that passes
on an **empty** or **fabricated** artifact.

### C-18 · Every acceptance test = exactly ONE distinct on-disk node driving the full chain

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

that drives the full chain the criterion describes. If you cannot point to that single node, the
criterion is **UNREALIZED**, no matter how green the neighborhood looks.

…

### C-25 · Gate evidence = one complete run owned by the orchestrator

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

### C-32 · Assert-the-painted-result

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

### freeze-then-measure — a figure is admissible only if it names what it measured

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

fold changes the text, each arm figure was measured against that text, so the next fold invalidates the
last one's numbers without anyone noticing. One batch burned **three requirement iterations** to its
soft cap this way, and the tell was an acceptance measured against an **890 B** body that shipped at
**1 975 B** — with one of its published mutations *impossible* against the shipping bytes.

…

measure **once** against the frozen bytes, and make it normative that **a figure is admissible only if
it names the block hash it was measured against.** That is what converts "measured against what
shipped" from an assertion into a checkable claim.

**The ceiling, found by the batch that introduced the mechanism.** A false, self-contradictory count
survived every gate **because its block matched its frozen hash**:

…

Freeze protects against *drift*, never against *content*. Pair it with a reader who checks the claim.

### C-66 · Flaky is a CLASS with a measured rate, never a name on a list

*(minted at flow rev75 from the operator's `C-45` sitting of 2026-09-11, `BRIEF-7` row 9. Origin:
batch-87 `01b-qa-validation-plan.md` §7, gate `G4-01`, 2026-08-24 — written, never encoded,
and still landing in neither of its declared homes **eighteen days** later. `BRIEF-7` said *seven
weeks* here and at two sibling sites; **none of the three re-derives**, and each is corrected where
it stands.)*

**Failure closed.** A node fails at the gate. Somebody writes *pre-existing* or *flaky* beside it and
the gate passes. **Neither word is a measurement**, and the disposition they support cannot be
falsified: a genuine regression introduced by the increment under review is indistinguishable, at the
gate, from a node that has always been unstable — they produce the identical red line. The failure
this closes is not the flaky node; it is **the sentence that disposes of it**.

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

runs.** Three parts, all three required, and the third is what makes the first two checkable:

1. **An empty source-scope diff.** The node's subject is untouched by the increment. Without this
   the other two measure the wrong tree.
2. **N ≥ 10 isolated reruns on that same base**, with the observed failure a member of a
   **recorded family** — a named signature, not “looks like the other one”.

…

**The class is published as an EXECUTED OUTPUT and never as a hand list** — the run list, the N,
and the node ids **the runs themselves produced**. A pre-registered whitelist of “known flaky”
ids is the defect this control exists to refuse: it is a claim about the past asserted over the
present, and it survives every run because nothing re-derives it.

**Exhibit — the record's own pre-existing family, and the figures are why the criterion has to be an
execution, and every figure is cited to where it is written.** **(i) The class, re-measured —
`<project>/.dev-flow/BACKLOG-CODE.md`, item `flaky-family-preexisting`, opened 2026-09-03**, which
*amends* batch-87's carry rather than rivalling it: three runs of the same base gave **6 / 10 / 6**
failures, **a union of 18** node ids of which **17 are non-reproducible**, and **a combined
population of 23** with the carry's eleven. ⚠ **Read *non-reproducible* as *did not appear in all
three runs*, which is the only reading the arithmetic admits** — 6+10+6 = 22 observations over 18
nodes leaves 4 duplicates, so 17 nodes appearing exactly once would put five appearances of one node
into three runs. The record's phrase is kept verbatim and the ambiguity is named rather than silently
resolved, because *did not recur* means *appeared once* three sentences below. **(ii) And the
machinery caught its own prior batch's vacuous check** — batch-87 `04-validation.md`, gap `G4-01`: of six PRE-REGISTERED
“known flaky” nodes, **5 did not recur at all**, while **5 of the 6 nodes that actually
failed were off the list**. A whitelist with a 1-in-6 hit rate had been clearing gates — which is
`C-31`'s input-set-as-oracle, committed against a population that moves — under a disposition rule of **n = 1, with the
verdict recorded as the word “passes”**, which is the sentence this control exists to refuse.
⚠ **One clause of the first cut is DROPPED rather than softened:** it said four batches had
described this family with four different figures, and a sweep of both backlog lanes sources **two**
descriptions — the carry's eleven and this pass's 18/23 — not four.

**What it costs, stated so the rule is a decision and not a wish.** N ≥ 10 isolated reruns is real
wall-clock time at the moment a batch most wants to close, and a rule that false-fails correct work
is as expensive as one that passes wrong work (`C-53`). **The compensation is that the cost is
bounded and the alternative is not:** ten reruns are ten reruns, while an unfalsifiable disposition
costs one escaped regression at an unknown date. Where N reruns cannot be afforded, the honest output
is **not** *flaky* — it is `blocked` or `not-run` with the reason, per the flow's evidence-state
vocabulary.

**No rule reads this, and that is the sitting's ruling rather than an omission.** The criterion is
executed by whoever triages the gate; a validator can see neither the reruns nor the base. What a
mechanism CAN hold is the published output's SHAPE — run list, N, node ids — and that is the
arm this control would take if it is ever built, named here so the entry is not cited as if it
existed (`C-62`'s posture, `C-58`'s warning). ⚠ **And the reader is not the only thing missing — the
OUTPUT this control mandates has NO DECLARED HOME either, which is worse and is said rather than
left to be discovered.** `increment-template.md` and `validation-template.md` carry no field for a
flaky-class disposition and no gate row names one, so an author who WANTS to discharge this has
nowhere to write the run list, the N or the node ids. Compare `C-59`, which arrived at rev66 with
**both** its template section (`Evidence files`) and its reader (`V41`); this entry arrives with
**neither**. **The field is owed by the next revision that opens either template** — an unread
field is still a home, and a control whose output has nowhere to land is a paragraph twice over.

⚠ **THE HISTORICAL RE-MEASUREMENT IS NOT DONE, AND IT IS NOT THIS CATALOG'S TO DO.** Whether the
N ≥ 10 / class-membership criterion would have changed batch-87's own `G4-01` disposition
is **asserted by that batch's record and has never been re-derived** — `BRIEF-7` named this as one
of the five things it could not measure. It is chartered as **`the record` batch-91**, CODE lane. Until
it runs, the exhibit above is evidence that the class EXISTS and moves, not evidence that this
criterion would have caught anything in particular.

### Gates & evidence rules (§4)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

  observe GREEN. For **net-new files** use **move-aside**, never `git stash` — untracked files
  stash nothing, and a bare `pop` can resurrect a parked stash into a conflict. (b15,35)

…

  approval. A gate decision must be idempotent under retry. (b12)
- **Re-reconcile after any gate amendment.** When acceptance tests change (13→17 adopted
  unchanged), the increment cut must be re-derived, or you get an unrealized pair. (b35,36)

…

  symbol — at each increment gate. A narrow `-k` filter in the corpus missed a crash, a 35-second
  perf cliff, and a sibling-file census, all at once. (b28,37,38,46)

---

## Cross-phase · Multi-agent orchestration (§6)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

  localizes defects. A blocker caught in review is one iteration; the same defect caught
  mid-implementation is a reopened increment. (b01,05,06)

…

  was nearly killed on mis-attribution; a `.output` file can read 0 bytes while live. Verify by
  command line, and budget verification subagents against the tool budget. (b33,46,47,48)

…

**Fix ids with per-id SEMANTICS before dispatch, not just ranges.** One batch fixed id *ranges* before
dispatching two parallel lanes and declared the collision "removed by construction" — then both lanes
filled the same range with **different content**, and 9-10 of 12 ids bound to different observables.
Ranges are necessary and not sufficient. Assigning each id its *observable* before dispatch produced
**zero collisions** in the following batch, with the lanes converging independently.

**Brief a discharge audit against the SOURCE reviews, never against the fold's own amendment table.**
An amendment table is a container; a green amendment count cannot see what the fold dropped. Audited
against the sources, one fold was measured at **163 union items · 136 carried · 7 retired with reason ·
20 dropped silently** — and it had printed "Unchanged" twice where executed diffs showed change. The
same audit against the discharge matrix would have passed it.

**Never read and write the same artifact from two sessions at once.** Dispatching a reader and a writer
concurrently produced a phantom finding that would have blocked a gate on the claim that an entire fold
never landed — the reader had snapshotted the file mid-write. In one batch this recurred **five times**,
the last being an unrelated process rewriting a *shipped* file mid-review. Run mutations and
counterfactuals in an export or your own increment tree.

## Cross-phase · The security lens on "just text" (§7)

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

> surface."** The corpus's security defects did not arrive through obvious network or auth
> surfaces. They arrived through **text**: a feature that takes a new string and renders or
> persists it is an injection surface, even when it looks like "just a label." Run the security
> lens whenever a feature's shape is **"new string → rendered or stored surface,"** not only when
> it adds an external endpoint. (b19,24,27)

Concretely, in a terminal-UI corpus this meant that dynamic text flowing into a markup-parsing
render path (labels, option lists, status lines) was an injection/crash surface: an unescaped `[`
is parsed as a style tag and can crash the render or mis-style it. The generalization is
provider-agnostic — any "harmless" string that reaches a parser, a template, a shell, or a
persistence layer deserves the same review a network input gets. The category error is treating
**rendering** as safe because it is **local**.

---

## Cross-phase · C-44 — work that never landed

**Failure closed.** Work that is finished but **unlanded** is indistinguishable, to every later reader,
from work that was never done. Worse, the canonical state files are exactly what the next session reads
to orient itself — so an unlanded close-out makes the project's own state file **assert something
false**, which the next batch then inherits as a premise (**C-43**).

**Example — four instances surfaced inside ONE session, none of them a code defect.** (1) A completed,
pushed close-out branch that was never merged, leaving `state.json` on the main branch claiming a
finished batch was still mid-phase — which then misled the *next* batch at its intake gate, and cost
that batch a full re-orientation. (2) Two corrective items from a merge gate that closed
**CONDITIONALLY** — *"once items 1–5 land this is a MERGE"* — written, approved, and never applied,
**while the batch merged anyway**: the conditional verdict was consumed as an unconditional one.
(3) An abandoned uncommitted edit in an auxiliary skills repo — the unfinished last step of that same
close-out, containing a whole encoded control that was therefore invisible to everyone. (4) Two
uncommitted global command files, found only because a later session happened to open them.

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

created or modified into exactly one terminal state, and **say which**: ✅ **committed** *and, where the
work only matters once integrated, landed* (**a commit that never lands is not a terminal state**) ·
🗑️ **reverted or deleted, deliberately** · 📋 **left in place ON PURPOSE, with its path and remaining
work written into the canonical backlog**.

**Discharge — mechanical, never from memory.** `git status --short` in **every repository the session
touched, auxiliary repos outside the project tree included** (skills / commands / config are where this
hides); an unpushed-commit check (`git log @{u}..HEAD`); and, for any branch other work depends on,
confirm an open PR actually exists. **Report pre-existing uncommitted changes as FOUND rather than
sweeping them up** — committing another session's work in progress is its own defect, and in a shared
config repo it is the likely default.

…

**RIDER — characterise VCS state from REFS, never from the working tree.** *(folded in at flow rev71
under `Q23` as a rider on this control rather than as `C-64`: it is the measurement this control
already depends on, and the discharge above is unperformable without it.)* Before stating what is
committed, inspect **refs**: `git log --all --oneline`, `git branch -a -vv`, `git worktree list`, and
`git fetch` **first**. *A dirty working tree is fully compatible with the identical content being
committed, pushed and merged elsewhere.* The tree describes one checkout; refs describe the
repository. **Two exhibits, and the second is this catalog's own house.** (i) An external session
reported *"the rewrite was never committed — it is sitting uncommitted in the working tree"* and
recommended committing or discarding on that basis; the content was in fact a commit on a branch that
was pushed, checked out in a separate worktree, and **merged upstream as PR #1 while the session was
running**. A later push was correctly rejected, which is the only reason the wrong conclusion
surfaced before anyone acted on it. (ii) A flow session called a dirty `REFERENCE.md` *"another
session's"* **twice, from `git status` alone**, and the operator corrected it — re-measured from refs,
the file is indeed modified in the `agent-skills` working tree while `main` equals `origin/main`,
**which is precisely the state that says nothing about what is committed**. When content appears both
as working-tree modifications and as a commit, compare **tree objects** (`git rev-parse <ref>:<path>`)
and **normalise line endings before any content comparison** — a naïve md5 pass over one such corpus
reported all eight files different and every difference was CRLF, which is `C-59`'s exhibit 1 arriving
through a diagnostic instead of through a store.

## Cross-phase · C-45 — the flow is a shared asset, and changes flow BOTH ways

**Failure closed.** Controls are discovered inside one project but are **not that project's property**.
Encoded locally, a control is active for exactly one operator and invisible to everyone else — so every
other project re-learns the same lesson at full price. The mirror failure is quieter: a batch that runs
a **stale** flow **inherits a solved problem as an open one**, and has no way to notice.

**PUSH — a portable control is not encoded until it lands upstream.** Four parts, and a batch owes all
four before it closes: the **command** (the rule) · its **artifact** (a template section — *a control
with no output degrades to "I thought about it"*, this catalog's oldest meta-rule) · the **catalog**
entry (here, with the measured origin) · **committed and pushed**, SHAs recorded at the close. Per
**C-44**, an unpushed control is indistinguishable from one never written. **Say which of the four
landed** — command-but-not-template is *half-encoded*, and the missing half is the enforceable half.

**PULL — verify flow currency at Phase 0, beside RC-1.** RC-1 asserts your branch is current against
`origin/main`; this asserts the **flow itself** is. Make it mechanical rather than well-intentioned:
publish a manifest with a version, a per-file SHA256 and an aggregate hash, and re-derive the aggregate
locally in one command. A mismatch is either uncommitted local work (push it) or staleness (pull it) —
the per-file rows say which. **Record the flow revision next to the RC-1 line: a batch that cannot
state its flow revision cannot claim its controls were current.**

**Placement is still decided by portability, not convenience.** Portable principle → the global flow;
stack-specific mechanics (UI framework, snapshot tooling, frozen-file set) → the project's own rules
doc. A stack-specific rule pushed upstream pollutes every other project; a portable one kept local is a
lesson paid for once and used once.

**The manifest has its own failure mode, so name it:** a stale manifest is worse than none, because it
reports a mismatch as drift when the real defect is that nobody re-hashed. **Whoever edits a flow file
owns the bump**, and the manifest is written **last, over final content** — hashing before the last
edit publishes a hash of something that no longer exists.

**From flow rev71 the close artifact declares how many controls the batch minted, as a keyed field
`V51` reads.** The four landings above say WHERE each one went; nothing counted them, which is how
this project reached **four consecutive batches at zero catalog entries, and then a fifth**, before
anybody wrote the number down — the debt was visible only to a human opening every close artifact in
the record one at a time. ⚠ **The reader is not an approval:** whether a lesson deserves to be minted is the operator's
sitting under the project's own control-encode rule. What the field removes is the condition that let
the debt go UNCOUNTED between sittings.

**Rider — LEARNING a lesson and ENCODING it are different acts** *(batch-89 portable lesson 3,
2026-08-28; ruled onto this control at the `C-45` sitting of 2026-09-11, `BRIEF-7` row 6 — stated
once, at the control whose four-part landing table exists to close it)*. The catalog can hold a trap
and the flow can ship it anyway, because a lesson READ is not a lesson ENFORCED. **One clean, dated,
re-measured exhibit:** the `python3` trap entered this catalog on **2026-08-18** (`5e6dc00`,
verified by `git log -S python3` in the skills repo), and the flow shipped `python3` regardless,
with **`V17` certifying a guard that had never run** on **2026-08-29/31** — **eleven days after
the catalog already carried the trap** — and closing it cost `V17`'s rewrite plus five flow
revisions, rev49 through rev53. **A commit that touches the catalog is not a control-encode**, and
reading a landing row as *paid* because a SHA now exists is this rider's own failure mode one
register up. The four cells above are what make the difference visible; **this rider is why they are
four and not one.**

## Cross-phase · C-62 — a rewrite converts prescriptions into permissions

*(corpus: an agent-authored rewrite of a skill, 2026-09-08, outside the record — the SPEC layer, and
the one genuinely new AXIS of the five candidates `Q23` ruled on; minted at flow rev71)*

**Failure closed.** Erosion of an artifact's **quality pressure** during a structural rewrite that is,
on every other axis, a genuine improvement. **The improvement is what makes it pass review.** Every
other control here is about a check that cannot fail; this is about a *requirement* quietly ceasing to
be one, in a diff that reviewers score as good work — and they score it as good work because it is.

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

1. **Review a rewrite along two independent axes: structure and enforcement.** A gain on one does not
   license a loss on the other, and reviewers reliably score the visible axis.

…

   *Prose length is not the metric; enforcement density is.*
3. **Validate a restored control by running it against output the weakened version already produced.**
   If everything passes, the restoration is decorative. In the origin corpus all four restored checks
   **failed** the existing artifact, forcing a redesign that then passed — and that failure is the
   evidence the restoration was real.

**Example.** A skill — the spec layer governing an agent's output — went from **552 lines to 54** plus
progressive-disclosure references. The architecture genuinely improved: on-demand loading, separated
semantic colour channels, new epistemic discipline. In the same change, **five controls were deleted**:

…

|---|---|

…

**The tell is hedge phrases** — *"do not automatically require"*, *"is a choice, not a quality
criterion"*, *"a starting point, not a universal requirement"*. Each one removes a constraint the
executor would otherwise have had to satisfy. The output degraded accordingly and passed self-review.

**And this flow did the same thing and did not measure it — which is the in-house exhibit and it is a
GAP, not a success.** Flow rev57 performed exactly this kind of extraction: narrative share fell
**26,046 → 3,974 chars** across six normative files, every moved origin story was verified to keep a
resolvable tag, and **no imperative was counted at either end**. The rewrite was checked for what it
MOVED and never for what it stopped REQUIRING. Measured at flow rev70, the words *enforcement density*
and any MUST-census occurred in `docs/`, `commands/` and `templates/` exactly **once** — inside the
handoff proposing this control.

**Mechanism — NAMED AS A CANDIDATE AND NOT BUILT, so nobody reads this entry as discharged.** A
derived per-file count of MUST / required / BLOCK tokens per manifest revision, reported as a **delta**
beside `flow_hash`. It is cheap (the manifest already walks the file set in table order) and it is
unbuilt at rev71; until it exists, limb 2 is performed by a reader, and a limb performed by a reader
is the thing `C-58` warns about. Stated here rather than in a backlog so the entry cannot be cited as
if the instrument existed.

> ⚠ **`C-63` AND `C-64` ARE SKIPPED ON PURPOSE, AND THE SKIP IS MEASURED RATHER THAN
> STYLISTIC.** The next free number after `C-62` is 63, and rev75 mints **65** and **66** instead.
> Both 63 and 64 were spent as PROSE on **2026-09-11** by rev71's `Q23` ruling over an outside
> five-candidate corpus — `C-63` there names a FOLD into `C-57`, `C-64` a RIDER on `C-44` —
> and that prose is live **in five files, counted by PARAGRAPH so the unit cannot drift**: this
> catalog's `C-44` entry **1** · `docs/FLOW-VERSION.md`'s rev71 changelog row **1** ·
> `<project>/.dev-flow/BACKLOG-PROCESS.md` **4** · `<project>/.dev-flow/BACKLOG-CODE.md` **2** ·
> `<project>/.dev-flow/design/HANDOFF-devflow-session-2026-09-03-CONSOLIDATED-PLAN.md` **1** —
> in the manifest the unit is a changelog ROW, tables having no paragraph breaks, and both ids
> sit in rev71's —
> **9 paragraphs, 7 of them in a repository this lane does not write.** ⚠ **The first count of
> this said *five sites in three files* and missed two files entirely; the second said *at least
> eight* against an enumeration that totalled nine.** Both wrong counts are recorded rather than
> replaced, because a census that only ever publishes its final figure teaches nobody how it went
> wrong — and each correction STRENGTHENED the conclusion. **Minting 63/64 here would give a reader following either
> id two destinations** — `C-50`'s defect committed in the id space itself. **And the prose
> cannot be reworded away:** seven of the nine paragraphs are in another repository this lane does
> not write, and of the two that are here one is a DATED changelog row — rewriting a changelog so a present census comes
> out even is editing the past to make the present measurable, the same argument that keeps
> batch-74's `06-closeout.md` outside `V50`'s population. The manifest's row already says *the origin project
> numbering space, gaps expected*; **this is the first gap that is a decision rather than an
> accident**, so it is written down. `CAT ID-GAP-63-64` holds both halves — the two ids stay out of
> the heading set, and their prose stays in — **for the two files this lane owns, and for those only.**
> The seven `the record` paragraphs are outside any mechanism here, deliberately and not by oversight: an arm
> in this repository that reddened on another repository's prose would be `C-60`'s shared-input
> defect and would fail on every checkout that lacks it.

## Cross-phase · C-65 — a ruling is applied as a CENSUS over its axis, never as the instance

*(minted at flow rev75 from the operator's `C-45` sitting of 2026-09-11, `BRIEF-7` row 3. The
candidate paragraph stood in `commands/dev-flow.md` under the heading *Candidate control*, **byte-identical
in the NINE commits of that file from rev65 to rev74** — rev70 is the only revision in the range
that does not touch it — opening every time with the words “⚠ NOT A CONTROL”. ⚠ **`BRIEF-7` read this as *seven revisions,
five weeks*: seven is right only if you stop at rev72, and FIVE WEEKS IS WRONG BY ABOUT A FACTOR OF
NINE** — the manifest dates rev65 **2026-09-07** and rev74 **2026-09-11**, **four days**, and the
commit that introduced the paragraph is dated 2026-09-10, one day before rev74. **The lesson
survives both corrections and is sharper for each: NINE revisions each read this paragraph, each
shipped, and none of them minted it** — what the exhibit measures is revisions, not patience. That
paragraph is now a pointer here and not a second copy, per `C-50`.)*

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

versioned content* · *no rule reads an ambient fact* · *every mandate has a reader* — and
it is discharged by fixing **the one instance the finding produced**. The fold is correct. The gate
is green, the battery passes, the report is true. **All of that is evidence about the instance and
none of it is evidence about the axis**, so the ruling has not been applied — it has been
converted into a promise that the next reviewer will find the next member.

…

enumerates the class and closes the set.** Enumeration means a declared population plus an arm that
compares the source to it — the shape `_ATLAS_READS`, `_RULE_COVERS`, `_SELECTORS` and the bundle
mapping already have. **The census is over the AXIS THE RULING NAMES, not over the axis the
instrument finds convenient:** a census that counts the wrong unit cannot see the defects it was
built for, and that is not a hypothetical — it is round 7 below.

**Exhibit 1 — rev65, and it cost SEVEN review rounds.** `Q18` was ruled on the axis. Each round
folded whichever read the previous review had just demonstrated:

| round | the instance closed | what remained |
|---|---|---|
| 1 | directory existence (`_ATLAS_MARKS`, the batch-row enumeration) | five content corpora |
| 4 | `_ifc_corpus`, `_atlas_id_scan`, `v13`'s reacher index | six rule-side reads |
| 5 | `v10`/`v11`/`v12`/`v14`/`v19`'s corpus reads, `_atlas_registry` | `v14`'s consumer resolution |
| 6 | `v14`'s `_exists` / `_contains` | *unknown — and that was the point* |
| 7 | the CENSUS itself — it counted read PRIMITIVES, so seven `_read` sites were one row and rounds 5–6's defects were invisible to it | nothing known; the census now counts SITES and pins its own vocabulary |

*(Rounds 2 and 3 are absent because they closed INSTRUMENT defects — an arm keyed on an ambient
fact, a rule that deadlocked its own gate — rather than `Q18` instances.)* Each fold was correct,
each was verified, and **none of them was the ruling**. Round 7 stopped answering instances and
enumerated the population. **rev65's mutation battery scored `claims_unmet 0` against a fold
covering three of six inputs**: the reviewer had to prove the gap in-process because nothing in the
flow could.

**Exhibit 2 — the pattern did not stop at rev65, and three later revisions shipped a per-instance
fold that the independent review caught — each named by the finding that caught it, not by
recollection.** rev66: the manifest's control count, hand-kept beside its own published derivation,
and the validator's own comment calls it *the one the independent review found still standing in the
file rev66 must edit anyway* · rev69, finding `M2`, quoted whole — ***the `T06` population was 3
and the catalog is a fourth***: the enumeration was real, was verified, and stopped one member
short, which is this control's failure in miniature · rev72 (`Q21`'s authorization precedence, where **the prose enumeration
and the arm's own declared set had disagreed on the day they shipped** — the prose named six sites
across three files, the arm four documents including this catalog; both correct, nothing holding
them together, which is `C-50` committed inside the sentence announcing the census). Three
revisions, three reviews, one shape.

**Exhibit 3 — rev74, and it is the sharpest of the three because THE CENSUS REFUTED THE RULING'S
OWN WORDING.** The `C-45` sitting ruled that the Atlas tokenizer must “exclude a bare trailing
`.` and a wildcard `*`”. Run as a census over the record's whole scan corpus — 1102 files,
30 166 accepted matches, grouped by the character following each match — refusing every
trailing `*` would refuse **1393** matches of which **1351 are markdown bold closings**, and
refusing every trailing `.` would refuse **1046** of which **377 are sentence-final**: the exact
`C-53` false-fail rev45 had already measured and declined, and one of them is asserted by a test in
another repository. **The literal ruling was wrong, and only enumerating the axis could say so.**
What the record actually holds is 84 family-marker sites, and those are what rev74 refused. **A
per-instance fold would have shipped the ruling as written.**

**THIS REV COMMITTED THIS CONTROL'S OWN DEFECT WHILE MINTING IT — TWICE — AND THE RECORD IS HERE
RATHER THAN TIDIED AWAY.** Renaming `commands/dev-flow.md` §*Candidate control* into this entry's
pointer left cross-references to the old heading standing; the first independent review found
eight of them, the second found a ninth the first fold had missed. **The axis was enumerated three
times and the first two enumerations were themselves the defect.** The first reported *69
citations, 8 of them the renamed heading*, from a regex over a prose citation form — a tightened
spelling of the same regex returned 68, and six plausible derivations over one corpus returned
**24, 27, 62, 88, 109 and 112**. **A census whose figure moves with the reader's pattern is a
census nobody can re-run**, which is this control committed inside the paragraph repairing the
first commission of it.

**So the predicate is a LITERAL and the corpus is DECLARED**, which is the only form in which
either figure is worth writing down. *Predicate:* the literal string `Candidate control`.
*Corpus:* the **34 files the manifest tables, plus `docs/FLOW-VERSION.md` itself** — 35 documents.
Before rev75 the string stood at **10 sites in 4 files**: the heading in `commands/dev-flow.md`
(1), and **nine citations** — `docs/tools/devflow-validate.py` **5**, `docs/FLOW-VERSION.md` **3**,
`docs/tools/devflow-mutants.json` **1**. **Six of the nine are FORWARD-POINTING rationale a future
author greps for, and are updated to cite `C-65` BY ID** (the five validator comments and the
registry's `r67-M19` `why`) — by id and not by section title, because an elided title
(`§*A ruling ... as a CENSUS*`) is precisely the un-findable cross-reference this census exists to
detect, and two of the six shipped that way in the first fold. **The remaining three are DATED
changelog rows and are deliberately FROZEN**, on the same argument the `C-63`/`C-64` note makes.
`BRIEF-7`'s own **3** further occurrences are OUT of corpus with their reason: `docs/analysis/` is
not tabled, and the brief is a dated verbatim investigation record — the changelog argument applied
to a second document class.

⚠ **Every figure above is measured at the COMMITTED pre-rev75 tree (`29da5f6`), not at the
working copy, and the third try is what taught that.** A census published over a corpus that
includes the document describing the census **counts itself**, so its figure moves with every edit
to the sentence reporting it — measured twice while this paragraph was being written, the same
predicate returned 7 and then 10 for one of the members below. **A self-counting figure is not
wrong, it is un-re-derivable**, and the repair is to name the tree rather than to subtract the
document.

**So: what this census does NOT close — and the FIRST answer to that question was this
control's own failure, for the third time in one entry.** ⚠ **And the predicate below carries two qualifiers that the first writing of it left
unstated — which, applied literally, is the difference between two members and about twenty-six**
(`§Verdict` 6, `§Restrictions` 4, `§P4` 3 and some twenty singletons, every one of them citing a
section of some OTHER document). So both are said: *a `§Name` cited **as a section of
`commands/dev-flow.md`**, matching no `#{1,4}` heading there, **an elided or truncated title counting
as a match***, over the same 35 documents at `29da5f6`:

| member | citations | headings | where |
|---|---|---|---|
| `§Severity` | **10** | 0 | validator 4 · registry 2 · manifest 4 |
| `§Independent review` | **2** | 0 | `templates/dev-flow/increment-template.md` §4b · this catalog's `code-reviewer-absent` exhibit — `C-58`'s finding, and the token stands in that SAME `C-58` origin note under `### From commands/dev-flow.md` — which is where a reader following this cell must look. *(Two rounds put a wrong id in this cell: first `C-58` alone, which sends a reader to the control's entry rather than to its origin note, then `C-45`, which names an ORIGIN note that does not exist — `C-45` has a control entry, but not one here. A locator is a claim and gets measured like one.)* |

Both name a **prose paragraph** and a **bullet** rather than headings; both are **pre-existing**,
both are now counted, and **neither is this rev's to mint**. Two edges, because a census
that hides them is the thing this entry is about.

**(i) Scoped strictly to citations that NAME the file they cite, the first row is 9 and not 10.**
Exactly ONE of the ten omits the filename, and it is not prose — it is the `FV SEVERITY-census`
expectation label printed by `--selftest`. *(An earlier writing of this footnote said TWO such
sites, "a validator comment and a manifest sentence": the second has no referent on the tree, and
the first is a print label rather than a comment. Both figures here are pinned to `29da5f6`, so
both stay true.)*

**(ii) Both rows GROW in this rev, because THIS ENTRY CITES THEM — and the size of the growth is
DELIBERATELY NOT PUBLISHED.** Two attempts at that number have now been wrong. The first published
a shipped-tree pair; re-measured, one of the two had already moved, **because the sentence
reporting the number is itself one of the citations the number counts** — and a replacement figure
would move again, for the same reason, the moment it was written here. That is the self-counting
trap for the fourth time in one entry, each time one layer deeper: in the census, in the correction
of the census, and twice in the disclosure written for the correction. **A figure that its own
report changes is not a figure.** The terminating move is the one already taken above — pin the
population to a named tree, and say in WORDS that the shipped tree is larger. That is everything a
reader needs, and all of it stays true.

⚠ **The figures first published here were 9 and 0, and they were produced by a predicate this
entry never declared.** The strict form `§Name` was silently used, which excludes the emphasized
spelling `§*Name*` — **and that is precisely the spelling this entry singles out two paragraphs
above as the dangerous one** (*an elided or emphasized title is the un-findable cross-reference this
census exists to detect*). Under the declared-inclusive predicate `§\*{0,2}Name`, `§Severity` is
10 and `§Independent review` is **2, not 0**. **So the sentence that stood here — *rev75
introduces `§Independent review`* — was false**: two members already stood, in two tabled
documents, one of which (`increment-template.md`) this diff does not touch at all. **And the
correction of the previous round was itself wrong**: round 2 measured 2 and was recorded here as
having miscounted rev75's own text. It had not. **Three enumerations of one axis, each stopping
short, each inside the entry that mints the rule against exactly that** — and what caught the
third was a reader re-running the predicate rather than reading the number. The sequence is kept
because a control whose own entry needed three passes to enumerate one small axis is making its
case better than any exhibit written from outside could.

**The arm shape, so the discharge is not left as an intention.** Where the population is declarable
in source, this control is performed mechanically and the flow already does it: a declared set
beside the code plus an arm comparing source to set, BOTH WAYS — `Q18 READS-census`,
`CMD AUTHORIZATION-precedence`, `FV SEVERITY-census`, `DOC-FAMILIES-both-ways`. **Both ways is the
load-bearing half:** a one-way arm catches a member dropped from the code and is blind to one
dropped from the declaration, which is the same per-instance fold one level up.

**What this control does NOT claim, said at the minting rather than discovered later.** It is **not
checkable by `devflow-validate.py`**, because the discharge is *did the fold enumerate the axis* and
a mechanism would have to understand the ruling's own subject to ask it. It is a **review-time
obligation**, so it carries no `V`-rule — and by `C-58`'s own argument that makes it exactly the
kind of paragraph that costs nothing to skip. **The compensation is named, not assumed:** the
discharge is a POPULATION IN THE DIFF, which a reviewer can see and a later arm can adopt. And the
honest reading of all three exhibits — five revisions between them — is that **every one was caught by the independent review and
none by a rule** — the reviewer is this control's instrument, which is precisely why rev75 also
writes down when the reviewer is dispatched (`commands/dev-flow.md` §*Independent review*).

## Implementation/Validation · C-46 — a hash-verified restore does not restore the CACHE

**Failure closed** (increment 22b, 2026-07-31). A mutation battery mutated
`range(0, 4)` → `range(0, 1)` — the **same byte count** — and restored the file within the same
second. Python keys a `.pyc` on (source mtime, source size); both matched, so `__pycache__` kept the
**mutant's** bytecode and the next full-suite run executed the mutant from a byte-identical working
tree: 13 tests red with no diff to explain them, one step from being misread as a real regression.
The md5-verified restore — this catalog's own discipline — was true and insufficient: it proves the
*source* is back, and the interpreter was not reading the source.

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

- Run mutation batteries under **`PYTHONDONTWRITEBYTECODE=1`** so the mutant never enters the cache.

…

  and re-run before diagnosing. (A locked cache dir — OneDrive, an open process — that refuses the
  purge is a finding to report, not to force.)

Portable by construction: any bytecode/artifact cache keyed on (mtime, size) has the same blind
spot — Python is merely where it was paid for.

## Phase 5 · Postmortem — honesty note, the scope of these claims (§8)

> **These are hard-won controls from ONE project's 54 batches — not universal law.** Every control
> here was observed, and earned, in a single supervised multi-agent development flow over 54
> post-mortems. They are **battle-tested inside that corpus**, and the failure modes they close are
> real and recurred. But a single-project observation is not a proven law: the frequencies (9
> vacuous checks in one batch, ~half of inferences wrong, 3-of-5 REDs mispredicted) are
> **evidence, not statistics**. Treat the catalog as a strong prior — a checklist worth defaulting
> to — and re-earn each control in your own context rather than importing it as gospel.

**What was deliberately excluded as too app-specific to teach.** Several lessons in the corpus
were too tied to one application to generalize honestly, so they are not in this catalog:
Intel-HEX byte-stability rules, a `variant_id` stem-collision, 1-based operator indices,
single-owner chip / duplicate-PR hygiene, and a `state.json` surgical-edit mojibake failure. Where
such a lesson had a generalizable moral, it was folded into the negative-oracle guidance
(reader-as-oracle, the discriminating negative) rather than shipped as its own control. Naming the
exclusions is part of the honesty: a catalog that claims to teach everything it saw is itself a
vacuous check.

When writing a new postmortem, also remember: **a recommendation that recurs unactioned across
batches is itself a process failure** (ruff absent 3 batches running, §5) — track whether prior
postmortem recommendations were actually adopted.

---

## Writing canon — a parenthetical may carry provenance, NEVER a definition

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

is normative and it is in the wrong place. Hoist it into the rule's own prose before anything moves.

**How it was earned, and the root cause is OURS.** rev57 moved every origin story out of the flow's
five normative files into this catalog. The extraction rule applied was mechanical and correct —
*a parenthetical tagged `(Origin: …)` is narrative; move it* — and at one site the result was
wrong anyway: the sentence *"A dependant is not only something that reads the value; it is anything
that would break if the address moved"* left **both** its normative homes, `commands/dev-flow.md`
and `templates/ifc-template.md`, and survived only here. That sentence is the SCOPE of the
`consumers` field, and **`V13` and `V14` parse that field against it.** Canon had buried a binding
definition inside an `(Origin: …)` parenthetical, so a right rule produced a wrong result.

**Three more sites in the same sweep were the same shape**, which is why this is a rule and not an
anecdote: the ≤4 source-file cap's derivation (*why 4, and why source-only*) sat inside its origin
parenthetical while the constant sat outside it — extract the parenthetical and the number survives
with no answer to the only question anyone asks of it; the `RC-S1` naming ruling sat inside the
audit story that explains why the audit happened; and the **misaddressed observable** definition sat
inside a batch-79 narrative in a template that *uses the term two dozen lines above it*.

…

---

---

## ORIGINAL CANDIDATES SECTION (pre-pruning, verbatim)

## ⏸ Candidates — observed, transcribed, NOT controls

**This section is minted at flow rev71 and it did not exist before, which is itself the finding.**
Until now a lesson was either encoded or lost: the only holding pen was a project backlog, and the
`C-45` escalation reached **four consecutive batches at zero** partly because there was nowhere in the
catalog for an unminted shape to sit and be counted. A candidate here is **not a control** — it is
cited by nothing, read by nothing, and owes an operator sitting under the control-encode rule before
it can be numbered.

⚠ **A number written beside a candidate is not a reservation.** The `C-55` candidate was declined and
the number was later minted for a *different* control (batch-84, *an emptiness is doing work*). So

> ↪ *Excerpts — the rule is in `SKILL.md` under this heading.*

⏸ **THE PEN IS OCCUPIED AGAIN FROM flow rev83, BY ONE SHAPE** — *a human review without a
record is indistinguishable from one that never happened*, transcribed the day it was observed
(2026-09-18) with its measurement attached and its reader already built. It is named by its shape
and carries no id, per this section's own rule. From rev75 to rev83 the pen was EMPTY, and an empty
pen is declared rather than deleted (`C-55` — *say which kind of emptiness*: that was **nothing
waiting**, never **nothing recorded**). The operator held the `C-45` sitting on **2026-09-11** over
`BRIEF-7`'s fourteen rows, and both shapes rev71 transcribed here were ruled and landed at flow
rev75:

| the shape rev71 transcribed | ruled | where it lives now |
|---|---|---|
| a mutation that removes a guard tests nothing — the one that tests a guard makes its SUBJECT wrong | FOLD | `C-40`, first of the two rev75 riders |
| a fix can be correct and held by nothing | RIDER | `C-58` |

**The section did its job, and the measurement of that is the dates**: both shapes were observed at
rev70, written here at rev71, and carried — *counted, citable, unminted* — for exactly one
sitting. Before it existed a lesson was either encoded or lost, and the `C-45` escalation reached
four consecutive batches at zero partly because there was nowhere for an unminted shape to sit.
**The rev83 entry is the rule working as designed**: the shape was observed, measured and
transcribed on the same day, and it sits here — counted, citable, unminted — until a sitting rules
on it. A new candidate goes here the day it is observed, not the day someone remembers it.

---

## Origins extracted at rev57

Origin stories, measured evidence and rejection rationales moved at **rev57** out of the **five**
flow files that carried them — `commands/dev-flow.md`, `commands/fast-dev-flow.md`,
`commands/dev-flow-sync.md`, `templates/req-template.md`, `templates/ifc-template.md` — plus the
single marker in `templates/validation-template.md` (proposal P3 of the 2026-09-01 standards
review). **The extraction landed at every file or it did not land at all:** a partial one leaves
two registers alive, which is the disease it was written to cure.

**Every binding sentence stayed in those files**, and where a parenthetical carried both a story
and a rule, the rule was rewritten in place as normative prose *before* the story moved — see
*A parenthetical may carry provenance, never a definition* above. Each site keeps a one-line
`(Origin: … — see dev-flow-lessons)` tag pointing here; one entry per control, origin text kept
intact.

### From `commands/dev-flow.md`

#### Backlog reconciliation — carry-over contract (2026-07-20 audit, extended 2026-07-28)

(Origin: 2026-07-20 operator audit — the canonical backlog had gone ~10 batches stale because no phase enforced the update, forcing repeated manual "what's the backlog?" re-asks. Extended 2026-07-28 after a lane split left this command naming a file that had become a router holding no open work.)

#### No gate passes an unfilled-template artifact (batch-14)

(Origin: batch-14 closed with an empty validation artifact; the two-layer model and the A-5 matrix presuppose execution and cannot catch a blank artifact.)

#### No story done without a black-box AT (batch-14)

(Origin: a project-report story whose white-box TCs passed green while the report was never produced as a user-facing output; batch-14.)

#### Escaped-bug regression (batch-11 SCOPE-1; batch-14 US-016)

(Origin: batch-11 SCOPE-1; batch-14 US-016 A↔B compare — `_diff_load_maps` swallowed parse failures; engine tested, the `CompareRequested` handler path not.)

#### C-25 — orchestrator owns the Phase-4 gate run (batches 35-36)

(Origin: batch-35 AND batch-36 — twice the Phase-4 qa agent backgrounded the ~14-min suite and exited pre-completion; batch-36 recovered with zero rework only because the orchestrator caught the completed run and resumed the agent with its context intact.)

#### Golden double-proof (batch-24 I3)

(Origin: batch-24 I3 — the reviewer's re-derivation from a detached origin/main worktree byte-matched 2437B/2386B, upgrading the regression from test-asserted to double-proven.)

#### C-21 — AT-amending-gate re-reconciliation (batch-35)

(Origin: batch-35 — a Phase-2 amendment split AT-056a and redefined AT-053b after the architect's 5-increment cut, so AT-053b became nobody's increment; the C-18 sweep caught it only post-Inc-5, forcing an unplanned Inc-6.)

#### C-18 — spec-AT realization gate (batch-29)

(Origin: batch-29 — the file-derived C-17 test `AT-043-c17` was folded through Phase-2 yet never built across Inc2–4 because no increment owned its realization; "covered in parts" masqueraded as coverage and only the Phase-4 reconciliation caught the missing node → closed in a follow-on increment.)

#### Coverage-claim discipline (batch-08 LLR-004.1)

(Origin: batch-08 LLR-004.1 gap.)

#### C-20 — net-new-file RED via move-aside (batch-35 Inc-1)

(Origin: batch-35 Inc-1 — a stash-based RED on the untracked new module popped a months-old parked batch-29 stash and conflicted `state.json`.)

#### C-19 — test-run evidence discipline (batch-35)

> **The rule of this family lives in §*Test hygiene & environment* (Phase 3), added at flow rev75: *a wrapper that re-encodes a child's stdout can destroy the evidence the run exists to produce.* The link is written in BOTH directions on purpose — a reader navigating by id lands here, and this stub is two lines long.**

(Origin: batch-35 — 7 pytest-backgrounding / tool-cap incidents: 3 agent stalls in Inc-0 alone, and the Phase-4 blocking mandate was physically unsatisfiable at the 10-min cap vs an ~11-min suite.)

#### C-27 — frozen-file dual-guard (batch-38 F-1)

(Origin: batch-38 F-1 — Inc-2's `AT-066a` landed in the frozen `test_tui_a2l.py`; the increment gate ran only `test_engine_unchanged.py` (source) and passed GREEN, tripping `test_tc032` only at the Inc-5/Phase-4 broader run — fixed test-only by reverting `test_tui_a2l.py` to `main` and relocating `AT-066a` to the non-frozen `test_tui_a2l_issue_recolor.py`, net-zero test count.)

#### Toolchain entry gate (batches 02-04, ruff absent)

(Origin: ruff absent for whole batches 02-04.)

#### C-26 — touched-symbol reverse census (batch-37)

**Reader: `V43`, flow rev68 — and it is declared once, under `C-48`, not twice.** The per-increment
half of this control is recorded in the increment packet's `**Reverse census**` field; the measurement
and the rule's contract live in `C-48`'s entry above, because a second copy here would be the
two-inventories defect `C-50` names. **The CROSSED half — the census run per lane and shared before a
fork — is NOT in `V43`'s population**: it is the trunk's act, `C-52`'s third fork precondition says it
*structurally cannot be performed from inside a lane*, and **from flow rev69 its reader is `V46`**, on
`C-52`'s `Fork preconditions` field in the requirements document — see that entry for the enumeration
that settled it as condition 3 rather than an obligation of its own. *(This sentence read "and it has
no reader yet" from rev68 to rev68.)*

(Origin: batch-37 — batch-36's `test_tc319_regroup_section_structure_census` (`tests/test_tui_patch_layout.py`, owned by US-057/LLR-057.1) pins the exact child list of the `#patch_doc_controls` button group; batch-37's LLR-064a.2 added `#patch_doc_refresh_button` to that same container and updated the census in the STORY'S HOME file (`test_at057a`, `test_tui_patch_editor_v2.py`) but not the sibling census in the other file — because each increment ran only its own story's test file. Forward traceability was intact (TC-319 correctly owned by US-057, 0 orphans); the miss was REVERSE — nobody grepped `#patch_doc_controls` / `patch_doc_refresh_button` across `tests/`. It passed every per-increment gate and failed only at the Phase-4 whole-suite run; a reverse-grep of the touched id would have caught it at the increment.)

#### C-24 — report-golden census membership (batch-36 US-059)

(Origin: batch-36 US-059 — the census enumerated the legend's ASSERTION consumers but not its BYTE-IDENTITY consumer, the batch-35 `at055b` report golden that snapshots the whole report incl. the legend; adding the Hex block drifted it, caught at Inc-1 by the failing golden rather than by the census.)

#### C-14 — location-move census sweep (batch-21 US-027)

(Origin: batch-21 US-027 — the census keyed on the white-box placement tests, which assert generic containment and survive a subdir move, while 2 e2e tests pinned the OLD root location via a non-recursive glob and broke at Inc1. The white-box lens asks *where the code writes*; the miss was *who observes the written file*.)

#### C-54 — Information Flow Contract (batch-79 LLR-120.2)

(Origin: batch-79 `LLR-120.2` — *"shall render a row naming the active project, and **shall not alter** the existing three artifact slots"*, threshold *"the three slot rows' text unchanged (set equality)"*. The new row was given the class the three slots carry; two shipped readers select on it and index positionally. **Apply the threshold as written and it HOLDS** — the three texts are identical. Six shipped tests broke anyway. Not a vacuous check: the predicate could fail, and it measured a property that is *true in the failing case* — a **misaddressed observable**. The requirement declared the value; the change moved the address; the oracle chosen was the one operation that discards order. **Measured while encoding this control, and it is why `V13` exists:** the consumer list in this control's own worked example was corrected **three times** — two names copied verbatim from a source comment, then three by grep, then four when `V13` was run against the shipped tree and found the stylesheet, which reads nothing and breaks silently if the class is renamed. **A dependant is not only something that reads the value; it is anything that would break if the address moved.**)

#### C-17 — untrusted-render-mode markup-safety (batch-27 B-1)

(Origin: batch-27 B-1 — colouring the Memory Map flipped `markup=False→True` over `ValidationIssue.message/.symbol/.code`; `_scrub_issue_message` stripped ANSI but not `[`/`]` and never touched `.symbol`, and is engine-frozen — a malformed A2L symbol `sensor[red]` would corrupt/crash the screen on the core untrusted-firmware load path; caught by two independent Phase-2 reviewers, but designable-in at Phase 1.)

#### C-16 — prototype-fidelity check (batch-27 Inc-2)

(Origin: batch-27 Inc-2 — an operator-approved HTML prototype demoed arrow-key grid navigation and spec §7 assumed `press("right")` worked, but the UI framework does no spatial arrow-focus by default, so `MapCell.on_key` (Enter-only) never moved focus; the original AT-036a used `.focus()` and would have shipped the gap GREEN. It surfaced ONLY when the AT was hardened to press real arrows → an unplanned in-increment follow-on.)

#### C-58 — a mandate nothing reads is a paragraph (batches 88-89; flow rev63)

(Origin: two items of `the record`'s process backlog, both routed to flow rev63 and both re-measured on 2026-09-07 rather than carried. **`R-89-8`** records that `Boundary catalog`, `Acceptance test(s)` and `Negative control` were made mandatory in `req-template.md` by the 2026-08-28 field-set ruling and were *"checked by nothing"*; case-insensitively against the shipped rev62 validator, `Negative control` returned **6** hits and `Boundary catalog` **3**, every one of them a comment about the validator's own arms, and `Acceptance test(s)` returned **0**. The item carries its own measured argument, which is why it is the naming exhibit: the same ruling had RETURNED `Negative control` to the template because, measured on batch-88, the negative side was inline in **9 of 10** thresholds, so exactly one requirement had no RED side **and nothing said so** — *a mandate carried by convention is carried by nobody*, and the row itself was in that position. **`code-reviewer-absent` (`= G-89-04`)** records the second exhibit and it is the sharper one: `commands/dev-flow.md` §*Independent review* mandates a `code-reviewer` pass at every increment gate and states that a HIGH blocks; batch-88 ran it at **7 of 7** increments (the close records 6 returning BLOCK, and re-reading all seven at the 2026-09-03 reconciliation found **every one** carrying a BLOCK-shaped verdict, so the close may undercount by one), while batch-89 ran it at **0 of 6**, wrote `**ABSENT.**` in an `### Independent review` section of all six packets, shipped five flow revisions, and **every gate passed**. `Independent review` returned **2** hits in the validator, both comments. The third exhibit is the one that is not a failure and it fixes the SHAPE of the remedy: `increment-004.md` and `increment-005.md` of the same batch performed the instrument-RED-proof law in a hand-written gate-checklist row **that exists in no template**, with opposite outcomes and different wordings, and `04-validation.md` carries a third wording — three sites, three sentences, zero templates. That is the same population effect the rev60 block measured at **19 sites and 19 distinct phrasings** for the correction-population law, and it is why the discharge is a KEYED FIELD read by a rule rather than a detector for a phrase. Measured while encoding it, and it is the reason all four readers ship as NOTICE rather than BLOCK: over the active batches the fields cost nothing — batch-89 declares `Negative control` and `Boundary catalog` in **16 of 16** requirement blocks and `Acceptance test(s)` in **6 of 6** HLRs, batch-90 in **9 of 9** and **2 of 2** — but over the whole corpus of **66** `01-requirements.md` documents and **929** requirement blocks the fields are absent in **696 of 712**, **595 of 712** and **235 of 329**, because 64 of those batches predate the 2026-08-28 ruling; and a rule scoped to the ACTIVE batch is one `state.json` edit away from any of them, which `R-89-9` records this project actually doing. For `Independent review` the retroactive figure is not a projection at all: over the `the record` checkout, whose `state.json` names batch-89, a BLOCK would fire **six times** on six packets that were honest about the absence before the row existed. `C-53`'s false-fail cost, measured twice.)

#### C-60 — harness and check must not share an input (an outside course-verification corpus; flow rev71)

(Origin: a verification harness declared an absolute `SIBDIR` to a directory that no longer existed; fifteen assertions filtered through `existsSync`, got `[]` and reported green, and BOTH mutation harnesses carried the same dead constant — one printing `BASELINE rc=0 green` before crashing on `FileNotFoundError` opening its own target. Resolving all three constants from the harness's own location moved `verify-course.js` from 16 failures / 530 asserts to 0 / 584 (+54 assertions that had never been evaluated) and the two mutation runs from unrunnable to killed=22/survived=0 and killed=5/survived=0. The flow's own two exhibits predate the proposal and were not known to it: rev65's `Q18 TRACKED-foreign-root`, keyed on the ambient fact that `~/.claude` is a git repository — *as was the mutant written to record that very finding* — and rev67's `DEVFLOW_HOME` pop, where a fixture's `finally` deleted the override that points a staged run at its scratch tree, so every later arm re-read the live tree and five mutants scored SURVIVED falsely. Ruled MINT by the operator at `Q23`, 2026-09-10, the first control in this catalog earned outside the record.)

#### C-62 — a rewrite converts prescriptions into permissions (external skill corpus; flow rev71)

(Origin: a skill governing an agent's output went from 552 lines to 54 plus progressive-disclosure references, improving on-demand loading, semantic colour separation and epistemic discipline, while deleting five controls — `you MUST include evidence artifacts` became `include examples only when they clarify the question`, two named pass/fail tests were deleted, and `the container test` became `there is no target percentage of boxed text`. The tell was hedge phrases: *do not automatically require*, *is a choice, not a quality criterion*, *a starting point, not a universal requirement*. The output degraded and passed self-review, because reviewers score the visible axis and the visible axis had genuinely improved. This flow's own rev57 extraction is the in-house exhibit AS A GAP: narrative share fell 26,046 → 3,974 chars over six normative files with every moved tag verified resolvable, and NO imperative was counted at either end — measured at rev70, *enforcement density* and any MUST-census occurred across `docs/`, `commands/` and `templates/` exactly once, inside the handoff proposing this control. Ruled MINT by the operator at `Q23` as the one new AXIS of the five. The mechanism — a derived per-file MUST/required/BLOCK count per manifest revision, reported as a delta — is NAMED AND UNBUILT at rev71.)

#### C-57 — instrument blindness (batch-89; flow rev59-60)

(Origin: batch-89 of the record, whose own record tabulates five instruments that reported the opposite of the truth and closes *"the law is one control, not five fixes, and it is not yet encoded"* — a substring reader scoring 6 of 6 kills as survivors (`01-requirements-ledger.md`), an AST walk reporting a 3.7 floor on a 3.12 interpreter (`01-requirements.md` §`P-6`, `05-close.md` §1 Story 4), a backwards regex under colour reporting `0 killed / 12 survived` where 12 were killed, `ast.parse(feature_version=)` read as a statement about 3.7 when it returns the RUNNING interpreter's verdict, and an arm comparing a constant to itself (both in `increment-004.md`). The strongest exhibit is the one that is NOT a failure: `increment-005.md`'s gate checklist carries a hand-written row — *"| 4 | Detector proven able to see RED before any verdict | ✓ | `SENTINEL-must-be-RED` KILLED first, by 3 arms |"* — that exists in no template, `increment-004.md` carries the same row with the opposite outcome recorded honestly, and `04-validation.md` carries a third wording; three sites, three sentences, zero templates, which is why the encoding is a declared field and not a phrase. `05-close.md` §2 supplies the corollary that makes it non-trivial: `N7-case-probe-is-assumed` replaced a whole case-fold probe with `return True, None` and survived twelve mutants *"because this machine really does fold case, so the verdict was armed and the mechanism was not."* Two later instances come from the flow's own machinery and are the reason the entry is dated forward: at rev59 a mutation harness scored an alias mutant SURVIVED because a file dying at import emits no arm line, repaired before its verdicts were believed; at rev60 a `SyntaxWarning` shipped at rev59 was found interleaving mid-line into the arm transcript under Python 3.12, so the transcript itself under-counted its own arms by one — an instrument correct about its subject and wrong about its own output. Measured 2026-09-06 while encoding it: **11 of the 13 increment packets of batches 88-89 carry no such obligation**, the two that do are the two above, and no shipped rule read a packet for a verification section — `v9_source_budget` was the only rule reading a packet for a declared FIELD at all, which is why `V31` is shaped after it and, like it, NOTICEs rather than blocks.)

#### C-40 — falsifiability-before-correctness (batch-63 corpus)

(Origin: batch-63 — a corpus of vacuous acceptances that has grown every time someone looked for more, three of them authored *after* vacuity was already that batch's identified theme and three the orchestrator's (`05-postmortem.md:59-65`). Three of the five related an accounting helper to a byte count — both pure functions of the same input — while the writer, the declared subject, never appeared in the expression (`00b-measurements-rescoped.md:211-216`); the executed counterfactual read `RED cases against the WRONG implementation: 0` (`:207`). The **sixth was found by applying this control** and is live on `main`: `AT-172b` asserts `raw == document_bytes(raw.decode("utf-8"))`, an identity for every valid UTF-8 string, while its docstring claims to be *"the clause that fails on a text-mode writer"* — 0 RED cases across {pre-fix, post-fix} × {LF, CRLF}, and it is missed by C-10, C-31 **and** C-39. Instance (i) is `AT-193b`, built only from cases its own detector already caught, which omitted this repo's own `p.open("w")` idiom. Instance (ii) is the revision-3 fold, which replaced a 40-row TC layer with three id ranges and dropped **8 of ~18** union observables, including the only structural check the merge gate could run (`02-regate-discharge-qa.md:66`, `:102`). **Dropping one limb measurably loses members of that corpus while the other limb keeps them — the arms, their domains and their exact figures are recorded in the batch artifact rather than in this block, because a count encoded in a control becomes wrong the moment the corpus grows, and that is exactly what happened while this control was being written.**)

#### C-40 rider — assert the expected arm COUNT (batches 76/84)

(Origin: batch-76 of the record built a per-arm harness after four arms survived a fully removed gate under a green aggregate; batch-84 re-committed the identical error eight batches later and found it only by discovering that tool — which is the argument for encoding it here rather than in one project's scripts.)

#### C-39 — pre-execute every executable threshold (batch-62)

(Origin: batch-62 — Phase 2 failed on 14 blockers of which **three were predicted thresholds**: a golden drift specced as "exactly 2 lines, an unpredicted 3rd blocks" was measured `{14, 15, 51}` = **3** (the probe sampled a twice-emitted field once), so a correct implementation would have tripped the batch's own gate; a "the benign no-op arm still holds" claim was false (`SYM_A` → `SYM\_A`, breaking 3 sites in 2 files, one in no C-27 list); and a security review's cost estimate "the flow-report goldens move" was measured as **1 test, 0 goldens** — the repo has no flow-report golden. Executing every threshold in the refined spec then caught a FRESH one inside the fold: an amendment named Unicode categories `Cc`/`Cf` and claimed to close a survivor list containing `U+2028`, which is `Zl` and passed both that filter and the newline collapse. Inc-2 later hit the measured drift set exactly, with no unpredicted line.)

#### C-36 — fold-against-defined-vocabulary (batch-51 Phase-2)

(Origin: batch-51 Phase-2 — the orchestrator's Phase-1 fold of a `qa-reviewer` gating-coverage finding authored `AT-086c` against a phantom gating value `"block"` + a phantom status `"blocked"` + a false-failing entries-absent trigger, none defined by the model (real tokens `CHECK_GATING_ADVISORY`/`CHECK_GATING_BLOCK_OWN`; statuses `ok/notices/error/skipped`; LLR-086.4's 4-case matrix — only tabulated during the fix — shows a readable-but-failing check never flips the status). The phantom would have false-failed a correct implementation; it was caught only because the architect + qa Phase-2 reviews independently re-derived the identical blocker. The fix reauthored AT-086c against the real tokens on the one matrix cell where the flag actually changes the status, and tabulated LLR-086.4.)

#### C-35 — draft-time EXECUTION probe (batches 60-64 catalog)

(Origin: batch-50 — P-1b's acceptance cited the real `ASAP2_Demo_V161.a2l` CURVE as "→ 25 B green", specced by READING `parse_characteristic_header` + the fixture separately; only EXECUTING `parse_a2l_file` over the fixture at Phase 2 revealed the parser reads single-line headers while the demo is multi-line → 49/50 CHARACTERISTICs parse `char_type=None` and the feature fires on nothing. Even a source-reading architect review only partially surfaced it; the execution probe nailed it, and the story was descoped before a wasted implementation increment. Pre-existing: P-1's own scalar derivation silently no-ops on the same file — never caught because no batch executed the pipeline over a real multi-line fixture.)

#### C-15.1 — writer-census probe (batch-24 B-1)

(Origin: batch-24 B-1 — P-10 probed `update_a2l_view`'s body and correctly read the call order, but never opened `update_mac_view`, whose no-MAC branch WIPES `_validation_issues` and early-returns; both reconcile-story AT fixtures were no-MAC sessions, so the gate ATs were unreachable as specced and the planned reorder made the path strictly worse. A writers-grep for `_validation_issues =` lists the wipe sites in seconds and forces the body read at Phase 1; instead the hole was caught by the Phase-2 architect one gate later.)

#### C-15 — symbol-identity + sweep-back check (batch-23 D-1)

(Origin: batch-23 D-1 — the spec (and two reviewers who read the framework SOURCE and verified every behavior claim true) named `Select.BLANK` as the blank sentinel; on the UI framework 8.2.5 it resolves to the inherited `Widget.BLANK` bool (`False`) and can never match — the real sentinel is `Select.NULL`. Third occurrence on arrival: the same trap had shipped silently in two prior batches (US-026 change-file filter, AbDiff) with a green suite. The truth was already on the page: the F-4 fold wrote `Changed(Select.NULL)` into one section while the AT asserts two sections up still said `Select.BLANK`.)

#### RC-1 — base-currency gate (batch-14)

(Origin: batch-14 was scaffolded in a worktree off a stale `main` while `origin/main` had already shipped one of the batch's stories + closed the audit, forcing a mid-flight rebase + a full-spec story drop — invisible waste a `git fetch` would have prevented.)

#### C-33 — critical-path sub-agent liveness (batch-49)

(Origin: batch-49 — a delegated code-review sub-agent hung ~10.5h with no completion event; the orchestrator waited passively on the notification and only re-engaged when the operator flagged it; the byte-size liveness monitor was useless because the transcript files were 0 bytes throughout. Corrective action: active `TaskOutput` polling + source-mtime liveness, inline takeover on a confirmed hang.)

#### C-44 — session-close working-file reconciliation (batch-70)

(Origin: batch-70, operator-instructed — *"esto no puede seguir pasando"* — after **four instances of the same pattern surfaced inside a single session**: (1) a completed, pushed close-out branch that was never merged, leaving `state.json` on the main branch claiming a finished batch was still mid-phase, which then misled the *next* batch at its intake gate; (2) two corrective items from a merge gate that closed CONDITIONALLY — *"once items 1–5 land this is a MERGE"* — written, approved and never applied, while the batch merged anyway; (3) an abandoned uncommitted edit in an auxiliary skills repo, the unfinished last step of that same close-out; (4) two uncommitted global command files, found only because a later session happened to open them. **None was a code defect. All four were work that had been done and never landed.**)

#### Interruption protocol — resume rule (batch-24 I4)

(Origin: batch-24 I4 — a session-limit death mid-increment was absorbed with ZERO rework because the checkpoint was clean-RED and the resume agent found MORE done than briefed and extended instead of redoing.)

#### C-56 — an evidence transcript is corpus input (batch-86 Inc-1 F2)

(Origin: the record batch-86 Inc-1 code review, finding F2 — measured, not reasoned. The increment packet quoted the RED arm's corrupted id verbatim and used two range tokens; the Atlas id-scanner adopted **THREE phantom ids**, and one `--atlas --write` stood between them and the committed derived plane. The batch's sha256-proven revert had verified the wrong plane — correctly, and irrelevantly. **The same batch reproduced the class twice more on the same day:** the orchestrator nearly re-committed the defect while drafting the close record, and a zero-padded dotted range in batch-51's `traceability-matrix.md` turned out to be pre-existing, sitting scannable in the tree since it was written. The tokenizer half is closed mechanically at rev45 — the Atlas id pattern refuses a token whose continuation is not registry grammar instead of truncating it to a stem, `AT-043-c17` no longer yielding `AT-043` — but a scanner hardened against mangled tokens does not make a mangled token in the corpus true.)

#### C-55 — load-bearing emptiness, both limbs (batch-84)

(Origin: batch-84 of the record, and both limbs came from the same batch. **Limb 1:** the batch's whole result was that no widget address in the tree is assembled from parts — sound only because the binding walk deliberately over-collects, reporting bindings from unrelated functions in the same file. Nothing but one guard, explicitly labelled as protecting the conclusion, stops a later scope-precise "fix" from weakening every such claim with the suite green. **Limb 2:** the criterion read *"emit it under its own outcome and NEVER DROP IT"*; only the classifier half was mutated. Filtering unresolved rows out of the resolver's return passed **all sixteen** guards — it dropped nothing, because the tree holds **zero** instances of the unresolvable case. It was found by an adversarial pass, not by the suite, and the fix is a synthetic tree containing exactly the case the real one lacks. **The reviewer's own proposed fix was written, executed, and stayed green** — see the C-50 rider below.)

#### C-55 rider — absence admissible only via non-absence probe (probe-failure cleanup session)

(Origin: a cleanup session produced three broken probes in a row, all with the same signature. `grep -P` supports only unibyte and UTF-8 locales and errors out under others, so 27 of 27 branches reported "no PR", the merged ones included. a shell rewrote `rev:path` into `rev\path`, so **35 of 35 files reported ABSENT from `main`** when all 35 were present — that one was one sentence away from being reported as 35 files of lost work, and what caught it was contradicting an earlier probe, not any guard. The same bug recurred immediately because the environment variable does not survive a new shell. In the same session the ONE probe carrying a positive control — a case required to return `loose=1 indirect=1` — was the only trustworthy measurement taken.)

#### C-43 — premise evaluation at every gate (batch-70 Phase 0)

(Origin: batch-70 Phase 0. Ten premises of an inherited design were executed against disk; eight held exactly — including two file line-counts and a cited line ADDRESS. Two did not, and both would have cost real work. **(i) A FALSE premise.** The design cited a module's `variant_id=None` line as *"the single-variant assumption is explicit in the code"* and concluded the feature was *"mostly threading an existing dimension, not building one"*. The line was real and at exactly that address — but sat inside a different block handler's operation input, whose `variant_id` is the operations kernel's reporting metadata. The module had no variant dimension at all: three occurrences of the word across 531 lines, none of them a seam. An implementer trusting it would have wired the new dimension into the wrong object and believed the increment closed. **(ii) An INCOMPLETENESS.** The spec's security section declared a containment constraint mandatory, yet none of its six acceptance criteria observed it — the nearest covered a unit *aborting*, and an abort is not a containment rejection. Folding both subjects into one criterion was rejected on the project's own prior evidence that a two-subject acceptance loses its threshold; a seventh criterion was added instead, consuming an existing completeness census rather than building a new oracle. The requirement set came out larger, which is the point.)

#### C-50 rider — structural invariant, no output assertion (batch-84)

(Origin: batch-84 of the record. An adversarial review correctly found the guard overpromising and proposed a printed-output assertion; **it was written, executed, and stayed green under the mutation** — two expressions that are the same set counted from opposite ends cannot be separated by any output. Running the proposed fix is what revealed it did not work, which is the general lesson: a reviewer's remedy is a hypothesis, and C-43 already says a hypothesis is not verified by having been written down.)

#### C-31 — input-set-is-an-oracle (batch-48 HIGH-1; batch-47 Inc-3)

(Origin: batch-48 HIGH-1 — a hue-distance test asserted "≥40° from every claimed hue" while its hand-listed census omitted the one live hue at 38.4°; arithmetic exact, every code mutation green, false because the input set was incomplete. The fix derived the census by sweeping every colour literal in the tree and asserting completeness — dropping an element now goes RED. Also the batch-47 Inc-3 deleted-oracle and the batch-48 missed-sweep are this family: the *set of guarded sites* was the incomplete input.)

#### C-12 — output-then-consume AT discipline (batch-16 G-3)

(Origin: batch-16 G-3 — the batch closing batch-11's "tested via direct-kwargs, not the shipped surface" nearly shipped its own consumer-pickup AT via a same-values direct write.)

#### C-10 — AT-authoring discipline (batch-14 F1/F2)

(Origin: batch-14 F1 default-value-reliant driver + F2 unobserved preserve branch — both slipped past a green AT suite and were caught only by code-review.)

#### Worktree-not-editor-root gate protocol (batches 19-20)

(Origin: batches 19-20 worktree-not-editor-root friction; operator-formalized batch-20 Phase-5.)

#### Living plan & in-conversation reporting (batch-12)

(Origin: batch-12 mid-batch comms-collapse; memory `feedback_devflow_living_compendium`.)

#### Batch rollover — single-slot state.json (batch-88/89, measured 2026-08-29)

**Every field in `state.json` except the project identity describes THE ACTIVE BATCH ONLY.** Opening a
new batch therefore has to RETIRE the outgoing batch's values, and until rev51 nothing here said so.
Measured 2026-08-29: batch-89's `state.json` still carried batch-88's ten `decisions_log` entries
(newest dated 2026-08-27, before batch-89 existed), batch-88's `iterations_per_station`, and
`artifact_homes` paths still resolving to `.dev-flow/2026-08-24-batch-88/`. The per-batch convention
was real — batch-88's log holds not one batch-87 entry — so this is **drift, not a design choice**,
and it is why `V27`'s logged-with-no-packet direction reported increments 1 and 2 of a batch that had
already closed. A rollover is a procedure, not a rename.

#### Batch-open creation of 01-requirements.md + ledger (batch-86)

(measured at batch-86's open: it landed on batch-01's frozen doc and produced 17 false `V4` blocks)

#### Phase-3 file budget ≤4 source files (measured 2026-08-10, 178 packets)

- *(Origin — measured, not estimated. Over the 178 parseable increment packets of the record's 67 batches the **TOTAL-deliverable** distribution was median 3 files, p90 6, max 12 — **`TOTAL` is load-bearing and its absence here was a real defect until flow rev67**: `/dev-flow` §Phase 3 published these same three figures under the word *source*, where a p90 of 6 cannot stand beside a 95 % share at ≤4, and an external review caught the contradiction on 2026-09-08. The **SOURCE** distribution over the same corpus was median 2, p90 4, max 10. But of the 24 increments that broke the old flat ≤5, **16 — 67 % — touched ≤4 SOURCE files**: they broke the cap by writing tests, not by sprawling. 95.3 % of all increments touch ≤4 source files; tests run median 1, p90 3, historical max 4. **These figures are the 2026-08-10 corpus and stay dated rather than refreshed** — an origin note that silently adopts a later measurement stops being an origin. The live figures are re-derived at `/dev-flow` §Phase 3 (2026-09-10: 198 packets, SOURCE p90 4, 95.8 % ≤4). The old cap measured the wrong variable — 3 source + 3 tests was a violation while 5 source + 0 tests complied. Re-run the analysis: `~/.claude/docs/analysis/increment-file-history.py`.)*

#### Requirement-amendment record §6.5 (batch-13 operator convention)

(Origin: batch-13 operator convention; complements the §6.4 reconciliation log. §6.5 is also the record for `iterate-to-refine` from Phase 4.)

### From `commands/fast-dev-flow.md`

#### C-55 (fast lane) — load-bearing emptiness, both limbs (batch-84)

(Origin: batch-84 of the record, both limbs from one batch. The result — no widget address in the tree is assembled — held only because the binding walk deliberately over-collects. And a criterion reading "emit it under its own outcome and NEVER DROP IT" was mutated on the classifier half only: filtering unresolved rows out of the resolver passed **all sixteen** guards, because the tree holds **zero** unresolvable rows.)

#### Backlog reconciliation on the fast lane (2026-07-20 audit, extended 2026-07-28)

(Origin: 2026-07-20 operator audit — the backlog went ~10 batches stale because no close step enforced the update. Extended 2026-07-28 after a lane split left both flows naming a file that had become a router holding no open work.)

### From `commands/dev-flow-sync.md`

#### RC-S1 — the sync-side blank-artifact net (2026-06-23 black-box audit)

(Origin: the 2026-06-23 black-box audit found a batch that passed the orchestrator gate with a blank Phase-4 artifact — RC-S1; this is the sync-side net. The id is `RC-S1`, not `RC-1`, since rev56: `RC-1` is the base-currency gate of `/dev-flow` §Phase 0 — measured 2026-09-03, that sense holds **21** occurrences elsewhere in the flow: 13 in prose across `dev-flow.md`, `FLOW-VERSION.md`, this catalog and `phase-checklists.md`, plus 8 in four diagram labels, each stored twice by excalidraw. One token cannot carry two different reject-checks. **The naming ruling itself stayed in the command** — it is a definition; only this measurement moved.)

#### Repo-hygiene line — the checkout left on a merged branch (batch-23)

(Origin: batch-23 — a concurrently-deployed agent left the primary checkout on its merged PR branch.)

#### Visual evidence is regenerated INSIDE the sync (2026-07-02 audit)

(Origin: 2026-07-02 audit — the the record evidence gallery froze at 2026-05-22 because regeneration + vault copy was a manual side-channel outside sync; batches 05→23 shipped with a stale gallery and no check noticed until a manual audit.)

#### Setting a flag is not persisting it — land the `state.json` edit (C-44)

(Origin: a batch whose vault sync completed correctly and whose close-out commit was never merged; `origin/main` claimed `obsidian_synced: false` and `phase_status: in-progress` for a batch that was finished, and it misled the following batch at its intake gate.)

### From `templates/validation-template.md`

#### QC-2 — the value-discriminating counterfactual (batch-16)

(Origin: batch-16. A pre-fix RED that is a *shape* failure — TypeError, missing argument, constructor or signature mismatch — proves the call path is wired, not that the assertion discriminates the right value. A regression whose only RED is a shape failure is a wiring test wearing a regression's name, so the post-fix assertion must also be shown to fail on a wrong-but-well-typed value.)

### From `templates/req-template.md`

#### Executed-verification reminder (batches 02-03)

> Reminder from the batch-02 + batch-03 post-mortems: the absence of an executed verification + numeric pass threshold on `test`/`analysis` requirements was the recurring root cause of forced phase-1 iteration. Capture at draft time, not at the phase-2 gate.

#### Environmental-measurement citation rule (batch-06 B-1)

(Origin: batch-06 B-1 — a batch-05 narrow-regime observation sitting in a test comment ("~113 at 119", measured with the activity rail COLLAPSED) was generalised into the universal constant `body_w = term − 6` without re-measuring in the ≥120-column regime, where the rail consumes 18 more columns; the wrong constant then propagated as asserted fact through five-plus sections (§1.3, §2.5, HLR-001, LLR-001.3, LLR-001.5, §6.3) and produced 1 blocker plus 2 majors from one bad number. **The symbol-citation rule did not and could not prevent it: the measurement HAD a citation — its validity REGIME was unstated.** "grep-verifiable" covers existence, which is binary and regime-free; an environmental measurement is a function of conditions, so citing the value without the conditions fails one regime later. Found pre-code at the Phase-2 gate by BOTH reviewers independently (F-A-01 = F-Q-01), so it cost nine fixes and one iteration rather than a redesign — what it threatened was not broken code but a MIS-INFORMED gate: the operator's floor decision was initially computed from wrong facts. Recorded at flow rev75, because the rule's `(Origin: batch-06 B-1.)` tag in `req-template.md` had resolved to no heading in this catalog since the rev57 extraction. **That template carries twenty-one `(Origin: …)` tags**; twenty now carry an explicit `— see dev-flow-lessons` pointer, and the twenty-first — `(Origin: batch-09; relocated flow rev60, this site swept flow rev69.)` — carries its own relocation history instead, which is a declaration and not a dangle. **This was the only one that pointed nowhere.** ⚠ The axis is wider than one file and is named rather than closed: **80 origin tags across the 18 normative documents of `commands/` + `templates/dev-flow/`**, and NOTHING in the flow reads them — `grep Origin devflow-validate.py` returns 0. An arm of `CAT INDEX-matches-headings`'s shape would close it; the nearest remaining candidate the review named is `increment-template.md`'s `(Origin: batch-66 …)`, where `batch-66` appears only in `C-59`'s italic subtitle and not in any heading. **Owed, not done, and counted here so it cannot go uncounted** (`C-58`).)

#### State-lifetime provenance rule (batch-24 B-2)

(Origin: batch-24 B-2 — `last_summary` survived project switches with no source-image field; the specced before/after report would pair project B's file with project A's patch, and every then-specced AT passed over it. Fix: `source_image_path` stamp + refusal class + a cross-project refusal AT.)

#### Two-layer validation rule (batch-14)

(Origin: a project-report story whose white-box TCs — `test_full_report_content`, builders, window math — passed green while the report was never produced as a user-facing output; batch-14.)

#### Story-dimension coverage / surface-reachability (A-5, batch-11 SCOPE-1)

(Origin: batch-11 SCOPE-1 — a manifest writer fully tested via direct kwargs while the save handler passed empty batch/assignments, so the shipped artifact carried only `active_variant`; 23/23 TCs + full suite passed because coverage was keyed on the writer's API, not the user's story.)

#### Purity-probe form rule (batch-09 DEV-5)

(Origin: batch-09 DEV-5 — `rg -c "textual"` matched the word "textual" in a module docstring.)

#### Provisional-identifier scope rule (batch-09 DEV-1)

(Origin: batch-09 DEV-1 — the spec pinned `tests/test_diff_report.py`; the implementer chose `test_diff_report_service.py`, producing a Phase-6 rename-reconciliation chore.)

#### Ban the 'VERIFIED COMPLETE' census stamp (A-2, batch-10)

(Origin: batch-10 — Phase-2 certified the census "VERIFIED COMPLETE (re-ran all 3 grep families)"; "all 3" was the bug, and the 4th family broke at the I1 gate.)

#### Census = completeness principle, change-first (A-1/A-3, batch-10)

(Origin: batch-10 — the emitter into the frozen `hexfile.py`.)

#### Supersession-census-completeness rule (batches 09-10)

(Origin: batch-09 — two package-root placement guards escaped a placeholder-only census; batch-10 — a 4th family, the engine-frozen guards that git-freeze `core.py`/`hexfile.py`/`range_index.py`/`validation/`/`<ui-package>/a2l.py`/`<ui-package>/mac.py`/`<ui-package>/color_policy.py`, was MISSED even after the b09 widening and broke the emitter's `hexfile.py` placement at the I1 gate, forcing the R2 relocation to `<ui-package>/changes/io.py`.)

#### Probe-regime rule (batch-08 B-2)

(Origin: batch-08 B-2 — a reverse-import probe whose executed control ran at single-dot import depth while the protected targets lived one package level deeper, where the natural violation form was two-dot relative and escaped the regex on the SOLE verification of its LLR.)

#### AC-artifact citation rule (batch-08 B-1)

(Origin: batch-08 B-1 — an acceptance criterion demanded "a real `.hex` example from `examples/`" on a tree measured to contain zero `.hex` files; found independently by two reviewers because the rule's wording covered only symbols.)

#### Contract-touch rule (batch-07 B-1/B-2)

(Origin: batch-07 B-1/B-2 — LLR-002.7/002.8 added `saved_path`/`issues` hours after the C-6 contract was drafted.)

#### Probe self-test rule (batch-07 B-3/B-4)

(Origin: batch-07 B-3 — a BRE grep returning 0 on a tree known to contain 164 hits — and B-4 — a double-apply equality no correct implementation could satisfy.)

#### LLR symbol-citation rule (batch-05 F-A-01)

> (Root cause of the batch-05 F-A-01 blocker + three Phase-3 doc deviations: LLRs named specific private fields/methods — `_alt_hex_window_start`, `_mac_hex_window_start`, `_on_mac_records_row_highlighted`, `current_file.sorted_ranges` — and a layout constant (`width: 78`) that were inferred from plausible symmetry, NOT from observed code. The fabricated paging fields were caught by the independent Phase-2 re-review before any code was written; the other three survived to Phase 3 and surfaced only at implementation time. The common failure mode is "named a symbol that looks like it should exist." A rule that says "verify" with no required artifact silently degrades to "I assumed," so this mandates a CITATION, not a process step.)

#### Testing-strategy-vs-ADR rule (batch-06 F-6)

> (Root cause of the batch-06 F-6 / Phase-3 infrastructure correction: every `test (...)` label was labelled against a testing stack — JSDOM + Testing Library — that didn't exist in the repo and was explicitly rejected by ADR-0002. The software-dev agent correctly stopped at the boundary, but the gap should be caught in Phase 1.)

#### Parent-HLR re-read rule (batches 06-08 reconciliation cluster)

> (Root cause of the batch-06 A-B1 + batch-07 A-03 + batch-08 A-01-cluster post-mortems: THREE consecutive batches relaxed an LLR threshold or claimed a promotion during reconciliation without propagating the change up to the parent HLR / into the LLR body, leaving §6.4 asserting things the §3/§4 body didn't reflect. Adding this rule as prose at batch-07 closeout did NOT prevent the batch-08 recurrence — because a rule that says "re-read" with no required output silently degrades to "I thought about it." The corrective action is to mandate an ARTIFACT, not a process step.)

#### Verifiability rule — executed verification + numeric threshold (batches 02-03)

> (Root cause of the batch-02 + batch-03 post-mortems: both batches forced a phase-1 iteration for the same reason — `test`/`analysis` validation labels without a named executed verification and a numeric pass threshold. The corrective action is baked into the template.)

#### rev48 lean contract — live-contract size measurement (batch-88)

(Measured on batch-88's record: 193,364 chars, of which the findings table is 8.1% and forensic prose 26.6%, leaving 65.3% of *normative* text written in the forensic register.)

### From `templates/ifc-template.md`

#### IFC worked example meta-lesson — the consumer list corrected three times by measurement

> ### ⚠️ The first draft of this very block was wrong, and how it was wrong is the lesson
>
> It listed **two** consumers of `.loaded-detail`. A grep of the shipped tree finds **three** —
> the missing one being the regression test written for this exact defect, which reaches the
> address and asserts its cardinality is 3.
>
> The two-name list did not come from nowhere. **It is copied verbatim from a comment in the
> source file**, which the design document copied, which this template then copied. *Three
> copies of one list, and the tree contradicts all three.* Nobody was careless: the comment was
> accurate when written, and a new consumer arrived afterwards, which is the only thing a
> hand-maintained list of dependants ever does.
>
> **`V13` is the rule that exists to catch precisely this**, and it catches it here: grep the
> declared literal, and any file that reaches it and is not listed is an undeclared consumer.
> A control whose first application finds a defect in the document that introduces it is
> reporting something real about how this class of list behaves.
>
> **It then did it again.** With `V13` written and run against the shipped tree, the corrected
> three-name list was still short: **the stylesheet reaches the address too.** Rename the class
> and its rule silently stops applying — that is a dependant, and it is now declared. Three
> corrections to one list, each found by measuring rather than reading. **A dependant is not
> only something that reads the value; it is anything that would break if the address moved.**

#### C-54 / IFC — the batch-79 misaddressed-observable defect story

A batch-79 requirement read: *shall render a row naming the active project, and **shall not
alter** the existing three artifact slots*, with the threshold *the three slot rows' text
unchanged (set equality)*.

The implementation gave the new row the same class the three slots carry. Two shipped readers
select on that class and index **positionally**. The query began returning four cells.

**Apply the threshold as written: the three rows' text is identical. Set equality HOLDS. Six
shipped tests broke anyway.**

| | |
|---|---|
| What the requirement declared | the **value** displayed |
| What the change actually moved | the **address** by which the value is reached |
| The oracle it chose | set equality — the operation that discards order, which is exactly where the failure lived |

This is not a vacuous check: the predicate could fail, and it measured a property that is *true
in the failing case*. Call it a **misaddressed observable**, and note what was missing — the
requirement never stated the panel's contract with its consumers. *"Shall not alter X"* —
altered **for whom?** For a human reading the panel, nothing was altered.

#### IFC worked example — values measured against shipped code

**Every value below was measured against the shipped code, not copied from the postmortem.**
That distinction turned out to matter — see the note after the block.

## Provenance

- Distilled from **54 post-mortems** of the the record project's `.dev-flow` batches, deduplicated
  through three distillation passes into this named control catalog (Bucket B). Batch numbers
  (`bNN`) cite where in that corpus a control was earned; they reference the internal batch record
  and expose no private application internals.
  **Corpus size is MEASURED, not carried** — `ls .dev-flow/*/05-postmortem.md | wc -l` on the repo,
  re-run at each extension. It read **38** at the first three distillation passes and **54** on
  2026-07-28, when the catalog already cited controls earned as late as `b64` while still claiming 38
  — an index understating its own coverage. Note the count is *not* the highest batch number (56 batch
  directories exist, and numbering has gaps), and a blind find-replace of the figure is unsafe: of the
  16 occurrences of "38" in this file, 11 are batch citations (`b38`, `35-38`) and one is a hue value
  (`38.44°`); only the corpus-size claims move.
- Distilled catalog canonical (interactive HTML): `<vault root>`
- Local HTML copy this skill was extracted from: `~/.claude\docs\dev-flow-lessons.html`
- Raw postmortems: `<corpus root>/.dev-flow/*/05-postmortem.md`

---

## `C-62` dispositions of the fold's moved imperatives — flow rev80

**What.** One ruled row for every canon line the 2026-09-14 prune moved out of the consultable
catalog and that the origin classification `docs/analysis/briefs-2026-09-03/C62-classification-catalog-prune-2026-09-16.md`
(claude-config) scored `RULE` or `LIMIT` — 53 of the 95 moved. That document is the ORIGIN and is
not amended; this section is the disposition, and it ships with the catalog so the rulings are hashed
and readable wherever the catalog is.

⚠ **The origin document's `canon line` column is STALE and the `REFERENCE.md line` column is not.**
rev77 and rev78 inserted 26 lines into the catalog after the classification was taken, so every canon
line number below its first insertion point is off by one or by 24. The rulings below are keyed on the
`REFERENCE.md` line, which was verified byte-for-byte when the classification was made; all 53 resolve.

**Why the count differs from *53 return*.** The classification measured VERBATIM line absence. `C-62`'s
own test is *does the operator still have to do the same thing?*, and the pruned prose already carries
most of these imperatives in its own words — re-inserting the canon line beside a sentence that already
says it would be two copies of one rule, which is `C-50`'s defect and not `C-62`'s remedy. So each line
is ruled one of three ways, and **every ruling is read by `CAT C62-dispositions-resolve`** rather than
believed: a `RETURNED` line must be in `SKILL.md` and absent from `REFERENCE.md`; a `DISCHARGED` row's
quoted sentence must resolve in `SKILL.md`; a `SUBJECT-MOVED` row's line must be in `REFERENCE.md`.

| Disposition | Count | Meaning |
|---|---|---|
| `RETURNED` | 11 | the canon line is back in `SKILL.md`, verbatim, and is not in `REFERENCE.md` |
| `DISCHARGED` | 39 | `SKILL.md` already states the imperative with the same force; the sentence is quoted |
| `SUBJECT-MOVED` | 3 | the line qualifies a figure the fold moved; the limit sits beside its subject in `REFERENCE.md` |
| **Total** | **53** | |

### Five rulings worth naming

The origin document flags no row as low-confidence — said plainly, because the task that commissioned
this fold expected five flagged rows and there are none in the file. These five were selected by
re-reading and are the ones where the class could honestly have gone the other way:

- **#1** (`LIMIT`, meta-rule) — *a mutation that never applied reads as a survivor*. **DISCHARGED**: the
  pruned file states it and states it BETTER, with the operable half the canon line lacks (*count the
  substitutions actually made and abort on zero*). Returning the canon line would import the `python3`
  narrative with it.
- **#12** (`LIMIT`, `C-40`) — *no hand pass over the 38 has been run*. **SUBJECT-MOVED**: it is a caveat on
  a number the consultable file no longer prints. A caveat with no subject is not a limit; it is litter.
- **#21** (`LIMIT`, `C-58`) — *a file being REACHED says an arm exists somewhere in it*. **SUBJECT-MOVED**,
  for the same reason: its subject is the 24-reached-files count.
- **#59** (`RULE`, §6) — the classification read the line as *never read and write the same artifact from
  two sessions at once*, but the LINE itself is the narrative tail of that rule. **DISCHARGED** against the
  pruned file's own imperative sentence.
- **#82** (`RULE`, `C-60` stub) — a `####` provenance-stub HEADING, classified `RULE` because the heading
  names the obligation. **SUBJECT-MOVED**: `C-60`'s limb 1 states that obligation in `SKILL.md` already,
  and a heading is an id, not a rule.

### The rulings

| # | Control | Class | Disposition | Canon line (normalised) | Discharging sentence in `SKILL.md` |
|---|---|---|---|---|---|
| 1 | C-40-family (meta-rule) | LIMIT | `DISCHARGED` | - **A mutation that never applied reads as a survivor.** The first driver called `python3`, which | **A mutation that never applied reads as a survivor.** Count the substitutions actually made and abort on zero — *and keep a negative control that mus |
| 3 | Candidates (uncontrolled) | RULE | `RETURNED` | candidates are named by their shape, never by an id — and the manifest's `controls:` derivation reads | candidates are named by their shape, never by an id — and the manifest's `controls:` derivation reads |
| 4 | C-31 | RULE | `DISCHARGED` | set's completeness), never trust a hand-typed list to be exhaustive. | **derive or guard its input set**, never trust a hand-typed list to be exhaustive. **Rule.** |
| 6 | C-40 | RULE | `DISCHARGED` | **Rider — the verdict is PER RESOLVED ARM, never the process exit code** *(b76, re-committed b84)*. | **Rider — the verdict is PER RESOLVED ARM, never the process exit code.** A runner exits non-zero if ANY node fails, so one aggregate verdict cannot s |
| 7 | C-40 | LIMIT | `RETURNED` | because the vacuity never reaches one. **A control that works leaves no rejection**, so a count of | because the vacuity never reaches one. **A control that works leaves no rejection**, so a count of |
| 8 | C-40 | LIMIT | `RETURNED` | **What no rule reaches, said plainly:** `V33` tests for a **filled** field, never an **executed** one. | **What no rule reaches, said plainly:** `V33` tests for a **filled** field, never an **executed** one. |
| 10 | C-40 | RULE | `DISCHARGED` | RED is captured by moving the file aside, never by `git stash`, and the restore is proven by the file | by **moving the file aside**, never by `git stash`. #### C-26 — touched-symbol reverse census (batch-37) **Reader: `V43`, flow rev68 — declared once,  |
| 12 | C-40 | LIMIT | `SUBJECT-MOVED` | a vacuous one, and **no hand pass over the 38 has been run** — said here so the number is never | the 38-mutant figure this caveat qualifies is in REFERENCE.md |
| 14 | C-40 | RULE | `DISCHARGED` | the asserting node never reads cannot change that node's verdict. The canonical harness already | the mutated expression names an observable THE ASSERTING NODE READS. |
| 15 | C-40 | LIMIT | `DISCHARGED` | enforces (i) — a non-unique anchor and a byte-identical substitution are both `BAD`, never | The harness enforces uniqueness mechanically; reachability and observability are performed by a reader. |
| 16 | C-59 | RULE | `DISCHARGED` | `repo:` or `vault:` location — durable, named at the batch, **never a session-scoped `Temp` | named at the batch, **never a session-scoped `Temp` path**), stored **byte for byte**, and cited with the **SHA-256 of the bytes at that path** — re-d |
| 17 | C-59 | RULE | `RETURNED` | the storage layer is part of the system under test.* Assert the STORED artifact, never the one you | the storage layer is part of the system under test.* Assert the STORED artifact, never the one you |
| 19 | C-59 | LIMIT | `DISCHARGED` | per-installation `vault_root`, so digests under it are **reported and never verified** from the | limit: a `vault:` home's digests are reported, never verified. (Published-figure correction in REFERENCE.md.) |
| 20 | C-58 | RULE | `DISCHARGED` | The reader must be keyed on a **declared field**, never on a phrase. A corpus states the same | keyed on a **declared field**, never on a phrase (the corpus states one obligation in **19 sites, 19 distinct phrasings**); and the **declared-empty w |
| 21 | C-58 | LIMIT | `SUBJECT-MOVED` | counted wrong and the last.** *A file being REACHED says an arm exists somewhere in it, never that a | the 24-reached-files figure this caveat qualifies is in REFERENCE.md |
| 22 | C-57 | LIMIT | `DISCHARGED` | 2026-08 lived. None of those carries an `AT`/`TC` id; none sits under any gate; `C-40` never reaches | None carries an `AT`/`TC` id; none sits under any gate. |
| 23 | C-57 | RULE | `DISCHARGED` | emits no arm line at all. Three verdicts, never two: **KILLED / CRASH / SURVIVED**. *(Flow rev64 | armed, the mechanism was not). And score three verdicts, never two — **KILLED / CRASH / SURVIVED** — plus a fourth (flow rev64): a mutant that never * |
| 24 | C-57 | RULE | `DISCHARGED` | adds a fourth, and it is the same lesson one step earlier: a mutant that never **applied** — its | plus a fourth (flow rev64): a mutant that never **applied** is **BAD**, not SURVIVED, and `BAD` fails the run. |
| 27 | C-57 | LIMIT | `DISCHARGED` | **Honest limit.** `V31` reads whether the question was ANSWERED, never whether the answer is true or | reads whether the question was ANSWERED, never whether the answer is true. ### C-60 · The harness that proves a check must not share a fixture with it |
| 28 | C-60 | RULE | `DISCHARGED` | 2. **A mutation run that cannot resolve its target is a hard RED, never a pass.** Assert the expected | 2. **A mutation run that cannot resolve its target is a hard RED, never a pass.** Assert the expected mutant count *before* running. |
| 30 | C-43 | RULE | `DISCHARGED` | exists" — executed against disk, never trusted). | disk, never trusted). **An axiom is re-litigable, but only CONSTRUCTIVELY** — on an executed counterexample or a logical invalidation, in practice alm |
| 31 | C-43 | RULE | `DISCHARGED` | disposition ENLARGES the requirement; it never deletes it.** Worked example: a spec's security section | requirement; it never deletes it** (measured example in REFERENCE.md). **Reader: `V45`, flow rev69**, on the requirements document's `**Premise evalua |
| 32 | C-55 | RULE | `DISCHARGED` | that control, never the verdict** — the correct answer can be uniform too, and in the origin below it | inputs is the TRIGGER for that control, never the verdict** — the correct answer can be uniform too, and treating uniformity as a verdict false-fails  |
| 34 | C-55 | RULE | `DISCHARGED` | never a reason to skip it. | guard is needed, never a reason to skip it. (Probe measurements in REFERENCE.md.) ### C-56 · An evidence transcript is corpus input *(batch 86)* **Fai |
| 35 | C-56 | RULE | `DISCHARGED` | character, digit → letter"); never paste the mangled token. | and operation** ("the id's fourth character, digit → letter"); never paste the mangled token. 2. |
| 36 | C-56 | LIMIT | `RETURNED` | never be written in the corpus it guards — and it is recorded at the arm and here rather than | never be written in the corpus it guards — and it is recorded at the arm and here rather than |
| 38 | C-52 | RULE | `DISCHARGED` | 4. **One owner of the trunk.** Requirements, traceability, backlog and spec are never written from a lane. | 4. **One owner of the trunk.** Requirements, traceability, backlog and spec are never written from a lane. |
| 39 | C-52 | RULE | `DISCHARGED` | executed evidence; `none — this batch runs one lane` is the legal empty and MUST be written, because an | `**Fork preconditions**` field (`req-template.md` §2.8); `none — this batch runs one lane` is the legal empty and MUST be written. |
| 40 | C-51 | RULE | `DISCHARGED` | **Anti-theatre clause:** layer 0 is measured by **mutation**, never by line coverage. High coverage made of | **Anti-theatre clause:** layer 0 is measured by **mutation**, never by line coverage. **Reader: `V49`, since flow rev70**, on the keyed `**Layer 0:**` |
| 41 | C-51 | LIMIT | `DISCHARGED` | field-keyed rule can:** it reads whether the question was ANSWERED, never whether the count is true or the | criterion`**. It reads whether the question was ANSWERED, never whether the count is true. **Rider — an arm over a HELPER is not an arm over the RULE; |
| 42 | C-51 | LIMIT | `DISCHARGED` | one a real gate invokes with its argument marshalling, its defaults and its guards, is never | an arm that drives the private helper never executes the rule's own entry point — its marshalling, defaults and guards. |
| 43 | C-51 | LIMIT | `DISCHARGED` | which SYMBOL the arm names**, and it is answered by reading the arm, never by running it: a | names**, answered by reading the arm, never by running it: a helper-level arm and a rule-level arm are both green. |
| 44 | C-50 | RULE | `DISCHARGED` | function that owns it), never by comparing what the two produce. An adversarial review proposed a | Guard it by **parsing the artifact and asserting the shape**, never by comparing outputs. **One home per artifact, declared in configuration, and no c |
| 45 | C-48 | RULE | `DISCHARGED` | probe output beside it is textually indistinguishable from `"B1 was never evaluated"`, and the second | indistinguishable from `"B1 was never evaluated"`, and the second is what actually happens under time pressure. |
| 46 | C-48 | RULE | `RETURNED` | - **Triggers only raise.** They turn controls on; none turns one off. A floor, never a ceiling — and the | - **Triggers only raise.** They turn controls on; none turns one off. A floor, never a ceiling — and the |
| 47 | C-48 | RULE | `RETURNED` | strict lane ignores them upward, so a trigger can never be the reason something got skipped. | strict lane ignores them upward, so a trigger can never be the reason something got skipped. |
| 48 | C-48 | RULE | `RETURNED` | - **Apply C-40 to the triggers themselves.** A trigger that has never fired in several batches is not | - **Apply C-40 to the triggers themselves.** A trigger that has never fired in several batches is not |
| 51 | Test hygiene (S5) | RULE | `DISCHARGED` | provenance stub and **a parenthetical may carry provenance, never a definition** (§*Writing | ## Writing canon — a parenthetical may carry provenance, NEVER a definition **The rule.** |
| 52 | freeze-then-measure | LIMIT | `DISCHARGED` | Freeze protects against *drift*, never against *content*. Pair it with a reader who checks the claim. | Freeze protects against *drift*, never against *content*. Pair it with a reader who checks the claim. |
| 54 | C-66 | RULE | `DISCHARGED` | **The class is published as an EXECUTED OUTPUT and never as a hand list** — the run list, the N, | **The class is published as an EXECUTED OUTPUT and never as a hand list.** A pre-registered whitelist of "known flaky" ids is the defect this control  |
| 56 | Gates & evidence (S4) | RULE | `DISCHARGED` | observe GREEN. For **net-new files** use **move-aside**, never `git stash` — untracked files | observe GREEN. For **net-new files** use **move-aside** (`C-20`), never `git stash`. (b15,35) - **Gate decisions need transport idempotency.** |
| 57 | Gates & evidence (S4) | RULE | `RETURNED` | CI-portable `git diff` tests must resolve the ref or `skip`, and must never read stdout | CI-portable `git diff` tests must resolve the ref or `skip`, and must never read stdout |
| 58 | Multi-agent orch (S6) | RULE | `DISCHARGED` | **Brief a discharge audit against the SOURCE reviews, never against the fold's own amendment table.** | against the SOURCE reviews, never the fold's own amendment table** — a green amendment count cannot see what the fold dropped (one fold: 163 union ite |
| 59 | Multi-agent orch (S6) | RULE | `DISCHARGED` | never landed — the reader had snapshotted the file mid-write. In one batch this recurred **five times**, | **never read and write the same artifact from two sessions at once.** ## Cross-phase · The security lens on "just text" (§7) > **The tell is not "new  |
| 63 | C-44 | RULE | `DISCHARGED` | work only matters once integrated, landed* (**a commit that never lands is not a terminal state**) · | the work only matters once integrated, landed* (**a commit that never lands is not a terminal state**) · 🗑️ **reverted or deleted, deliberately** · 📋  |
| 64 | C-44 | RULE | `DISCHARGED` | **Discharge — mechanical, never from memory.** `git status --short` in **every repository the session | **Discharge — mechanical, never from memory.** `git status --short` in **every repository the session touched, auxiliary repos included**; `git log @{ |
| 65 | C-44 | RULE | `RETURNED` | never by trusting that the corrective pass ran. **From flow rev71 the close artifact carries the | never by trusting that the corrective pass ran. **From flow rev71 the close artifact carries the |
| 66 | C-44 | LIMIT | `RETURNED` | clause has had. It reads whether the roll-up was WRITTEN, never whether the discharge is real; the | clause has had. It reads whether the roll-up was WRITTEN, never whether the discharge is real; the |
| 67 | C-44 | RULE | `DISCHARGED` | **RIDER — characterise VCS state from REFS, never from the working tree.** *(folded in at flow rev71 | **RIDER — characterise VCS state from REFS, never from the working tree.** Inspect **refs** first: `git log --all --oneline`, `git branch -a -vv`, `gi |
| 69 | C-45 | RULE | `DISCHARGED` | **C-44**, an unpushed control is indistinguishable from one never written. **Say which of the four | **Say which of the four landed** — command-but-not-template is *half-encoded*, and the missing half is the enforceable half. |
| 73 | C-62 | LIMIT | `DISCHARGED` | derived per-file count of MUST / required / BLOCK tokens per manifest revision, reported as a **delta** | **Mechanism — NAMED AND NOT BUILT:** a per-file MUST / required / BLOCK count per manifest revision, reported as a delta beside `flow_hash`; until it  |
| 75 | C-46 | RULE | `DISCHARGED` | - Run mutation batteries under **`PYTHONDONTWRITEBYTECODE=1`** so the mutant never enters the cache. | - Run mutation batteries under **`PYTHONDONTWRITEBYTECODE=1`** so the mutant never enters the cache. |
| 82 | C-60 stub | RULE | `SUBJECT-MOVED` | #### C-60 — harness and check must not share an input (an outside course-verification corpus; flow rev71) | a `####` provenance-stub HEADING whose obligation is stated by `C-60`'s own limb 1 in SKILL.md; returning the heading would be a second inventory of o |

### Machine-readable rulings (read by `CAT C62-dispositions-resolve`)

Tab-separated: `#`, disposition, and — for `DISCHARGED` — the sentence that must resolve in `SKILL.md`.

```
1	DISCHARGED	**A mutation that never applied reads as a survivor.** Count the substitutions actually made and abort on zero — *and keep a negative control that must die.*
3	RETURNED	candidates are named by their shape, never by an id — and the manifest's `controls:` derivation reads
4	DISCHARGED	**derive or guard its input set**, never trust a hand-typed list to be exhaustive. **Rule.**
6	DISCHARGED	**Rider — the verdict is PER RESOLVED ARM, never the process exit code.** A runner exits non-zero if ANY node fails, so one aggregate verdict cannot say **which** arms reddened: an inert arm hides behind a sibling that failed.
7	RETURNED	because the vacuity never reaches one. **A control that works leaves no rejection**, so a count of
8	RETURNED	**What no rule reaches, said plainly:** `V33` tests for a **filled** field, never an **executed** one.
10	DISCHARGED	by **moving the file aside**, never by `git stash`. #### C-26 — touched-symbol reverse census (batch-37) **Reader: `V43`, flow rev68 — declared once, under `C-48`, not twice.**
12	SUBJECT-MOVED	a vacuous one, and **no hand pass over the 38 has been run** — said here so the number is never
14	DISCHARGED	the mutated expression names an observable THE ASSERTING NODE READS.
15	DISCHARGED	The harness enforces uniqueness mechanically; reachability and observability are performed by a reader.
16	DISCHARGED	named at the batch, **never a session-scoped `Temp` path**), stored **byte for byte**, and cited with the **SHA-256 of the bytes at that path** — re-derived from where the artifact LANDED.
17	RETURNED	the storage layer is part of the system under test.* Assert the STORED artifact, never the one you
19	DISCHARGED	limit: a `vault:` home's digests are reported, never verified. (Published-figure correction in REFERENCE.md.)
20	DISCHARGED	keyed on a **declared field**, never on a phrase (the corpus states one obligation in **19 sites, 19 distinct phrasings**); and the **declared-empty wording is part of the mandate** (`none — <reason>`, or `ABSENT`), so an absence DECLARED and an absence OMITTED do not render alike.
21	SUBJECT-MOVED	counted wrong and the last.** *A file being REACHED says an arm exists somewhere in it, never that a
22	DISCHARGED	None carries an `AT`/`TC` id; none sits under any gate.
23	DISCHARGED	armed, the mechanism was not). And score three verdicts, never two — **KILLED / CRASH / SURVIVED** — plus a fourth (flow rev64): a mutant that never **applied** is **BAD**, not SURVIVED, and `BAD` fails the run.
24	DISCHARGED	plus a fourth (flow rev64): a mutant that never **applied** is **BAD**, not SURVIVED, and `BAD` fails the run.
27	DISCHARGED	reads whether the question was ANSWERED, never whether the answer is true. ### C-60 · The harness that proves a check must not share a fixture with it *(corpus: an outside course-verification harness, 2026-09-10; flow rev71)* **Failure closed.**
28	DISCHARGED	2. **A mutation run that cannot resolve its target is a hard RED, never a pass.** Assert the expected mutant count *before* running.
30	DISCHARGED	disk, never trusted). **An axiom is re-litigable, but only CONSTRUCTIVELY** — on an executed counterexample or a logical invalidation, in practice almost always **INCOMPLETENESS**.
31	DISCHARGED	requirement; it never deletes it** (measured example in REFERENCE.md). **Reader: `V45`, flow rev69**, on the requirements document's `**Premise evaluation**` field (`req-template.md` §2.7): one of the three tokens or the legal empty `none — <why no premise applies>`; a cell reading `done` scores **unidentified**.
32	DISCHARGED	inputs is the TRIGGER for that control, never the verdict** — the correct answer can be uniform too, and treating uniformity as a verdict false-fails correct work (`C-53`).
34	DISCHARGED	guard is needed, never a reason to skip it. (Probe measurements in REFERENCE.md.) ### C-56 · An evidence transcript is corpus input *(batch 86)* **Failure closed.**
35	DISCHARGED	and operation** ("the id's fourth character, digit → letter"); never paste the mangled token. 2.
36	RETURNED	never be written in the corpus it guards — and it is recorded at the arm and here rather than
38	DISCHARGED	4. **One owner of the trunk.** Requirements, traceability, backlog and spec are never written from a lane.
39	DISCHARGED	`**Fork preconditions**` field (`req-template.md` §2.8); `none — this batch runs one lane` is the legal empty and MUST be written.
40	DISCHARGED	**Anti-theatre clause:** layer 0 is measured by **mutation**, never by line coverage. **Reader: `V49`, since flow rev70**, on the keyed `**Layer 0:**` roll-up in the active batch's `04-validation.md`, or the legal empty **`none — no unit met the decision or boundary criterion`**.
41	DISCHARGED	criterion`**. It reads whether the question was ANSWERED, never whether the count is true. **Rider — an arm over a HELPER is not an arm over the RULE; an arm over the CORE is not an arm over the LOADER** *(batch-89)*.
42	DISCHARGED	an arm that drives the private helper never executes the rule's own entry point — its marshalling, defaults and guards.
43	DISCHARGED	names**, answered by reading the arm, never by running it: a helper-level arm and a rule-level arm are both green.
44	DISCHARGED	Guard it by **parsing the artifact and asserting the shape**, never by comparing outputs. **One home per artifact, declared in configuration, and no command may write a path that is not declared there.**
45	DISCHARGED	indistinguishable from `"B1 was never evaluated"`, and the second is what actually happens under time pressure.
46	RETURNED	- **Triggers only raise.** They turn controls on; none turns one off. A floor, never a ceiling — and the
47	RETURNED	strict lane ignores them upward, so a trigger can never be the reason something got skipped.
48	RETURNED	- **Apply C-40 to the triggers themselves.** A trigger that has never fired in several batches is not
51	DISCHARGED	## Writing canon — a parenthetical may carry provenance, NEVER a definition **The rule.**
52	DISCHARGED	Freeze protects against *drift*, never against *content*. Pair it with a reader who checks the claim.
54	DISCHARGED	**The class is published as an EXECUTED OUTPUT and never as a hand list.** A pre-registered whitelist of "known flaky" ids is the defect this control exists to refuse.
56	DISCHARGED	observe GREEN. For **net-new files** use **move-aside** (`C-20`), never `git stash`. (b15,35) - **Gate decisions need transport idempotency.**
57	RETURNED	CI-portable `git diff` tests must resolve the ref or `skip`, and must never read stdout
58	DISCHARGED	against the SOURCE reviews, never the fold's own amendment table** — a green amendment count cannot see what the fold dropped (one fold: 163 union items · 20 dropped silently); **never read and write the same artifact from two sessions at once.**
59	DISCHARGED	**never read and write the same artifact from two sessions at once.** ## Cross-phase · The security lens on "just text" (§7) > **The tell is not "new external surface" — it is "new string reaching a rendered/persisted > surface."**
63	DISCHARGED	the work only matters once integrated, landed* (**a commit that never lands is not a terminal state**) · 🗑️ **reverted or deleted, deliberately** · 📋 **left in place ON PURPOSE, with its path and remaining work written into the canonical backlog**.
64	DISCHARGED	**Discharge — mechanical, never from memory.** `git status --short` in **every repository the session touched, auxiliary repos included**; `git log @{u}..HEAD` for unpushed commits; confirm an open PR exists for any branch other work depends on.
65	RETURNED	never by trusting that the corrective pass ran. **From flow rev71 the close artifact carries the
66	RETURNED	clause has had. It reads whether the roll-up was WRITTEN, never whether the discharge is real; the
67	DISCHARGED	**RIDER — characterise VCS state from REFS, never from the working tree.** Inspect **refs** first: `git log --all --oneline`, `git branch -a -vv`, `git worktree list`, `git fetch`.
69	DISCHARGED	**Say which of the four landed** — command-but-not-template is *half-encoded*, and the missing half is the enforceable half.
73	DISCHARGED	**Mechanism — NAMED AND NOT BUILT:** a per-file MUST / required / BLOCK count per manifest revision, reported as a delta beside `flow_hash`; until it exists limb 2 is performed by a reader (`C-58`'s warning).
75	DISCHARGED	- Run mutation batteries under **`PYTHONDONTWRITEBYTECODE=1`** so the mutant never enters the cache.
82	SUBJECT-MOVED	#### C-60 — harness and check must not share an input (an outside course-verification corpus; flow rev71)
```
