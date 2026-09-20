# Requirements Document — <PROJECT> — Batch <BATCH_ID>

> **Artifact language**
> This template is the canonical **English scaffold**. Generate the artifact in the batch's development language (`state.json` `language`). For Spanish batches, translate the **prose** — section headers and guidance — **and never a label**, and use `deberá` as the normative keyword (≡ `shall`). The normative RULES in this preamble are **language-independent** and enforced regardless of artifact language.

> **Owed in.** `fast` — · `core` ✓ · `full` ✓
> **Source:** `/dev-flow-init` step 4's seed-by-mode table, which is this fact's one home (flow rev72, `T05`). A mode marked `—` **does not owe this artifact, and its absence is not an omission**; `by trigger` means the station exists only when the `triggers` block fired, and `stations_active` in `state.json` is the authority for *this* batch. Where a SECTION or a gate row is owed more narrowly than the artifact, it says so on the row.

> **Reserved field names.** The **field names and block keywords below are language-independent** — the
> validator parses them literally and they are never translated:
> `Validation` · `Acceptance test(s)` · `Boundary catalog` · `Negative control` · `Premise evaluation` · `Fork preconditions` · `Ledger` · `Requirement` · `⏸ DEFER`
> Everything else on this page — headings, guidance, the prose in every cell — is translated with the batch.
> **One strategy, not two:** the flow ships no alias table, so a translated label is read as an ABSENT one and the rule keyed on it reports a true-sounding silence.
> **And one FLOW-WIDE reserved token, read out of this artifact by `V42` no matter which template minted it:** `⏸ DEFER`. It is a MARKER rather than a field name, which is why it is stated here *and* in `/dev-flow` §Language of artifacts rather than in a per-template list — a deferral can be written in any batch artifact, including the ones that carry no block at all. Measured: `⏸ DIFERIDO` returns the empty declaration list AND the empty near-spelling list, so a translated marker is indistinguishable from a batch that deferred nothing.
>
> The IFC block keywords this document also carries — `FLOW`, `COMPONENT` and their fields — are reserved
> on the same terms and are listed once, in `ifc-template.md`, which is where they are minted. Two copies of
> one inventory is `C-50`'s defect, and the list a reader needs is the one beside the syntax.

> **THE LEAN CONTRACT — two documents, and only one of them is editable (rev48, `V26`).**
> The batch authors **`01-requirements.md`, the live contract**, and **`01-requirements-ledger.md`, the append-only ledger**. This is not a filing convention; it is what makes the record readable and what keeps a correction from having an unenumerated population.
>
> - **The live contract holds CURRENT STATE ONLY.** Every requirement reads as what it obliges *today*: no strikethrough, no amendment bullets, no supersession narration, no measurement written inside a normative sentence. A requirement of the form *"the X shall Y, **because measured `<date>` the Z…"*** is two sentences wearing one: the obligation stays here, the measurement goes to the ledger. **Splitting the FILES is a 35% cut and not a fix — splitting the SENTENCE is the fix.** (Origin: batch-88 record measurement — see dev-flow-lessons)
> - **The ledger is APPEND-ONLY and is NEVER edited.** Entries are added, never rewritten and never deleted, each stamped with its date. A previously-written entry that turns out wrong is corrected by a NEW entry that supersedes it and says so.
> - **Both documents declare the link, and it is compared both ways.** Every requirement carries a **`**Ledger:**`** field naming its entries; every ledger entry carries a **`**Requirement:**`** field naming the requirement it amends. `V26` compares the two SETS OF (requirement, entry) PAIRS and BLOCKs on any pair present on one side only.
> - **`**Ledger:** none` is legal and MUST be written.** An omitted field is a question nobody asked — the same ruling this flow already makes about `consumers : none`.
> - **Why an append-only ledger rather than two editable files:** two editable files disagree, and *"a correction has a population and nothing enumerates it"* is the most repeated defect this flow has measured. A naive split rehouses that defect instead of closing it. What closes it is that the population **is** enumerated — as pairs, on both sides, checked.
> - **The budget is a MEASURED SIZE, and its number lives in the code.** `V26` NOTICEs a live contract past `_LEAN_MAX_CHARS` (`devflow-validate.py`). Cite that symbol; **do not restate the figure in a record**, or the record and the rule acquire two copies of one number. The budget applies to the live contract and **never to the ledger** — a budget over an append-only file is a standing instruction to delete history.
> - **What is NOT checked, said out loud:** the register itself. `V26` sees strikethrough, which is a Markdown *delimiter* and therefore has a grammar; it does not police the words "superseded", "amended" or "measured", because prose has no grammar to derive a class from and an enumeration of banned phrases kills only the wordings someone thought of. **Whether a normative sentence carries its own justification is a reviewer's judgement, and it is a Phase-2 blocker class.**

> **Strict normative convention — ISO/IEC/IEEE 29148 + EARS** *(29148:2018 supersedes the retired IEEE 830, which this flow cited until rev40)*
> - `shall` / `deberá` = normative, binding, verifiable requirement. **Only** inside HLR / LLR statements.
> - `should` / `debería` = informative / explanatory text, **NOT binding**. **Only** outside HLR / LLR statements (rationale, description, context).
> - Any modal `should` / `debería` inside an HLR / LLR statement is a **writing error** and will be flagged as a blocker in phase 2.
> - `may` = optional. `will` = future declaration or fact about an external actor.

> **Verifiability rule — captured at draft, not at phase-2 gate**
> (Origin: batches 02-03 — see dev-flow-lessons)
>
> Every requirement labelled `test` or `analysis` **must** carry TWO fields on its line:
> - **Executed verification:** what EXACTLY runs / is inspected (e.g. `npm run typecheck`, `vitest run path/to/file.test.ts -t TC-001`, `signature-diff inspection vs main`). Without this the method is not executable.
> - **Numeric pass threshold:** the quantitative pass criterion (e.g. `0 errors`, `peak post-limiter ≤ −6 dBFS`, `RMS error < 0.01`, `LLR coverage ≥ 100 %`). Without this the result is not objective.
>
> For `demo` (perceptual): describe the observable procedure + the named qualitative criterion.
> For `inspection` (structural): name the file / commit / section to inspect + the observable condition.
>
> **Any `test`/`analysis` LLR missing these two fields is a phase-2 blocker.**

