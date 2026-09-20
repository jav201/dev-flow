# Validation — <PROJECT> — Batch <BATCH_ID>

> **Artifact language:** canonical English scaffold. Generate in the batch's development language (`state.json` `language`); for Spanish batches **translate the prose, never a label** — the reserved field names are declared in §✅ Verdict and are read literally.
> Phase 4 artifact. Owner: `qa-reviewer`, who **EVALUATES** the results of the validation strategy fixed in Phase 1 and **names who executed each one**. The ONE complete gate-suite run is the orchestrator's (`C-25`); a sub-agent consumes the result and never owns the run. *(This line read `Executes the validation strategy fixed in Phase 1` until flow rev73 — the retired claim, live, in the artifact the agent owns, and the site rev73's first census pass missed while congratulating itself on finding another.)*

> **Owed in.** `fast` — · `core` ✓ · `full` ✓
> **Source:** `/dev-flow-init` step 4's seed-by-mode table, which is this fact's one home (flow rev72, `T05`). A mode marked `—` **does not owe this artifact, and its absence is not an omission**; `by trigger` means the station exists only when the `triggers` block fired, and `stations_active` in `state.json` is the authority for *this* batch. Where a SECTION or a gate row is owed more narrowly than the artifact, it says so on the row.

> **Why one artifact — vs the six documents of IEEE 829 / ISO/IEC/IEEE 29119-3.** The
> test-documentation standards split plan, design, cases, procedures, log and report into six
> documents because they assume separate authors, audiences and approval cycles. This flow has one
> author (`qa-reviewer`), one audience (the gate) and one cycle (the batch), so the six collapse
> into two homes: the PLAN half (plan · design · cases) is authored in Phase 1 — every requirement
> carries its executed verification + numeric threshold, and `AT`/`TC` are born with the spec; the
> RESULT half (procedures · log · report) is THIS artifact — verdict-first, evidence per row,
> reconciliable ledger. What the standard demands survives as **fields**, not as documents. Under
> the living-artifact model (rev42+), the RESULT half is also the increment that feeds the living
> validation/evidence canon — the human-audit plane that must stay coherent with the
> machine-readable plane (IFC/Atlas) — and fields, not documents, are what make that coherence
> mechanically checkable.

## ✅ Verdict (read first)

> **Reserved field names.** The **field names and block keywords below are language-independent** — the
> validator parses them literally and they are never translated:
> `Result` · `Layer 0` · `Evidence checklist` · `⏸ DEFER`
> Everything else on this page — headings, guidance, the prose in every cell — is translated with the batch.
> **One strategy, not two:** the flow ships no alias table, so a translated label is read as an ABSENT one and the rule keyed on it reports a true-sounding silence.
> **And one FLOW-WIDE reserved token, read out of this artifact by `V42` no matter which template minted it:** `⏸ DEFER`. It is a MARKER rather than a field name, which is why it is stated here *and* in `/dev-flow` §Language of artifacts rather than in a per-template list — a deferral can be written in any batch artifact, including the ones that carry no block at all. Measured: `⏸ DIFERIDO` returns the empty declaration list AND the empty near-spelling list, so a translated marker is indistinguishable from a batch that deferred nothing.
>
> **And so are the three verdict tokens** `PASS` · `PASS-WITH-NOTES` · `FAIL`, which are VALUES and not prose.
> A Spanish batch writes `- **Result:** PASS`, not `- **Resultado:** aprobado`: the label, the tokens and the
> reviewer-identity tokens below are the machine's vocabulary.

