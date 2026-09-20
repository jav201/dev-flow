---
name: dev-flow-lessons
description: Control catalog of lessons learned from 54 dev-flow batch postmortems of one project — vacuous-check detection, acceptance-test oracles, gates and evidence, test hygiene, multi-agent orchestration, security lens. Consult during any /dev-flow or /fast-dev-flow phase (requirements, review, implementation, validation, postmortem), before starting a batch, or when writing a postmortem. Trigger on "lessons learned", "catálogo de controles", "qué aprendimos en los batches", "control catalog", "vacuous check", or when designing acceptance tests / increment gates.
---

# Dev-Flow Lessons — a control catalog for supervised AI development

Hard-won testing and process controls distilled from **54 post-mortems** of one supervised,
multi-agent, increment-gated development flow. This is a reference you open to look up a
control for the phase you are in — not a narrative to read end to end.

## How to use this mid-flow

1. Find your current dev-flow phase in the **index table** below.
2. Read the controls tagged with that phase (jump by control ID).
3. Before closing the phase, run the **meta-rule** against every assertion and every recorded RED
   you produced.

## The meta-rule (everything below is a special case of this)

**The dominant defect class is the vacuous check: an assertion or fixture that passes on broken
code.** A green suite full of vacuous checks is theater, not evidence. In the corpus these
clustered one level up, in the SPECS and BRIEFS — the artifacts that define what "correct" means.

> **Mutation-test every assert, and every recorded RED.** A check that cannot fail is
> non-evidence. A RED (a test you claim proves a bug exists) that was *never actually executed* is
> worthless. So: for every assertion, construct the mutation it should catch and confirm the
> assertion goes RED under it; for every RED, run it and watch it fail before you trust it.

**The vacuous-check test, executable by hand.** For a check under suspicion, evaluate it twice:
on correct code, and on code with the mutation the check claims to catch. A **discriminating**
check is PASS on correct code and RED on the mutation — the gap between those two is the evidence.
A **vacuous** check is PASS on *both*: the mutation walks straight through it. Three canonical
pairs from the corpus:

| Case | Vacuous version | Why it can't fail | Discriminating version |
|---|---|---|---|
| Palindrome fixture vs a reversal bug | `fixture = ['ok','warn','ok']; assert render(fixture) == fixture` | Fixture is a palindrome; a render that reverses output still equals it | Non-palindrome fixture `['ok','warn','err']` |
| `spans==[]` on safe input | `text = 'hello world'; assert escape(text).spans == []` | No brackets in input → zero spans whether escaping works or not | Unsafe input `'[bold]hi[/bold]'` — mutant (escaping off) produces spans |
| `result == expected … or True` | `assert result == expected or True` | OR-ed tautology can never fail | Drop the tautology: `assert result == expected` |

**A fourth place it hides: the oracle's source.** A harness that reads the *expected* value out of
the very page it verifies is a mirror: change the datum and **both sides move together**, so the
assertion passes while its own message claims it compared. Mutation is what exposes it. (The
measured narrative — 14 harnesses, 97 deliberate edits — is in REFERENCE.md.)

> **The law: the expected value may not come from the artifact under verification.** Pin it in the
> harness. A harness that reads its oracle from what it checks is a mirror, not a test — and it
> costs two edits to change a datum, which is the correct price of a check that bites.

**Two method traps found while catching it**, both of the same family as the defect itself:

- **A mutation that never applied reads as a survivor.** Count the substitutions actually made and
  abort on zero — *and keep a negative control that must die.* A mutation harness needs its own
  mutation test.
- **Judge a harness by its exit code, never by grepping its output.** Counting anything that did not
  print "FAILURES" as green reports 14/14 while all 14 are crashing.
## Index — all controls, by phase

Phase key: **P1-2** = requirements / spec / review (dev-flow phases 1-2; fast-dev-flow phase 1) ·
**P3** = implementation · **P4** = validation & gates · **P5** = postmortem · **X** = cross-phase
(orchestration / security, applies throughout).

**Modes key — read this column BEFORE opening a control's entry, and note WHO decides it.**
Four forms, and only four: **`all`** = the control applies in every mode · **`core·full ‹row›`** and
**`by trigger ‹row›`** = `/dev-flow` §*Modes* does not activate it in `fast`, and the cell CITES the
row of that table which decides it, in ‹guillemets›, by that row's own leading text ·
**``all · fast → `<token>` ``** = the control applies, and in a `fast` batch its honest answer is the named
declared empty, spelled exactly as the artifact that receives it spells it.
**The column is DERIVED, never judged.** `/dev-flow` §*Modes* is the one authority for what a mode
activates; a control that table does not mention is `all`, whatever its cost feels like on a small
batch. `CAT MODES-declared-at-the-index` resolves every citation against that table and refuses a
cell whose cited row is active in `fast`, and refuses a `fast →` token no shipped fast artifact
mints. Until rev86 this column was 43 authorial judgements with no reader — which is `C-58` one
level in, on the column added to answer `C-58` — and it shipped one that was FALSE: `C-45` was
marked `core·full` while every fast spec carries a mandatory `C-45` PULL row, so the index routed a
reader AWAY from the control that documents an obligation the flow still imposes on them.
**Stopping at the index is the point**: a fast reader on a one-expression change who follows the
KAT-anchor row into its entry, or one on a repository with no remote who follows `C-45`, pays for an
answer that is printed right here.