> **Parent-HLR re-read rule — captured at the Phase-1 reconciliation gate**
> **Why this rule mandates an ARTIFACT and not a process step:** a rule that says *"re-read"* with no required output silently degrades to *"I thought about it,"* which is why writing it as prose did not stop the third recurrence. (Origin: batches 06-08 — see dev-flow-lessons)
>
> **Any time an LLR's `Numeric pass threshold` or `Statement` changes at the Phase-1 reconciliation gate — or an LLR is added/promoted/removed — the §6.4 reconciliation log MUST contain a per-decision audit table** with one row per changed decision and these columns: `Decision ID | What changed | Parent HLR re-read? (which HLR + what changed there, or "no change required" + why) | Body edit landed? (the §3/§4 line that now reflects it)`.
>
> **Body-first ordering is mandatory:** write the §3/§4 HLR/LLR body edit FIRST, then write the §6.4 audit row that points at it. Never write a §6.4 claim before the body line it describes exists. This eliminates the "claimed but missing" failure mode that recurred in batch-06/07/08.
>
> **Two phase-2 blockers enforce this:** (a) any HLR threshold contradicting its decomposed LLRs; (b) any §6.4 audit row whose "Body edit landed?" column points at a §3/§4 line that does not exist (a reviewer greps for it). Both are mechanically checkable.

> **Testing-strategy-vs-ADR rule — captured at draft, not at phase-3 boundary**
> (Origin: batch-06 — see dev-flow-lessons)
>
> **Every `test (...)` validation label MUST be cross-checked against the project's testing-strategy ADR and the actual `package.json` / `requirements.txt`** before locking the LLR. If the labelled runtime isn't installed and isn't the strategy-ratified path, that's a phase-2 blocker.

> **LLR symbol-citation rule — captured at draft, not at the phase-3 boundary**
> **The failure mode this closes is "named a symbol that looks like it should exist"** — a symbol inferred from plausible symmetry rather than read off the code. **And it mandates a CITATION, not a process step,** because a rule that says *"verify"* with no required artifact silently degrades to *"I assumed."* (Origin: batch-05 — see dev-flow-lessons)
>
> **Any LLR (or its `Acceptance test(s)` / `Negative control` / `Executed verification`) that names a concrete code symbol — a private field, method, function, class, or widget id — MUST cite a grep-verified `file:line` for that symbol at draft time.** If the symbol does not yet exist (it will be created by the increment), it MUST be explicitly flagged `NEW — created in Phase 3` so the reviewer does not expect to find it. Layout-geometry / magic-number constants (pane widths, row counts, byte offsets) MUST either cite a measured value with the measurement method, or be flagged `assumed — verify in Phase 3`.
>
> **Two phase-2 blockers enforce this:** (a) any LLR that names a symbol without a `file:line` citation and without a `NEW` flag (a reviewer greps for the symbol; if it neither exists nor is flagged NEW, block); (b) any layout/magic-number constant asserted as fact without a measurement citation or an `assumed` flag. Both are mechanically checkable by grep.

> **Environmental-measurement citation rule — extends the LLR symbol-citation rule.** Any constant describing the runtime or layout **environment** — container/parent widths, derived geometry (e.g. `body_w`, pane shares), responsive breakpoints and transition points, timing/latency budgets, platform or CI environment values — MUST cite, at draft time: **(a) WHERE it was measured** (the probe or test `file:line`, or the exact `App.run_test(size=...)` / command invocation), **AND (b) the REGIME/CONDITIONS under which the measurement holds** (terminal-size band, CSS class state, rail/panel visibility, platform, dataset size). A measurement applied **outside its measured regime** MUST be re-measured in that regime or flagged `assumed — verify per-regime`. **Derived numbers inherit the flag**: any cell count, threshold, or transition point computed from an environmental constant is not a fact until the underlying measurement is regime-valid, and must cite the constant it derives from. **Phase-2 blocker classes:** (a) an environmental constant asserted as fact whose citation lacks its measurement conditions; (b) a constant or its derivatives applied in a regime other than the one cited. (Origin: batch-06 B-1 — see dev-flow-lessons)

> **Probe self-test rule — captured from batch-07 B-3/B-4.** Any executable verification artifact written into an HLR/LLR — a grep/rg probe, a regex, a pytest node id, a determinism/equality procedure, an inspection command — MUST be EXECUTED at draft time against the current tree, with its **expected pre-state result recorded next to the spec** (e.g. "probe run 2026-06-10: 164 hits pre-retirement; pass condition = 0 post"). A probe that cannot demonstrate a non-trivial pre-state — hits today for a future-absence check, a failing-then-passing pair for a behavioral check, both sides exercised for an equality — is unproven and shall be flagged `unexecuted — verify in Phase 2`. **Phase-2 blocker classes:** (a) a verification command recorded without executed pre-state evidence; (b) a verification whose pre-state execution contradicts its claimed semantics. (Origin: batch-07 — see dev-flow-lessons)

> **Contract-touch rule — captured from batch-07 B-1/B-2.** A cross-cutting interface contract (canonical field set, producer/consumer table) is reconciled at merge but **invalidated by any subsequent edit to any LLR it cites** — including gate-decision insertions, which are the most likely to add fields and the least likely to be reconciled. Any post-draft edit touching a producer or consumer LLR re-opens the contract as a mandatory checklist row: the editor shall re-run the identity check (field-set equality across every producer and consumer enumeration) and record the re-run in that edit's audit-table row. An edit that adds a field to one side without the recorded re-run is a Phase-2 blocker. (Origin: batch-07 — see dev-flow-lessons)

> **AC-artifact citation rule — extends the LLR symbol-citation rule.** Any data artifact named in an HLR/LLR acceptance slot — `Acceptance test(s)`, `Boundary catalog`, `Negative control` or `Executed verification` — a test fixture, example file, directory, or data path — is citation surface, same as a code symbol: it MUST carry either an EXECUTED existence probe recorded at draft time (e.g. `Glob examples/**/*.hex → N files, <date>`) or an explicit `NEW — created in Phase 3` flag with the artifact counted in the increment file budget. **Phase-2 blocker:** an AC-named artifact with neither an executed existence probe nor a NEW flag. (Origin: batch-08 — see dev-flow-lessons)