- **Result:** `<PASS | PASS-WITH-NOTES | FAIL>`
  > *The three tokens are the flow's WHOLE batch-verdict vocabulary, and the same set is named at every*
  > *site that states one: `phase-checklists.md` row 9, `dev-flow-sync.md`'s `RC-S1` structural detect, and*
  > *the gate rule that reads this line. Write ONE token here — the alternation is guidance and belongs*
  > *outside the value. `FAIL` routes to `iterate-to-fix` (P3, an implementation defect) or to*
  > *`iterate-to-refine` (P1, a requirement defect); name which one on the line below this field.*
  > *The reviewer verdict of an increment gate is a DIFFERENT vocabulary (`PASS` / `PASS-WITH-NOTES` /*
  > *`BLOCK`, `increment-template.md` §4b) and is not written here.*
- **Layer 0:** `<N unit(s) met the criterion · N carry a named reddening mutation>`
  > *`C-51`. The roll-up over §*Layer 0 — unit*'s two tables. The legal empty is*
  > *`none — no unit met the decision or boundary criterion`, and it is a DECLARATION: `C-51` supplies*
  > *the exclusion list (pure delegations, getters, UI wiring, constructors that only assign,*
  > *branchless one-liners), so an empty population is an answer and a blank line is not.*
  > *The signed-balance test ledger is a different fact with its own reader (`V5`) and its own row below —*
  > *do not restate its arithmetic here.*
- **Requirements:** `<P>`/`<T>` pass · `<N>` blocker fails
- **Black-box acceptance (Layer B):** ✓ every story's `AT` observes its outcome through the shipped surface (boundary + negative)  /  ⚠ `<N>` stories with no deliverable observation
- **Surface-reachability (bidirectional):** ✓ all named inputs AND outputs/deliverables reached/observed at the surface  /  ⚠ `<N>` gaps
- **Supersession inspection (read off the P3 packets, rev60):** ✓ all surviving refs negative  /  ⚠ live dependency found  /  ⚠ no packet ran it
- **Test ledger:** ✓ reconciles (`base − D + A = post`)  /  ✗ mismatch
- **Evidence checklist (qa-reviewer):** `<reviewer · N of M rows ✓ with evidence>`
  > *Lead the value with WHO completed it — `qa-reviewer` · `code-reviewer` · `security-reviewer` ·*
  > *`ux-reviewer` · `tester` · `human:<name>` · `WAIVED-BY-OPERATOR — <reason>`. This is `V36`'s identity grammar,*
  > *reused rather than re-minted, and it is the same question at a different station: a checklist that*
  > *names nobody is not an answer. Then `N of M` rows ✓, counted over the section*
  > *`Evidence checklist — qa-reviewer (full)` below. **Every unchecked row carries its reason***
  > *there — the record's own*
  > *checklists are written six different ways (`- [x]` lists, ✓/✗ glyph lists, three- and four-column*
  > *tables), so the count is declared here and the rows are read there.*

> If every line is ✓, the Detail below is reference only. Any ⚠/✗ → read the matching part.

---

## Detail (reference)

### Layer 0 — unit

Applies where **either** criterion holds: the unit has **cyclomatic complexity ≥ 3**, **or** it transforms
data crossing a boundary declared in `docs/ARCHITECTURE.md`. Out: pure delegations, getters, UI wiring,
constructors that only assign, branchless one-liners.

| Unit | Which criterion | Node id | Result |
|---|---|---|---|

**Measured by mutation, never by line coverage.** For each unit, name the mutation and paste the RED:

| Unit | Mutation applied | RED observed? | Transcript |
|---|---|---|---|

- ⚠ A layer-0 node whose reddening mutation cannot be named is not a test yet.
- **If no unit met either criterion, say so** — `none — no unit met the decision or boundary criterion`
  — and roll it up into the keyed `**Layer 0:**` field at the top. An empty population DECLARED is an
  answer; two empty tables are not, and nothing can tell them from a section nobody reached.

### UX walkthrough — only if trigger family D fired

| Criterion (when the user does X, they observe Y) | Driven with the REAL mechanism | Painted result asserted | Verdict |
|---|---|---|---|

**Mechanism used:** `<the UI framework the UI test driver | a headless-browser driver | CLI subprocess | artifact on disk | none — inspected only>`

> **No browser driver ships with this flow.** If this runtime has none, the row is
> `not-run — no browser driver on this runtime` and the walkthrough is an **inspection**, which
> has its own name and its own bound. `agents/ux-reviewer.md`'s surface table is that fact's one
> home; this row records the ANSWER.

- ✗ A proxy in place of the interaction (a direct setter, `.focus()` instead of the real keys) is not evidence of the interaction (C-16).
- ✗ On web, a selector you authored without looking is a vacuous check — a selector that matches nothing fails exactly like an absent element. Act by a ref the driver itself reported from a live snapshot of the page, never by a selector you typed from memory.
- ⚠ A console/network count of `0` counts as evidence **only** if the capture header is clean; `** capture DEGRADED **` means the signal was off, not that the page was healthy.
- ✗ A pre-layout assertion is not the painted result (C-32).

**Evaluation with users (ISO 9241-210) — state which of the three happened, never which one did not.**
The three are different acts and the weaker one is never evidence of the stronger:

| Act | What it is | Performed? |
|---|---|---|
| Automated walkthrough | the criteria above, driven through the REAL mechanism | `<performed · not performed — <reason> · not applicable — no trigger-D surface>` |
| Expert inspection | a cognitive walkthrough against declared criteria, by a reviewer and not a user | `<same three states>` |
| Evaluation with users | real users of the system, doing the tasks named in the context of use | `<same three states>` |

- **Method:** `<how it was run — tasks, setting, whether the operator sat with the participant>`
- **Participants or population:** `<how many, and what makes them users of THIS system — no PII: no names, no contact details, no employer, no anything that identifies a person>`
- **Evidence of the evaluation:** `<where the record is — a path under the batch's declared `evidence` home, a transcript, an artifact on disk>`
- **Limits:** `<what this does NOT establish — sample size, self-selection, the operator watching, tasks chosen by the author>`

- ✗ A driver run is not a user. Promoting an automated walkthrough or an expert inspection into
  *evaluation with users* is the vacuous assertion this section exists to refuse.
- ✓ `not performed — this team is one person and no user of this surface exists outside it` is a
  complete and honest answer. **What is refused is the OPPOSITE defect:** a pre-written sentence
  denying an evaluation that did happen. `close-template.md` states this obligation in the form
  this section now uses — *declare what was NOT done*, keyed to what happened.
- ⚠ **Nothing reads this section, and that is stated rather than left to be discovered** (`C-58`).
  Its precondition is `state.json` `triggers.fired` containing `D`, which the flow has only seeded
  since rev62 and which no CLOSED batch carries — so the corpus a reader would need does not exist
  yet. This section is a paragraph on purpose, and it becomes a keyed field the day one closed batch
  carries a real trigger-D record. The keyed rows at the top of this page are the ones the gate reads.

### Layer A — functional (white-box): per-requirement results
> `TC-NNN` ↔ LLR/HLR. `Result` = pass / fail. `Evidence` = command output, observed behavior, inspection note, or analysis result.

| Req | Method | Executed verification | Numeric threshold | Result | Evidence |
|-----|--------|-----------------------|-------------------|--------|----------|
| *(example — delete)* HLR-001 | test | `pytest … -k TC-001` | exit 0 | | |
| *(example — delete)* LLR-001.1 | test (unit) | `…` | `…` | | |

### Layer B — behavioral (black-box) acceptance
> `AT-NNN` ↔ user story. Drive the SHIPPED surface (the UI framework the UI test driver `App.run_test()` / CLI / artifact-on-disk), assert the outcome with representative + boundary + negative inputs PLUS the actual deliverable observed. An output-producing story's `AT` FAILS if the deliverable is silently absent. `AT-NNN` reconciled to the real collected node per V-5.

| US | Acceptance test (`AT-NNN`) | Surface driven | Deliverable observed (path / element) | repr · boundary · negative | Result |
|----|----------------------------|----------------|---------------------------------------|----------------------------|--------|
| *(example — delete)* US-001 | `AT-NNN` | `<handler/screen/CLI>` | `<file:path non-empty + content \| element>` | ✓·✓·✓ | pass / fail |

### Bidirectional surface-reachability matrix (extends A-5, batch-11)
> Every named INPUT dimension AND every named OUTPUT/deliverable is exercised/observed through the handler — not only the service API.

| Direction | US dimension / deliverable | Service param / producer | Reached/observed at surface? | TC / AT | Status |
|-----------|---------------------------|--------------------------|------------------------------|---------|--------|
| input | `<dimension>` | `<param>` | yes/no | `TC-NNN` | ✓ / gap |
| output | `<deliverable>` | `<producer>` | yes/no | `AT-NNN` | ✓ / gap |

### Supersession-completeness inspection — MOVED to P3 at flow rev60
> It now lives in `increment-template.md` §*"Correction population"*, as that field's executed inspection step. **Why it moved:** run here, at P4, the sweep happens after every site has already been edited, so it measures damage rather than risk — and the obligation it encodes is the population rule, which belongs before the first edit. Read the increment packets' tables; this section is a pointer, not a second home (C-50).

### Signed-balance test ledger (batch-07 / 09)
> `post = base − D + A`. State counts in collected / passed-lean / passed-full form.

| base | − D | + A | = post | actual collected | passed-lean / full | reconciles? |
|------|-----|-----|--------|------------------|--------------------|-------------|
| `<N>` | `<N>` | `<N>` | `<N>` | `<N>` | `<N>` / `<N>` | yes/no |

### Gaps detected
| ID | Requirement | Gap | Severity | Proposed action |
|----|-------------|-----|----------|-----------------|
| G-001 | | | blocker / major / minor | |

### Escaped-bug regression (if a defect escaped the suite)
> The fix ships a shipped-surface regression that demonstrably FAILS pre-fix (capture the failing run) then passes. Id provisional per V-5.
> **QC-2 — value-discriminating counterfactual:** when the pre-fix RED is a *shape* failure (TypeError, missing-arg, constructor/signature mismatch) rather than a *value* mismatch, the regression proves the call path is wired, not that the assertion discriminates the right value. Confirm the POST-fix assertion also fails on a wrong-but-well-typed value. (Origin: batch-16 QC-2 — see dev-flow-lessons)

| Regression id (`AT-NNN` / `TC-NNN`) | Pre-fix run (evidence it FAILED) | Pre-fix RED kind (value / shape) | Post-fix value-discriminating? (QC-2) | Post-fix result | Reconciled node |
|-------------------------------------|----------------------------------|----------------------------------|----------------------------------------|-----------------|-----------------|
| | | | | | |

### Evidence checklist — qa-reviewer (full)
> Attach `qa-reviewer`'s completed evidence checklist (items in `agents/qa-reviewer.md`), each marked ✓/✗ with one-line evidence. An unchecked or evidence-less item blocks the gate.
> **Every ✗ row carries its reason on the row** — an unchecked item with no reason is indistinguishable
> from one nobody read. Roll the result up into the keyed `**Evidence checklist (qa-reviewer):**` field at
> the top of this page: the reviewer who completed it, then `N of M` rows ✓.
> ⚠ **The row SHAPE is deliberately not fixed and the count is therefore declared, not derived.**
> Measured over this project's record on 2026-09-10, the 32 artifacts carrying this section write its rows
> six ways — `- [x]` checkbox lists (6 to 12 rows), ✓/✗ glyph lists (8 to 15), a `# · Item · ✓/✗ · Evidence`
> table, a `✓ · Item · Evidence` table, and two that carry neither form. A rule counting rows would be a
> rule keyed on one of six spellings; the keyed field above is what the gate reads.
