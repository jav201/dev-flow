# Increment <NNN> — <REQ-ID> · `<Short title>`

> **Artifact language**
> This template is the canonical **English scaffold**. Generate the artifact in the batch's development
> language — the **prose**, and never a label. **Where that language is declared depends on the mode:**
> `state.json`'s `language` key in `core` and `full`; in `fast` the five-key declaration carries no
> such key by design, and the spec's §0/§1 is where the batch's language is fixed. The normative RULES below are
> language-independent.

> **Owed in.** `fast` — · `core` ✓ · `full` ✓
> **`fast` HAS ITS OWN PACKET from flow rev86** — `templates/fast-dev-flow/increment-template.md`, which carries ONLY the rows a rule reads on a `mode: fast` tree. This one is 489 lines and a fast batch could fill ten of its rows; both readers of the 2026-09-19 publication test named that ratio as the single biggest obstacle to running a fast batch at all. **The `in `fast`` spellings on this page stay and are not dead text:** a batch PROMOTED through §*Escape hatch* keeps the packets it already wrote and writes its next ones from here, so the two packet families have to be readable side by side in one batch.
> **Source:** `/dev-flow-init` step 4's seed-by-mode table, which is this fact's one home (flow rev72, `T05`). A mode marked `—` **does not owe this artifact, and its absence is not an omission**; `by trigger` means the station exists only when the `triggers` block fired, and `stations_active` in `state.json` is the authority for *this* batch. Where a SECTION or a gate row is owed more narrowly than the artifact, it says so on the row.

> **Reserved field names.** The **field names and block keywords below are language-independent** — the
> validator parses them literally and they are never translated:
> `SOURCE files` · `Instrument RED-proof` · `Correction population` · `Mutation verdicts` · `Emitted-form assertion` · `Reverse census` · `RED counterfactual` · `Independent review` · `Evidence files` · `⏸ DEFER`
> Everything else on this page — headings, guidance, the prose in every cell — is translated with the batch.
> **One strategy, not two:** the flow ships no alias table, so a translated label is read as an ABSENT one and the rule keyed on it reports a true-sounding silence.
> **And one FLOW-WIDE reserved token, read out of this artifact by `V42` no matter which template minted it:** `⏸ DEFER`. It is a MARKER rather than a field name, which is why it is stated here *and* in `/dev-flow` §Language of artifacts rather than in a per-template list — a deferral can be written in any batch artifact, including the ones that carry no block at all. Measured: `⏸ DIFERIDO` returns the empty declaration list AND the empty near-spelling list, so a translated marker is indistinguishable from a batch that deferred nothing.

> **Where this lives:** the **repo**, next to the diff it describes —
> `.dev-flow/<batch_id>/03-increments/increment-<NNN>.md`. It is not synced to the vault.

> **Notice convention.** `⚠` yellow = notice: does not block, obliges you to DECLARE the reason here.
> `✗` red = block. `✓` green = satisfied **with its evidence cited**. A notice repeated for three
> consecutive batches becomes a rule or is retired.

| Field | Value |
|---|---|
| Batch | `<batch_id>` |
| Increment | `<NNN>` |
| Lane (if the batch forked) | `<lane name>` · `<modules owned by this lane>` — in `fast`: `none — batch not forked` |
| Requirement(s) | `<R-NNN vN / LLR-NNN.n>` — in `fast`: the acceptance-criterion ids, `AC-<n>` |
| Acceptance | `<AT-NNN>` · white-box `<TC-NNN>` · unit `<layer-0 nodes>` — in `fast`: `AC-<n>`, and `n/a — not owed in fast` for the white-box and unit cells |
| Agent | `software-dev` |
| Date | `<YYYY-MM-DD>` |

> **THE `fast` SPELLINGS ABOVE ARE THE ANSWER, NOT A LICENCE TO LEAVE A CELL EMPTY.** `fast` mints no
> `R-`, `LLR-`, `AT-` or `TC-` ids — `/fast-dev-flow` §*Difference vs `/dev-flow` phase 3* is that
> fact's one home — so every field whose vocabulary is full-flow-only carries either the `AC-<n>` id
> this flow really has or the reserved `n/a — not owed in fast`. **A fast reader is never told to fill
> a full-flow-only block**: until rev85 this header offered no fast reading at all, and the reader of
> the 2026-09-18 re-run invented one and said so.

---

## 1 · What changed

*(BLUF: state the outcome first, then the mechanism. Name the shipped surface the user reaches.)*

---

## 2 · Files modified

**The budget counts SOURCE files only. Tests are not capped. Product docs and `.dev-flow/**` are outside the count.**