| Control | Name | The failure it closes | Phase | Modes | Prov. |
|---|---|---|---|---|---|
| META | mutation-test every assert and every RED | A check that cannot fail; a RED never executed | P1-2, P4 | all | corpus-wide |
| C-10 | AT off a non-default value | A test that passes on the default state proves nothing about the shipped policy branch | P1-2 | all | b14,16,17 |
| C-12 | output-then-consume through the artifact | Testing a handler and its consumer in isolation misses that the on-disk artifact between them is malformed | P1-2 | all | b16,17,20,26 |
| C-13 / 13.1 | measure rendered geometry at draft | A layout "story" declared ready on arithmetic that was never measured against the real render | P1-2 | all | b17,18,22,24,26 |
| C-14 | a MOVE or a CORRECTION greps its whole population *(trigger widened 2026-09-06)* | Moving an artifact on disk orphans every reader of the old path — and correcting a claim that lives in more than one artifact lands at one site of several, silently | P3 | all | b21, b88, b89 |
| C-15 / 15.1 | probe a framework symbol's runtime identity; grep assignment sites | A spec-conformant filter shipped DEAD because a sentinel resolved to an inherited `False` | P1-2, P3 | all | b23,24 |
| C-18 | every AT = one on-disk node | "Covered in parts" across several artifacts means the end-to-end chain was never actually exercised | P1-2, P4 | core·full ‹reverse census of the touched symbol› | b29,32,35-38,47,48 |
| C-25 | one complete gate run owned by the orchestrator | Gate evidence assembled from fragments, or a validation agent that exits before the run completes | P4 | core·full ‹one complete run owned by the orchestrator› | b35-38 |
| C-31 | input-set-as-oracle | A test of a UNIVERSAL claim whose hand-listed input set omits the one failing member | P1-2 | all | b33,47,48 |
| — | **coincidence oracle** | An oracle computed by DIFFERENT logic that happens to agree with the code; fixing the code turns the test red and it reads as a regression | P1-2 | all | ui/2026-08 |
| C-32 | assert-the-painted-result | Asserting a pre-layout proxy; a `display:none` strip shipped green because the proxy is geometry-independent | P4 | all | b48 |
| **C-40** | **falsifiability before correctness** | A predicate that is correct, exact and complete — and never mentions the thing under test | P1-2, P4 | all | b63,64 |
| **C-42** | **assert the EMITTED form** | Running the producer, then asserting against the form a human reads — false-fails a correct implementation | P1-2, P3 | all | b60-64 |
| — | **freeze-then-measure** | Folding a spec silently expires every measurement taken against its previous text | P1-2, P4 | all | b64 |
| **C-43** | **premise evaluation at every gate** | Work fully compliant with a spec whose PREMISE about the world is false; a design decision inherited from a prior batch treated as verified | P1-2, all gates | all | b70 |
| **C-55** | **an emptiness is doing work — say which kind** | A result or a guard resting on the tree holding NO instance of some case: the claim is true, the suite is green, and the change that falsifies both will be connected to neither | P1-2, P3, P4 | all | b84 |
| **C-56** | **an evidence transcript is corpus input** | A mutation reverted in its target file but spelled verbatim in the packet that proves the revert: the hash verified the wrong plane, and the id-scanner adopts the corrupted token as real | P3, P4 | all | b86 |
| **C-57** | **an instrument is blind until it has reported a failure** | A figure in the record produced by a measuring instrument that has never been shown a known-bad input: the verdict is armed and the mechanism is not, and no `AT`/`TC` id covers it | P3, P4 | all | b89, flow rev59-60 |
| **C-58** | **a mandate nothing reads is a paragraph** | An obligation the process declares MANDATORY in its own template or command, with no mechanism that reads it: skipping it costs nothing, so it is skipped, and every gate stays green while it is | P1-2, P3 | all | b88, b89, flow rev63 |
| **C-59** | **evidence bytes live at a declared home, verbatim, and the store is verified** | An artifact committed as PROOF whose store rewrote its bytes on the way in, or whose only copy sat somewhere that does not survive the session: the digest describes something else, or there is nothing left to compare one against — and every gate stays green | P3, P4 | all | b66; flow rev66 |
| **C-44** | **session-close file reconciliation** | Work that was done, was correct, and never landed — indistinguishable from work never done, and it makes the state files the next session reads assert something false | X | all | b65,70 |
| **C-45** | **the flow is a shared asset — push & pull** | A control encoded locally, so every other project re-learns the same lesson at full price; and a batch run on a stale flow, inheriting a solved problem as an open one | X | all · fast → `not-run — no canon remote on this runtime` | b70 |
| **C-46** | **a hash-verified restore does not restore the CACHE** | A same-size mutation restored within the second: the verified source is back, but `__pycache__` still holds the mutant's bytecode, so the suite runs the mutant from a byte-identical working tree | P3, P4 | all | 22b |
| — | reader-as-oracle (+ corrupted negative control) | Validating a writer against itself; a round-trip that can't distinguish good output from corrupt | P1-2 | all | b09-13 |
| — | KAT anchor | Self-consistency that agrees with its own bug; no externally-published known answer pins reality | P1-2 | all · fast → `none — no instrument beyond the suite` | b12 |
| — | assert-the-discriminating-negative | Only asserting what must exist, never the file that must NOT exist or the bytes that must NOT be written | P1-2 | all | b11,12 |
| **C-53** | **a rule that false-fails correct work is as expensive as one that passes wrong work** | A checker scoped to the wrong unit manufactures findings on correct artifacts — and trains everyone to ignore it | P3, P4 | all | rev11 |
| **C-52** | **the four conditions that make a fork safe** | Parallel lanes without a frozen contract are not parallelism — they are a collision with a delay, discovered at integration, the most expensive moment | P3 | all | rev9 |
| **C-51** | **layer 0 — the unit both existing layers look past** | White-box over the LLR and black-box over the story both skip the unit; bugs inside a single function are visible to neither | P3, P4 | core·full ‹one complete run owned by the orchestrator› | rev9 |
| **C-50** | **one home per artifact; the link crosses by ID** | Splitting artifact homes without id-linking breaks traceability instead of organising it — and any copy means one of the two is false, with nobody knowing which | X | all | rev8 |
| **C-49** | **forward applicability — a design review's output must be someone's input** | A design phase that produces artifacts nobody consumes is pure cost, and it is invisible because it *looks* like rigour | P1-2 | by trigger ‹ARQ · PDR · DDR› | rev7 |
| **C-48** | **a trigger's NON-activation is evidence too** | "Did not fire" with no probe recorded is indistinguishable from "was never evaluated" — and the second is what actually happened | P3, all gates | all | rev6 |
| **C-47** | **the increment budget counts SOURCE, not total** | A cap on total files per increment penalises writing tests: it makes 3 source + 3 tests a violation while 5 source + 0 tests complies | P3 | all | measured over 178 packets / 67 batches |
| §3 | census & blast-radius principles | Incomplete checklists, inferred (not measured) behavior, narrow test filters, uncited symbols, stale contracts | P3, P4 | all | b05-12,28,37,38,46 |
| §4 | gates & evidence rules | Gates passing on empty/fabricated artifacts; unproven escaped-bug fixes; non-idempotent decisions | P4 | all | b12,13,15,18,35,36 |
| §5 | test hygiene & environment | Deleted oracles, AST phantom failures, flaky glob order, substring false-greens, decorative lint, a wrapper that re-encodes the run's own transcript | P3 | all | b02-04,07-12,20,21,32,38,47,48,87 |
| §6 | multi-agent orchestration | Sunk-cost review, dirty-tree git mutations, mis-attributed long runs, namespace collisions, stale renders | X | all | b01,05-07,12,24,33,38,46-48 |
| §7 | security lens on "just text" | New string reaching a rendered/persisted surface treated as harmless because it is local | X | all | b19,24,27 |
| §8 | honesty note | Importing single-project observations as universal law | P5 | all | corpus-wide |
| **C-60** | **the harness that proves a check must not share a fixture with it** | One root cause disables both a check and the mutation harness meant to expose it, so nothing can go red | P1-2 | all | outside corpus 2026-09-10; flow rev65/rev67 |
| **C-62** | **a rewrite converts prescriptions into permissions** | A structural rewrite that improves every visible axis quietly deletes the constraints, and passes review for the improvement | X | all | external skill 2026-09-08; flow rev57 |
| **C-65** | **a ruling is applied as a CENSUS over its axis, never as the instance** | A ruling stated on an axis, discharged by folding the one instance the finding produced: green gate, passing battery, true report — all of it evidence about the instance and none of it about the axis, so the next reviewer finds the next member | X | all | flow rev65, 66, 69, 72, 74 |
| **C-66** | **flaky is a CLASS with a measured rate, never a name on a list** | A failing node waved through as “pre-existing” or “flaky” on a hand-kept id list nobody re-ran: the disposition cannot be falsified, and a real regression rides through it wearing the same word | P4 | all | b87 `G4-01`; flow rev75 |

---

## ⏸ Candidates — observed, transcribed, NOT controls

**The pen holds ONE shape since flow rev83**; the two it held before were ruled and landed at rev75 (one folded into `C-40`, one a rider on `C-58`). ⚠ **A number written beside a candidate is not a reservation** — the `C-55` candidate was declined and the number was later minted for a *different* control. So
candidates are named by their shape, never by an id — and the manifest's `controls:` derivation reads
`#{1,3}` headings, so nothing in this section can enter the control census by accident.
History, and whichever of *nothing waiting* / *something waiting* the pen is currently declaring, live in REFERENCE.md.

**⏸ A human review without a record is indistinguishable from one that never happened.**
*(observed 2026-09-18, transcribed at flow rev83)*

The gates record every **machine** verdict — rules, digests, transcripts — and the record already
names WHO reviewed and WHEN. What nothing records is the **depth** of a human reading, or a reading
**declined**: a light pass and a rigorous one produce byte-identical records, and the perimeter the
flow does not cover (whatever a project decides that is) survives as a verbal understanding rather
than a declaration — an omitted emptiness, not a declared one. It is `C-48`'s class on the human
side of the balance, and it bites hardest exactly where the artifact record IS the deliverable: an
auditor arriving at a complete, green record cannot tell in two minutes where the team put its eyes
and where it did not, which is the first thing an auditor needs.

**Measured before a line was written, which is why it is here rather than in a proposal.** Over one
project's whole record, through the validator's own field grammars: the roll-up is absent from
**5 of 5** close artifacts a reader can reach, and either string stands in **0 of 952** record
files — while the same reader scores two neighbouring fields *declared* 10 and 12 on the same
corpus, so the zero is a fact about the record and not a failure of the instrument. **A reader
exists** (a NOTICE-severity rule under the three-batch convention, carrying a two-field close-artifact
obligation: the ledger roll-up and a declared perimeter). What is still owed is the operator sitting
that decides whether the shape is portable enough to be numbered. ⚠ **It does not judge the review's
quality** — a reviewer can write *rigorous* and have skimmed, and no keyed field detects that; what
the record gains is that the choice of depth, and the choice not to read, become facts instead of
acts.

## Phase 1-2 · Requirements, spec & review — designing oracles that can fail

The V-model writes acceptance tests at spec time, so oracle-design controls belong here — apply the
meta-rule to every AT you spec.

### C-10 · Acceptance test exercises the shipped surface off a NON-DEFAULT value
*(batch 14, 16, 17)*

**Failure closed.** A default-valued fixture makes a test pass without touching the logic under
test: a test run with a policy flag left at its default exercises the un-branched path and asserts
nothing about the branch that shipped.

**Example.** A formatter takes `precision`, default 2. A test that formats `3.14159` and asserts
non-emptiness passes whether precision is honored or ignored. Set `precision=5`, assert the exact
string `"3.14159"` — the assertion moves iff the branch works; write **one AT per policy branch**.

**Rule.** Assert content, not non-emptiness; drive each test off a value that differs from the
default; one acceptance test per policy branch.

### C-12 · Output-then-consume chains through the written artifact
*(batch 16, 17, 20, 26)*

**Failure closed.** A producer and a consumer can each pass their own unit test while the artifact
that flows between them — the file, the serialized record — is malformed. The bug lives in the
seam, and neither isolated test can see the seam.

**Example.** A handler writes a report to disk; a downstream service reads it. Test the full
chain: call the handler → **re-read the written artifact from disk** → feed it to the
**unmodified** real consumer → assert the exact end outcome. If you shimmed the read, you tested
your shim, not the seam.

**Rule.** The acceptance test drives handler → re-read the on-disk artifact → unmodified
consumer → exact outcome. No shim across the seam.

### C-13 · Measure rendered geometry at DRAFT time (+ C-13.1 deficit-matched fallback)
*(batch 17, 18, 22, 24, 26)*

**Failure closed.** A layout declared "ready" on paper arithmetic that the real renderer
contradicts — ratios measured up to **4.5x off** the truth; a fallback rung chosen for cheapness
cannot close the deficit actually measured.

**Example.** Before calling a geometry story done, drive the real layout engine through its
headless test driver at each size and **measure both dimensions** of the rendered
regions. Pick a fallback by the **measured deficit**, not by which is easiest.
(Origin figures in `REFERENCE.md`.)

**Rule.** A geometry story is not "ready" until measured under the real renderer at draft time;
size fallbacks to the measured deficit (C-13.1).