> **Probe-regime rule — extends the probe self-test rule.** A probe's positive control MUST exercise the same syntactic/structural REGIME as the protected targets (import depth, package level, file class, CSS state, platform), and the ledger entry MUST state that regime next to the recorded execution. If the target does not exist yet, the control runs on a synthetic in-regime fixture created at the exact target location/depth and deleted after (the batch-08 `_b2_scratch` pattern: scratch package at target depth → probe hits all violation forms → negative control on a known-legitimate module → scratch removed). An out-of-regime control does not discharge the probe self-test rule — it is recorded `superseded-pending` until an in-regime control exists. **Phase-2 blocker classes:** (a) a probe whose positive control's regime differs from the target regime; (b) a ledger entry that omits the control's regime. (Origin: batch-08 — see dev-flow-lessons)

> **Supersession-census-completeness rule — captured from batch-09 Lesson 1, reframed at batch-10.** When a batch supersedes scaffold/placeholder behavior OR adds/moves a module OR edits an existing file, the Phase-1 supersession census MUST account for ALL guard families that the change can break, not only the named behavioral-placeholder one: (a) **behavioral-placeholder guards** — deferral/placeholder/"not-yet" assertions; (b) **structural / placement / allowlist guards** — package-shape invariants (e.g. `rg -n 'glob\(.\*\.py.\)|listdir|iterdir|allowlist|_root_modules' tests/`); (c) **AST-composition guards** (e.g. `rg -n 'ast\.|\.body|calls\s*<=' tests/`); (d) **engine-frozen / no-diff-vs-main guards** (e.g. `rg -n '_ENGINE_PATHS|no_diff_vs_main|engine_modules_unchanged' tests/`). The predicted-red set is incomplete until all run; any guard whose invariant the change violates is added with its disposition at Phase 1, not discovered at the increment gate. (Origin: batches 09-10 — see dev-flow-lessons)

> **Census = completeness PRINCIPLE, not a grep checklist (A-1, batch-10).** The family list above is a starting set, NOT an exhaustive enumeration — "grep these N patterns" is structurally blind to any guard whose pattern isn't listed. The census MUST be run **change-first**: take the batch's planned new/moved/edited file list and, for EACH file, check it against EVERY test that asserts on a file PATH / module STRUCTURE / import GRAPH / git-DIFF (key on the CATEGORY of assertion, not the specific pattern). A guard that fires on a planned file is a Phase-1 finding, before code. **Corollary — new-symbol-into-existing-file probe (A-3):** any LLR adding a NEW symbol to an EXISTING module MUST cite a draft-time probe proving that file is not frozen/allowlisted against the edit. (Origin: batch-10 — see dev-flow-lessons)

> **Ban the "VERIFIED COMPLETE" census stamp (A-2, batch-10).** A census/completeness claim MUST NOT be stamped "VERIFIED COMPLETE" by re-running the known families — re-running an incomplete checklist cannot detect that the checklist is incomplete. A completeness verdict must EITHER show why no (N+1)th family exists (the enumeration of the whole structural-guard surface), OR be downgraded to "best-effort + gate-confirmed." **The increment GATE — running the actual moved/edited file against the real suite — is the completeness guarantee; the census is a Phase-1 cost-reduction heuristic that catches it cheaply, not a proof.** (Origin: batch-10 — see dev-flow-lessons)

> **Supersession-completeness inspection (V-3, batch-09) — EXECUTED AT P3, VERIFIED AT P4. One station, and this sentence used to name the wrong one.** The inspection greps the WHOLE class of superseded placeholder constants/markers and asserts every surviving reference is a NEGATIVE assertion (absence), not a live dependency — e.g. confirm the only surviving `#diff_deferral_notice` reference is `not bool(...)` and the removed constants survive solely inside a "they're gone" guard. **Its executed home is `increment-template.md` §*Correction population* / §*Supersession-completeness inspection*, at P3, read by `V32`** — run at P4 the sweep happens after every site has already been edited, so it measures damage rather than risk. **P4 keeps a matrix row and its subject is the RECORDED P3 RESULT**: `validation-template.md`'s *Supersession inspection (read off the P3 packets)* row, which verifies the recorded population is still current and reports *no packet recorded one* as its own state. A by-hand confirmation is insufficient at either station. ⚠ **Correction to flow rev60's population, recorded where this record keeps history:** rev60 relocated the inspection and judged THIS site *a different object*, so the mandate above survived reading `the Phase-4 validation matrix MUST include a row that greps the WHOLE class` — an EXECUTED row at P4, not a planning census at P1/P2, in its own words. Measured 2026-09-10 by CATEGORY rather than by the string `Phase-4`: six sites state this obligation and five already name P3-executes / P4-verifies; this was the one that did not. (Origin: batch-09; relocated flow rev60, this site swept flow rev69.)

> **Provisional-identifier scope rule (V-5, batch-09).** The `provisional until Phase 3` flag (batch-08 A-3) covers EVERY implementer-owned identifier in an Executed-verification line — the test FILE path AND the `-k` selector AND the pytest node id — not only node ids. A pinned-but-wrong file name or `-k` token produces a false "test missing" signal at the validation gate exactly as a pinned node id does. Spec convention: "Executed-verification file paths, `-k` selectors, and node ids are all provisional-until-Phase-3; the implemented names are reconciled from the real tree at Phase 4." (Origin: batch-09 — see dev-flow-lessons)

> **Purity-probe form rule (V-4, batch-09).** An import-purity probe MUST match import statements, not the bare token — use `rg -n "import <pkg>|from <pkg>|<Pkg>"`, never substring `rg -c "<pkg>"` (which matches the word in docstrings/prose and yields a benign-but-noisy false positive that must then be hand-resolved). (Origin: batch-09 — see dev-flow-lessons)