| File | Kind | Change |
|---|---|---|
| `<path>` | source / test / doc | `<what changed in it>` |

| Count | Value |
|---|---|
| **SOURCE files** | **`<N>` / 4** |
| Test files | `<N>` (uncapped) |
| Doc files | `<N>` (outside the count) |

- ⚠ **At exactly 4 source files:** state here why this increment could not be cut smaller.
- ⚠ **Above 4:** this does not auto-block, but the reason goes here **and** the design/close review looks at it.
- ✗ If a file belongs to another lane's file set, stop: lanes may not share a file.

---

## 3 · How to test

```bash
<the exact commands, copy-pasteable>
```

---

> ⚠ **Before you write the first evidence file: mark the evidence home `-text` in
> `.gitattributes`.** Evidence carries mixed line endings by nature, and a git that normalises
> them stores bytes that do not hash to the digest you recorded — the commit looks healthy and a
> rollback from it restores the wrong bytes. `/dev-flow-init` step 3's `artifact_homes.evidence`
> bullet is that rule's one home and carries the measurement; this line exists because the reader
> who needs it is here, writing §*Evidence files*, and not there.

## 4 · Test results

**One complete run. The exit code and the tail are read from THAT run's own output — never stitched
across partial runs, never inferred from a killed or backgrounded call (C-19).**

| Layer | Owed in | Nodes | Result |
|---|---|---|---|
| **0 · unit** (cyclomatic ≥3, or crosses a declared module boundary) | `core` · `full` | `<nodes>` | `<N passed>` |
| **A · white-box** `TC-NNN` ↔ LLR | `core` · `full` | `<nodes>` | `<N passed>` |
| **B · black-box** `AT-NNN` ↔ story, through the shipped surface — **in `fast`, `AC-<n>` ↔ criterion** | `fast` · `core` · `full` | `<nodes>` | `<N passed>` |

**The `Owed in` column is read exactly as the gate checklist's is**: a mode this row does not name
writes `n/a — not owed in fast` in its Result cell and nothing else. In `fast` that is rows 0 and A;
row B is owed, and its ids are the acceptance-criterion ids, because *each test maps to an acceptance
criterion by name or reference* is what `/fast-dev-flow` requires instead of formal `TC`/`AT` ids.
Until rev85 this table named full-flow ids in all three rows with no fast reading, while the checklist
beside it was scrupulously mode-aware — one artifact answering the same question two ways.

### RED counterfactual — executed, not predicted

| Field | Value |
|---|---|
| Mutation applied | `<what was changed to make the assertion fail>` |
| Where it ran | **my own tree / worktree** — never a tree another lane or session is reading |
| Transcript | `<paste: the RED output, plus confirmation the mutation actually applied>` |
| Restore proven by | **file hash returned to its pre-mutation value** (`git status` alone is insufficient, and vacuous for an untracked file) |
| Bytecode cache | cleared / run with `PYTHONDONTWRITEBYTECODE=1` (C-46) |
| Arms resolved at baseline | `<N>` — **assert the expected count.** An arm the harness cannot see is an arm it cannot report inert; a whitespace-delimited node pattern silently drops every *parametrized* arm |
| Verdict granularity | **per resolved node id**, never the process exit code — a runner exits non-zero if ANY arm fails, so an inert arm hides behind a sibling that failed |
| Arms that stayed GREEN | `<name them, or 'none'>` — `3 passed` unread in a transcript is how four arms once survived a fully removed gate |

| Field | Value |
|---|---|
| **RED counterfactual** | `<the mutation that made THIS increment's OWN new assertion fail, by position and operation · where its transcript is stored · the restore digest that returned the file to its pre-mutation bytes — or: none — no new assertion in this increment>` |

**The row above is what a rule reads (`V44`, flow rev68); the table is where the evidence lives** —
the same division as the `Reverse census` row below. **Where the two overlap, the ROW is authoritative:**
`Restore proven by` in the table states the *method*, and this cell names the *digest itself*, because
the method survived in the corpus and the digest did not.

**And this row is the ONE counterfactual, not the battery's tally.** `**Mutation verdicts**` below
carries what the harness's arms returned; this row carries the single mutation that showed **this
packet's own new test** able to go RED, and the proof the tree came back. Measured over the 14 packets
that carry the obligation, and the label/value correspondence is exact: the **2** whose gate row still
carried the words *and restored by hash* both named a restore digest here; the **12** whose row text
had lost those words named **none**, and 10 of them wrote a mutation tally instead. **The restore half
is the half that disappears**, which is why it is named in the cell and not left to the table above.
- ✗ A tally of mutants is not a counterfactual. `34 scored, 34 reddened` says nothing about whether the assertion this increment wrote can fail.
- ✗ A transcript nobody can open is not a transcript: cite the path under `artifact_homes.evidence` (`C-59`, and its digest belongs in the **Evidence files** row). A batch whose SUBJECT is the flow itself may cite a registry id instead; project code has no registry and cites the transcript.
- **When there is nothing to declare, write `none — no new assertion in this increment`.**