### C-15 / C-15.1 · Probe a framework symbol's runtime identity; grep its assignment sites
*(batch 23, 24)*

**Failure closed.** A spec that reasons about a named framework symbol from its *name* can ship
dead code: a sentinel constant on a framework class resolved at runtime to an INHERITED
constant whose value was `False` — so a spec-conformant filter against it was **always false and
shipped dead, twice**.
Only `repr()`/`type()` against the pinned version catches this.

**Example.** At draft time, print `repr(SYMBOL)` and `type(SYMBOL)` in the pinned environment and
read the actual identity. Then (C-15.1) grep **every assignment site** of any state your story
consumes, so a value written somewhere unexpected can't invalidate the branch silently.

**Rule.** Probe a named framework symbol's runtime `repr`/`type` at draft (C-15); grep every
assignment site of consumed state (C-15.1). Names are not identities.

### C-31 · Input-set-as-oracle
*(batch 33, 47, 48)*

**Failure closed.** A test that certifies a **universal** ("every hue is distinguishable") is only
as strong as its input set — and a hand-listed input set is a spec artifact that can omit the one
failing member. Code mutation cannot find this: the code is correct; the *oracle's input list* is
wrong, one level above the code.

**Example.** A census asserted every hue in a palette was distinguishable. The arithmetic was
exact — but the hand-listed set **omitted 38.44°**, the single hue that failed. The test must
**derive or guard its input set**, never trust a hand-typed list to be exhaustive.

**Rule.** A test of a universal must derive or guard its input set; a hand-listed domain is an
unproven spec claim, not an oracle.

### C-40 · Falsifiability BEFORE correctness — "can it go RED?" is a separate question
*(batch 63-64; attribution corrected 2026-09-07 — forensics in REFERENCE.md)*

**Failure closed.** A predicate can be **correct** — valid arithmetic, complete input set, measured
threshold — and still **never mention the thing under test**. C-10 mutates the CODE, C-31 mutates the
INPUT SET, C-39 executes the THRESHOLD; a predicate can satisfy all three and remain **invariant under
the change it gates**.

**Example.** Five predicates each related an accounting helper to a string join — both pure functions
of the same input — while the **file writer**, the actual subject, never appeared in the expression.
The executed counterfactual read `RED cases against the WRONG implementation: 0`.

**Rule — two limbs, both discharged by execution.**
1. **The declared subject must be IN the expression.** *Corollary:* when the declared subject is not
   the subject of the change, the predicate is a **regression PIN, not a gate** — keep it and label
   it so.
2. **A quantified set must come from the RULE, not the implementation.** A set drawn from what the
   code currently handles certifies a completeness the code does not have.

**Rider — the verdict is PER RESOLVED ARM, never the process exit code.** A runner exits non-zero if
ANY node fails, so one aggregate verdict cannot say **which** arms reddened: an inert arm hides
behind a sibling that failed. Record one verdict per resolved node id, NAME the arms that stayed
green, and assert the expected **arm count** first — a baseline resolving ZERO arms makes the
all-green check compare `0 == 0` and pass. **An arm the harness cannot see is an arm it cannot
report inert.**

**Rider — a mutation that REMOVES THE GUARD tests nothing; the discriminating one corrupts the
SUBJECT the guard reads** *(flow rev75)*. **Discharge, at authoring time:** *name what this mutant
makes WRONG*, not what it removes.

**Rider — "it applied" is not "it landed where it matters"** *(flow rev75)*: the anchor matches
EXACTLY ONCE, on REACHABLE code, and the mutated expression names an observable THE ASSERTING NODE
READS. The harness enforces uniqueness mechanically; reachability and observability are performed by
a reader.

**Discharge:** name the mutation, **execute it**, paste the transcript, then **restore it, confirmed
by hash** (for a NET-NEW file the RED is captured by **moving the file aside** — `C-20`'s move-aside
— never by `git stash`). **Reader: `V33`/`V44`; per-arm verdicts under `V37` `Mutation verdicts`.**
Measured fire record in REFERENCE.md.

**Limit — a rejection count cannot see this control working.** Its live use is authoring-time
shaping rather than rejection at a gate,
because the vacuity never reaches one. **A control that works leaves no rejection**, so a count of
rejections is structurally blind to it working.

**What no rule reaches, said plainly:** `V33` tests for a **filled** field, never an **executed** one.

### C-59 · Evidence bytes live at a declared home, verbatim, and the store is verified
*(batch-66; flow rev66)*

**Failure closed.** An artifact is committed as PROOF and the hash recorded beside it *is* the
contract. Either of two independent failures voids the proof while every gate stays green: the STORE
rewrites the bytes on the way in, so the digest no longer describes what is stored; or the bytes are
kept somewhere that does not survive.

**Example.** batch-66 committed `.PRE` copies of four out-of-VCS files whose recorded SHA-256 was
the entire rollback contract; `core.autocrlf=true` normalised them on the way in, so a rollback
would have restored bytes that do not hash to the original. **`text eol=lf` is the WRONG fix** —
evidence carries mixed line endings by nature, so only `-text` is correct.

**Rule.** An evidence artifact is written to the home `artifact_homes.evidence` declares (durable,
named at the batch, **never a session-scoped `Temp` path**), stored **byte for byte**, and cited
with the **SHA-256 of the bytes at that path** — re-derived from where the artifact LANDED.
*Whenever a hash is the contract,
the storage layer is part of the system under test.* Assert the STORED artifact, never the one you
handed to the store.

**Reader: `V41`** on the packet's **`Evidence files`** section (artifact · path · SHA-256, with a
declared-empty wording); it BLOCKs a cited digest that disagrees with the bytes on disk. Honest
limit: a `vault:` home's digests are reported, never verified. (Published-figure correction in
REFERENCE.md.)

### C-58 · A mandate nothing reads is a paragraph
*(batches 88-89; flow rev63)*

**Failure closed.** A process can declare a field, a section or a pass **mandatory** in its own
template and then ship for months with nothing that reads it. Skipping it costs nothing — no
finding, no notice, no exit code — so it gets skipped, and every gate stays green while it is.
`C-40` asks whether a predicate can go RED; this asks the question one level out, of an obligation
that has **no predicate at all**.

**Example.** The flow's own `commands/dev-flow.md` mandates an independent `code-reviewer`
pass at every increment gate and says a HIGH blocks.
batch-88 ran it at **7 of 7** increments; batch-89 ran it at **0 of 6**, wrote `ABSENT` in all six
packets, shipped **five flow revisions** — and **every gate passed**.

**Rule.** Every field or pass a template or command calls MANDATORY owes either **a mechanism
that reads it** or **a written exemption saying why not**. Two corollaries: the reader must be
keyed on a **declared field**, never on a phrase (the corpus states one obligation in **19 sites,
19 distinct phrasings**); and the **declared-empty wording is part of the mandate** (`none —
<reason>`, or `ABSENT`), so an absence DECLARED and an absence OMITTED do not render alike.

**Discharge.** In the flow's own tooling: at every revision that mints or amends a MANDATORY field,
name the rule that reads it in the same increment, and prove the reader RED on a document with the
field deleted and on one holding the placeholder.