> **Story-dimension coverage / surface-reachability rule (A-5, batch-11).** Coverage must reach the SHIPPED surface, not only a service's direct API. (a) For each input dimension named in a source user story, ≥1 TC MUST exercise it through the shipped surface (the handler/UI call-site), not only via direct service kwargs. (b) When a handler wires a writer/service that accepts dimensions the handler defaults empty, decompose a COMPOSITION LLR for that wiring or record the dimension out-of-scope explicitly. (c) Phase-4 carries a standing surface-reachability matrix row: handler call-site kwargs vs service signature vs story dimensions. (Origin: batch-11 — see dev-flow-lessons)

> **Two-layer validation rule — black-box behavioral acceptance + white-box functional (headline, non-negotiable).** A user story is a user-verified OUTCOME / observable behavior (the WHAT), validated black-box through the shipped surface; HLR/LLR are the internal workings (the HOW), validated white-box by functional TCs. **No story is "done" until a black-box test (`AT-NNN`) observes its user-verified outcome through the shipped surface, with boundary + negative evidence — independent of the white-box `TC-NNN` that validate the HLR/LLR mechanism. A green white-box suite that never observes the behavior is not acceptance.** Every output-producing requirement MUST name its concrete deliverable and how it is observed (file at path + non-empty + required content; or rendered screen element). **Dual traceability is mandatory** — and it is DERIVED, never transcribed here: behavioral `US → AT-NNN → observed outcome` AND functional `US → HLR → LLR → TC-NNN`; a requirement with only one chain is incomplete. Both chains are read from the per-requirement `Traceability` and `Acceptance test(s)` fields, by `V10`/`V21`, and published at `.dev-flow/_derived/ATLAS-TRACE.md`. *(The §5.2 section that used to hold two transcribed tables was retired 2026-08-28 and its heading deleted at flow rev69 — a heading whose whole body said the thing under it was gone is a fourth opinion, and 13 of 66 live contracts had copied it forward after its content was withdrawn.)* Layer B is the `test (driver)` / e2e / artifact-on-disk idiom (automated), **not `demo`**; `AT-NNN` ids are provisional-until-Phase-3 per the **Provisional-identifier scope rule (V-5)** and reconciled at Phase 4. **Phase-2 blocker classes:** (a) a story with no `AT`; (b) an output-producing requirement that doesn't name its observable deliverable + observation method; (c) an incomplete traceability chain (either side); (d) an "acceptance" test that references an internal symbol (not genuinely black-box). (Origin: batch-14 — see dev-flow-lessons)
>
> **State-lifetime provenance rule (batch-24).** When a story CONSUMES state captured earlier by another flow (a retained summary, a cached result, a stamped path), the spec MUST state that state's LIFETIME story — who writes it, what invalidates/clears it, what happens if the world changed since capture (file reloaded, project switched) — and bind consumption to provenance (a recorded link to what the state was derived FROM, refused on mismatch). A consume-only story gets no new-write-surface security pass by default, so this is the spec-layer net. (Origin: batch-24 — see dev-flow-lessons)

> **Per-item versioning and baselines (operator decision, 2026-08-10).**
> Requirements and their verifying nodes carry a **version of their own**, not only the document's:
> `R-014 v3` · `AT-014a v2` · `TC-014.1 v1`. The consolidated requirement document stops being prose —
> every line has a version, an owner and a proof.
> - **A requirement does NOT rise in version unless its `AT`/`TC` rises with it, or is explicitly re-confirmed.** That single rule is what keeps the document from drifting away from what is actually verified.
> - **Baseline:** at batch close the full `(item, version)` list is sealed. *That* is what QA reviews when it "reviews numbering".
> - **The batch's contribution = the delta:** which items rose in version, which were born, which died. It is the same §6.5 Before/After delta — now with a destination.
> - Every requirement cites, by id, the design record that originated it — the record's own id, then `#D` and the decision number, as in `PDR-2026-09-07-batch-01#D3`. **Written as a CONCRETE id and not as `<placeholder>`, because `V23` reads this line in every copy of this template and an angle-bracketed batch segment does not parse under the grammar it enforces.** The ids are the glue of the repo↔vault split; without them the split breaks traceability instead of organising it.

> **Context of use in the source stories (ISO 9241-210, activity 1).**
> A story that reads "as `<role>` I want `<goal>` so that `<benefit>`" stops short: it names the user and
> the goal but not the **task** or the **environment**, and a UX criterion has nothing to be true *about*
> without them. Every story in §2.6 therefore carries four lines:
> **user** (who, with what expertise) · **task** (what they are in the middle of doing) ·
> **environment** (where, on what, under what constraint — terminal size, offline, interruption, hurry) ·
> **observable outcome** (what they see when it worked).
> This is four lines, not a study. Its consumer is the `ux-reviewer` lens and the acceptance block; if a
> story's outcome is not observable through the shipped surface, it is mis-captured → `REFINE`.

---

## 1. Introduction