| Field | Value |
|---|---|
| **Mutation verdicts** | `<per resolved node: the mutation by position and operation · KILLED / CRASH / SURVIVED / BAD (the mutation's anchor did not apply) · the arms that stayed GREEN, named · the transcript's path under artifact_homes.evidence and the restore digest — or: none — no mutation battery in this increment>` |

**RECORD THE VERDICT PER ARM, AND FOR PROJECT CODE THE INSTRUMENT IS YOUR OWN HAND.** The obligation
in a project batch is: **one RED counterfactual per resolved node** — mutate what the assertion
claims to certify, witness the arm go RED, restore the file, and **prove the restore by hash**, with
the transcript written to `artifact_homes.evidence` and cited with its digest. That is re-runnable by
anyone holding the packet, and it needs no tool the flow does not ship.

⚠ **The harness in `scripts/` is NOT that instrument, and the packet stops implying it is.**
`scripts/devflow-mutate.py` says in its own module docstring that it is **not offered to projects**:
its subject is this flow's validator, and its registry (`scripts/devflow-mutants.json`) names mutants
of that file with the arms each claims to redden (`expect_arms`), which the harness executes and
reports UNMET by name (`R-88-12`). **A batch whose subject IS the flow** cites registry ids here and
owes that negative control; **a batch on project code** cites its transcripts. Until rev84 this
paragraph mandated the registry for every increment, so the row's re-runnability claim rested on an
instrument no project has — measured 2026-09-18, when two readers on two runtimes each had to invent
a substitute and say so.

**Why the restore is proven by HASH and not by `git status`** — measured on a two-function library,
which is as small as a batch gets: the restore edit matched the WRONG function's line (both read
identically mid-mutation), leaving each function computing the other's result. `git status` showed one
modified file, exactly as a correct restore would; the SHA-256 against the pre-mutation digest is what
refused it. The ceremony paid for itself on the smallest possible change.

- ✗ A predicate that stays GREEN under the mutation of what it claims to certify is inert: rewrite it, do not re-argue it.
- ✗ **A verdict per MUTANT is not a verdict.** A runner exits non-zero if any arm fails, so an inert arm hides behind a sibling that failed. One verdict per resolved node id, and name the arms that stayed green.
- **When there is nothing to declare, write `none — no mutation battery in this increment`.**
- ⚠ **This packet is corpus input (C-56)** — `.dev-flow/**` is scanned. **Describe the mutation by position and operation; never spell a corrupted id, symbol or token here**, or the restore above proved the wrong plane. No dotted-range id shorthand (`AT-020..024`): enumerate, or write `AT-020` through `AT-024`.

### Instrument RED-proof — every instrument shown able to report FAILURE first