**Rider — a fix can be correct, LAND, and be held by nothing** *(flow rev75)*. A fix can land
carrying **no arm that would redden if it were reverted** — its correctness is a fact about the day
it shipped. Distinct from `C-57`: that asks whether an instrument CAN report failure; this asks
whether any instrument is POINTED AT THE FIX AT ALL. **Discharge, one question at the gate:** *name
the arm that reddens if this diff is reverted* — and when the honest answer is "none", write that
down (`C-55`'s declared emptiness). (Measurement saga in REFERENCE.md.)

### C-57 · An instrument is blind until it has reported a failure
*(batch 89; flow rev59-60)*

**Failure closed.** `C-40` asks whether the **acceptance predicate** can go RED. Nothing asked it of
the **measuring apparatus** — the substring reader, the AST walk, the regex, the self-comparing arm
— and that is where the corpus's instrument defects lived. None carries an `AT`/`TC` id; none sits
under any gate.

**Example.** A backwards regex under colour reported `0 killed / 12 survived` when 12 were killed;
an AST walk on the running interpreter reported a Python floor of 3.7 when it was 3.12. **The law is
one control, not five fixes.**

**Rule.** A verification instrument must demonstrate it can report **FAILURE on a known-bad input**
before a single PASS from it is believed — and the known-bad input must corrupt the instrument's
**mechanism**, not merely its **verdict** (replacing the whole probe with a constant is not a
mechanism test: `N7-case-probe-is-assumed` did so and **survived twelve mutants** — the verdict was
armed, the mechanism was not). And score three verdicts, never two — **KILLED / CRASH / SURVIVED** —
plus a fourth (flow rev64): a mutant that never **applied** is **BAD**, not SURVIVED, and `BAD`
fails the run.

**Sub-cases, one law each:**
- **FIXTURE — the predicate is fine and the DATA cannot tell the difference.** A fixture's own
  symmetry can collapse the distinction the predicate tests (all-`F` fixtures: leading-K and
  trailing-K hex are byte-identical). **Ask of every fixture: *what does this make
  indistinguishable?*** Add one **deliberately non-uniform** arm with its discriminating
  precondition ASSERTED.
- **INTER-TOOL — the tool that ran the step is not the oracle that it ran.** A step can **report
  success and have done nothing** — strictly worse than a crash, because a silent no-op propagates.
  The gate is an **observable delta measured by something that did not run the step**. (Same shape
  as `C-60` one abstraction up.)
- **PARTITIONED-INSTRUMENT — an `any` over an instrument that reports a VECTOR passes on the
  instrument's own good half** *(flow rev75)*. **An arm over a partitioned instrument asserts the
  WHOLE partition, by name and by count**; `any` is admissible only where the instrument returns one
  thing. Unlike `C-40`'s arm-count limb: **here the arm sees every member and is satisfied by one.**

**Discharge.** In the increment packet, `**Instrument RED-proof**`: per instrument, the known-bad
input fed to it and the FAILURE it returned, before any PASS from it was believed; write
`none — no instrument beyond the suite` when there is nothing to declare. **Reader: `V31`** — it
reads whether the question was ANSWERED, never whether the answer is true.

### C-60 · The harness that proves a check must not share a fixture with it
*(corpus: an outside course-verification harness, 2026-09-10; flow rev71)*

**Failure closed.** `C-57` prescribes mutation testing as the remedy for a vacuous check. **That
remedy fails silently when the mutation harness resolves its target through the same constant,
path, or discovery helper as the assertion under test.** One root cause then disables both the
check and its detector, and nothing can go red.

**Rule — three limbs.**
1. **The harness resolves its inputs independently of the artifact under test, and relative to its
   own location** (`__dirname`, `Path(__file__).parent`). A shared absolute path, a shared config
   constant and a shared discovery helper are the same defect wearing different clothes.
2. **A mutation run that cannot resolve its target is a hard RED, never a pass.** Assert the
   expected mutant count *before* running. `total=0` is failure, not success.
3. **A green baseline is not evidence the harness works. The only evidence is a killed mutant.**
   `BASELINE green` immediately followed by a crash is this defect's signature.

**Example.** A verifier declared `SIBDIR` as an absolute path to a directory that no longer
existed; fifteen assertions filtered that set through `fs.existsSync`, got `[]`, and reported
green — and both mutation harnesses carried the **same dead constant**. Measured, before → after
resolving all three constants from the harness's own location: **16 failures / 530 asserts → 0 /
584**; both mutation runs unrunnable → **killed=22 survived=0** and **killed=5 survived=0**.

**Rider.** Extends `C-40`'s arm-count rider one level up: assert the harness's own **input
resolution**, not only its arm count — an arm count is meaningless if the set being armed is empty
(`C-55`). (In-house exhibits in REFERENCE.md.)

### C-43 · Premise evaluation — verifying work against a spec never verifies the SPEC's claims about the world

**Failure closed.** Every control above asks whether a *predicate* is sound, executable or
falsifiable. None asks whether the **claim the predicate rests on** is true. A stage can be fully
compliant with a requirement whose premise is false — and the gate passes, because the gate was
checking conformance.

**Example.** A design batch cited a module's `variant_id=None` line as *"the single-variant
assumption, explicit in the code"*. The line was real and at exactly the cited address — but sat
inside a **different block handler's** input; the module had **no such dimension at all**. Ten
premises executed; **eight held exactly** — which is why "it looked verified" is not a defence.

**Rule — three verdicts, three tiers.** Verdicts: ✅ **TRUE** (an *executed* probe — command
output, a `file:line`; **citing another document is not evidence**) · ❌ **FALSE** (blocks) · ❓
**UNDECIDABLE** (blocks until decided or declared out of scope **in writing**). Tiers: **axioms**
(validated AND verified — law by default) · **hypotheses** (*whatever this batch introduces or
inherits — written down is not verified*) · **premises** (claims about the world — executed against
disk, never trusted).

**An axiom is re-litigable, but only CONSTRUCTIVELY** — on an executed counterexample or a logical
invalidation, in practice almost always **INCOMPLETENESS**. **The disposition ENLARGES the
requirement; it never deletes it** (measured example in REFERENCE.md).

**Reader: `V45`, flow rev69**, on the requirements document's `**Premise evaluation**` field
(`req-template.md` §2.7): one of the three tokens or the legal empty `none — <why no premise
applies>`; a cell reading `done` scores **unidentified**. (Adoption census in REFERENCE.md.)

### C-55 · An emptiness is doing work — say which kind
*(batch 84)*

**Failure closed.** A result or a guard that depends on the tree **containing no instance of some
case**. Nothing is wrong today: the claim is true, the suite is green, and the change that will
falsify both is one nobody will connect to either. C-40 asks whether a predicate *can* go red;
C-43 asks whether a premise is *true*; C-55 asks **what is this resting on that is only
accidentally the case right now?**

**Rule — two limbs.**
1. **The emptiness is the FINDING.** When the result is an *absence* ("no X exists in the tree"),
   the property that made the search wide enough is **part of the result**: narrow it later and
   every derived claim weakens while every guard stays green. Guard the over-breadth, and **say in
   the guard's own docstring that it protects a CONCLUSION, not a behaviour**.
2. **The emptiness is an ACCIDENT of today's data.** A guard clause that is a **no-op on the
   current tree** is untested however green the suite; the tell is mechanical: **mutating it
   changes nothing today.** So: **a conjunctive criterion needs one mutation per conjunct**, and
   **mutating a stage is not mutating the pipeline**.

**Rider — an absence is admissible only if the probe that produced it CAN produce a non-absence.**
Run the same probe, unmodified, over a case known to be present. **Uniformity over heterogeneous
inputs is the TRIGGER for that control, never the verdict** — the correct answer can be uniform
too, and treating uniformity as a verdict false-fails correct work (`C-53`). **If no known-present
case can be constructed, say so and downgrade the claim from a finding to an unverified
observation.**

**Example.** A batch's entire result — no widget address is assembled from parts — was sound only
because the binding walk deliberately **over-collects**. In the same batch, filtering unresolved
rows passed **all sixteen** guards because the tree holds **zero** instances of the case.

**Discharge:** construct the case the tree lacks — a fixture tree, an in-memory module, a
synthetic input — and assert the property against it. *"There are none today"* is the reason the
guard is needed, never a reason to skip it. (Probe measurements in REFERENCE.md.)

### C-56 · An evidence transcript is corpus input
*(batch 86)*

**Failure closed.** An artifact written to PROVE something is read by the same scanners as the
work it describes — and no scanner distinguishes a token being *reported* from one being
*declared*.

**Rule — three consequences.**
1. **A mutation reverted in its target file but SPELLED verbatim in a transcript is not
   reverted.** A sha256-proven revert can verify the wrong plane. **Describe mutations by position
   and operation** ("the id's fourth character, digit → letter"); never paste the mangled token.
2. **Dotted-range id shorthand is forbidden wherever an id-scanner reads.** `AT-020..024` is not a
   range to a tokenizer. Enumerate, or write `AT-020` through `AT-024`.
3. **AN ARM'S OWN NAME IS CORPUS TOO.** Citing an arm BY NAME in a canon document puts its id in
   the corpus — the selftest goes red and blames the id rather than the citation. rev75 did that and found it
   with its own selftest. **The cost is a standing, invisible constraint on PROSE** — a name that may
   never be written in the corpus it guards — and it is recorded at the arm and here rather than
   closed by widening a negative control from inside an unrelated revision. *A known cost with a named
   size is a different object from a surprise.*

**Example.** An Inc-1 packet quoted the RED arm's corrupted id and two range tokens; the Atlas
id-scanner adopted **three phantom ids**, one `--atlas --write` from the committed derived plane.
Hardening the scanner does not make a mangled token in the corpus true.

**The WILDCARD-STEM sub-case.** Family-wildcard forms (`AT-057.*`, `AT-057*`) are refused — a
scanner that mints ids the corpus never declared **manufactures its own corpus**. (Declared
residual and Atlas-moved measurement forensics in REFERENCE.md.)

### C-42 · assert the EMITTED form, never the rendered one
*(batch 60-63 · the C-35 rider, and C-42 for stack specifics)*

**Failure closed.** Executing the producer is **not enough** if the assertion is then written
against the form a *human reads*. Producers escape, encode, wrap and substitute, so confirming a
named output *exists* passes while a search for its readable form **false-fails a correct
implementation**.

**Example.** A snapshot export emits `&#160;` entities for spaces, so a literal search for a
visible label returns **0 matches** while the label is plainly on screen; the emitted form returns
**29/29**.

**Rule.** Write the predicate against the bytes/tokens the **producer emits** — run it, paste the
actual output, assert against that. Prefer the producer's own structured output to a substring
search over serialized text: a substring search cannot tell a value from its own encoding.

**Reader/Discharge:** the `**Emitted-form assertion**` field in `increment-template.md`, read by
**`V38`** (flow rev64), keyed on the increment packet, where an artifact is actually emitted.
(Measured fires and the recorded dissent in REFERENCE.md.)

### reader-as-oracle (+ a MANDATORY corrupted negative control)
*(batch 09-13 · 5 uses)*

**Failure closed.** Validating a writer by inspecting its own output is circular — the check
agrees with the writer's bug. And a round-trip through a reader is only evidence if the reader
would **reject corruption**; a round-trip that passes on garbage proves nothing.

**Example.** Validate a new writer by round-tripping its output through the **existing trusted
reader**, and **always** include a corrupted negative control (feed the reader deliberately broken
bytes and assert it fails). Pin **one canonical comparison form** — a `repr` mismatch between the
two sides makes the comparison unpassable, i.e. vacuous.

**Rule.** Round-trip a writer through the trusted reader; mandatory corrupted negative control;
one canonical comparison form.

### KAT anchor — pin at least one externally-published known answer
*(batch 12)*

**Failure closed.** Self-consistency tests agree with their own bug. If every test derives its
expectation from the same implementation, a shared error is invisible — the whole suite is
internally consistent and externally wrong.

**Example.** Anchor at least one **Known-Answer Test** to an externally-published value. In the
corpus, `crc32(b"123456789") == 0xCBF43926` (a standard published CRC check value) caught a seed
bug that every self-consistent test had ratified.

**Rule.** At least one assertion pins an externally-published known answer, not self-consistency.

### assert-the-discriminating-negative
*(batch 11, 12)*

**Failure closed.** Asserting only what must be present, never what must be absent. A test that
checks the right file exists misses that a **wrong** file was also written, or that bytes that
must never appear did.

**Rule.** Assert the discriminating negative — the artifact that must not exist, the bytes that
must not be written.

### The coincidence oracle
*(a UI-design session, 2026-08)*

**Failure closed.** A test that computes its expected value with **different logic** from the code
under test — normally good practice — where the two agree **by coincidence** rather than by
correctness. Green test, wrong code, and the agreement is an accident of the fixture.

**Example (measured).** A screen rendered a scrolling *window* of N items; its test asserted the
count by measuring the whole source `dict`. They agreed only because that fixture's window
happened to be the same size as the dict. When the window bug was **fixed**, the test went red —
and the red looked exactly like a regression introduced by the fix.

**Why the META rule does not catch it.** Mutating the *code* does turn this test red, so it passes
the discriminating-check test. What is broken is **referent**: the oracle measures a different
quantity that currently has the same value — a third failure mode alongside the fixture (C-31) and
the assertion.

**Rule.** When an oracle recomputes a value independently, **name the quantity in the assertion
message**, and prove the two quantities are the same by making them **differ** — choose a fixture
where the dict and the window are provably different sizes. If you cannot construct such a
fixture, the two are not independently verified; you have one measurement written twice.

**Corollary for reviews: a test that goes red when a bug is fixed is evidence about the TEST, not
about the fix.** Chase the oracle before reverting anything.

### Spec-side census rules (from §3)

- **Symbol- and consumer-citation.** A named private symbol needs a grep-verified `file:line` or
  it is a blocker. Cite the consumer's real **input type** before binding a producer to it. (b05,06,08,12)
- **Cross-cutting contracts go stale on any edit.** Re-derive, don't trust the cached version. (b07,08,09)
---

## Phase 3 · Implementation — census, blast-radius & test hygiene

### C-53 · A rule that false-fails correct work is as expensive as one that passes wrong work

**Failure closed.** The failure mode nobody budgets for is the **false block**: a checker scoped to
the wrong unit, flagging artifacts that were correct all along. It is worse than a missing check,
because a checker that cries wolf gets routed around — and the checks that *were* sound go with it.

**Example (measured, this flow's own validator).** A rule implemented **line-scoped** produced **44
blocks** across the historical corpus — every one false, because the convention puts those fields
on their own lines. Re-scoped to the **requirement block**, the same corpus yields **14**, all in
batches that genuinely predate the rule. The defect was the unit, not the rule.

**Rule — three habits.**
- **Run a new rule over a corpus you believe is CORRECT.** A rule that lights up everywhere is far
  more likely to be mis-scoped than to have discovered a systemic defect.
- **Scope to the unit the convention uses** — block, section, file — not to the unit that is
  easiest to iterate.
- **Pair every rule with a positive AND a negative control** (the RED and the GREEN fixture), kept
  in the tool itself. *Can it go RED?* and *does it stay GREEN on correct work?* are different
  questions; passing only the first is how a false-failing rule ships looking rigorous.

### C-52 · The four conditions that make a fork safe — and the one that changes category

**Failure closed.** Parallel lanes without a frozen contract are not parallelism — they are **a
collision with a delay**, discovered at integration, the most expensive moment.

**Rule — four conditions, checked before forking; if one is missing you do not fork:**
1. **Frozen contract.** No shared interface is touched inside a lane; if one must change, the work
   returns to the trunk.
2. **Disjoint FILE sets, not just modules.** Two lanes may not edit the same file, not even
   different regions of it.
3. **Crossed reverse census.** The shared-surface family is run per lane and shared *before*
   starting. **This is the only check that structurally cannot be performed from inside a lane** —
   which is precisely why it gets forgotten.
4. **One owner of the trunk.** Requirements, traceability, backlog and spec are never written from
   a lane. Lanes propose; the trunk integrates.

**The condition that changes category under parallelism:** C-40's *capture the RED where no other
session is reading* was a precaution with one agent; **with N lanes it is a correctness
condition** — each lane needs its own worktree, not for convenience but for **evidence
isolation**. **The honest economics:** a fork buys **wall-clock, not work** — the batch ends when
the longest lane ends.

**Reader: `V46`, flow rev69** — also the CROSSED census's reader — on the requirements document's
`**Fork preconditions**` field (`req-template.md` §2.8); `none — this batch runs one lane` is the
legal empty and MUST be written. `V43` reads the per-lane `Reverse census`. (Adoption census in
REFERENCE.md.)

### C-51 · Layer 0 — the unit that both existing layers look past

**Failure closed.** White-box tests sit over the low-level requirement; black-box acceptance sits
over the user's story. Both look *past* the unit, so a bug inside a single function is visible to
neither.

**Rule.** Layer 0 is additive: it replaces nothing. The threshold must be operable, or it degrades
into taste — two criteria, either one sufficient:
- **decision** — the unit has 2+ paths (`if`/`elif`/`for`/`while`/`except`/a conditional
  comprehension), i.e. **cyclomatic complexity ≥ 3**, measurable with a standard AST walk;
- **boundary** — the unit **transforms data crossing a declared module boundary**: parses,
  serialises, computes an offset, validates, converts.

Explicitly **out**: pure delegations, getters, UI wiring, constructors that only assign, one-line
branchless functions — without that exclusion list the rule silently becomes "test everything".
**Anti-theatre clause:** layer 0 is measured by **mutation**, never by line coverage.

**Reader: `V49`, since flow rev70**, on the keyed `**Layer 0:**` roll-up in the active batch's
`04-validation.md`, or the legal empty **`none — no unit met the decision or boundary
criterion`**. It reads whether the question was ANSWERED, never whether the count is true.

**Rider — an arm over a HELPER is not an arm over the RULE; an arm over the CORE is not an arm over
the LOADER** *(batch-89)*. The layers above look past the unit by **scope**; this rider looks past
it by **call depth**: an arm that drives the private helper never executes the rule's own entry
point — its marshalling, defaults and guards. **The authoring question is which SYMBOL the arm
names**, answered by reading the arm, never by running it: a helper-level arm and a rule-level arm
are both green.

### C-50 · One home per artifact — and the link crosses by ID, never by content

**Failure closed.** Splitting artifact homes without id-linking breaks traceability instead of
organising it: two copies means one is false and nobody knows which — exactly how a canonical
backlog went ~10 batches stale while every phase kept reading it.

**Rule.** **The dividing line: if a mechanical check needs to READ it, it goes in the repo; if a
human reads it to decide, it goes in the document store.** The split rots in two specific ways:
- **Copying instead of routing.** This invariant is STRUCTURAL, so no assertion over output can
  guard it *(b84)*: collapsing two copies of a predicate into one call site is behaviour-preserving
  **by construction**. Guard it by **parsing the artifact and asserting the shape**, never by
  comparing outputs. **One home per artifact, declared in configuration, and no command may write a
  path that is not declared there.**
- **Linking by content instead of by id.** The requirement in the repo cites `PDR-<batch>#D3`; the
  record in the store cites `R-014 v3`. **The ids are the glue.**

**Where it lives matters too.** Design deliberation has weak traceability to code, so it belongs in the
vault, sealed and cited by id. But **what decides code lands in the repo** — a frozen interface or a
design characteristic is reflected in the requirement or in the module map, which are versioned beside
the code. The vault keeps the deliberation; the repo keeps the commitment. A split that copies instead
of citing is how the canonical source starts drifting (see C-44).

### C-49 · Forward applicability — every output of a design review must be someone's declared input

**Failure closed.** Adding a design phase is the easiest way to add cost that *looks* like rigour:
the review produces a document nobody downstream ever opens, and nobody notices because a thick
artifact reads as diligence.

**Rule, distilled from ISO/IEC/IEEE 15288.** The standard defines *Design Definition*'s outputs as
**"design characteristics and design enablers necessary for implementation"**. Necessary *for
implementation* — that is the whole test. So: **everything a design review produces must be NAMED
as the input of a later activity. If an artifact is nobody's input, it does not belong in the
review.** Make it an artifact: the proposal carries a **forward-applicability table** — one row per
output, with its named consumer. **A row with an empty consumer column means delete the output or
justify it.**

**Corollary — how big may a design review be?** Half the batch, *provided that half is the literal
input of the other half*. Cost is not the measure; consumption is — at close, count how many of
the review's outputs were actually consumed.

**READER, since flow `rev77`: `V52`.** For seventy revisions this control was realised in four
places and cited by no rule — `C-58`'s mandate-with-no-reader, four times over. `V52` reads the
ACTIVE batch's staged design proposal(s) (NOTICE, `S1`) and asks TWO questions, because the
shipped template PRE-FILLS the consumer column: every row must NAME a consumer, and at least one
must say WHERE that consumer reads the output. Scoped by `stations_active` naming `PDR`, never by
mode (`C-53`). ⚠ **What it cannot do:** it reads the LOCAL STAGING, and whether the rows were
ANSWERED — never whether the consumer consumes anything. (Measurement in REFERENCE.md.)

### C-48 · A trigger's NON-activation is evidence, and is recorded with its probe

**Failure closed.** `"B1 did not fire"` with no probe output beside it is textually
indistinguishable from `"B1 was never evaluated"`, and the second is what actually happens under
time pressure.

**Rule.** Record **id · verdict · probe output** for every trigger, fired or not. 

Three corollaries that keep the mechanism honest:

- **Triggers only raise.** They turn controls on; none turns one off. A floor, never a ceiling — and the
  strict lane ignores them upward, so a trigger can never be the reason something got skipped.
- **Monotonic within the batch.** Once fired, it stays fired even if scope shrinks. Lowering rigour
  mid-flight requires closing the batch, which leaves a record; silently relaxing does not.
- **Apply C-40 to the triggers themselves.** A trigger that has never fired in several batches is not
  proof the code is clean — it is a probe that must demonstrate its own RED or be rewritten. A condition
  that cannot be evaluated *before* code exists is not a trigger at all: it is a question for the design
  review, and saying so out loud is the difference between a decision and a drift.

**Reader: `V43`, from flow rev68**, on the increment packet's keyed `**Reverse census**` row
(NOTICE), accepting the declared empty `none — this increment touches no code symbol or shared
surface`; keyed on the FIELD, never on the row number. (Adoption census in REFERENCE.md.)

### C-47 · The increment budget counts SOURCE files, not the total

**Failure closed.** **A cap on the TOTAL files per increment penalises writing tests:** under a
flat "≤5 files", an increment of 3 source + 3 tests is a violation, while 5 source + 0 tests
complies. The cap was invented to bound the *blast radius of the code change*; counting tests
inside it inverts the incentive precisely where you least want it inverted.

**Rule.** Cap **SOURCE** files (default: ≤4). Leave tests **uncapped** — each still has to map to
its TC/AT, which is the real control on them. Keep product docs and the flow's own `.dev-flow/**`
artifacts outside the count. **Do not add a total ceiling to compensate**: any total cap
re-introduces the defect. Reaching the cap is a **⚠ notice** (declare why the increment could not
be cut smaller), not a block; exceeding it is declared and reviewed, not auto-rejected.

**Why the numbers, and how to re-derive them.** Measured over the 178 parseable increment packets of
the record's 67 batches (95.7 % coverage; the 8 unparseable ones are enumerated, not dropped): median 3
total files, p90 6, max 12. Of the **24** increments that broke the old flat ≤5, **16 — 67 % — touched
≤4 SOURCE files**; their means were 4.2 source and 2.5 tests. 95.3 % of all increments touch ≤4 source
files; tests run median 1, p90 3, historical max 4. Re-run before changing the number again:
`increment-file-history.py` — the flow's own analysis script, canon-only and not shipped with the skill — pointed at the project you are arguing about.

**Two honest limits, stated because the number will be quoted.** (i) It is ONE project — a single-language UI
app with a frozen renderer; a backend with migrations or a component-heavy
frontend will have a different shape. (ii) Increments that were cut *in order not to break the old cap* do not appear as breaches:
there is a survivorship bias no later count can recover. The rule is defensible for this corpus and
for what resembles it, not as a universal.

### C-14 · A move OR a correction greps its whole population (census the readers, and the claims)
*(batch 21; **trigger widened 2026-09-06** from batches 88-89)*

**Failure closed — the original.** Moving an artifact to a new on-disk location silently orphans
every test and consumer that still reads the old path. A green suite hides it because the orphaned
readers now read stale or absent data without erroring.

**Failure closed — the extension.** *A correction has a population.* Batch-88 landed **8+**
corrections at one site of several — **every one found by a lens and none by a rule.** `C-14`'s
trigger was *a path MOVE*, and a corrected sentence is not a path move — **so this control fired on
none of them**, which is why the trigger is widened rather than a new control minted.

**Example.** You relocate `build/report.json` to `dist/report.json`. Recursively grep (`rglob`)
every reader of that artifact; **count a net-zero in-place rewrite as a touched file**. And: you
correct a sentence a design review quotes — enumerate every artifact asserting that claim **by the
assertion category, not by the marker**, before editing the first one. **A census keyed on a marker
cannot see what carries no marker.**

**Rule.** On any on-disk location move **or any correction to a claim that appears in more than one
artifact**, census the whole population by recursive grep keyed on the assertion category, **before
the first site is edited**, and record the method with the count; net-0 in-place rewrites still
count as touched, and sites left unedited are named with their reason. The supersession-completeness
inspection is this census's executed form and lives at `P3`. **Reader: `V32`**, keyed on the
declared `**Correction population**` field, never on a sentence (the corpus states this obligation
in nineteen distinct phrasings — forensics in REFERENCE.md).

**SECOND READER, since flow `rev78`: `V53`, and it reads the CLAIMS limb rather than the
readers limb.** A correction's population is not only the files that must change — it is every
SENTENCE that cites the thing being moved, and a citation is a claim that can be EXECUTED.
`V53` resolves every `path::symbol` anchor in `.dev-flow/**/*.md` against the working tree — the
file must exist and the symbol must be BOUND in it — sharing `V14`'s resolver (`C-50`).
⚠ **A wrong SYMBOL is worse than a stale LINE number:** a stale line fails visibly; a wrong
symbol lands the reader inside a real, plausible method. **Severity
is split by corpus:** a wrong anchor in the ACTIVE batch is a BLOCK, the CLOSED record a census
and never a block, because those batches are sealed. ⚠ **What it cannot do:** it asserts the
symbol is BOUND, never that the sentence around it is true. (Exhibit and rulings in REFERENCE.md.)

### Census & blast-radius principles (§3)

A **census** is a completeness principle, not a fixed grep list — and blast-radius is how far a
change actually reaches, which is almost always further than it looks.

- **A census is a principle, not a checklist.** Never stamp "VERIFIED COMPLETE": re-running an
  incomplete checklist can't detect that it is incomplete. Key the census on the **assertion
  category**, not on a frozen list of sites. (b09,10) It is `C-14`'s rule stated without a trigger
  — see `C-14`/`V32`.
- **Build disposition tables from MEASURED behavior, not inferred.** In the corpus, measuring gave
  355 true entries vs 192 inferred — inference missed **~half** (+85%). If you didn't run it, you
  don't know it. (b06,07)

### Test hygiene & environment (§5)

- **Never delete a test in the same increment that changes the behavior it guards.** Port the
  assertions first. A cleanup once killed a bar's only oracle (plus 3 nets) in one increment → an
  invisible-bar bug reached PR-QA. (b47)
- **Never edit a source file while a suite that AST-inspects it runs.** The line-shift produces
  phantom failures; three agents independently hit this. (b48)
- **Deterministic test inputs.** Sort filesystem-ordered collections and select by name — glob
  order is a flaky gate. (b21)
- **Kill substring false-greens.** Match `\b1\b`, not `1` (which is a substring of `100`); avoid
  reconstruction tautologies where the test rebuilds the expected value from the same source it
  checks. (b20)
- **Signed-balance test ledger:** `post = base - D + A` on **collected** counts (`base` = test
  count before the change; `D` = deleted; `A` = added). A constant offset between expected and
  observed post-count is the signature of a units bug. (b07-12)
- **Run BOTH frozen-source AND frozen-test guards.** A new test added to a frozen test file passed
  a source-only gate. (b38)
- **Lint is a gate whose exit code blocks the commit.** `ruff … || echo` swallows the exit code —
  the lint became decorative. Pre-provision the toolchain as a hard entry gate. (b32,02,03,04)
- **Never invoke the gate suite through a wrapper that RE-ENCODES the child's stdout.** `conda run`
  transcodes what the child prints; one non-cp1252 byte can destroy a whole run's evidence. **The
  transcript IS the deliverable** — a corrupted transcript voids `C-25`'s one complete run whatever
  the exit code says. Invoke the interpreter directly (`<env>/python.exe -m pytest`) with
  `PYTHONIOENCODING=utf-8`. (`C-19`'s family, batch-35; b87 `G4-03`)
---

## Phase 4 · Validation & gates — evidence that cannot be faked

### C-18 · Every acceptance test = exactly ONE distinct on-disk node driving the full chain
*(batch 29, 32, 35-38, 47, 48 — also applies at spec time when cutting increments)*

**Failure closed.** "This acceptance criterion is covered in parts" — a bit by test A, a bit by
test B — means the end-to-end chain was **never exercised as one thing**. The parts pass; the
whole was never run. Reconciliation of coverage tables is a backstop, not a gate.

**Example.** For each acceptance test there must exist exactly one concrete, on-disk test node
that drives the full chain the criterion describes; if you cannot point to it, the criterion is
**UNREALIZED**, no matter how green the neighborhood looks.

**Rule.** Each AT maps to exactly one distinct on-disk test node exercising the full chain;
"covered in parts" = unrealized.

### C-25 · Gate evidence = one complete run owned by the orchestrator
*(batch 35-38)*

**Failure closed.** Gate evidence assembled from fragments, or produced by a validation agent that
exits before the run finishes, is not evidence of a passing gate. A mandated-blocking call that
exceeds a tool's output cap is a **spec bug**, not an excuse to read partial output.

**Example.** The orchestrator runs the full gate once, reads the result **from its own captured
output**, and the validation agent is **forbidden to exit first**. If the blocking run can't fit
the tool budget, fix the spec (chunk it, redirect to a file), don't accept a truncated pass.

**Rule.** One complete gate run, owned by the orchestrator, read from its own output; no early
exit; a blocking call over the tool cap is a spec bug to fix.

### C-32 · Assert-the-painted-result
*(batch 48)*

**Failure closed.** Asserting a pre-layout proxy instead of the rendered surface. A widget's
`render()` output is **geometry-independent** — it returns the same content whether the widget is
visible or clipped to zero size — so a `display:none` strip **shipped green** against a
render-only assertion while painting nothing.

**Example.** Observe the **rendered surface and its geometry** (does it occupy cells, at the
expected position?), not just the pre-layout render string. And still **mutation-test the
oracle**: a painted-result assertion can itself be vacuous.

**Rule.** Assert the painted result plus geometry, never a geometry-independent proxy; then
mutation-test that assertion too.

### freeze-then-measure — a figure is admissible only if it names what it measured
*(batch 64)*

**Failure closed.** When a spec is still being folded, **every measurement silently expires**: each
fold changes the text, each arm figure was measured against that text, so the next fold invalidates
the last one's numbers without anyone noticing. One batch burned **three requirement iterations**
to its soft cap this way — an acceptance measured against an **890 B** body shipped at **1 975 B**.

**Rule.** Freeze the deliverable first — a manifest of each block with byte count and SHA256 — then
measure **once** against the frozen bytes, and make it normative that **a figure is admissible
only if it names the block hash it was measured against.** That is what converts "measured against
what shipped" from an assertion into a checkable claim.

**The ceiling, found by the batch that introduced the mechanism.** A false, self-contradictory
count survived every gate **because its block matched its frozen hash**:

> **A hash proves the text did not change. It does not prove the text was right.**

Freeze protects against *drift*, never against *content*. Pair it with a reader who checks the
claim.

### C-66 · Flaky is a CLASS with a measured rate, never a name on a list
*(minted at flow rev75; origin: batch-87 gate `G4-01`)*

**Failure closed.** A node fails at the gate. Somebody writes *pre-existing* or *flaky* beside it
and the gate passes. **Neither word is a measurement**, and the disposition cannot be falsified: a
genuine regression and a long-unstable node produce the identical red line. The failure this
closes is not the flaky node; it is **the sentence that disposes of it**.

**Rule — a node is flaky IFF it fails in some runs and passes in others OF THE SAME BASE, over N
runs.** Three parts, all three required:

1. **An empty source-scope diff.** The node's subject is untouched by the increment.
2. **N ≥ 10 isolated reruns on that same base**, the observed failure a member of a **recorded
   family** — a named signature, not "looks like the other one".
3. **The rate is recorded as a FIGURE.** *7 of 10* is a disposition; *flaky* is an adjective.

**The class is published as an EXECUTED OUTPUT and never as a hand list.** A pre-registered
whitelist of "known flaky" ids is the defect this control exists to refuse. batch-87's `G4-01`: of
six pre-registered nodes **5 did not recur**, while **5 of the 6 nodes that actually failed were
off the list** — a 1-in-6 whitelist clearing gates.

**What it costs.** N ≥ 10 reruns is real wall-clock at close; where reruns cannot be afforded, the
honest output is `blocked` or `not-run` with the reason, never *flaky*. No rule reads this and the
output has no declared home yet — declared, not omitted (`C-58`'s warning). (Forensics in
REFERENCE.md.)

### Gates & evidence rules (§4)

- **Gate on FILLED-ness, not presence.** Auto-reject artifacts containing placeholder tokens. A
  blank Phase-4 template once passed a gate and let a bug escape. (b15)
- **Escaped-bug proof is a ritual:** `git stash` the fix → observe the **verbatim RED** → `pop` →
  observe GREEN. For **net-new files** use **move-aside** (`C-20`), never `git stash`. (b15,35)
- **Gate decisions need transport idempotency.** A disconnect-plus-retry once injected a phantom
  approval. (b12)
- **Re-reconcile after any gate amendment.** When acceptance tests change, the increment cut must
  be re-derived, or you get an unrealized pair. (b35,36)
- **Verify-before-delete on irreversible deletion.** Prove coverage is preserved **before** the
  delete; use `git rm` not `rm`; size is not a coverage proof. (b36)
- **Pin the real base commit.** Use `git merge-base HEAD origin/main`, never a bare local ref;
  CI-portable `git diff` tests must resolve the ref or `skip`, and must never read stdout
  only. (b13,18)
- **Blast-radius gate.** Run the full suite — or at least every file importing the touched
  symbol — at each increment gate. A narrow `-k` filter in the corpus missed a crash, a perf
  cliff, and a sibling-file census, all at once. (b28,37,38,46)

---

## Cross-phase · Multi-agent orchestration (§6)

- **Parallel-for-review, sequential-for-implement.** Independent review passes (architect + QA +
  security) carry no sunk-cost attachment and converge on real blockers; per-increment gating
  localizes defects. (b01,05,06)
- **Interruption/resume.** Re-verify on-disk state before extending work — never regenerate
  finished work — and checkpoint where the failing tests ARE the specced RED. (b24)
- **Subagents must not run git mutations on a dirty tree.** A `git checkout` once discarded
  uncommitted work; a commit once landed on a stale branch. Commit promptly in a contended
  tree. (b07,12,33,46,47,48)
- **Long-run liveness: a PID's existence is not evidence — the command line is.** A 57-minute run
  was nearly killed on mis-attribution; a `.output` file can read 0 bytes while live. (b33,46,47,48)
- **Shared-namespace collision.** Two individually-correct increments can collide in a finite
  container-scoped namespace (hues, keybindings, ids, CSS specificity). Symbol-keyed censuses are
  **blind** to this — same value, different symbol — so you need a `resource → {claimants}`
  reverse index. (b48)
- **Provenance-stamp derived/rendered state** so a stale render fails loud instead of silently
  showing old data. (b38,48)

**Fix ids with per-id SEMANTICS before dispatch, not just ranges**; **brief a discharge audit
against the SOURCE reviews, never the fold's own amendment table** — a green amendment count cannot
see what the fold dropped (one fold: 163 union items · 20 dropped silently); **never read and write
the same artifact from two sessions at once.**

## Cross-phase · The security lens on "just text" (§7)

> **The tell is not "new external surface" — it is "new string reaching a rendered/persisted
> surface."** The corpus's security defects arrived through **text**: a feature that takes a new
> string and renders or persists it is an injection surface, even when it looks like "just a
> label." Run the security lens whenever a feature's shape is **"new string → rendered or stored
> surface,"** not only when it adds an external endpoint. (b19,24,27)

The category error is treating **rendering** as safe because it is **local**.

---

## Cross-phase · C-44 — work that never landed

**Failure closed.** Work that is finished but **unlanded** is indistinguishable, to every later
reader, from work that was never done — and the canonical state files are what the next session
reads, so an unlanded close-out makes the project's own state file **assert something false**,
which the next batch inherits as a premise (**C-43**).

**Example — four instances in ONE session, none a code defect:** an unmerged close-out branch
leaving `state.json` false to the next batch's intake; two approved corrective items from a
**CONDITIONALLY** closed gate never applied **while the batch merged anyway**; an abandoned
uncommitted edit holding a whole encoded control; two uncommitted command files found by a later
session.

**Rule.** At session close — and again at every batch close — reconcile **every** file the session
created or modified into exactly one terminal state, and **say which**: ✅ **committed** *and, where
the work only matters once integrated, landed* (**a commit that never lands is not a terminal
state**) · 🗑️ **reverted or deleted, deliberately** · 📋 **left in place ON PURPOSE, with its path
and remaining work written into the canonical backlog**.

**Discharge — mechanical, never from memory.** `git status --short` in **every repository the
session touched, auxiliary repos included**; `git log @{u}..HEAD` for unpushed commits; confirm an
open PR exists for any branch other work depends on. **Report pre-existing uncommitted changes as
FOUND rather than sweeping them up.**

**A conditional gate verdict is not a merge authorisation.** If a gate closes "once items 1–N land",
the discharge of those N items is itself a gate condition — verify each **by re-reading the artifact**,
never by trusting that the corrective pass ran. **From flow rev71 the close artifact carries the
`Conditional-gate discharge` roll-up as a keyed field and `V50` reads it** — the first reader this
clause has had. It reads whether the roll-up was WRITTEN, never whether the discharge is real; the
third column of that table asks for *the artifact line*, which is what makes the re-reading checkable.

**RIDER — characterise VCS state from REFS, never from the working tree.** Inspect **refs** first:
`git log --all --oneline`, `git branch -a -vv`, `git worktree list`, `git fetch`. *A dirty working
tree is fully compatible with the identical content being committed, pushed and merged elsewhere.*
When content appears in both, compare **tree objects** (`git rev-parse <ref>:<path>`) and
**normalise line endings before any content comparison**. (Exhibits in REFERENCE.md.)

## Cross-phase · C-45 — the flow is a shared asset, and changes flow BOTH ways

**Failure closed.** Controls are discovered inside one project but are **not that project's
property**. Encoded locally, a control is active for exactly one operator — every other project
re-learns the lesson at full price. The mirror failure: a batch run on a **stale** flow **inherits
a solved problem as an open one**, with no way to notice.

**Rule — PUSH: a portable control is not encoded until it lands upstream.** Four parts, owed before
the batch closes: the **command** (the rule) · its **artifact** (a template section — *a control
with no output degrades to "I thought about it"*) · the **catalog** entry · **committed and
pushed**, SHAs recorded at the close. **Say which of the four landed** — command-but-not-template
is *half-encoded*, and the missing half is the enforceable half.

**PULL — verify flow currency at Phase 0, beside RC-1.** Publish a manifest (version, per-file
SHA256, aggregate hash re-derivable locally in one command); a mismatch is uncommitted local work
(push it) or staleness (pull it). **Record the flow revision next to the RC-1 line. Whoever edits a
flow file owns the bump, and the manifest is written last, over final content** — a stale manifest
is worse than none.

**Placement is decided by portability, not convenience:** portable principle → the global flow;
stack-specific mechanics → the project's own rules doc. From flow rev71 the close artifact declares
how many controls the batch minted (**`V51`**) — the reader removes the debt going UNCOUNTED
between sittings.

**Rider — LEARNING a lesson and ENCODING it are different acts** *(batch-89)*: the `python3` trap
entered this catalog and the flow shipped `python3` regardless eleven days later, with **`V17`
certifying a guard that had never run**. **A commit that touches the catalog is not a
control-encode.** (Dated exhibit in REFERENCE.md.)

## Cross-phase · C-62 — a rewrite converts prescriptions into permissions

*(corpus: an agent-authored rewrite of a skill, 2026-09-08, outside the record; minted at flow rev71)*

**Failure closed.** Erosion of an artifact's **quality pressure** during a structural rewrite that
is, on every other axis, a genuine improvement. **The improvement is what makes it pass review** —
a *requirement* quietly ceasing to be one, in a diff reviewers score as good work.

**Example.** A skill went from **552 lines to 54** plus progressive-disclosure references; the
architecture genuinely improved, and in the same change **five controls were deleted**:

| Before | After |
|---|---|
| `you MUST include evidence artifacts` | `include examples only when they clarify the question` |
| two named pass/fail tests | deleted |
| `the container test` | `there is no target percentage of boxed text` |

**Rule — three limbs.**
1. **Review a rewrite along two independent axes: structure and enforcement.** A gain on one does
   not license a loss on the other, and reviewers reliably score the visible axis.
2. **Diff the imperatives specifically.** Count MUST / required / pass-fail gates before and after.
   *Prose length is not the metric; enforcement density is.* The tell is hedge phrases — *"do not
   automatically require"*, *"is a choice, not a quality criterion"*.
3. **Validate a restored control by running it against output the weakened version already
   produced.** If everything passes, the restoration is decorative.

**Mechanism — NAMED AND NOT BUILT:** a per-file MUST / required / BLOCK count per manifest
revision, reported as a delta beside `flow_hash`; until it exists limb 2 is performed by a reader
(`C-58`'s warning). (In-house gap exhibit and the `C-63`/`C-64` id-skip note in REFERENCE.md.)

## Cross-phase · C-65 — a ruling is applied as a CENSUS over its axis, never as the instance

*(minted at flow rev75 from the operator's `C-45` sitting of 2026-09-11)*

**Failure closed.** A ruling is stated on an **axis** — *a derived artifact depends only on
versioned content* · *no rule reads an ambient fact* — and discharged by fixing **the one instance
the finding produced**. The fold is correct and the gate green — **and all of it is evidence about
the instance, none about the axis**: the ruling becomes a promise that the next reviewer finds the
next member.

**Example.** One ruling cost SEVEN review rounds: each folded whichever instance the
previous review had demonstrated, and none was the ruling. (That exhibit and the
later ones — one of which REFUTED THE RULING'S OWN WORDING — in REFERENCE.md.)

**Rule.** When a ruling's subject is a CLASS, **the same commit that closes the first instance
enumerates the class and closes the set**: a declared population plus an arm comparing source to
set, BOTH WAYS — a one-way arm catches a member dropped from the code and is blind to one dropped
from the declaration. **The census is over the AXIS THE RULING NAMES, not the axis the instrument
finds convenient.**

**Discharge.** A **review-time obligation** whose discharge is a POPULATION IN THE DIFF — every
exhibit here was caught by independent review and none by a rule; the reviewer is this control's
instrument.

## Implementation/Validation · C-46 — a hash-verified restore does not restore the CACHE

**Failure closed** (increment 22b). A mutation battery mutated `range(0, 4)` →
`range(0, 1)` — the **same byte count** — and restored within the same second. Python keys a `.pyc`
on (source mtime, source size); both matched, so `__pycache__` kept the **mutant's** bytecode and
the next full-suite run executed it from a byte-identical tree: 13 tests red with no diff to
explain them. The hash-verified restore proves the *source* is back; the interpreter was not
reading the source.

**The controls, all three:**
- Run mutation batteries under **`PYTHONDONTWRITEBYTECODE=1`** so the mutant never enters the
  cache.
- **The proof of a clean battery is a green suite run *immediately after* it** — not the restore
  hash. Same-size mutations and sub-second restores are exactly the case the hash cannot see.
- On unexplained reds with a clean diff, **suspect the cache before the code**: purge `__pycache__`
  and re-run before diagnosing.

Any bytecode/artifact cache keyed on (mtime, size) has the same blind spot — Python is merely where
it was paid for.

## Phase 5 · Postmortem — honesty note, the scope of these claims (§8)

> **These are hard-won controls from ONE project's 54 batches — not universal law.** The failure
> modes they close are real and recurred inside that corpus, but a single-project observation is
> not a proven law: the frequencies quoted here are **evidence, not statistics**. Treat the catalog
> as a strong prior — a checklist worth defaulting to — and re-earn each control in your own
> context rather than importing it as gospel.

Lessons too app-specific to teach were excluded (named in REFERENCE.md); **a recommendation that
recurs unactioned across batches is itself a process failure** (§5).

---

## Origin-only ids — headings the control census deliberately scores 0

`V44` cites `C-20` and `V43` cites `C-26`, and neither is a numbered control. They keep `####`
headings here so those citations resolve, while the manifest's `controls:` derivation reads
`#{1,3}` and does not count them — a declared exclusion, not a widening (operator, 2026-09-17).

#### C-20 — net-new-file RED via move-aside (batch-35 Inc-1)

The rule is in `C-40`'s Discharge and §*Gates & evidence rules*: a NET-NEW file's RED is captured
by **moving the file aside**, never by `git stash`.

#### C-26 — touched-symbol reverse census (batch-37)

**Reader: `V43`, flow rev68 — declared once, under `C-48`, not twice.** A second copy here would
be the two-inventories defect `C-50` names.

---

## Writing canon — a parenthetical may carry provenance, NEVER a definition

**The rule.** A parenthetical — `(Origin: …)`, `(Root cause …)`, `(measured …)` — may carry only
**provenance**: where a rule was learned, what was measured, which batch paid for it. The moment a
parenthetical carries a **definition**, a **scope**, or the **derivation of a constant**, that text
is normative and it is in the wrong place. Hoist it into the rule's own prose before anything
moves.

**How it was earned.** rev57 moved every origin story out of the flow's five normative
files into this catalog, and at one site a mechanically correct extraction moved a BINDING
definition -- the scope of the `consumers` field that `V13` and `V14` parse against. Canon
had buried a definition inside an `(Origin: ...)` parenthetical, so a right rule produced a
wrong result. (The site, verbatim, in REFERENCE.md.)

**Three more sites in the same sweep were the same shape** — a constant's derivation, a naming
ruling, and a term's definition all buried in origin narratives — which is why this is a rule and
not an anecdote. (Sites enumerated verbatim in REFERENCE.md.)

**The check.** Before moving any parenthetical, ask of every sentence inside it: *if I delete this,
does a rule become unreadable, a term undefined, or a constant unexplained?* If yes, that sentence
is not provenance and it does not move. **A term used in a normative file must be defined in a
normative file** — a definition that lives only in a catalog is a dangling reference wearing a
citation's clothes.

---

## Provenance (short)

- Distilled from **54 post-mortems** of one project's `.dev-flow` batches. Batch numbers
  (`bNN`) cite where in that corpus a control was earned.
- **This catalog ships as TWO files and a line lives in exactly one of them.** `SKILL.md` (this
  file) is the consultable half — controls, rules, stated limits, readers. **`REFERENCE.md`**
  beside it is the forensic half — origin stories, dated measurements, corrections, candidate
  history — under a locator map keyed on the same headings. Nothing was deleted, and the census
  that says so is an arm (`CAT SPLIT-census`), not a claim.
- Landed at **flow rev80**, which also RULES every imperative the 2026-09-14 prune moved: the
  table is in `REFERENCE.md` and is READ by `CAT C62-dispositions-resolve`, not asserted.