### 1.1 Purpose
*(Informative text. Describes the document's objective.)*

### 1.2 Scope
*(What this batch covers and what it does NOT cover.)*

### 1.3 Definitions, acronyms, abbreviations
| Term | Definition |
|------|------------|
| | |

### 1.4 References
*(Related documents, standards, external tickets.)*

### 1.5 Document overview
*(How this document is structured.)*

---

## 2. Overall description

### 2.1 Product perspective
*(How the change fits into the larger system.)*

### 2.2 Product functions
*(High-level list of functional capabilities.)*

### 2.3 User characteristics
*(Roles, permissions, expected experience levels.)*

### 2.4 Constraints
*(Technological, regulatory, business.)*

### 2.5 Assumptions and dependencies
*(What we take for granted. If an assumption fails, the batch is invalidated.)*
> ⚠️ An assumption listed here that the batch RELIES ON must be evaluated in **§2.7** with a verdict. Prose here is a statement of intent; §2.7 is where it becomes checkable.

### 2.6 Source user stories

> Connextra format: **"As a `<role>`, I want `<goal>`, so that `<benefit>`"**. Each US gets a unique ID `US-NNN` and must be traceable to one or more HLRs.
> **Phase 0 — Definition of Ready (INVEST):** every story is refined and classified before it can be derived into HLR (Phase 1). Only `READY` stories proceed.

| ID | User Story | Source | DoR status |
|----|------------|--------|------------|
| US-001 | As a `<role>`, I want `<goal>`, so that `<benefit>`. | `<ticket / conversation / client>` | READY \| REFINE \| SPIKE \| OUT |
| US-002 | | | |

#### Refinement log (one block per story)

**US-001 — `<short title>`**
- **INVEST:** I · N · V · E · S · T  (mark ✓/✗ each)
- **Functionality (V, N):** user = … · outcome = … · why = … · out of scope = …
- **Feasibility (E, S):** implementation path = … · dependencies/unknowns = … · fits one batch? = yes/no (split or spike if no)
- **Evaluability (T) — behavioral, black-box:** ≥1 observable acceptance criterion at the behavior level = "When `<input>`, the user observes `<outcome through the shipped surface>`" (becomes an `AT-NNN` in Phase 1). A story phrased as a mechanism (implementation spec) is mis-captured → REFINE.
- **Open questions:** …
- **Classification:** `READY` / `REFINE` / `SPIKE` / `OUT` — `<reason / next action>`

### 2.7 Premise evaluation (C-43) — MANDATORY, one row per premise

> **Why this section exists.** Verifying the work against this document answers *"does the work match the spec?"* It never answers *"is what this spec ASSERTS ABOUT THE WORLD true?"* A batch can be fully compliant with a requirement whose premise is false. This section is the ARTIFACT that makes C-43 checkable — without it the control degrades to *"I thought about it"*.
>
> **What goes in it.** Every claim this batch RELIES ON: a symbol exists · a function has this signature · a file is this size · a line does this · "X is already shipped" · "this is mostly reuse" · any figure or decision **inherited from a prior batch**.
>
> **Tier each premise before evaluating it.** **Axiom** = a requirement already validated AND verified — law by default, but **re-openable** on an executed counterexample or a **logical invalidation (in practice almost always INCOMPLETENESS)**; a successful challenge is recorded in **§6.5** and **ENLARGES** the requirement, never deletes it. **Hypothesis** = anything this batch introduces, *including every decision, ADR and acceptance criterion inherited from a prior DESIGN batch — written down is not verified.* **Premise** = a claim about the world; executed against disk, never trusted.

| # | Premise, as a truth-apt proposition | Tier | Verdict | Executed evidence (command output / `file:line` — **NOT** a citation of another document) | Disposition |
|---|---|---|---|---|---|
| *(example — delete)* P-1 | `<"X exists at Y" / "Z is already reused" / "the count is N">` | axiom \| hypothesis \| premise | ✅ TRUE | `<the probe and its output>` | — |
| *(example — delete)* P-2 | | | ❌ FALSE | `<the counterexample>` | **BLOCKS** — `<correction + where it landed>` |
| *(example — delete)* P-3 | | | ❓ UNDECIDABLE | `<what is missing>` | **BLOCKS** — decided as `<…>` \| out of scope per `<…>` |

**Gate rule:** ❌ and ❓ both block. ❓ is dispositioned explicitly — decided, or declared out of scope **in writing**. A premise with no executed evidence is ❓, not ✅.

- **Premise evaluation:** `<the table's roll-up: N premise(s) · ✅ TRUE / ❌ FALSE / ❓ UNDECIDABLE — or: none — this batch relies on no premise>`
  *(**Mandatory on every requirements document**, and READ BY `V45` from flow rev69. The table above holds the rows; this field holds the answer a gate reads, and the two are the same act — the `Reverse census` precedent, where the template mints a fixed table and the keyed row is what a rule can see. **The cell must carry one of the three verdict tokens the table mints** — `✅`/`❌`/`❓` or their spelled forms `TRUE`/`FALSE`/`UNDECIDABLE` — **or the declared empty `none — <why no premise applies>`**. A cell reading `done`, `see the table` or `evaluated` answers nothing the gate rule turns on, and is scored as naming no verdict. Measured 2026-09-10: the heading above is present in **10 of 66** live contracts and this keyed field in **0 of 66**, which is what `C-43` — the most-cited control in the flow, called mandatory at every gate — had bought so far.)*

### 2.8 Fork preconditions (C-52) — MANDATORY, and the declared empty when the batch does not fork

> **Why this section exists.** A fork into parallel lanes is not made safe by intent; it is made safe by four conditions checked **before** forking. Missing one is not slower parallelism — it is **a collision with a delay**: both lanes advance happily and meet the conflict at integration, the most expensive moment. Measured 2026-09-10 over the batch record: **17 of 66** live contracts carry lane/fork language and none of them declares these four as a block.
>
> **The third condition is the one this document owes, and it is the reason the block lives HERE and not in a lane's packet.** The crossed reverse census — family B run per lane and shared *before* starting, because a symbol lane A touches may carry tests lane B also touches — is the one check that **structurally cannot be performed from inside a lane**. It is the TRUNK's act. `V43` reads the per-increment `Reverse census` in each lane's packet; nothing read the crossed one until this field, and the two are different objects with different authors.

| # | Condition (`C-52`) | Discharged? | The executed evidence |
|---|---|---|---|
| 1 | **Frozen contract** — no shared interface is touched inside a lane; one that must change returns to the trunk (trigger A3) | ✅ \| ❌ \| ❓ | `<the interface list and where it is frozen>` |
| 2 | **Disjoint FILE sets**, not just modules — two lanes may not edit the same file, not even different regions | ✅ \| ❌ \| ❓ | `<the per-lane file sets and the intersection test>` |
| 3 | **Crossed reverse census** — family B run per lane and **shared before starting**; the trunk's act, impossible from inside a lane | ✅ \| ❌ \| ❓ | `<the per-lane symbol sets, the cross-grep and its output>` |
| 4 | **One owner of the trunk** — requirements, traceability, backlog and spec are never written from a lane | ✅ \| ❌ \| ❓ | `<who owns the trunk>` |

- **Fork preconditions:** `<N lane(s) · the four conditions, each with its verdict — or: none — this batch runs one lane>`
  *(**Mandatory on every requirements document**, and READ BY `V46` from flow rev69. **`none — this batch runs one lane` is the legal empty and MUST be written** when there is no fork: an absence declared is a declaration, an absence omitted is a gap, and no rule can tell them apart otherwise. If one condition is ❌ or ❓, **you do not fork** — and each lane still needs its own worktree, because `C-40` requires capturing the RED counterfactual where no other session is reading, which is a precaution with one agent and a correctness condition with N.)*

---

## 3. High-level requirements (HLR)

> **FIELD SET — RULED 2026-08-28 ON MEASUREMENT, and the criterion is one sentence: of the six
> fields this ruling examined, only two change what gets TESTED. The other four describe or
> justify, and their home is the ledger.**
>
> **Three are LIVE and mandatory**, because each one obliges an arm that would otherwise not
> exist:
> - **`Boundary catalog`** — GENERATIVE, not descriptive: it enumerates the input classes an
>   arm is then obliged to exercise. **Scope: every requirement whose `Validation` is `test`
>   or `analysis`** — HLR or LLR alike. The scope is tied to that field rather than to the
>   requirement's level, because the catalog exists to generate cases for an arm, and a
>   requirement validated by `inspection` has no arm to generate them for. Stated here rather
>   than left implicit.
> - **`Acceptance test(s)`** — an id, so acceptance can be referenced and traced like anything
>   else. **`owed at <increment>` is the legal empty and MUST be written** when the arm does
>   not exist yet; an omitted field is a question nobody asked.
> - **`Negative control`** — its own named slot, never a clause inside the threshold. *A test
>   that cannot fail is vacuous* is this flow's central doctrine, and a doctrine carried by
>   convention is carried by nobody: measured on batch-88, the negative side was inline in 9
>   of 10 thresholds, so exactly one requirement had no RED side **and nothing said so**.
>
> **AND FROM flow rev63 EACH OF THE THREE IS READ BY A RULE** — `V33` (`Negative
> control`), `V34` (`Boundary catalog`), `V35` (`Acceptance test(s)`) — because a mandate
> nothing reads is a paragraph. Each value is now a KEYED slot: leave it holding the
> template's `<…>` and the rule says so by name. `V33`/`V34` are scoped by the
> `Validation` field, `V35` to HLR blocks, which is exactly where this ruling put them.
> (Origin: `R-89-8` and the batch-88 measurement above — see dev-flow-lessons, `C-58`,
> *a mandate nothing reads is a paragraph*.)
>
> **Three are RETIRED, and the reasons are recorded here rather than in a deleted line:**
> - **`Acceptance criteria (informative, complementary)`** — 16 instances and 10,876 chars in
>   batch-88, **5.6% of the record**, and *self-declared informative*. It changes nothing that
>   is tested. Where an observable condition is load-bearing it belongs in the `Numeric pass
>   threshold`; where it is context it belongs in the ledger.
> - **`Deliverable + observation`** — covered by `Validation` plus `Executed verification`,
>   which already name what runs and what it produces. Two fields describing one obligation
>   drift apart, and the flow has paid for that shape before.
> - **The dual-traceability TABLES** *(they sat in a §5.2 whose heading was itself deleted at
>   flow rev69, the body having been a retirement notice since 2026-08-28)* — covered by the
>   per-requirement `Traceability`
>   field, which was populated in 10 of 10 requirements measured. A table transcribing a field
>   that is already mandatory is a second copy of one truth; `V10`, `V21` and the Atlas derive
>   the chains from the fields themselves.

> Each HLR is an EARS statement. Allowed patterns:
>
> - **Ubiquitous:** `The <system> shall <response>.`
> - **Event-driven:** `When <trigger>, the <system> shall <response>.`
> - **State-driven:** `While <state>, the <system> shall <response>.`
> - **Optional feature:** `Where <feature is included>, the <system> shall <response>.`
> - **Unwanted behavior:** `If <unwanted condition>, then the <system> shall <response>.`
> - **Complex:** combinations of the above.

### HLR-001 — `<Short title>`
- **Traceability:** US-001
- **Ledger:** none *(or `LED-<batch id>.<n>, …` — every entry in `01-requirements-ledger.md` that amended this requirement, written in §7's recommended form. Mandatory field; `none` is the declared empty.)*
- **Statement:** When `<trigger>`, the system shall `<response>`. *(Current state only. If you are about to write "because measured …", stop: the obligation belongs here, the measurement belongs in a ledger entry.)*
- **Rationale (informative):** *(why this requirement exists — `should` may technically be used here informally, but avoid it to prevent confusion.)*
- **Validation:** `test` | `demo` | `inspection` | `analysis`
- **Executed verification:** *(required if `test`/`analysis`. e.g. `npm run typecheck`, `vitest run TC-001`, `worst-case gain-staging sum analysis`.)*
- **Numeric pass threshold:** *(required if `test`/`analysis`. e.g. `0 errors`, `peak post-limiter ≤ −6 dBFS`.)*
- **Priority:** high | medium | low
- **Acceptance (black-box) — the user-verified outcome (the WHAT):**
  - **Observable outcome:** *(what the user observes)*
  - **Shipped surface:** *(the handler / screen / CLI that produces it)*
  - **Acceptance test(s):** `<AT-NNN, or the words `owed at` and the increment that will mint it>`
    *(**Mandatory on every HLR**, and READ BY `V35`. `owed at <the increment>` is the legal empty and MUST be written when the arm does not exist yet; an omitted field is a question nobody asked. Provisional-until-Phase-3 per V-5; drives the surface, asserts the outcome, references NO internal symbol; FAILS if the deliverable is silently absent.)* ⚠ **`V2` resolves this id against the node corpus `artifact_homes.tests` DECLARES in `state.json`** (rev58) — `repo:tests/` is what `/dev-flow-init` seeds, `tests/` is what an undeclared home means, and **the declared corpus REPLACES `tests/` rather than extending it**. So a batch whose acceptance surface lives elsewhere — the flow's own `--selftest`, for one — names that home instead of duplicating arms into `tests/`. **Three ways a declaration fails to resolve, and each is a SKIP carrying the words *this is not a pass*, never a silent green:** a `repo:` home that is not on disk, a `vault:` home (no mechanical check can read one, by design), and a value that is not `repo:<path>` at all. *(This warning read `<project>/tests/ and NOTHING ELSE` from rev6 to rev68 — false since rev58, and its cost was specific: it invited the author either to declare a valid acceptance unreachable, or to copy tests into `tests/` to satisfy a constraint that no longer existed.)*
  - **Boundary catalog (QC-3):** `<☐ empty ☐ boundary ☐ invalid ☐ error — tick each class that gets an AT/TC, or: none — and the reason no input class applies>`
    *(**Mandatory wherever `Validation` is `test`/`analysis`** — HLR or LLR alike — authored at Phase 1, not rescued in review, and READ BY `V34`. Mark a class N/A only with a one-line reason; a class left blank without a reason is a Phase-2 finding. **It is GENERATIVE: each ticked class is an arm somebody owes.** **When there is nothing to declare, write `none — <the reason no input class applies>`**: an absence declared is a declaration, an absence omitted is a gap, and no rule can tell them apart otherwise.)*
  - **Negative control:** `<the executed input on which this verification GOES RED, or: none — and why it has no executed RED side>`
    *(**Mandatory wherever `Validation` is `test`/`analysis`**, and READ BY `V33`. Not "the assertion could fail" — the observed failing case. A verification with no demonstrated RED side is vacuous, and this field is where that is proven rather than assumed. **When there is nothing to declare, write `none — <the reason>`** — which DECLARES the gap and does not excuse it: Phase 2 reads a declared `none` here as a finding, and the point of writing it is that the finding becomes visible instead of silent.)*

### HLR-002 — `<Short title>`

> **The second example is the first with its values blanked, and that is a RULE, not a
> coincidence.** Until flow rev69 it collapsed the whole acceptance block into one line and the
> three keyed slots below were gone, so an author who copied THIS block produced a document
> `V33`, `V34` and `V35` each reported against. One canonical form per level: every example of a
> level instantiates the same conditional field set, and `REQ TEMPLATE-example-form` is the arm
> that reddens if one of them stops.

- **Traceability:** US-NNN
- **Ledger:** none
- **Statement:** While `<state>`, the system shall `<response>`.
- **Rationale (informative):**
- **Validation:** `test` | `demo` | `inspection` | `analysis`
- **Executed verification:**
- **Numeric pass threshold:**
- **Priority:**
- **Acceptance (black-box) — the user-verified outcome (the WHAT):**
  - **Observable outcome:**
  - **Shipped surface:**
  - **Acceptance test(s):** `<AT-NNN, or the words `owed at` and the increment that will mint it>`
  - **Boundary catalog (QC-3):** `<☐ empty ☐ boundary ☐ invalid ☐ error — tick each class that gets an AT/TC, or: none — and the reason no input class applies>`
  - **Negative control:** `<the executed input on which this verification GOES RED, or: none — and why it has no executed RED side>`

---

## 4. Low-level requirements (LLR)

> Each LLR decomposes an HLR into a verifiable property at the implementation level.
> Same EARS regime. ID format: `LLR-<HLR>.<M>`.

### LLR-001.1 — `<Short title>`
- **Traceability:** HLR-001
- **Ledger:** none
- **Statement:** The `<component>` shall `<verifiable technical response>`.
- **Validation:** `test (unit)` | `test (integration)` | `test (e2e)` | `inspection` | `analysis`
- **Executed verification:** *(required if `test`/`analysis`. e.g. `vitest run src/lib/audio/masterBus.test.ts -t TC-001`; `gain-sum analysis vs the compressor threshold`.)*
- **Numeric pass threshold:** *(required if `test`/`analysis`. e.g. `assert exit code 0`; `peak ≤ −6 dBFS`; `RMS error < 0.01`.)*
- **Negative control:** `<the executed input on which this verification goes RED, or: none — and why it has no executed RED side>`
  *(mandatory wherever `Validation` is `test`/`analysis`; read by `V33`. See HLR-001 above for the full wording and for what a declared `none` costs.)*
- **Boundary catalog:** `<☐ empty ☐ boundary ☐ invalid ☐ error — tick each class that gets an AT/TC, or: none — and the reason no input class applies>`
  *(mandatory wherever `Validation` is `test`/`analysis`; read by `V34`. Each ticked class is an arm somebody owes; a class marked N/A carries its one-line reason.)*
*(`Acceptance criteria (informative, complementary)` was RETIRED 2026-08-28 — self-declared informative, 5.6% of batch-88's record, and it changed nothing that was tested. A load-bearing observable condition belongs in the threshold; context belongs in the ledger.)*

### LLR-001.2 — `<Short title>`
- **Traceability:** HLR-001
- **Ledger:** none
- **Statement:**
- **Validation:** `test (unit)` | `test (integration)` | `test (e2e)` | `inspection` | `analysis`
- **Executed verification:**
- **Numeric pass threshold:**
- **Negative control:** `<the executed input on which this verification goes RED, or: none — and why it has no executed RED side>`
- **Boundary catalog:** `<☐ empty ☐ boundary ☐ invalid ☐ error — tick each class that gets an AT/TC, or: none — and the reason no input class applies>`
*(Until flow rev69 this block omitted both of the above and re-introduced `- **Acceptance criteria:**`, the field the block immediately above declares RETIRED in its own parenthetical — the retired name outnumbering two of the live ones inside the file that retired it.)*

---

## 5. Validation strategy

### 5.1 Methods

> **Two layers** (per the Two-layer validation rule). Every batch declares BOTH:
> - **Layer A — white-box / functional (`TC-NNN`):** validates the HLR/LLR mechanism (the HOW). Methods: `test`, `inspection`, `analysis`.
> - **Layer B — black-box / behavioral acceptance (`AT-NNN`):** validates the user story's outcome through the shipped surface (the WHAT). Method: `acceptance`.

- **Test (Layer A · white-box):** automated execution (unit / integration / e2e). Default for LLR. **Every `test` LLR must name the exact executed verification and the numeric pass threshold — otherwise it is not executable.**
- **Inspection (Layer A · white-box):** static review of code or document. Useful for structural requirements. Name the file / commit / section + the observable condition.
- **Analysis (Layer A · white-box):** formal or quantitative reasoning (performance, complexity, security). **Every `analysis` LLR must name the executed calculation (with input values) and the numeric pass threshold — otherwise it is not executable.**
- **Acceptance (Layer B · black-box):** exercise the system as the user — the UI framework the UI test driver e2e (`App.run_test()`), CLI invocation, or artifact-on-disk inspection — and assert the story's outcome through the SHIPPED surface with representative + boundary + negative evidence + the actual deliverable observed. Marked `AT-NNN` (distinct from white-box `TC-NNN`). This is the `test (driver)` form, NOT `demo`. Required for every user story; an output-producing story's `AT` must FAIL if the output is silently absent.
- **Demo (auxiliary · perceptual):** observed execution of behavior; qualitative UX check. Describe the observable procedure + the named qualitative criterion. NOT a substitute for an automated `AT`.

> **Capture the executed verification + numeric pass threshold at DRAFT time, not at the phase-2 gate** — their absence on `test`/`analysis` requirements is the recurring root cause of forced phase-1 iteration. (Origin: batches 02-03 — see dev-flow-lessons)

### 5.2 Batch acceptance criteria
- *(e.g.: 100% of LLRs covered by at least one TC with pass result.)*
- *(e.g.: 0 blocker fails in validation.)*
- *(e.g.: test coverage >= X% where applicable.)*
- *(e.g.: no requirement without an assigned validation method.)*
- *(e.g.: every user story has ≥1 passing `AT-NNN` black-box acceptance test observing its outcome through the shipped surface — with boundary + negative evidence.)*

---

## 6. Appendices (optional)

### 6.1 Extended glossary
### 6.2 Relevant design decisions
### 6.3 Open risks
### 6.4 Phase-1 reconciliation log
**Moved to the ledger (rev48).** Reconciliation events are ledger entries, one per changed decision, carrying the same four columns as before: *what changed · parent HLR re-read? · body edit landed? · the `§3`/`§4` line that now reflects it*. The **body-first ordering still binds** — write the `§3`/`§4` edit FIRST, then the ledger entry that points at it — and the two phase-2 blockers are unchanged.

### 6.5 Requirement amendments (Before / After · Deleted / New)
**Moved to the ledger (rev48).** An amendment is an APPEND, never an edit-in-place of this document's history: the live requirement is rewritten to its new current state, and a ledger entry records the Before text, the Deleted/New tokens, the parent-HLR re-read result and the re-derived `TC`/`AT`. Nothing struck, nothing narrated here.

---

## 7. The ledger — authored as a SEPARATE FILE

> **This section is a scaffold for `01-requirements-ledger.md`, not a section of this document.** Copy it into that file at batch open, beside the live contract. The two are created in the same commit as `state.json`, for the reason the flow already gives about `01-requirements.md`: a declared batch with no copy of its own is judged on whichever historical document the validator's walk reaches first.
>
> **Append only. Never edit an entry, never delete one, never renumber one.** An entry that turns out wrong is superseded by a new entry that names it. This is the property `V26`'s pairing exists to protect, and it is the reason the split is safe rather than merely tidy.

**COPY THE FIRST FENCE, AND ONLY THE FIRST.** It is the whole seed: a ledger with a header, the append-only law, and **no entries**. The second fence is the shape an entry takes when there is one to write; it is documentation and is never copied at batch open.

**Why the two are separate, measured rather than argued.** Until rev62 this was ONE fence carrying two worked examples, and seeding it seeded them: a project scaffolded from this template BLOCKed its own gate twice on the day it was created — `V26` on *"1 ledger entry/entries name no requirement — LED-2026"* and `V1` on the live `<YYYY-MM-DD>` placeholder. **An empty ledger is not an unfinished one.** `V26` reads zero entries against zero pointers and passes on both directions of the pairing, which is the correct reading of a batch that has amended nothing yet.

> **ONE ID GRAMMAR, AND THE RECOMMENDED FORM IS `LED-<batch id>.<n>` — flow rev69 (`T01`).** Until rev68 `_LEAN_ENTRY_HEAD` and `_LEAN_LED_ID` spelled the id `LED-\w+(?:\.\w+)*`, and `\w` does not admit a hyphen: `LED-2026-09-07-batch-01.1` and `LED-2026-09-07-batch-01.2` were **both read as `LED-2026`**, and a body reference to the first yielded `LED-2026` too. **The failure was not a refusal, it was an ACCEPTANCE OF THE WRONG REFERENCE** — a contract pointing at entry 1 beside a ledger holding only entry 2 presented `V26` with one matching pair in both directions, and it declared the pairing complete. Both readers now spell the id the way `_LEAN_REQ_HEAD` and `_ATLAS_ID_REQ` already spelled requirement ids — `LED-[\w.]+(?:-[\w.]+)*\b` — so the two sides cannot disagree about where an id ends. **`LED-<batch id>.<n>` is the recommended form** *(the batch id is already unique and already the directory's name, so an entry id carries its own provenance and two batches' ledgers can never collide when a record is read out of context)*; **`LED-<N>.<n>`, the historical short form, stays legal and stays discriminating** — the grammar admits both, and the regression that proves it pairs two ids differing only AFTER a hyphen.

```markdown
# Requirements ledger — <PROJECT> — Batch <BATCH_ID>

> Append-only. Entries are added in chronological order and never rewritten. The live
> contract is `01-requirements.md`; this file records how it came to say what it says.
> Every entry names the requirement it amends; every requirement names its entries. `V26`
> compares the two sets of pairs both ways.

_No entries yet. The first amendment to the live contract writes the first one, in the
shape below, and nothing above this line is ever edited._
```

**The shape of an entry — NOT part of the seed.** Add one only when there is an amendment to record. The heading is `LED-` + this batch's id + `.` + the next number; `**Requirement:**` names a requirement that **exists as a heading in the live contract**, because an entry naming nobody pairs with nothing and `V26` BLOCKs on it.

```markdown
### LED-2026-09-07-batch-01.1 — the threshold moved from 5 to 3
- **Requirement:** HLR-014 — must exist as a heading in the live contract
- **Date:** 2026-09-07
- **What changed:** the live contract said "at least 5"; it now says "at least 3"
- **Why:** the measurement, the counterexample, the operator ruling — the reason that used
  to sit inside the normative sentence
- **Evidence:** command output, `file:line`, or the probe that decided it
```