**A verification instrument is blind until it has reported a failure.** For each instrument the
figures in this packet rest on — a test, a counter, a mutation harness, a grep, a parser — name the
known-bad input it was fed and the FAILURE it returned, **before any PASS from it was believed**. The
known-bad input must corrupt the instrument's *mechanism*, not merely its *verdict*: a case-fold probe
once replaced wholesale by `return True` survived twelve mutants, because the machine really does fold
case, so the verdict was armed and the mechanism was not. This is `C-40` moved off the acceptance
predicate and onto the measuring apparatus, which is where the 2026-08 defects lived.
**And the same question is owed of the FIXTURE the instrument runs on** (`C-57`, the vacuous-fixture
sub-case): a fixture whose own symmetry collapses the distinction being tested makes a correct
predicate unable to fail — an all-`F` address makes leading and trailing hex digits byte-identical,
and a batch-89 constant was satisfied by case-folding alone — so name what this fixture makes
indistinguishable, and add one deliberately non-uniform arm with its discriminating precondition
asserted.
(Origin: batch-89's five instruments and the rev59 harness — see dev-flow-lessons, `C-57`)

| Instrument | Known-bad input fed to it | The FAILURE it reported |
|---|---|---|
| `<test / counter / mutation harness / grep / parser>` | `<the corruption planted in its MECHANISM, not in its verdict>` | `<the failure it printed, verbatim — and where>` |

| Field | Value |
|---|---|
| **Instrument RED-proof** | `<N instruments, each shown RED before its first PASS was believed — or: none — no instrument beyond the suite>` |

- ✗ A figure produced by an instrument that has never reported a failure is not evidence, however green.
- ✗ An instrument that dies at import emits no line at all; a reader that scores only what it printed calls that a survivor. Distinguish **KILLED / CRASH / SURVIVED / BAD** — `BAD` is the fourth and it is not a survivor: the mutation's anchor did not apply, so nothing was measured and the arm's verdict is about nothing.
- **When there is nothing to declare, write `none — no instrument beyond the suite`.** An absence declared is a declaration; an absence omitted is a gap, and the two must never read alike.

### Emitted-form assertion — assert the bytes the producer EMITS (C-42)

**Executing the producer is not enough if the assertion is then written against the form a human
reads.** Producers escape, encode, wrap and substitute, so confirming a named output *exists* passes
while a search for its readable form **false-fails a correct implementation**. For every artifact this
increment emits — a file, a report, a rendered screen, a serialized record — run the producer, paste
what it actually emitted, and assert against that. Prefer the producer's own structured output (its
parser's token stream, a language-aware source parse) to a substring search over serialized text: a
substring search cannot tell a value from its own encoding.
(Origin: a heading emitted as a code span, unfindable by its bare text; a snapshot emitting `&#160;`
that returned 0 matches for a label plainly on screen and 29/29 for the emitted form — see
dev-flow-lessons, `C-42`)

| Artifact emitted | The assertion, run against the EMITTED form | What it returned |
|---|---|---|
| `<the file / report / screen / record>` | `<the command or predicate, pasted>` | `<its actual output, verbatim>` |

| Field | Value |
|---|---|
| **Emitted-form assertion** | `<N artifacts, each asserted against the form its producer emitted — or: none — this increment emits no artifact>` |

- ✗ A predicate written against the *rendered* form false-fails a correct implementation, and the failure looks like a bug in the code.
- **When there is nothing to declare, write `none — this increment emits no artifact`.**

### Evidence files — bytes at a declared home, verbatim, hash-verified (C-59)

**A hash is only a contract if something re-derives it from the bytes that are actually
stored.** Every artifact this packet cites as PROOF — a transcript, a capture, a snapshot, a
`.PRE` copy of a file that lives outside version control — is written to the home
`artifact_homes.evidence` declares, byte for byte, and cited here with its SHA-256. Not a
session-scoped `Temp` path: that directory is gone by the time anyone wants the rollback.
**Assert the STORED artifact, never the one you handed to the store** — if the store is git,
mark the path `-text` in `.gitattributes` and not `text eol=lf`, because evidence carries
mixed line endings by nature.
(Origin: batch-66 stored four `.PRE` files whose recorded SHA-256 *was* the entire rollback
contract, and `core.autocrlf` normalised them on the way in — one blob read `d46bb314…`
against a recorded `e103af29…`. The commit looked healthy. See dev-flow-lessons, `C-59`)

| Evidence artifact | Path — under `artifact_homes.evidence` | SHA-256 |
|---|---|---|
| `<the transcript / capture / snapshot / .PRE copy>` | `<the path, as stored>` | `<the 64-hex digest of the bytes AT THAT PATH>` |

| Field | Value |
|---|---|
| **Evidence files** | `<N artifacts, each at the declared home and cited with the digest of its stored bytes — or: none — this increment cites no evidence file>` |

- ✗ A digest taken from the file you handed the store proves the wrong plane. Re-read it from where it landed — for git, from the index blob.
- ✗ The corruption is **bidirectional and half of it is invisible at commit time**: a CRLF file normalises to LF going in, and an LF file converts to CRLF coming out at the next checkout, so its blob matches and its checkout does not.
- **When there is nothing to declare, write `none — this increment cites no evidence file`.**

### Load-bearing emptiness — what is this resting on that is only true today? (C-55)

| Field | Value |
|---|---|
| Does any claim here rest on the tree holding NO instance of some case? | `<yes: name it / no>` |
| If the result is an ABSENCE, what made the search wide enough | `<the over-broad property — and the guard that protects it>` |
| Guard labelled as protecting a CONCLUSION, not a behaviour | `<node id — else the next reader "improves" it away>` |
| Conjunctive criteria: one mutation per conjunct | `<per-conjunct verdicts, or 'no conjunctive criterion'>` |
| Synthetic instance of the absent case | `<fixture / in-memory module that contains what the tree lacks>` |
| **Positive control for every probe that returned an ABSENCE** | `<the known-present case, and the NON-absent output the same unmodified probe returned on it>` — uniformity over heterogeneous inputs (N-of-N) is one failure repeated, not a measurement |

- ✗ A clause that is a **no-op on today's data** is untested however green the suite. The tell: mutating it changes nothing.
- "There are none today" is the reason the guard is needed, never a reason to skip it.

### Reverse census — trigger family B

| Probe | Command | Result |
|---|---|---|
| B1 symbols asserted by **other** tests | `grep -rl <symbol> tests/` | `<files, and whose they are>` |
| B2 file moved on disk | `<glob probe over the old path>` | `<readers found>` |
| B3 byte-identical golden captures this source | `grep <source> tests/goldens/**` | `<hits>` |
| B4 artifact produced here is consumed elsewhere | `<who reads the path/format written>` | `<consumers>` |

| A3 | interface consumed by another module changed | `grep <symbol>` outside its owning module | `<hits>` |

| Field | Value |
|---|---|
| **Reverse census** | `<N probes run of B1 · B2 · B3 · B4 · A3, each with its command and its verdict — N hits, and where every hit was re-validated — or: none — this increment touches no code symbol or shared surface>` |

**C-48 — record the ones that did NOT fire too, with their probe.** "Did not fire" without evidence is
textually indistinguishable from "was not evaluated", and the second is what happens under pressure.
**The row above is what a rule reads (`V43`, flow rev68); the table is where the evidence lives.** The
five probes are fixed and each asserts a different reverse question: **B1** — which EXISTING tests, from
any requirement or batch, assert against the symbol this increment touches; **B2** — which readers still
name a path this increment moved; **B3** — which byte-identity goldens capture a source this increment
changed; **B4** — who consumes an artifact produced here; **A3** — who outside the owning module consumes
a changed interface. Forward traceability can be fully intact while every one of these is unasked, which
is why the census is keyed REVERSE, by symbol (`C-26`).
- ✗ If **A3** fired inside a lane, stop: a frozen interface goes back to the trunk, it is not changed in a lane.
- ✗ "Ran the census" with no probe output is the sentence `C-48` exists to refuse: it is textually indistinguishable from "was not evaluated".
- **When there is nothing to declare, write `none — this increment touches no code symbol or shared surface`.** An absence declared is a declaration; an absence omitted is a gap.

### Correction population — enumerated BEFORE the first site was edited

**A correction has a population, and it must be enumerated — with the method that enumerated it —
before its first site is edited.** For every correction this increment makes to a claim that can
appear in more than one artifact, enumerate first, then edit. Key the census on the **assertion
category** — what kind of thing must be true everywhere — never on a frozen list of sites: a census
keyed on a marker is structurally blind to what carries no marker (measured at rev57: 65 claimed,
72 found, 11 of them unmarked, 2 in a file whose marker count was zero). Sites left unedited are
named with their reason; a subset edited in silence is the defect itself.
(Origin: batch-88 Increment 6 and batch-89's close — see dev-flow-lessons, `C-14`)

| Correction | Population — the assertion category | Enumeration method (the command) | Count | Sites edited | Sites left, and why |
|---|---|---|---|---|---|
| `<the claim being corrected>` | `<what kind of thing must be true everywhere>` | `<the command, pasted>` | `<N>` | `<…>` | `<…>` |

| Field | Value |
|---|---|
| **Correction population** | `<N corrections, each enumerated with its method before its first site was edited — or: none — no correction>` |

- ✗ A count with no method is a claim, not a census. Never stamp one "VERIFIED COMPLETE": re-running an incomplete checklist cannot detect that it is incomplete.
- **When there is nothing to declare, write `none — no correction`.**

#### Supersession-completeness inspection (batch-09 V-3)

> Grep the whole class of superseded markers/constants; every surviving reference must be a NEGATIVE
> assertion (absence), not a live dependency. **This inspection ran at P4 until flow rev60 and runs
> HERE, at P3, from rev60 on:** a completeness sweep performed after every site has already been
> edited measures damage, not risk. It is the executed step of the population field above.

| Superseded marker | grep result | All surviving refs negative? | Evidence (file:line) |
|-------------------|-------------|------------------------------|----------------------|
| `<marker>` | `<N hits>` | yes/no | `<…>` |

### Signed-balance test ledger

`post = base − deleted + added` → `<post> = <base> − <D> + <A>`  ✓ reconciles

---

## 4b · Independent review — the lens the author cannot be

**The flow MANDATES this pass** (`commands/dev-flow.md` §*Independent review*): at each increment
gate `code-reviewer` reviews the diff — correctness, simplicity, reuse, convention conformance,
test-intent — BEFORE user approval and independently of `software-dev`; **a HIGH finding blocks the
increment until it is fixed**, and a security concern routes to `security-reviewer`.

**THE CELL MUST NAME SOMEBODY, and `V36` refuses it otherwise.** From flow rev64 the test is
inverted: the cell is read as answered only when it contains one of seven identity tokens —
`code-reviewer`, `security-reviewer`, `qa-reviewer`, `ux-reviewer`, `tester`, `human:<name>` (the
prefix is required; the rule does not guess at names), or `WAIVED-BY-OPERATOR — <reason>` — and
**anything else is the empty state**, whatever it says. rev63 screened the cell against a list of forbidden
words instead, and a blocklist is incomplete by construction: `author self-review only` led with a
word the list did not hold and scored as an answer. The rule's silence now means *somebody is named*
rather than *no forbidden word appeared*.

**IN `fast` THE REVIEWER IS THE AUTHOR, AND THAT IS DECLARED — NOT OMITTED, AND NOT WAIVED.** A batch
whose `state.json` says `mode: fast` writes the reserved token **`SELF-REVIEW — fast mode`** in the
cell: `/fast-dev-flow` mandates a light self-review and no `code-reviewer` pass, so the truthful cell
names the state the flow actually asks for. **`V36` accepts that token ONLY when `state.json` declares
`mode: fast`** — in `core` or `full` a `SELF-REVIEW` cell names nobody and is the EMPTY state, which is
what it has always been. `WAIVED-BY-OPERATOR — <reason>` remains the only OTHER legal empty, in every
mode; it says the review was owed and skipped, which is a different fact from a self-review and must not
be spelled with it. This paragraph and gate row 15 are the same sentence said once (`C-50`): the row
points here for the grammar, and the checklist's mode column does not exempt the row.
(Origin: 2026-09-18 — §4b mandated the pass unconditionally while the gate table exempted `fast`, and
two readers resolved the contradiction two different ways, one waiving and one self-reviewing.)

**`ABSENT` IS NOT AN ACCEPTED VALUE HERE. It is the EMPTY state, and `V36` reads it as such.** That
is the one place this field departs from `Instrument RED-proof` and `Correction population`, and the
departure is measured: batch-89 wrote a hand-authored `Independent review` section reading `ABSENT`
in **6 of 6** packets, shipped five flow revisions, and **every gate passed** — the absence cost
nothing, which is the definition of a paragraph. Those six packets were honest; what was missing was
a reader. A review that did not happen is a gap to declare in §6 and carry, never a value that
satisfies the row.
(Origin: batch-88's 7-of-7 against batch-89's 0-of-6, and the five flow revisions that
shipped between them — see dev-flow-lessons, `C-58`.)

**One row, and it is the row a rule reads.** Write the three facts into the single cell
below, separated by `·`, in this order — a second table repeating them would be a second
inventory of one truth (`C-50`), and only this one is read:

1. **WHO reviewed** — the agent or role, named, in one of the seven forms `V36` accepts in every
   mode: `code-reviewer`, `security-reviewer`, `qa-reviewer`, `ux-reviewer`, `tester`, `human:<name>`,
   or `WAIVED-BY-OPERATOR — <reason>` — plus, in `fast` alone, the reserved `SELF-REVIEW — fast mode`. A verdict with no reviewer named is the author's own opinion in
   the third person. ⚠ **`tester` joined the grammar at flow rev73 because a tester AUTHORS
   evidence and completes checklists (`V48` reuses this same table for that), NOT because it may
   approve.** Naming the tester as the independent reviewer of the tests it wrote is the author
   reviewing itself — which this field has forbidden since rev64 and which no grammar can see, so
   it is stated here and in `agents/tester.md` rather than pretended to be mechanical.
2. **The VERDICT** — `PASS`, `PASS-WITH-NOTES`, or `BLOCK` with the count of HIGH findings. **A CONDITIONAL verdict is written `BLOCK — BLOCK-UNTIL: F1, F3` (flow rev73):** the token stays `BLOCK`, which is what `V36`/`V37` read, and the owed finding ids ride beside it so the discharge has somewhere to land — item 3 is where it is recorded when the fix is applied AND re-read. A conditional verdict that can only be spoken in conversation is the state `V50` exists to stop.
3. **HOW EVERY HIGH WAS RESOLVED** — per finding, what changed and where; or `no HIGH finding`.

| Field | Value |
|---|---|
| **Independent review** | `<who reviewed · the verdict · how every HIGH was resolved — or: WAIVED-BY-OPERATOR — and the reason, in the operator's own words>` |

*Example of a filled cell:* `` `code-reviewer` · PASS-WITH-NOTES, 0 HIGH / 5 MEDIUM · all five
folded into this increment — F1 severity census, F2 block truncation, F3 blocklist, F4 scope
state, F5 this table ``

- ✗ A verdict with no reviewer named is not an independent review — it is the author's own opinion in the third person.
- ✗ A HIGH recorded without its resolution is an open block, not a review.
- **`WAIVED-BY-OPERATOR — <reason>` is the only legal empty**, and the reason is not optional: a waiver nobody has to justify is the paragraph this field replaced.

---

## 5 · Risks

*(What could break that this increment does not cover. Be specific enough to act on.)*

---

## 6 · Pending items / spec deviations

*(Anything surfaced and not closed here. Every line lands in the canonical backlog at batch close —
if the increment surfaced it, the backlog owns it.)*

---

## 7 · Suggested next task

---

## Increment gate checklist

> **MODE APPLICABILITY — `Owed in` is a column, and *absent by design* does not look like *omitted*
> (flow rev72, `T05`).** This template is seeded in **all three modes** (`/dev-flow-init` step 4), and
> five of the rows below are controls `/dev-flow` §Modes activates at `core` and above. **A row this
> batch's mode does not owe is written `n/a — not owed in <mode>` and NEVER left blank**: a blank is
> an omission and the two must not read alike. `stations_active` and the `triggers` block decide
> whether a STATION exists in this batch; the `Owed in` column decides whether a ROW does.
>
> ⚠ **`n/a — not owed in fast` IN THIS COLUMN NEVER MEANS "LEAVE THE FIELD ROW BLANK".** The
> `Owed in` cells govern the GATE CHECKLIST; the reserved field rows above — `RED counterfactual`,
> `Reverse census`, `Mutation verdicts`, `Evidence files`, `Independent review` — are read by
> rules **in every mode**, and each one's empty state is its own declared token (`none — <why>`,
> `SELF-REVIEW — fast mode`), never an absence. A `fast` batch writes `n/a — not owed in fast` in
> the checklist cell AND a real declaration in the field row. Both readers of the 2026-09-19
> publication test found the safe path only by reading the paragraph below and the gate's own
> output; it is stated here, on the column it qualifies, for that reason.
>
> ⚠ **THE PACKET RULES ARE NOT MODE-AWARE, WITH ONE DECLARED EXCEPTION — measured, and the rest left
> alone deliberately.** Run on a synthetic `mode: fast` tree holding one empty packet, **nine** rules
> fire — `V9`, `V31`, `V32`, `V36`, `V37`, `V38`, `V41`, `V43`, `V44` — and **every one of them is a
> NOTICE**, which the flow's notice convention already defines as *does not block, obliges you to
> declare the reason*. That is exactly the answer this column mandates, at the right severity, so a
> `fast` batch is **asked** and never **blocked**. Teaching nine rules the mode table would put a second
> copy of it inside the validator — the first is `V39`'s `_V39_OWED_IN`, and keeping that one in step
> with `/dev-flow-init` step 4 is already a standing cost (`C-50`).
>
> **THE EXCEPTION IS `V36`'s GRAMMAR, AND IT IS NOT THE MODE TABLE IN DISGUISE (rev84).** `V36` reads
> one extra ACCEPTED FORM when `state.json` says `mode: fast` — the reserved `SELF-REVIEW — fast mode`
> of §4b — and reads no row, no station and no seed table to do it. What changes is the vocabulary of a
> truthful answer, not whether the row is owed: the fast flow's own text mandates a self-review, and
> before rev84 there was no legal way to write that down, so one reader waived a review that had
> happened and another wrote a cell the rule scored as empty. **Independent review stays mandatory in
> `core` and `full`**, where `SELF-REVIEW` names nobody; nothing here weakens it.

| # | Item | Owed in | ✓/⚠/✗ | Evidence (node id · command output · file:line) |
|---|---|---|---|---|
| 1 | ≤4 source files, or reason declared | all | | |
| 2 | Tests written in this same increment | all | | |
| 3 | Layer 0 written where the criterion applies | `core` · `full` ‹one complete run owned by the orchestrator ~ Layer 0› | | |
| 4 | **RED counterfactual** declared — the mutation that made this increment's OWN new assertion fail, where its transcript is stored, and the restore digest, or `none` (C-20/C-40; read by `V44` from rev68) | `core` · `full` ‹RED counterfactual mandatory ~ RED counterfactual› | | |
| 5 | **Reverse census** declared — the five probes run with their commands and verdicts, the ones that did NOT fire named with their probe, or `none` (C-26/C-48; read by `V43` from rev68) | `core` · `full` ‹reverse census of the touched symbol ~ Reverse census› | | |
| 6 | `code-reviewer` passed — a HIGH blocks; the verdict, the reviewer and each HIGH's resolution are declared in **§4b** (`ABSENT` is the empty state there, not a value) | `core` · `full` ‹RED counterfactual mandatory ~ code-reviewer› | | |
| 7 | No file from another lane touched | all | | |
| 8 | Frozen interfaces untouched (or returned to the trunk) | all | | |
| 9 | Coverage claims verified **on disk**, not from intent | all | | |
| 10 | Load-bearing emptiness declared, with its synthetic instance (C-55) | all | | |
| 11 | **Mutation verdicts** declared — **per arm**, inert arms named, registry ids cited, or `none` (C-40 rider; read by `V37` from rev64) | all | | |
| 12 | **Instrument RED-proof** declared — every instrument shown able to report a FAILURE before its first PASS was believed, or `none` (C-57) | all | | |
| 13 | **Correction population** declared — enumerated with its method before the first site was edited, or `none` (C-14) | all | | |
| 14 | **Emitted-form assertion** declared — per artifact emitted, the assertion run against the EMITTED form and what it returned, or `none` (C-42; read by `V38` from rev64) | all | | |
| 15 | **Independent review** names somebody — in one of the forms §4b publishes, and in `fast` the reserved `SELF-REVIEW — fast mode`; a cell naming nobody is empty (`V36`, rev64; `tester` rev73; the `fast` token rev84). §4b is the grammar's one home | all | | |
| 16 | **Evidence files** declared — every cited artifact at the home `artifact_homes.evidence` names, cited with the digest of its STORED bytes, or `none` (C-59; read by `V41` from rev66) | all | | |

**Each `core` · `full` cell CITES the §Modes row that decides it**, in ‹guillemets›, by that row's own leading text — so the column is read OFF `/dev-flow` §Modes rather than chosen here, and `TPL MODE-column-derives` resolves every citation against that table and checks the cited row really is `—` for `fast`. A row with no citation is owed in all three modes, and the arm requires that too — **and requires the converse, which is the half that was missing:** a gate row whose BODY names a control the mode table marks `—` for `fast` may NOT be written `all`. Each citation therefore carries **two** things after `‹`: the §Modes row that decides the cell, and after `~` the token **in this row's own body** that marks it as that control's. A gate row whose body contains a token ANY `core` · `full` row declares may not itself be written `all` — so a row cannot escape the column by dropping its citation, which is exactly what `r72-M10` did, surviving the first fold of this arm. ⚠ **Until rev72's first review this paragraph said the same thing and it was not true:** the arm compared the row numbers against the literal tuple `(3, 4, 5, 6, 15)` and parsed exactly ONE cell out of §Modes, so flipping *reverse census* or *layered validation* to `✓` for `fast` in the mode table left this column wrong and the selftest green (`rh1`, `rh2`, both SURVIVED). The citation is what makes the derivation real instead of asserted.

**An item without a citation is not satisfied — it is asserted.**

**No rule reads a row NUMBER, and that is measured rather than preferred.** Of the 14 packets in the
record that carry this checklist, the same obligation sits at row **4** in nine and at row **3** in
five, and the checklists ship at four different lengths — 7 rows in 3 packets, 8 in 2, 9 in 5, 11 in
4 — all keeping the original labels. The ordinal is a spelling. Every keyed obligation above is read
from its `| **Field** | value |` row in the body of this packet, never from its position in this
table — so renumbering, reordering or shortening the checklist costs nothing, and deleting the FIELD
is what a rule notices.

> ✅ **THE THIRD COPY IS GONE — closed at flow rev72 (`T05`), on rev68's own enumeration.**
> `phase-checklists.md` §5 carried its own 10-row version of the table above: measured 2026-09-10 it
> had **no row at all** for `Instrument RED-proof`, `Correction population`, `Emitted-form assertion`,
> `Independent review` or `Evidence files` — revs 60, 63, 64 and 66 each extended the gate and skipped
> it — and it cited **0 of the 12** field-keyed rules. rev72 replaced it with a **POINTER to this
> table** rather than regenerating it, and the choice was measured rather than preferred: **no rule
> reads either table** (`00-checklists.md` is in no rule's artifact family), so a regenerated copy
> would need a generator and a guard to protect a document with no reader, while a pointer needs
> neither and cannot diverge. `TPL CHECKLIST-one-home` reddens if a gate table is planted back there.
> **This table is now the gate's one home** (`C-50`).
