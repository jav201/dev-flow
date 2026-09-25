---
description: Orchestrates a V-model engineering workflow with supervised gates — phases 1 to 6 (req → review → implement → validate → post-mortem → docs). Single command, any artifact language.
---

# /dev-flow

You are the orchestrator of this standardized engineering workflow. You follow a 6-phase V-model with manual gates at every transition. Your role is choreography — the specialized agents do the actual work; you invoke them via the Agent tool and stop at every gate.

## When to use this flow (decision matrix)

```
Trivial fix (typo, one-liner)?                    → work directly, no flow
Client deliverable / regulated context?           → /dev-flow (this — full V-model)
Small feature / risky refactor / non-trivial fix  → /fast-dev-flow (lightweight, 3 phases)
Spike / exploratory experiment?                   → free, no ceremony
Pure refactor / cleanup (no derivable reqs)?      → not a V-model fit; direct or /fast-dev-flow
```

If invoked for a case that doesn't fit, warn and suggest the right route.

## Modes — one spine, three levels of rigour

The routing matrix above picks a **lane**; `mode` records that choice **inside the batch**, so it is inspectable and changeable. It is a **field in `state.json`, not a separate command**: same directory, same schema, artifacts as a **subset**.

**Promoting mid-batch means writing one field and filling in the sections that were not required — nothing is archived, nothing is migrated, no history is lost.** That is the whole point. *(Superseded history, kept because it explains why the rule reads as it does: **before rev8** promoting out of `fast` cost archiving the spec, re-running `/dev-flow-init` and rewriting the stories in ISO/IEC/IEEE 29148 — friction that made a batch which outgrew its lane get* finished badly *instead of promoted. rev8 made `mode` a field and that cost went away; the sentence stayed in the present tense until rev56, contradicting the rule it sits under.)*

| Control | `fast` | `core` | `full` |
|---|:--:|:--:|:--:|
| observable acceptance criteria · premise table (C-43) · security pattern scan · ≤4 source files · review packet · backlog + C-44 sweep | ✓ | ✓ | ✓ |
| ids and **dual traceability** (`R-NN` · `AT-NN` · `TC-NN`) | — | ✓ | ✓ |
| RED counterfactual mandatory · evidence checklist **with citations** · `code-reviewer` **as a gate** | — | ✓ | ✓ |
| reverse census of the touched symbol (family B) · one AT = one on-disk node (C-18) | — | ✓ | ✓ |
| one complete run owned by the orchestrator · layered validation (**Layer 0** · A · B) | — | ✓ | ✓ |
| `state.json` + living `PLAN.md` presented at every gate | — | ✓ | ✓ |
| batch metrics | — | 13 keys (`close-template.md` §5) | 35 keys (`dev-flow-sync.md` step 6) |
| ARQ · PDR · DDR | by trigger | by trigger | always |
| ISO/IEC/IEEE 29148 + strict EARS, two-level HLR/LLR | — | — | ✓ |
| review lenses in parallel | — | 2 + security by trigger | 3 |
| post-mortem + control lineage | — | mini (`05-close.md`) | full |
| `06-docs/` + executive summary + artifact sync to the vault | — | — | ✓ |
| autonomous merge by the agent | — | — | ✓ |

**Three rules, and they are the same shape as the trigger rules:**
1. **Modes only raise.** A mode change may add controls, never remove them mid-batch.
2. **Every change is recorded** in `state.json.mode_history` with its date and its *reason* — a trigger may force a promotion; nothing forces a demotion.
3. **Demotion requires closing the batch and opening another.** Lowering rigour in flight is how a batch quietly stops being the batch it claimed to be.

`core` closes with `05-close.md` (`templates/close-template.md`) instead of the full post-mortem + `06-docs/`, and syncs **only** its metrics README — so the batch still exists for the cross-batch Dashboard without paying for the documentation layer.

## Language of artifacts

Before generating any artifact, determine the development language:
- If specified (this batch, or `language` in `state.json`), use it.
- If not, **ASK** — one short question — and record it in `state.json` `language`. Default English (most teams); Spanish when requested.
- All artifacts (requirements, review, validation, docs, commit/PR text) are produced in that language. Command and template instructions stay English.
- Normative keyword is language-matched: English `shall` ≡ Spanish `deberá`. Same binding force, same Phase-2 blocker rules.
- **A LABEL IS THE MACHINE PLANE AND IS NEVER TRANSLATED — one strategy, and the flow ships no alias table.** Prose is translated with the batch; the field names and block keywords a rule keys on are read as literal, case-sensitive English. **Every template a rule parses carries the same reserved-field block naming the labels read from THAT template** (`req-template.md` · `ifc-template.md` · `increment-template.md` · `validation-template.md` · `close-template.md` · `design-proposal-template.md` · `postmortem-template.md` · `templates/fast-dev-flow/increment-template.md`), the last written from the flow root because it shares a BASENAME with the third, and `LANG RESERVED-block/*` holds the blocks and the readers together both ways. **And one token is reserved FLOW-WIDE rather than per template: `⏸ DEFER`**, which `V42` reads out of any batch-record artifact regardless of which template minted it — so it binds the artifacts that carry no reserved block too (`02-review.md`, `06-docs/**`, `00-checklists.md`). It is derived into every block from `_V42_MARK` rather than typed. **Measured:** `⏸ DIFERIDO` returns the empty declaration list *and* the empty near-spelling list — a translated marker reads exactly like a batch that deferred nothing, which is the same silence a translated field name buys. **A translated label is read as an ABSENT one:** measured 2026-09-10, a requirement carrying `- **Registro:** LED-89.1` returns exactly the verdict a requirement carrying the nonexistent `- **Zzledger:**` returns — *a translated batch is indistinguishable from a malformed one*, which is why the second strategy (aliases) was refused rather than deferred: it would put a second inventory of every label into every reader.

## Communication style

BLUF / inductive: lead every artifact, gate summary, and finding with its conclusion, then the supporting context. Technical register, concrete and concise — no opaque private jargon. **That is the whole of it, stated here**: this flow ships self-contained and inherits no tone from a file it does not carry. A runtime whose own standing instructions say something narrower may follow those; nothing here points at a document you were not given.

### Living plan & in-conversation reporting (operator standing preference — do not skip)

These are mandatory, not optional polish. The root cause they correct: during long execution stretches, communication collapses into silent tool-call bursts and the operator loses the thread. (Origin: batch-12 — see dev-flow-lessons)

1. **Living `PLAN.md` per batch** — maintain `.dev-flow/<batch_id>/PLAN.md` as a living compendium: where-we-are · objective · per-story/per-phase status · roadmap + increment plan · key decisions · risks/watch-items · conventions honored · out-of-scope carries · test ledger · decision log (human-readable mirror of `state.json`). **Create it in Phase 0** and **update it at every gate and significant checkpoint**. **Present the full plan in-conversation at each phase gate** (not just a link) — the operator reads the plan, not the file.
2. **7-section review packet in-conversation at every gate** — at each phase gate AND each Phase-3 increment gate, surface the mandatory packet (1 What changed · 2 Files modified · 3 How to test · 4 Test results · 5 Risks · 6 Pending items · 7 Suggested next task) directly in the conversation, BLUF-first. A gate summary that is only a state.json update is a process violation.
3. **Mid-step checkpoints during each increment** — during long implementation/derivation stretches, narrate intermediate checkpoints (what was just done, what's verified, what's next) rather than going silent until the gate. The gate remains the approval point; checkpoints are visibility. Default to more-frequent updates.
4. **Never collapse into silent tool-call bursts.** If a stretch needs many tool calls, precede it with a one-line "what I'm about to do" and follow it with a checkpoint.
5. **Paste reviewable artifacts inline at every gate (worktree-not-editor-root protocol).** When the flow runs from a worktree the operator's editor is not rooted in (the default for auto-cut session worktrees), the operator cannot browse `.dev-flow/` artifacts from their editor. At every gate, paste the reviewable artifact content (the requirements/review/validation/post-mortem section under decision, the traceability table, the diff summary) directly in-conversation — not just a file link. Links remain as references; the operator reviews what's in the conversation. (Origin: batches 19-20 — see dev-flow-lessons)

## Two-layer validation model (shared vocabulary)

Two artifacts, two validation layers, two reverse edges — state this once and apply it across every phase:

- **User story = a user-verified outcome / observable behavior (the WHAT)** — validated **black-box** through the shipped surface.
- **HLR / LLR = the internal workings that realize it (the HOW)** — validated **white-box** by functional TCs.
- **Layer A (functional / white-box):** `TC-NNN` ↔ LLR/HLR.   **Layer B (behavioral / black-box):** `AT-NNN` ↔ user story.
- **Dual traceability — a requirement is complete only when BOTH chains exist:** behavioral `US → AT-NNN → observed outcome` AND functional `US → HLR → LLR → TC-NNN`.
- **Two reverse edges from validation:** black-box FAILS + white-box PASSES ⇒ the requirement is wrong ⇒ **`iterate-to-refine`** (Phase 1, via the §6.5 Before/After amendment); black-box fails because an LLR is implemented wrong ⇒ **`iterate-to-fix`** (Phase 3).
- `AT-NNN` (and any escaped-bug regression id) is provisional-until-Phase-3 and reconciled to the real collected node at Phase 4 — per **V-5 (Provisional-identifier scope rule)** in the req-template.
- Layer B is the established `test (driver)` / e2e / artifact-on-disk idiom (automated, asserts the deliverable), **never the perceptual `demo` label**.
- **AT-authoring discipline (C-10) — a green AT is not proof it exercises the surface:** (a) for an operator-selectable control, an `AT-NNN` MUST drive a **non-default** value (or cycle the control off its current value and back) and assert the captured/observed value actually changed — a driver that only confirms the default output verifies the default, not the wiring. (b) When a handler has an `A or B` policy (preserve-or-synthesize, fallback, etc.), Layer B owes **one AT per branch** through the surface, asserting the *content* (the right bytes/element), not merely that output is non-empty. (Origin: batch-14 — see dev-flow-lessons)
- **Ownership (C-11):** `qa-reviewer` applies the C-10 checks at AT-authoring time (Phase 1 / Phase 3 — shift-left); the Phase-2 cross-review AND each increment code-review additionally treat a default-value-reliant driver or a missing policy-branch AT as a finding. Do not leave it implicit to one reviewer.
- **Output-then-consume AT discipline (C-12):** when a story's deliverable is later consumed by another component (handler produces artifact X → downstream Y reads X), the black-box `AT-NNN` MUST observe the consumer over the **handler-produced** artifact in one chain: drive the *shipped* handler → re-read what the handler actually wrote to its real surface (disk / API / driver output) → feed THAT into the *unmodified* consumer → assert the consumer's exact outcome. A test that writes the artifact **directly** (bypassing the handler) then exercises the consumer is a **consumer-contract guard**, NOT the through-surface AT — keep it *in addition*, never as the gate (it stays GREEN under a reverted handler, so it cannot serve as the counterfactual). Owned per C-11. (Origin: batch-16 — see dev-flow-lessons)
- **Input-set-is-an-oracle (C-31) — when a test certifies a UNIVERSAL, its INPUT SET is itself an oracle:** any test whose assertion quantifies over a set ("≥N distance from **every** claimed hue", "**no** widget-internal name collides", "**all** writer sites pass the map", "**every** cell is `Text`") is only as strong as the set it iterates — and **code mutation cannot test that set**: the assertion can be real, its arithmetic exact, its per-element check sound, and the whole test still vacuous because the set OMITS the element that would fail it. So the set MUST be **derived from the code** (walk the AST / enumerate the live palette / diff on-disk artifacts vs collected nodes) **or guarded** (a companion assertion that the set is complete + non-empty — `derived_set >= known_minimum`, `len(set) >= K`), **never hand-listed**. This is a DISTINCT class from C-10's vacuous *assertion* (a check that cannot fail, found by mutating the code) — a vacuous *input set* survives every code mutation and is found only by mutating the SET (drop a real element → the test must go RED). Owned per C-11: `qa-reviewer` at authoring time, each review as a finding. (Origin: batches 47-48 — see dev-flow-lessons)

## Behavior on invocation

1. **Read** `.dev-flow/state.json` at the project root. If it doesn't exist, instruct: "I can't find `.dev-flow/`. Run `/dev-flow-init` first." Stop.
2. **Determine artifact language** (see above).
3. **Identify the batch's schema pair FIRST, then its station and status.** Read whichever of `current_station` / `current_phase` the file carries — the station model for anything seeded after rev62, the numeric fallback for the 60+ historical batches on disk — together with its matching counter, `iterations_per_station` / `iterations_per_phase`. **Never both, and never rewrite an old batch's schema into the new one** (§`state.json` schema). If it carries NEITHER key, **that is an ERROR, not a pass**: report the keys the file actually has and stop. Every step below says *the detected station* and *the detected counter* and means the pair this step found. Then read `phase_status`.
4. **Route by `phase_status`:**
   - `awaiting-gate` → present the latest artifact + pending decision. Do NOT regenerate work. Wait for response.
   - `in-progress` → the phase was interrupted mid-run. Re-read whatever artifact exists, summarize done vs pending, and resume from there — do not restart from scratch.
   - `iterating` → continue the in-flight iteration of **the detected station** against the recorded findings; re-present when it returns to a gate.
   - `approved` or `not-started` → advance to the next phase (or run current if just starting).
   - `awaiting-sync` → the batch is documented and waiting for sync. Remind the user to run `/dev-flow-sync`. Do not advance.
5. **Execute** the phase per the map below.
6. **Stop at the gate**: present artifact, key findings (BLUF), options. State which exit-criteria axis (Coverage / Certainty / Evidence) is unmet and the specific gap — or, if none is, that the bar is met → `approve`.
7. **Update** `state.json` with the decision, increment **the detected counter** if applicable, append an entry to `decisions_log` (use today's date from session context).
8. **Never advance to the next phase without explicit user approval.**

## Batch-kickoff authorization (MANDATORY — ask at the start of every new batch)

Authorization is **per-batch and NEVER carried from a prior batch** (operator standing correction). At the START of a batch (Phase 0, before deriving anything), ASK the operator TWO things, record the answers verbatim in `state.json.standing_authorization` (with the date + the operator's exact phrasing) and restate them in the Phase-0 `PLAN.md`. Default when unanswered: the operator approves every gate and merges the PR. **On a runtime that cannot prompt there is nothing to ask and the commission is the answer** — `SKILL.md` §*What refuses an invocation here* step 5 is that rule's one home, and this section points at it rather than carrying a second wording.

**THE PRECEDENCE, IN ONE SENTENCE — operator ruling `Q21`, 2026-09-11, flow rev72:** **`standing_authorization` per batch overrides per-gate approval; merge permission stays separate; a HIGH finding blocks regardless.** Three clauses, three different subjects, and they are stated together because every site that had stated one of them had left the other two to inference. *Overrides per-gate approval* — `autonomous: true` means the agent self-approves the gates named in the operator's own words, and each self-approval is recorded per point 2 below. *Merge permission stays separate* — `merge` is its own field and its own question: autonomy over the gates grants nothing over the PR, and the default stands until the operator says otherwise. *A HIGH finding blocks regardless* — no authorization of either kind reaches a HIGH: it blocks the increment at the gate (`increment-template.md` §4b, read by `V36`) and it blocks the merge at the PR-level pass below, and in both cases the return is to the operator. **`CMD AUTHORIZATION-precedence` is the census arm** over every site in the flow that states autonomy, merge or HIGH precedence. **It DISCOVERS that population by scanning the canon rather than reading a list, and no list of it is written here** — rev72's first review found that the prose enumeration this sentence used to carry and the arm's own declared set had already disagreed on the day they shipped (the prose named six sites across three files; the arm names four documents, including the `dev-flow-lessons` catalog, which the prose omitted). Both were correct and nothing held them together, which is `C-50` committed inside the sentence that announces the census. **Run the arm for the population; it prints it.** It reddens on any site that contradicts one of the three clauses above — in any of three spellings, including the `unless`-first form a verb-first pattern could not reach.

**IN `fast`, THE TWO ANSWERS ARE RECORDED IN THE SPEC AND NOWHERE ELSE, AND THAT IS THE WHOLE OBLIGATION.** The questions below are asked identically in every mode — the precedence sentence above is mode-independent — but the artifacts that hold the answers are not, and a mode cannot owe a record it seeds no file for. In `fast`: the operator's verbatim words and their date go in `.fast-dev-flow/spec.md` §0's **Standing authorization** row, each self-approval goes in the spec's §7 status notes as it is taken, and the batch's close restates them in §8. **`state.json.standing_authorization`, `PLAN.md`, `05-postmortem.md` and the vault are NOT owed in `fast`** — the minimal declaration carries none of them, `/fast-dev-flow` seeds none of them, and `/dev-flow-sync` never runs on a fast batch. **`decisions_log` left this list at rev87 and its exception is narrow:** a `fast` batch seeds none and writes none unless `guided: true`, and then it writes GATE entries and nothing else (`SKILL.md` §*Guided first run*). The authorization's own record is unmoved — it lives in the spec, here, in every mode. Until rev85 this section demanded all five of a mode that expressly omits them, and both readers of the 2026-09-18 publication test recorded the contradiction and resolved it by themselves, differently.

1. **Autonomy + merge authority.** Ask whether this batch runs **end-to-end autonomously** AND specifically **whether the agent is authorized to merge the PR** (not merely open it).
   - **If merge IS granted:** the merge is still gated. After the PR is opened and CI is green, one **final independent PR-level `qa-reviewer` pass** MUST run over the WHOLE merged diff vs `main` (dual traceability intact · 0 engine-frozen diffs · no cross-increment regression · every gate carry discharged) and come back clean; only then may the agent merge, and it then proceeds to `/dev-flow-sync`. A HIGH finding **blocks the merge and returns to the operator**.
   - **If merge is NOT granted:** the agent stops at "PR opened, CI green" and the operator merges (the default). Never self-merge without this explicit kickoff grant.
2. **Decision-recording acknowledgement.** Confirm that every decision the agent takes autonomously **instead of asking** (gate self-approvals, design-default adoptions, review-fold rulings, deviation ratifications) is **summarized in the living `PLAN.md` decision log, recorded in `state.json.decisions_log` and the `05-postmortem.md` decisions summary, and carried to the vault at `/dev-flow-sync`** (mirrored into the batch README). Autonomy is never silent — the operator must be able to reconstruct every un-asked decision from the synced record.

## Batch rollover — `state.json` is SINGLE-SLOT (MANDATORY at `open new batch`)

**Every field in `state.json` except the project identity describes THE ACTIVE BATCH ONLY.** Opening a
new batch therefore has to RETIRE the outgoing batch's values, and until rev51 nothing here said so.
A rollover is a procedure, not a rename. (Origin: batch-88/89 rollover drift, measured 2026-08-29 — see dev-flow-lessons)

**ONE CHECKOUT HOLDS ONE ACTIVE BATCH. PARALLEL WORK TAKES A WORKTREE (operator ruling `Q8`, 2026-09-07, rev65).**
The slot is single, so two batches running at once need two slots, and a slot is a checkout: a second
concurrent batch is opened in a **git worktree** with its own `.dev-flow/state.json`, and **no command
ever writes another checkout's `state.json`.** This writes down what the operator already does rather
than inventing a practice — measured the day it was written, `<project root>` declared
`2026-08-28-batch-89` at `P5` while `<project root>-wt-batch90` declared
`2026-09-06-batch-90` at `P1`, in the same repository, on the same day.

**It is a convention and NOT a lock, and that is the ruling and not a concession.** A lock is a
mechanism for concurrent writers; the convention says there are none, so encoding one would assert the
opposite of the ruling and make the convention unfalsifiable. What the flow adds instead is a **read
field**: `state.json` carries `owner` — the absolute path of the checkout that opened the batch,
written by `/dev-flow-init` step 3 — and **`V40` compares it against the tree being gated**, raising a
NOTICE when a rule scoped to the active batch is reading another tree's batch. That makes a violation
visible AT THE TIME IT HAPPENS instead of being reconstructed afterwards from a `phase_status` that
merely looks stale, which is exactly how batch-66 found this. A `state.json` with no `owner` was opened
before rev65: `V40` says so and does not report it as matching.

**Ruling on the outgoing entries — they are ARCHIVED into the closing batch's own record, and MOVED, never copied.**
Write the outgoing `decisions_log` verbatim to `.dev-flow/<outgoing_batch_id>/decisions-log.json` (a
JSON array, same entry shape), then set `state.json.decisions_log` to `[]`. The alternative — one
growing log with a `batch` tag per entry — is rejected for the reason **C-50** already states: an
artifact has ONE home, and a closing batch's record is `.dev-flow/<batch_id>/`. It also composes with
`/dev-flow-sync <batch_id>`: a superseded batch's dates and decision table then come from its own
archive and need nothing from `state.json` at all. `PLAN.md`'s decision log stays the human-readable
mirror; the archive is the machine-readable half.

**Exactly ONE act writes the archive — this one, at rollover, BEFORE `batch_id` changes.** Not at
close: a batch that rolls over unclosed (the `V28` case) would lose its log, and two writers would
duplicate it. A batch that closes with no successor stays active and its log stays in `state.json`,
which is where every reader already looks. Batches superseded BEFORE rev51 have no archive and will
not get a fabricated one — their logs are recoverable only from git history, and `/dev-flow-sync`
says so rather than inventing dates.

**Retire every single-slot field, one at a time. This table is the checklist, and "carried" is a decision too:**

| Field | At rollover |
|---|---|
| `decisions_log` | **MOVED** to `.dev-flow/<outgoing>/decisions-log.json`, then `[]` |
| `batch_id` · `batch_objective` | replaced. Never park the old objective under an invented key — `batch_objective_superseded` was one, added by hand, and no rule or command reads it |
| `current_station` / `current_phase` · `phase_status` | reset to the opening station and `not-started` |
| `iterations_per_station` / `iterations_per_phase` | reset to zero over the stations THIS batch activates |
| `stations_active` · `triggers` | re-evaluated for this batch. A carried `triggers` block asserts an evaluation that never ran, with its own `evaluated_at` timestamp to prove it |
| `artifacts` | cleared, then re-pointed at this batch's own files as they are created |
| `artifact_homes` | every `<batch_id>`-templated path re-pointed. A `repo:` home still naming the previous batch's directory sends this batch's writes into a closed batch's record |
| `mode` · `mode_history` | `mode` re-declared for this batch; `mode_history` is append-only PROJECT history and is CARRIED |
| `standing_authorization` | **re-asked** per §Batch-kickoff authorization — never carried |
| `obsidian_synced` | `false` |
| `project` · `language` | carried |
| `owner` | **re-stamped from the checkout doing the rollover** (`git rev-parse --show-toplevel`). Carrying it would let a batch opened in a worktree keep naming that worktree after the record moved back to the main checkout, which is the mismatch `V40` exists to report — and it would report a real one as an artefact of the rollover |
| `created_at` | re-stamped for this batch |

**Land the rollover in ONE commit**, together with the new batch's `01-requirements.md` and
`01-requirements-ledger.md` (§Phase 0) and the outgoing archive. Split across commits it leaves a
window in which `state.json` names a batch whose record does not exist — which is the `ghost` state
`V18` reports and `V1`-`V9` silently work around.

**Then read it back, do not assume it took.** Run the validator: `V29` is the readback (the active
batch's `decisions_log` is the active batch's), and it is what makes `V27`'s two coverage directions
mean anything across a rollover.

## Gate decisions (canonical vocabulary)

Standard gate offers `approve` / `iterate` / `cancel`. The `iterate` token has two validation-driven flavors: **`iterate-to-refine`** (back to Phase 1 — the requirement is wrong; recorded via the §6.5 Before/After amendment) and **`iterate-to-fix`** (back to Phase 3 — the implementation is wrong). Phase 5 additionally offers `close batch` / `open new batch`. Use these exact tokens. **If `state.json` declares `guided: true`, EVERY station gate is a GUIDED gate and takes four further steps before it closes.** **`SKILL.md` §*Guided first run* states them and is that gate's ONE home; this paragraph points and does not restate them** (`C-50`). `V55` derives the owed gates from `stations_active` and names any that carry no entry.

## Notice convention (operator-set, 2026-08-10)

Three levels, and they are visually distinct **inside the artifacts**, not only in conversation:

| Mark | Colour | Meaning |
|---|---|---|
| `⚠` | **yellow** | **Notice.** Does NOT block. Obliges you to DECLARE the reason in the artifact, and the batch continues. Written in yellow with the `⚠` sign so it is distinguishable at a glance from a satisfied item and from a block. |
| `✗` | red | **Block.** The gate does not pass until it is resolved: a code-review HIGH, a review blocker, a premise that came back FALSE or UNDECIDABLE. |
| `✓` | green | **Satisfied — with its evidence cited alongside.** Without a citation the item is not satisfied; it is merely asserted. |

**A notice that repeats for three consecutive batches stops being a notice.** Either it becomes a rule — and then it blocks — or it is retired — and then it stops cluttering the checklist. That decision is taken at the batch close and recorded like any other. Without this expiry, yellow degrades into background noise, which is how every notice system dies.

## Evidence states — ONE vocabulary, REUSED and not minted (flow rev73)

**Every agent and every template names the state of a piece of evidence from THIS table and from nowhere else.** The seven words come from an external handoff of 2026-09-10; **the distinctions do not** — the validator has been drawing them for eleven revisions under its own names, and a second vocabulary for one set of states is `C-50`'s second inventory applied to the word *evidence*. So the table below is a **binding of the prose word to the reader that already exists**, never a new set of states. **The right-hand column is what makes it checkable: a state with no reader is a wish.**

| State | What it asserts | The reader that already draws this line | The legal empty |
|---|---|---|---|
| `planned` | the check is named and has NOT been run — an intended test, a case written before the code | `V39` separates *written* from *the untouched template*: a plan that names its cases is WRITTEN, and `V39` calls its own coverage **"a BOUND and not a proof"** | — a plan states `planned` and is complete |
| `executed` | it ran, against a named revision, with the command and the output read from THAT run | `V31`'s per-instrument **RED-proof** field, and `C-19`'s ONE complete run whose tail is read from its own output | — |
| `approved` | it ran AND a named reviewer accepted the result | `V47`'s `PASS` / `PASS-WITH-NOTES` and `V36`'s reviewer identity — **the identity is part of the state**, not an annotation on it | — |
| `failed` | it ran and the result was negative | `V47`'s `FAIL`; at the increment gate the token is `BLOCK` (`increment-template.md` §4b, read by `V36`), deliberately NOT unified | — |
| `blocked` | it CANNOT run until something else lands — a HIGH finding, a missing fixture, an undecided premise | `V50`'s **conditional-gate discharge** and `C-43`'s FALSE/UNDECIDABLE premise; the `⚠`/`✗` split above | — |
| `not-run` | it was owed and nothing ran — **and the reason is named on the same line**, `not-run — <why>`; a bare `not-run` is the state this row exists to refuse, and `SKILL.md` step 4 spells the three the bundle owes | `V41`'s **"this is not a pass"** over a clause executed against nothing, and `V37`'s *packet with no verdict row* | — `not-run` IS the declaration |
| `n/a — <reason>` | it does not apply here, and the reason is written | `V36`'s `WAIVED-BY-OPERATOR — <reason>`, whose whole ruling is that **the waiver carries a reason or names nobody**; `C-55`'s *say which kind of emptiness* | the reason is NOT optional — `n/a` alone is `not-run` wearing a better word |

**Three rules that make the table do work rather than decorate:**
1. **A `planned` never becomes an `executed` by being read again.** The distinction the handoff asked for is exactly `V41`'s: *a test planned is not a test run*. An artifact that carries only `planned` rows is a **plan** and is complete as one; the same artifact presented as a **validation** is `not-run`.
2. **Evidence is bound to what produced it — revision, command, environment, result, limits** (`C-56`, and `V41`'s digest rows under the declared `artifact_homes.evidence`). **Evidence from another revision is `not-run` for this one.** A later change that touches the subject INVALIDATES the state and the check returns to `planned`.
3. **What this table does NOT do, said here rather than left to be found.** **No rule reads these seven words out of an artifact today.** They are the AUTHOR's vocabulary; the readers in the right-hand column draw the same line at the fields those rules actually do read (`PASS`/`FAIL`/`BLOCK`, the RED-proof field, the declared-vs-untouched test, `WAIVED-BY-OPERATOR — <reason>`). Binding the words to existing readers is the whole ruling — minting a parallel set of *fields* would have been the second inventory this refuses — but it means a bare `n/a` in prose is refused by a HUMAN reader and by `REV STATES-one-vocabulary`, not by a gate rule. That bound is the honest one.
4. **No file mints an eighth word.** `verified`, `done`, `ok`, `signed-off`, `validated` and `complete` are not states — each collapses two of the seven and hides which. **`REV STATES-one-vocabulary` is the census** over every command, template and agent in the canon: it DISCOVERS which files name a state, compares that to the declared population both ways, and reddens on a parallel spelling **IN THESE SHAPES** — a run of backticked tokens mixing one of these states with a foreign one, and any of the six words above used in the reserved backticked position. ⚠ **What it does NOT see, measured rather than assumed:** a parallel set anchored only on `approved` (deliberately not distinctive — `approved` is also a `phase_status` and a PDR verdict, and flagging those two legitimate runs would make this a rule people learn to ignore), and an eighth word minted *without* backticks. Those are the bound, and they are written here rather than left for the next reader to discover.

## Where the flow's own files live — paths in these documents are FLOW-RELATIVE

**Every path in this command, in `/fast-dev-flow`, in `/dev-flow-init`, in the templates and in the agent files that names a file OF THE FLOW is written relative to the flow's own root, in the layout the published bundle uses:** `commands/`, `templates/`, `templates/fast-dev-flow/`, `agents/`, `scripts/`, `FLOW-VERSION.md`. **This section is that fact's one home** (`C-50`); no other file restates the mapping, and none of them writes an installation path.

**A canonical Claude Code home holds the same files under two of those names spelled differently, and the pairing is not respelled here.** **It has exactly one machine-readable home** — the *Canon path → Bundle path* table in `FLOW-VERSION.md`, which `--sync-bundle` builds from and `--map` prints. Two reasons, and both are measured: a second copy in prose is the drift this flow has paid for five times, and an installation path written into a published instruction is a path most of its readers cannot open.

**Why bundle-relative and not the canonical spelling:** the flow is published as a skill, and a reader installing it has **no Claude Code home at all** — measured 2026-09-18 on two non-Claude runtimes, where every canon-home path in this prose was a path the reader could not open and had to re-map by hand before the first artifact was written. A path a reader cannot open is not a citation. `PUB no-leaked-shapes` reads this as a rule: `canon-home-path` reddens an installation path in any published command, template, agent file or in the adapter.

**Three parts of the flow are canon-only and are named as such wherever they appear, never cited as though they shipped:** the **deployment record** (the checkout table and `vault_root` — per-installation, deliberately unhashed, and named in `FLOW-VERSION.md`'s identity block), the two **hook executors** (Claude Code wiring), and the repository's **CI workflow**. A runtime without them runs without what they enforce, and `/dev-flow` says which — see the adapter's *What refuses an invocation here*.

## Artifact homes — one home per artifact, and the link crosses by ID

Where an artifact lives is **configuration**, not a hard-coded path: the `artifact_homes` block of `state.json` declares it — that block and nothing else — and **no command may write a FLOW ARTIFACT to a path that is not declared there** — and this
sentence is that rule's ONE home; every other site in the flow points here rather than restating
it. **It binds the flow's own RECORD and nothing else.** The source files, the tests, and whatever
the task itself asks for are the WORK, not the record, and no `artifact_homes` key is owed for
them — `artifact_homes.tests` exists because a RULE resolves acceptance ids against that corpus,
not to license writing there. A reader of the 2026-09-18 publication test read the unbounded
spelling as governing the product source file they had been commissioned to write, and had to
rule on it; four further sites said the same unbounded thing, and one bounded spelling beside four
unbounded ones is `C-50` inside the repair. If something needs a new location, it is declared first.

**One home is now READ by a rule and not only written to: `artifact_homes.tests` is the node corpus `V2` resolves acceptance ids against** — from rev58, taken from `state.json` alone — **rev62 retired `.dev-flow/config.json`, the second home this sentence had been warning about: no rule ever read it, and no project on disk ever held one** — defaulting to `tests/` when undeclared, accepting a `repo:` directory *or* a single `repo:` file, and reporting a `vault:`, unresolvable or absent corpus in its own sentence rather than passing. **From rev59 that rule reads BOTH id forms — `AT-B<batch>-<n>` and the global-numeric `AT-<n>` — and it reads them only where they are written BARE: an id inside backticks or a fenced block is a citation, not a declaration, so an acceptance id a requirement DECLARES is written as plain text or `V2` does not see it.**

**The dividing line, in one sentence: if a mechanical check needs to READ it, it goes in the repo; if a human reads it to decide, it goes in the vault.**

| Home | Artifacts | Why |
|---|---|---|
| **repo** | requirements (`SPEC`, `R-NN vN`) · traceability matrix · test cases · **module map** · increment review packets · canonical backlog | strong, executable traceability to code — and the module map is the **oracle** the A-family triggers read: in Drive no mechanical check could open it |
| **vault + Drive** | design proposal · **PDR** and **DDR** records · post-mortem and lessons · batch metrics README · architecture diagrams | deliberation: weak traceability to code, read by humans to decide |

**What `vault:` resolves to — one definition, in one place.** `artifact_homes` writes vault paths as `vault:<project>/…`. **The `vault:` prefix resolves against the `vault_root` row of the flow's deployment record** — the flow home's per-installation file, which a skill-only runtime does not have at all — and against nothing else. **What its absence implies is stated once, in `SKILL.md` step 4: `V15`, `V16` and `V17` are `not-run` there, by name and with the reason printed.** That home is deliberate: a vault root is a **per-installation** path, exactly like the checkouts already declared there — *"a per-installation fact cannot live in a shared identity"*. It therefore does **not** belong in `state.json` or in `artifact_homes`, which are per-project and per-checkout: a machine with N projects would hold N copies of one machine fact, and the first copy to drift sends a sync into the wrong vault. **A command that cannot read the row STOPS and asks; it never guesses a path.** Accepted limit, stated rather than discovered: like the rest of that record the row is unhashed by construction, so a wrong row is caught by reading, not by a rule. **A runtime that has no such record has no vault either** — `vault:` homes are then `n/a — no deployment record on this runtime`, which is an answer, and a guessed path is not.

**ONE ARTIFACT, ONE CANONICAL HOME *PER MODE*, AND EXACTLY ONE COMMAND WRITES THE VAULT — operator ruling `Q22`, 2026-09-11, flow rev72.** Rule 1 below says *one home per artifact, nothing is copied*, and until rev72 the flow broke it in two places at once: `artifact_homes.postmortem` declared a **vault** home while §Phase 5 declared the artifact to be `.dev-flow/<batch_id>/05-postmortem.md`, and `/dev-flow-init` seeded the local file while its own §Restrictions said *"do not touch the Obsidian vault"*. Two homes, no writer, and nobody could say which copy was true — `C-50`'s defect committed against the section that forbids it. The ruling, by mode:

| mode | the artifact | its ONE canonical home | who writes it |
|---|---|---|---|
| `core` | the close record | **`.dev-flow/<batch_id>/05-close.md`, in the repo** — this is the canonical copy | `/dev-flow` §Phase 5 |
| `core` | the vault batch `README` (`artifact_homes.metrics`) | a **GENERATED VIEW** of that close record, never a second source | **`/dev-flow-sync` alone**, step 6 |
| `full` | PDR · DDR · post-mortem | **the vault copies** (`artifact_homes.design_pdr` · `design_ddr` · `postmortem`) — these are canonical | **`/dev-flow-sync` alone** |
| `full` | the same three, under `.dev-flow/<batch_id>/` | **LOCAL STAGING, not a home** — where `/dev-flow` writes and what `/dev-flow-sync` publishes FROM | `/dev-flow` |

**`/dev-flow` NEVER WRITES THE VAULT, and neither does `/dev-flow-init`.** The vault is written by `/dev-flow-sync` and by nothing else — which is why it is a deliberate manual step run after commit/push/merge, and why a sealed record can be sealed at all. **Staging is not a second home**, on the same reasoning the evidence home already uses (*"a session-scoped scratch directory is not a home"*): a staged file is an INPUT to the publishing act, it carries no independent truth, and when the two disagree the vault copy is the one that is true in `full` while the repo copy is the one that is true in `core`. **This adds no `artifact_homes` key** — the block still declares **twelve**, `/dev-flow-init` step 3 is still their one inventory, and the staging paths are the batch record's own structure, exactly like `02-review.md` and `04-validation.md`, neither of which has ever had a key. `CMD VAULT-one-writer` is the census arm over every site naming where PDR, DDR, the post-mortem or the batch README is written.

**Three rules keep the split from rotting:**

1. **One home per artifact. Nothing is copied.** If a copy appears, one of the two is false and nobody knows which — that is exactly how the canonical backlog went ~10 batches stale without any phase noticing.
   **Rider — this invariant is STRUCTURAL, so no assertion over output can guard it.** Collapsing two copies of a predicate into one call site is *behaviour-preserving by construction*: the two expressions agree on every possible input, which is precisely why the duplication was invisible. Restore the copy and every behavioural test stays green. Guard it by **parsing the artifact and asserting the shape** — that the predicate is called from exactly the one function that owns it, that the id appears in exactly one file — never by comparing what the two produce. (Origin: batch-84 — see dev-flow-lessons)
2. **The link crosses by ID, never by content.** The requirement, in the repo, cites `PDR-<batch>#D3`; the PDR, in the vault, cites `R-014 v3`. **The ids are the glue of the split**; without them, separating the homes breaks traceability instead of organising it.
3. **What decides code lands in the repo.** A PDR decision that fixes an interface does not stay only in the vault: it is reflected in the requirement or in the module map, which are versioned beside the code. **The vault keeps the deliberation; the repo keeps the commitment.**

**What this costs, stated so it is a decision and not a discovery.** A record in Drive has no diff, no PR, no CI, and cannot be grepped from a hook. Compensation: the record is **sealed** (date · verdict · participants · approved ids) and cited by id; if it changes after the seal it is a new version with a new id, and the requirement that cited the old one keeps pointing there — which is the signal you want. **What is not compensated:** no CI will ever verify a PDR. That is a real boundary of the design. It also draws the automation frontier with a one-line rule instead of an argument per control: **the mechanical validator can only check what lives in the repo.**

## A ruling is applied as a CENSUS over its axis — `C-65`

✅ **MINTED. This paragraph stood here as “⚠ NOT A CONTROL”, byte-identical in the nine commits of this file from rev65 to rev74 — four days, not the five weeks `BRIEF-7` carried — and the operator's `C-45` sitting of 2026-09-11 minted it as `C-65`.** The rule, its four exhibits (rev65's seven rounds, the rev66/69/72 per-instance folds the independent review caught, and rev74's census refuting the ruling's own literal wording), the arm shape and the honest limit **live in `dev-flow-lessons` `C-65` and nowhere else**. ⚠ **Reproducing them here would be `C-50`'s second inventory committed inside the control that forbids folding one instance of a class** — and this file's own history says what that costs: the candidate text and the catalog would be two homes for one rule, drifting from the day they shipped, exactly as `Q21`'s prose enumeration and its arm did.

**In one sentence, so a reader at the gate needs no second file:** *when a ruling's subject is a CLASS, the same commit that closes the first instance enumerates the class and closes the set — a declared population plus an arm comparing source to it, BOTH WAYS.* Everything else is at `C-65`.

## Control placement (standing policy)

This global command carries only **project-agnostic** engineering discipline. A control that is specific to a project's stack — its UI framework, snapshot tooling, frozen-file set, or other framework-bound mechanics — is encoded in **that project's `docs/engineering-rules.md`**, never here. **Classify every new control before encoding:** portable principle → global command; stack-specific → the project's engineering-rules doc (no global edit). The project doc is consulted at the relevant phase alongside these general controls; the canonical cross-project history stays in the control-lineage memory.

### The flow is a SHARED asset — changes flow both ways (C-45)

Controls are discovered inside one project but they are not that project's property. **A portable control found anywhere must reach every project that runs this flow**, or each project re-learns the same lesson at full price. Two obligations, and the second is the one that gets forgotten:

**PUSH — a portable control is not encoded until it lands upstream.** Editing your own installed copy makes the control active *for you* and invisible to everyone else. The batch that discovered it owes, before it closes:
1. the **command** change (`commands/dev-flow.md` / `commands/fast-dev-flow.md`) — the rule itself;
2. its **artifact** (`templates/*.md`) — a control with no output degrades to *"I thought about it"*;
3. the **catalog** entry (`dev-flow-lessons`) — the distilled lesson, with the measured origin;
4. **committed and pushed** to the flow repos, with the SHAs recorded in the batch's close. Per **C-44**, an unpushed control is indistinguishable from one that was never written.

Record which of the four landed. A control that reached the command but not the template is *half-encoded*, and the half that is missing is the enforceable half.

**PULL — check flow currency at Phase 0, alongside RC-1.** RC-1 asserts the working branch is current against `origin/main`; this asserts the *flow itself* is current. Before deriving anything, confirm the local flow files are not behind their remotes — another project may have encoded a control that would have caught this batch's defect. **A batch run on a stale flow inherits a solved problem as an open one.** State the flow revision in `PLAN.md` next to the RC-1 line.

**Where a change belongs is still decided by the classification above** — portability is the test, not convenience. A stack-specific rule pushed upstream pollutes every other project; a portable one kept local is a lesson paid for once and used once.

## Objective exit criteria — no arbitrary "done"

A phase is "done" ONLY when its gate's exit bar is MET and EVIDENCED — never by judgment, fatigue, or "enough." `iterate` is the act of closing a NAMED gap to that bar; `approve` asserts the bar is met. Neither token is volume-driven: you do not iterate past the bar to pile on, nor approve below it because it "looks tested."

The bar is the requirement set + the encoded controls, on three measurable axes:

- **Coverage** — dual traceability complete: every `US → AT-NNN` and every `HLR/LLR → TC-NNN` chain exists and is GREEN; no requirement without a verifying node, no orphan test. The traceability matrix has zero gaps.
- **Certainty** — every acceptance is non-vacuous: the black-box `AT` observes the deliverable through the SHIPPED surface (A-5), with the counterfactual shown (the AT RED on the pre-fix tree), a negative control where an oracle is used, and boundary + negative evidence. No pass that cannot fail.
- **Evidence** — every gate-checklist item carries a citation a third party can re-run: a collected node id, command output, a `file:line`, or a diff. A checklist marked from intent is not evidence.

`iterate` REQUIRES a named gap against one of these axes (a missing trace, a vacuous/absent counterfactual, an unobserved deliverable, a false coverage claim, an un-cited checklist item). If no such gap can be named, the phase is done → `approve`. **At every gate the orchestrator MUST state which axis (if any) is unmet and the specific gap; offering `iterate` without a named gap is a process violation.**

## Premise evaluation at every gate (C-43)

**Every gate additionally evaluates the PREMISES its stage rests on, as explicit propositions — not prose.** Verifying an artifact against its requirements answers *"does the work match the spec?"*; it does not answer *"is what the spec ASSERTS ABOUT THE WORLD true?"* A stage can be fully compliant with a requirement whose premise is false. Extract the premises, state each as a truth-apt proposition, and record one of three verdicts:

| Verdict | Meaning | Gate effect |
|---|---|---|
| ✅ **TRUE** | Sustained by an **executed** probe — command output, a `file:line`, a run. **A citation of another document is not evidence.** | passes |
| ❌ **FALSE** | A counterexample is recorded. | **blocks** |
| ❓ **UNDECIDABLE** | Validation/verification is missing, or the requirement is ambiguous / incomplete. | **blocks** — dispositioned explicitly: decided, or declared out of scope **in writing** |

**The three-tier truth hierarchy, and how an axiom may be challenged.**

1. **Axioms** — requirements already validated AND verified. Default: law, not re-litigated. **They are NOT immune.** An axiom re-opens on either (a) an **executed counterexample**, or (b) a **logical invalidation**, which in practice is almost always **INCOMPLETENESS** rather than falsehood — the requirement fails to cover a case it must. **The disposition of a successful challenge ENLARGES the base of truth: the requirement comes out MORE COMPLETE, never deleted.** Use the existing machinery — `iterate-to-refine` + the §6.5 Before/After amendment; do not invent a second path.
2. **Hypotheses** — requirements this batch introduces. **Not law until they pass their own validation/verification stage.** Design-batch output (an ADR, resolved decisions, acceptance criteria inherited from a prior batch) sits HERE: *having been written down by an earlier batch does not make it verified.*
3. **Premises** — what the artifacts claim about the world: symbols, line numbers, file shapes, sizes, "X already exists". **Executed against disk, never trusted.**

**ARTIFACT — mandate an output, not a process step.** The premise table lives in **§2.7 of the requirements document** (`templates/req-template.md`) in `core` and `full`, and in **§3b of the spec** (`templates/fast-dev-flow/spec-template.md`) in `fast`, which is the artifact that mode owes — one table per mode, never two at once, one row per premise with its tier, verdict, executed evidence and disposition. A control that mandates re-reading with no artifact degrades to *"I thought about it"* — this project's oldest meta-rule. **AND FROM flow rev69 THE ARTIFACT HAS A READER: `V45`**, on the keyed `**Premise evaluation**` bullet that sits under the table and rolls it up — the count, then the verdict, **leading** the cell with one of the three tokens above or the legal empty `none — <why no premise applies>`. A cell reading `done` or `see the table` names no verdict and is scored as the empty state, because the gate effect above turns on the token and on nothing else. *Measured 2026-09-10 over the 66 live requirement documents of this project, case-sensitively: the §2.7 heading in 10, the keyed field in **0** — which is what the most-cited control in this command had bought in twenty-six revisions.*

**Relation to the neighbouring controls.** C-35 executes the PRODUCT's transform over a real input; C-39 executes the THRESHOLD the gate is keyed on; C-40 asks whether a predicate CAN go red. C-43 sits one layer earlier than all three: it asks whether the CLAIM the predicate rests on is true at all. A premise can be false while every predicate over it is well-formed, falsifiable and green.

(Origin: batch-70 Phase 0 — see dev-flow-lessons)

## An emptiness is doing work — say which kind (C-55)

**Whenever a claim or a guard depends on the tree currently containing NO instance of some case, that emptiness is LOAD-BEARING and must be declared.** It is the quietest defect in this catalog because nothing is wrong today: the claim is true, the suite is green, and the thing that will make both false is a change nobody will connect to either. C-40 asks whether a predicate *can* go red; C-43 asks whether the spec's premise is *true*. C-55 asks a third question both of them pass over — **what is this result resting on that is only accidentally the case right now?**

**Limb 1 — the emptiness is the FINDING.** When a batch's result is an *absence* ("no X exists in the tree", "the blind spot is empty", "zero call sites remain"), the property that made the search wide enough is **part of the result** and needs its own guard. A negative result is only worth having if the search that produced it was too WIDE; narrow it later and every claim derived from it silently weakens while every other guard stays green. **Name the over-breadth, guard it, and say in the guard's own docstring that it protects a conclusion rather than a behaviour** — otherwise the next reader files it as an implementation detail and "improves" it.

**Rider — an absence is admissible only if the probe that produced it can produce a NON-absence.** Before accepting *"there are none"*, run the same probe, unmodified, over a case known to be present. **Uniformity over heterogeneous inputs is the TRIGGER for that control, never the verdict.** 27-of-27 or 35-of-35 has the shape of one failure repeated — but the correct answer can be uniform too, and in the origin case below it *was*: all 35 files really were present. A clean tree greps zero everywhere and a passing type check is zero-of-all, so treating uniformity as a verdict would false-fail correct work, which **C-53** says costs as much as passing wrong work. Run the control and let it decide. A *plausible* zero reads as data; only an *impossible* value betrays itself, and that is luck rather than detection. **If no known-present case can be constructed** — a read-only external system, a case that cannot be synthesised — **say so and downgrade the claim from a finding to an unverified observation**; a mandated control that cannot be paid is one that gets skipped in silence. This is **C-53's own habits 1 and 3** — *a rule that lights up everywhere is far more likely mis-scoped than right*, and *pair every rule with a positive AND a negative control* — together with the reader-as-oracle / discriminating-negative discipline, applied to **diagnostic probes** rather than to checkers and tests — the gap being that nobody treats a probe as code to be verified, because *"I am only looking"*. (Origin: probe-failure cleanup session — see dev-flow-lessons)

**Limb 2 — the emptiness is an ACCIDENT of today's data.** A guard clause that is a **no-op on the current tree** is untested, however green the suite. The tell is mechanical: **a mutation of that clause changes nothing today.** Two operative consequences:
1. **A conjunctive criterion needs one mutation per conjunct.** *"The resolver shall classify it AND never drop it"* is two predicates. Mutating the classifier reddens the first and says nothing about the second.
2. **Mutating a stage is not mutating the pipeline.** A criterion that names an end-to-end property must be mutated at the stage that owns that property, not at the one that is easiest to reach.

**DISCHARGE — a synthetic instance, not an argument.** Both limbs are discharged the same way: **construct the case the tree does not currently contain** (a fixture tree, an in-memory module, a synthetic input) and assert the property against it. "The tree has none today" is the reason the guard is needed, never a reason to skip it.

(Origin: batch-84 — see dev-flow-lessons)

## An evidence transcript is corpus input (C-56)

**Any artifact a scanner reads is INPUT — including the artifacts written to PROVE something.** `.dev-flow/**` is read by the Atlas id-scanner and by V13's tree grep, so an increment packet, a review finding and a close record are corpus on exactly the same terms as a requirements document. A scanner cannot tell a token being *reported* from one being *declared*, and nothing downstream re-derives that distinction. Two obligations follow, and both are cheap only before the fact.

1. **A mutation reverted in its target file but SPELLED verbatim in a transcript is NOT reverted.** C-40's restore obligation — the hash back to the pre-mutation value — covers the file that was mutated and says nothing about the packet that QUOTES the mutation. **The obligation extends to every scannable artifact carrying the mutation's text.** Discharge it by construction: **describe mutations by position and operation** ("the id's fourth character, digit → letter"), never paste the mangled token. Otherwise the hash proves the wrong plane — the source is clean, and the defect has moved into the evidence.
2. **Dotted-range id shorthand is forbidden wherever an id-scanner reads.** `AT-020..024` is not a range to a tokenizer; it is characters it will resolve into ids nobody allocated. **Enumerate them, or write the prose form** (`AT-020` through `AT-024`).

(Origin: batch-86 — see dev-flow-lessons)

## Evidence bytes live at a declared home (`C-59`, `Q5`+`Q19`, 2026-09-07)

**An artifact a packet cites as PROOF is written to the home `artifact_homes.evidence`
declares** — a `repo:` or `vault:` location, durable and named at the batch, **never a
session-scoped `Temp` directory** — stored byte for byte, and cited in the packet with the
SHA-256 of the bytes at that path. `increment-template.md` mints the `Evidence files` section
and gate row 16; **`V41`** reads all three clauses and re-hashes the stored bytes itself.

**Its severities are not uniform, and that is the ruling.** A batch that declares no evidence
home, and a packet that leaves the field unanswered, are **NOTICE** — every batch on disk was
opened before rev66. A cited digest that disagrees with the bytes on disk is a **BLOCK**: that
is not an omission a reader may weigh, it is a false claim, and it is the defect that shipped
looking healthy at batch-66 when `core.autocrlf` normalised four `.PRE` files on the way into
the commit that was supposed to preserve them. **Assert the stored artifact, never the one you
handed to the store** — and if the store is git, mark the path `-text`, not `text eol=lf`.

## A deferral carries the marker, wherever it is born (`Q6`, 2026-09-07)

**Backlog carry-over fires at batch CLOSE, so it sweeps what a BATCH produced and nothing else.**
A deferral born BEFORE a batch — in a `/prototype` verdict's *Non-goals*, an ADR roadmap, a design
pass's findings list, an audit — is not a batch artifact, so no close step owns it. It is the
mirror image of what the flow already guards: carries OUT of a batch are enforced, deferrals INTO
the pipeline are not. Measured once: **six** items deferred across a handoff plan, a screens audit
and a prototype verdict, with **0** occurrences of each across all three backlog files.

**The marker is `⏸ DEFER`, and it is now VALID — not merely tolerated — in `.dev-flow/design/**`,
in ADR files and in the batch record.** That is the half of the ruling nothing else supplies: the
leaked deferrals were invisible partly because nothing said where a pre-batch deferral may
legitimately be written. Write it, then file the item; the marker is not a substitute for the
queue entry.

**`V42` counts the ones nobody filed** — every marker in that corpus whose text is keyed to no
entry in the project's backlog lanes, reported by file, line and opening words.
**HOW A MARKER IS KEYED, said here because a reader who does not know it cannot satisfy it.**
The key is the marker's **first TEN normalised words**, matched as a substring against the
backlog lanes; a marker carrying fewer than **FOUR** words is reported as unkeyable rather than
passed. **A shared id is NOT a key** — `BL-001` in both places matches nothing — so file the
deferral by repeating the backlog entry's opening words verbatim in the marker, then continue
the sentence however you like: ten words is long enough that a rewording breaks the link and
short enough that a differently-finished sentence still matches. (Origin: the 2026-09-19
publication test, where a reader with `BL-001` in both files got *a deferral marker whose text
is in no backlog lane* and had to read the validator's source to learn the grammar.) It is a **census
and not a gate**, deliberately: there is no close to hang a BLOCK on for something written before
any batch existed, so the strongest honest instrument is a number a reader must look at.

**Three properties of the census, each of which is a way it could have been useless.** *(a)* A
marker inside a **code span** is a citation, not a declaration — `V2`'s rev59 rule, and without it
the census reports the very document that specifies this section. *(b)* The corpus is `git
ls-files`, not a filesystem walk: a checkout with stale worktrees would otherwise report every
marker once per worktree, and a fresh clone would disagree with it. *(c)* An unenumerable corpus,
a missing backlog or an empty corpus is **reported**, never scored zero — zero is also what the
census says when nothing has leaked, and the two must not render alike.

**When you file the deferral, transcribe it by RE-EXECUTING it, never by copying.** Three of the
six items measured above came back NARROWER than their source once re-run, because work had
shipped in between; a verbatim transcription would have planted three false claims. And check for
an existing entry under another name first — one of the six was already tracked, and a rule with
no dedupe step manufactures duplicates.

## The mechanical validator — the half of the gate that should not depend on memory

```bash
python scripts/devflow-validate.py <project-root>   # exit 1 on any BLOCK
python scripts/devflow-validate.py --selftest       # prove every rule can go RED
```

**Both paths are FLOW-relative** (§*Where the flow's own files live*), so run them from the
flow's own root and pass your project as the argument — e.g. `cd <the flow root> && python
scripts/devflow-validate.py <the project you are gating>`. A reader standing in their project
and typing `scripts/…` gets nothing, which is the one friction the 2026-09-18 publication
test hit twice.

**Run it at every gate and paste its output as evidence.** It turns into an exit code the checks that are already greps and arithmetic, so they stop depending on the agent remembering them.

**The rule list is NOT written here, and that is the fix.** Until rev57 this section carried a hand-kept table of `V1`–`V9`: **9 rules of 28**, stale for **eight revisions**, and nothing could see it — a list maintained beside the list it guards, which is the defect this flow has now measured five times. Run the tool instead:

```bash
python scripts/devflow-validate.py --map
```

Its **COVERAGE** block names every registered rule, the corpus that rule reads (**SELECTORS**), and what it can tell you — derived from the same registry the checks run from, and guarded in both directions by `--selftest`. Three things it does not say: `V15`/`V16`/`V17` also run at invocation through the flow-guard hook; `V3` and `V24` are **retired numbers**, not gaps; and `V19` is *one `COMPONENT` id, one declaration, across the merged corpus*.

### Severity — a property of a finding, not of a rule

**Severity is a property of a FINDING, not of a rule — read it off a real run, never off `--map`.** Re-derived 2026-09-25 at flow rev94 — the census was built at rev74 and its own arm has re-run it at every bump since — by an AST census over all **55** registered rules — every `F(cid, SEV, …)` and every `(SEV, …)` outcome tuple in each rule's own call closure, the dispatcher's crash-BLOCK excluded because it is the harness's finding and is reachable from all of them: **9 can only BLOCK**, **34 can only NOTICE**, **12 raise BOTH depending on which condition fired** — `V7`, `V12`, `V15`, `V16`, `V17`, `V20`, `V26`, `V30`, `V39`, `V41`, `V53`, `V56` — and **0 can raise neither**. `V26` is the plain case: it NOTICEs a live contract past its size budget and BLOCKs a pairing that exists on one side only. So a per-rule severity column cannot be true for the rules just named, and the sentence *“BLOCK unless the tool marks it NOTICE”* is wrong twice over — it reads the NOTICE-only rules `--map` does not annotate (`V8`, `V9`, `V13`, `V18`, `V19`, `V22`, `V23`, `V25`, `V27`, `V28`, `V29`, `V31`, `V32`, `V33`, `V34`, `V35`, `V36`, `V37`, `V38`, `V40`, `V42`, `V43`, `V44`, `V45`, `V46`, `V47`, `V48`, `V49`, `V50`, `V51`, `V52`, `V54`, `V55`, `V57`) as blocking, and it asks at the rule level a question only the run can answer. **The gate prints the severity of every finding it raises; that is the answer, and it is the only one that is current.**

> ✅ **THE FIGURES ABOVE ARE NO LONGER HAND-KEPT — `rev74` BUILT THE ARM, AND IT IS THE READER THE NEXT THREE PARAGRAPHS SAY WAS MISSING.** `FV SEVERITY-census` (in `devflow-validate.py --selftest`) derives the partition from this file's own AST over `CHECKS` — the same registry the gate dispatches from — **parses** the five figures and both id lists out of the paragraph above rather than retyping them, and reddens on any disagreement. Registering a rule, or giving an existing rule a second severity, now reddens the arm until this sentence is rewritten; it cannot go stale a fourth time in silence. **The instrument was shown to report a failure before its PASS was believed** (`C-57`), on BOTH of its halves: six planted counterfactuals — a wrong figure, a rule added to the registry, an id dropped from the `BOTH` list, the paragraph reworded past its own parser, **a severity swapped in the validator's own source** (the derivation side, which the first cut of this arm left uncovered and the independent review caught), and the same figure given a second home — each make it red; the fourth reads `UNREADABLE` and the sixth `AMBIGUOUS`, neither as agreement. `FV SEVERITY-closure-models` additionally pins that a call-only closure derives the same partition, so no figure rests on that choice. **This discharges `C-58` for this file.** ⚠ **What the arm does NOT hold, said rather than implied:** the worked exemplar sentence naming `V26`, the re-derivation date, and the prose around the figures are not parsed — only the five figures and the two id lists are. Every figure in this paragraph is written **once**, in the form the arm reads: the two spelled-out duplicates the first cut of this rewrite carried (*“those ten”*, *“the **thirty** NOTICE-only rules”*) were second inventories of parsed facts and are deleted, not re-parsed. The two notices below are the record of the three failures that paid for it and are kept, not tidied away.
>
> ⚠ **This paragraph WAS a hand-kept census of a derivable fact, and it was wrong three times.** rev61 measured it at 30 rules on 2026-09-07 and rev63 falsified it the same day by registering four more — the census is reproducible from `devflow-validate.py`'s own AST (closure per registered rule, `run` excluded), so **nothing had to go stale here except that no reader compares the two**. That is `C-58` pointed at this file: an arm deriving the census and asserting these five figures against this sentence is a named candidate for a later revision, deliberately NOT built at rev63 — building it inside the rev that found the staleness would ship the reader and its first subject in one commit, with nothing but this paragraph to check it against.
>
> ⚠ **WAS STALE BY FOUR RULES AT rev65, and was stated rather than rewritten — and stayed stale for nine more revisions, by eleven more rules.** rev74 re-derived it: the population is **49**, not 34, and the partition moved in every bucket. (The figure is written once, above, in the form the arm parses — a second spelling of it here would be the second inventory this file's own `C-50` refuses.) The rev65 disagreement this notice ends on is now settled by derivation rather than by inspection: `V25` is **NOTICE-only**, which is what its own block comment says and what rev63's published list said, so the second census rev65 ran was the one that was wrong. rev64 registered `V37` and `V38` and rev65 registers `V39` and `V40`; the population is **38**, against a paragraph that says 34, and **neither revision moved the five figures**. ⚠ **And rev65 moved an EXISTING rule's RANGE, which a rule count cannot show:** `V20` gained a NOTICE — the unversioned-mark disclosure — so it LEAVES the BLOCK-only bucket, `V39` enters the raise-BOTH bucket beside it, and `V40` enters NOTICE-only. **No published figure above survives the bump, and this notice deliberately does not replace them with new ones:** a first draft of this clause said the partition is *9 / 8*, which is true only at the 34-rule population the stale paragraph describes and hides rev65's own new BLOCK rule — the third review caught it, and publishing a corrected unchecked number in the very block that says *replacing unchecked numbers with unchecked numbers is not a repair* would have been the defect committing itself. The whole partition is owed to `C-58`'s arm. rev65 re-derived them with a second AST census and got a different answer for `V25` than the published one — a rule whose own block comment says *"severity is NOTICE and never BLOCK"* — which means the two instruments do not agree and **only one of them can be right**. Replacing the numbers with the output of an instrument that has not itself been proven would be substituting one unchecked census for another, so the figures above stand as rev63 measured them and this notice says how far behind they are. What is certain about the two new rules is narrower than a census and is stated as such: **`V39` raises `{BLOCK, NOTICE, SKIP}` and `V40` raises `{NOTICE, SKIP}` over their whole arm sweep** — `V39 SEVERITY-set` and `V40 SEVERITY-set` assert exactly that, the severity *set* over every state the arms drive, which is what an "only" needs and what a single reachability arm cannot give. **`V39` therefore belongs in the raise-BOTH bucket, not the BLOCK-only one** — its NOTICE is the untouched-sibling disclosure. ⚠ A first draft of this sentence said `{BLOCK, SKIP}` and put `V39` in the BLOCK-only bucket, naming these very arms as its proof, one revision after the fold that gave the rule its NOTICE; the fourth review caught it by running the arm the sentence cites. **That is this paragraph's own thesis committing itself a second time, and it is left written down rather than tidied away.** (A first draft of this sentence cited `V39 SENTINEL-must-be-RED` and `V40 PASS!=NOOP` as the proof; rev65's reviewer pointed out that the first shows one BLOCK is reachable for one input and the second compares message strings and never touches a severity — neither establishes an "only", in a paragraph whose whole point is that inspection is what it refuses.) The reconciling arm for the five figures above is `C-58`'s candidate and it is still owed.

**What a reader WITHOUT the tool loses — both halves: the rule list AND the severities.** This file no longer carries either, deliberately, against a table that was wrong about nineteen rules for eight revisions. The trade is only sound because the tool ships in the same repository as this command and `V7`/`V15` prove the copy you are about to run is the declared one; on a checkout where they do not, read `--map`'s output from someone who ran it, not this file.

**What it deliberately cannot check, and why that is the design:** anything living in the vault — whether the design proposal is complete, whether the PDR verdict is honest, whether its open conditions were really discharged. **No CI will ever verify a design record.** The automation frontier is not argued control by control; it is decided by the artifact's home (see §Artifact homes).

**Two obligations that keep the validator from becoming the thing it is supposed to prevent:**

1. **Every rule must demonstrate its own RED.** `--selftest` feeds each rule a broken input (must go RED) and a clean one (must stay GREEN). A linter whose rules cannot fail is a vacuous check *with CI authority*, which is strictly worse than no linter. **The exemption set is DERIVED, never hand-listed:** the selftest harvests the rule ids at the label position of the arm lines it actually emitted, subtracts them from the registered set, and BLOCKs unless the difference equals the declared expectation `_SELFTEST_EXEMPT` — so a rule that is registered and never exercised cannot hide, and a rule dropped from the registry cannot be silently forgiven. Measured 2026-09-03: **28 registered, 28 armed, the derived set empty**, and `_SELFTEST_EXEMPT` is `frozenset()`. **Today no rule is exempt.** (Until rev56 this sentence named `V7` and `V8` by hand; that list had been wrong since rev47 and nothing could see it — the list beside the thing it describes, again.)
2. **A rule that false-fails correct work is as expensive as one that passes wrong work** — and it is more corrosive, because it trains people to ignore the check. See **C-53**.

**Run it on the batch you are in, not on history.** Pointed at a project's whole `.dev-flow/`, it will light up on batches closed before these rules existed. That is correct behaviour and not a backlog.

## Trigger evaluation — the rigour of a batch is DECIDED, not felt

A **trigger** is a condition that is **verifiable BEFORE any code is written**, carries an **executable probe**, and turns on **named** controls. Evaluate them at intake, before deriving anything; re-evaluate families **C** and **F** at **every gate** (run over the diff, not only over the opening spec) and family **B** at **every increment cut**.

**Four rules stop this from eroding precision — they are the whole point:**

1. **Triggers ONLY RAISE.** A trigger turns controls on; none turns one off. They are a floor, never a ceiling.
2. **Full rigour ignores them upward.** When the batch runs at full rigour everything is on by definition, and no trigger may lower it. Triggers exist to raise the light lanes, never to relax the strict one.
3. **Monotonic within the batch.** Once a trigger fires it stays fired, even if scope later shrinks. Dropping a rung requires closing the batch and opening another, with its record.
4. **Non-activation is recorded too, with its executed probe.** *"Did not fire"* without evidence is indistinguishable from *"was not evaluated"* — precisely the family C-43 and C-44 document. And every trigger must be able to demonstrate its own RED (a real case that fires it) or it is inert: **C-40 applied to the triggers themselves**.

### Family B — shared surface and regression · **LIVE: evaluate all four, every increment**

| id | Condition | Probe | Turns on |
|---|---|---|---|
| **B1** | the symbol I touch is asserted by tests belonging to **another** requirement or batch | `grep -rl <symbol> tests/` → files not owned by this story | reverse census (C-26) + design review |
| **B2** | the change moves a file's location on disk | grep the read-globs over the **old** path | reader census (C-14) |
| **B3** | it touches a source a byte-identical golden captures | `grep <source> tests/goldens/**` | golden drift named in the census (C-24) |
| **B4** | it produces an artifact another component consumes | who reads the path/format this change writes | output-then-consume AT (C-12) |

### Families A · C · D · E · F — declared, not yet mechanical

- **A — structure:** creates a module or moves a boundary · touches ≥2 modules · changes an interface another module consumes · plans parallel increments. *Needs the module map to have a probe; until then, judged and said so.*
- **C — security:** the same seven pattern families `/fast-dev-flow` already scans (auth · secrets · external integration · sensitive data · destructive DB · input surface · network exposure) **plus** turning on markup/ANSI/HTML rendering over file-derived text (C-17). Re-run **over the diff at every gate**, not once at P2.
- **D — interaction:** the change alters something the user sees or touches · the prototype was built in a different technology than the target (C-16).
- **E — size and risk:** ≥3 stories or ≥3 planned increments · high risk declared at intake · client deliverable or regulated context.
- **F — flow currency:** local `flow_hash` ≠ the manifest (C-45 PULL) · backlog not refreshed since the last close.

### The record, and what a trigger is NOT

The evaluation is written into `PLAN.md` at intake and into the increment packet at each cut: **id · verdict · probe output**, for the ones that fired *and* the ones that did not.

A trigger **never substitutes judgement** — it can ask for MORE work, never less; run a review nothing triggered and record that it was your call. It **never decides the approve**: it determines which gates exist in this batch, not whether they pass. And it **never guesses** — if a condition cannot be evaluated before code is written, it is not a valid trigger: it becomes an explicit question for the design review. *"We'll find out when we implement"* is a choice, and here it is declared as one.

## Iteration cap (soft)

If any phase reaches **3 iterations**, STOP and surface it: name the root cause, then ask whether to continue, re-scope, or escalate. Do not silently loop.

## Interruption protocol (mid-increment agent death: session limit, crash)

- **Checkpoint shape:** when work must stop mid-increment, stop at a COHERENT state and record in `state.json` exactly what is done vs pending (file-level map). Prefer checkpoints where the failing test set equals the increment's specced RED — a trigger-absent/deliverable-absent failure state doubles as counterfactual evidence (valid only under the batch-24 05b conditions: the failures match the specced counterfactual, capture precedes any completing edit, failures fail for the specced reason, tree state independently audited; a live-bug RED still requires its deliberate pre-fix run).
- **Resume rule:** the resuming agent MUST re-verify the on-disk tree state before extending — never regenerate work recorded (or discovered) as done; extend it. Briefings under-credit: verify, don't trust. (Origin: batch-24 — see dev-flow-lessons)

## Session-close working-file reconciliation (C-44)

**No file the session touched may be left in limbo at its close.** Before ending a session — and again at every batch close — reconcile EVERY file created or modified into exactly one of three terminal states, and SAY which:

| State | What it requires |
|---|---|
| ✅ **Committed** | …and, where the work is only useful once integrated, **pushed with its landing path named** (PR opened / merged). **A commit that never lands is not a terminal state.** |
| 🗑️ **Reverted / deleted** | Deliberately discarded — say so, rather than leaving it to be inferred. |
| 📋 **Recorded in the backlog** | Left in place ON PURPOSE, with its path and its remaining work written into the canonical backlog so a later session can find it. |

**Run it as a mechanical sweep, never from memory:** `git status --short` in *every* repository the session touched — **including auxiliary repos outside the project tree** (a skills / commands / config repo counts); `git log <branch> --not --remotes` for commits that exist but were never pushed; and, for any branch whose work other work depends on, confirm an open PR actually exists. **Uncommitted changes that PRE-DATE the session are reported as found, not swept up** — committing another session's work in progress is its own defect, and in a shared config repo it is the likely default.

**ARTIFACT.** The reconciliation table lives in the post-mortem (`templates/postmortem-template.md` → *Working-file reconciliation*), together with the **conditional-gate discharge table**: if any gate closed as *"once items 1–N land this is a PASS/MERGE"*, each item is listed with its discharge **verified by re-reading the artifact**, never by trusting that the corrective pass ran. A conditional verdict is not an authorisation.

**Why this is a gate and not hygiene.** Work that is finished but unlanded is indistinguishable, to every later reader, from work that was never done. Worse, the canonical state files are exactly what the next session reads to orient itself, so an unlanded close-out makes the project's own state file assert something false — and the next batch inherits it as a premise (see **C-43**).

(Origin: batch-70 — see dev-flow-lessons)

## Delegation

Invoke each named agent via the Agent tool. When a phase lists agents "in parallel," dispatch them in a single message so they run concurrently. The orchestrator does not do the agents' work inline.

**The agent inventory this flow dispatches, and the ONE line each owns** — the roles are bounded here so two files cannot answer the same question differently, which is the defect `rev73` closes. **Every one of them names evidence states from §Evidence states and from nowhere else.**

| Agent | Owns | Never |
|---|---|---|
| *orchestrator* (this command) | scope, authorizations, **the ONE complete gate-suite run and its collection** (`C-25`), the decision log | — |
| `architect` | boundaries, interfaces, design decisions, ADRs | implement production code; invent a business requirement; fabricate an alternative where no decision exists |
| `software-dev` | production code and its fixes; its own tests on small changes | claim an untested change works |
| `tester` | test automation, fixtures and **oracle controls** — RED-on-base / GREEN-with-fix evidence, wide matrices, E2E acceptance | approve anything; alter production to force a pass; become mandatory on a trivial change |
| `qa-reviewer` | acceptance **defined early**, and the verdict per requirement over **traceable results, with WHO executed them named** | claim personal execution of the suite; substitute a code read for an absent run |
| `code-reviewer` | the independent diff review, test quality included | approve its own corrections; close a HIGH with a *recommended* fix |
| `security-reviewer` | security risk and **verification of the mitigation** | close a HIGH with a *recommended* mitigation; replace the operator's authorization |
| `ux-reviewer` | observable interaction, the walkthrough and **its declared limits** | read a DOM and call it a painted result |
| `docs-writer` | documenting **verified** behaviour | introduce a product decision the batch never took |
| `presentation-builder` | the executive summary for a non-technical stakeholder (§Phase 6) | present a `planned` outcome as an achieved one |

**When `tester` is required, stated once so neither flow has to guess.** In `full` and `core`: whenever an **independent author** of the evidence is required — an **escaped regression** (the RED-on-base capture is the deliverable), a **wide matrix** (an input/output space bigger than the increment that owns it), an **end-to-end acceptance** node realizing one `AT-NNN` through the shipped surface, or an **oracle control** — a standing suspicion that a check is vacuous (an assertion that cannot fail, a fixture that no longer resembles production, a golden captured by its own author, a mutation that survives). **Four triggers, named in the SAME FOUR TERMS `agents/tester.md` §*When you are invoked* defines** — the agent defines the role, so its vocabulary is the vocabulary, and `REV TESTER-role-bounded` reads one list against the other. rev73's first cut named three here and four there, one paragraph under the sentence claiming this is stated once; its second named four in different words, which is the same defect one level quieter — two lists nothing could compare. Everywhere else `software-dev` writes its own tests and **no delegation is owed**; `fast` keeps the assignment light (see `/fast-dev-flow` §Phase B). **`tester` is an AUTHOR, never an approver:** it produces evidence, `qa-reviewer` judges it against acceptance, and `V36` records both names — *a different name does not prove independence; recording who produced and who reviewed each piece of evidence is what does.*

**C-33 — critical-path sub-agent liveness (never wait passively on a delegated gate).** When the orchestrator dispatches a sub-agent whose result GATES the next step (a review, a required implementation increment, a validation run), it MUST actively confirm the agent is alive rather than rely on a completion-notification alone — a hung agent never notifies, so a completion-only wait can stall indefinitely without surfacing. Discharge: after dispatch, either run the agent to completion with an active blocking wait (`TaskOutput block=true`, re-polling on timeout) OR poll a genuine progress signal (touched-file mtime for an implementer; `TaskOutput` status) on a bounded cadence, and STOP + take over (review/implement inline, or re-dispatch) once liveness cannot be confirmed. **A transcript-byte-size monitor is NOT a valid liveness signal when sub-agent transcript files do not grow** (e.g. they stay 0 bytes and results arrive only via the completion event) — verify the signal actually moves before trusting it. (Origin: batch-49 — see dev-flow-lessons)

## Phase map

### Phase 0 — Story intake & refinement (INVEST + Definition of Ready)
- **Input:** raw user stories (in `.dev-flow/<batch_id>/01-requirements.md` §2.6, or pasted by the user) **AND the project's canonical cross-batch backlog** — the file, or lane files, that the project's `docs/engineering-rules.md` designates; absent such a designation, `.dev-flow/BACKLOG.md`. It is the standing source of candidate stories + open carries. **Resolve the routing FIRST, then read the file it names.** A project that has partitioned its queue into lanes keeps **no open work** in the original file, so reading that file alone returns an empty queue that is indistinguishable from "nothing pending". Read it before deriving anything; it is reconciled at every batch close (Phase 6) so it should reflect true current state.
- **Base-currency gate (RC-1) — run BEFORE scaffolding a new batch or deriving anything:** `git fetch origin`; assert the working branch's merge-base equals the `origin/main` tip — if not, **rebase onto it first** (never derive requirements against a stale tree). Then for EACH candidate story run an *already-shipped* check: grep `origin/main` (REQUIREMENTS.md / the acceptance surface / the requirement id) for the story's outcome; a hit ⇒ reclassify `SATISFIED-EXTERNALLY` and drop it from scope HERE (Phase 0), not at Phase 3. Record the verified `origin/main` tip in PLAN.md *before* derivation. (Origin: batch-14 — see dev-flow-lessons)
- **Driver:** the orchestrator converses directly with the user (the "Conversation" of the 3 Cs). Consult `architect` ONLY for a feasibility judgment when the implementation path is unclear.
- **For each story, evaluate INVEST and drive a short Q&A to close gaps on three axes:**
  - **Functionality (Valuable, Negotiable):** who is the user · what outcome · why it matters · what is explicitly out of scope.
  - **Feasibility (Estimable, Small):** known implementation path? · dependencies/unknowns? · fits one batch or needs spike/split? (consult `architect` if unclear).
  - **Evaluability (Testable) — behavioral, black-box:** a story states a user-verified OBSERVABLE BEHAVIOR (the WHAT), not a mechanism (a story reading like an implementation spec is mis-captured → REFINE). NOT ready unless its outcome is observable through the real shipped surface AND ≥1 black-box acceptance criterion is stated at the behavior level ("When `<input>`, the user observes `<outcome through the surface>`" → becomes an `AT-NNN` in Phase 1).
  - Also note **Independent** for later implementation ordering.
- **Classify each story:** `READY` / `REFINE` (open questions) / `SPIKE` (feasibility unknown — needs an exploratory spike first) / `OUT` (deferred or rejected, with reason).
- **Artifact:** the §2.6 refinement block in `.dev-flow/<batch_id>/01-requirements.md`, updated. **The batch's OWN `01-requirements.md` AND `01-requirements-ledger.md` are created AT BATCH OPEN, in the same commit as its `state.json`** — a declared batch with no copy of its own is judged on whichever historical document the validator's `_artifacts()` walk reaches first (Origin: batch-86 — see dev-flow-lessons).
- **Gate (Definition of Ready):** present per-story status + open questions. Only `READY` stories pass to Phase 1. `REFINE`/`SPIKE`/`OUT` are listed with reason + next action. User approves which proceed. Gate per §Objective exit criteria.

### ARQ — Architecture & module map *(station, trigger-activated: fires on A1 / A2 / A3 / A4)*
- **When:** after intake, **BEFORE deriving requirements** — the module split *defines* the section and sub-section split of the requirements document, and everything derived from it.
- **Input:** the `READY` stories + the standing `docs/ARCHITECTURE.md`.
- **Agent:** `architect`. The operator approves the map **before anything is derived from it**.
- **Activity:** update the map — what each module encapsulates, where its boundaries are, what it **exposes**, what does **not** belong to it, which modules it depends on, and which ones this batch touches. Plus a `rationale` per structural decision (IEEE 1016 requires it, and it is what stops the decision being re-litigated every batch).
- **Artifact:** `docs/ARCHITECTURE.md` — **repo**, versioned beside the code, because it is the oracle the A-family triggers read.
- **Distilled from IEEE 1016, by one selection rule: a viewpoint enters the map only if it FEEDS A TRIGGER.** In: **Composition** (A1/A2 + the source-file budget) · **Dependency** (A3 + the parallelisation rule) · **Interface** (A3 + C-12) · **Context** (the whole security family). Out — they belong to the design proposal, and only when they apply: Logical, Information, Patterns, Structure, Interaction, State Dynamics, Algorithm, Resource.
- **What makes it an oracle instead of prose:** the map declares **paths**, so it is checkable against the real tree. A touched file that falls under **no** declared module means the map is stale, and ARQ fires on its own.
- **A no-op is declared, never silent:** a batch that moves no boundary states *"no architecture change"* **with its evidence** — the empty diff of the map.
- **Parallelisation rule (mechanical, not an opinion).** Two increments are parallelisable when `modules(A) ∩ modules(B) = {}`, **or** when they touch the same domain on **different layers** (UI/UX vs functional) *and* the interface between those layers is frozen at PDR and neither lane touches it. If the intersection is not empty there are exactly two exits, both explicit: **re-cut the increments**, or **move the module boundary here in ARQ** — and the second is the one that prevents spaghetti. This orders the *code*; the order of *merit* still comes from the intake risk estimate.
- **Gate:** approve the map, or `iterate` with the named gap.

### Phase 1 — Requirements engineering
- **Input:** the `READY` user stories from Phase 0 (in `.dev-flow/<batch_id>/01-requirements.md` §2.6). Do not derive from stories still in `REFINE`/`SPIKE`/`OUT`.
- **Agents (in parallel):**
  - `architect`: derives HLR from user stories applying ISO/IEC/IEEE 29148 + EARS.
  - `qa-reviewer`: defines validation method per requirement (test/demo/inspection/analysis).
- **Strict normative convention:** `shall`/`deberá` only inside HLR/LLR statements. `should`/`debería` only in informative text. Any modal `should`/`debería` inside an HLR/LLR statement is a writing error and you must flag it.
- **Traceability:** every HLR must trace to a US. Every LLR to a parent HLR.
- **Acceptance (black-box) block per story (the WHAT):** for each story, add a first-class Acceptance block in §3 (independent of the LLR decomposition): the observable outcome · the shipped surface that produces it · the `AT-NNN` acceptance test(s). Every OUTPUT-PRODUCING requirement MUST name its concrete deliverable and how it is observed (file at path + non-empty + required content; or rendered screen element). A requirement missing its acceptance block or observable-deliverable naming is incomplete. (req-template §3 Acceptance block + `AT-NNN` convention; dual traceability is DERIVED from the `Traceability` and `Acceptance test(s)` fields by `V10`/`V21` and published at `.dev-flow/_derived/ATLAS-TRACE.md` — the `§5.2` that used to hold transcribed tables was retired 2026-08-28 and its heading deleted at flow rev69.)
- **Draft-time verification (the dominant lesson across batches 05-11):** every spec claim that names a code symbol, data artifact, environmental constant, or executable check is EITHER verified against disk/execution at draft time (cite `file:line` / probe result / measured regime) OR flagged `assumed — verify in Phase N`. A claim that is neither verified nor flagged is a Phase-2 blocker. The `req-template` encodes the specific rules; enforce them at the gate.
- **Symbol-identity + sweep-back check (C-15) — verifying an API's behavior does not verify the spec's BINDING to it:** (a) when a spec names a framework CONSTANT / SENTINEL / dotted symbol as a value the code will compare against, draft-time verification MUST probe the symbol's runtime IDENTITY (`repr()` / `type()` of the exact dotted name), not just confirm behavior claims about the API — existence/`hasattr` is insufficient (inherited attributes satisfy it while denoting the wrong object). (b) When a review fold corrects a framework fact (name, semantics, version pin), grep ALL batch artifacts for the superseded symbol/claim and sweep the correction through — a fold that fixes one section while sibling sections still carry the stale name plants the bug in Phase 3. (Origin: batch-23 — see dev-flow-lessons)
- **Writer-census probe (C-15.1) — a data-flow claim is verified at the state's WRITERS, not at the caller:** when a draft-time probe establishes a claim of the form "state X is installed/retained/fresh at time T" (an attribute, a cache, a report list), the probe MUST grep for X's writers (e.g. `rg "_state_name\s*="`) and read EACH writer's branches — stopping at the function the spec edits, or at the first caller, is insufficient. The grep form is mechanical: list the assignment sites, read the guard around each. (Origin: batch-24 — see dev-flow-lessons)
- **Draft-time EXECUTION probe (C-35) — run the transform over the real input; reading the code and the input separately misses their INTERACTION:** when a requirement's acceptance asserts that a *specific real input* produces *specific parsed/derived output* through a transform (a parser, extractor, enrichment, or pipeline), the Phase-1/2 draft-time verification MUST **execute the transform over that actual input** and confirm the named fields/outputs exist — NOT merely read the transform's code and eyeball the input file. Reading both in isolation certifies each in isolation while missing the *interaction* that decides the outcome. EXTENDS the batches-05-11 draft-time-verification rule (from "cite the artifact exists" to "run the producer over it") and the C-15 / C-15.1 family (from "probe the symbol's identity / the state's writers" to "run the whole producer end-to-end over the real fixture"). A spec that names a concrete input as its acceptance surface without an executed probe of the produced output is a Phase-2 blocker. **Rider — executing the producer is not enough if the predicate is then written against the RENDERED form:** the run MUST end with the producer's **actual emitted output pasted into the artifact**, and the predicate written against that paste — never against a character list, the human-readable rendering, or the spec's own vocabulary for the thing. Producers escape, encode, wrap and substitute, so confirming that a named output *exists* passes while the predicate that searches for its readable form **false-fails a CORRECT implementation**; prefer a predicate over the producer's own structured output (its parser's token stream, a language-aware parse of the source) to a substring search over serialized text, because a substring search cannot tell a value from its own encoding. **The failure is quiet and symmetric, and that is what makes it expensive:** it returns a *plausible* number, so a predicate that under-counts by two orders of magnitude reads as a measurement rather than as a bug — and when a probe instead returns an **impossible** value (zero matches for something plainly present, a negative index for something that exists), that is luck, not detection. **Three spellings, each of which looks like careful work:** a `startswith`/prefix guard over a formatted line — widths, separators and padding are the producer's choice, not the predicate author's; a hand-listed character class standing in for *"this field is inert"*; and a predicate written from the requirement's wording instead of from the output. **Also EXTENDS C-36** — which reconciles an acceptance literal to a constant DEFINED on disk — from the *source-side definition* to the *output-side encoding of that same constant*: a literal can satisfy C-36 in full, being a defined constant, and still be unfindable in the emitted output, so C-36 and this rider fail independently. Stack-specific emitted-form traps belong in the project's `docs/engineering-rules.md`, never here. (Measured: a report heading emitted as `` #### Checklist: `chk.json` `` is unfindable by its bare form — the probe returned an impossible `-1`, which is the only reason it was caught; `.dev-flow/2026-07-26-batch-63/00-measurements.md:96-98`. Same family, enumerated (never totalled — three registers disagree, and the enumeration itself has been re-drawn) across batches 60–63 in `.dev-flow/2026-07-27-batch-64/01b-qa-catalog.md` §AT-B64-04 — cite the enumeration, never a total: three registers disagree.) (Origin: batches 60-64 — see dev-flow-lessons)
- **Fold-against-defined-vocabulary (C-36) — an acceptance VALUE is verified against the model's DEFINED constant set, not a reviewer's prose shorthand:** when an `AT`/`LLR` acceptance is authored or **folded from a review finding** and names a concrete VALUE the code will produce or compare against — a status token, an enum member, a gating/mode string, a sentinel — that literal MUST reconcile to a constant actually DEFINED on disk (grep the enum/constant module) or be flagged `NEW — created in Phase 3`; an acceptance literal that matches no defined constant is a **phantom** that false-fails a CORRECT implementation, and is a **Phase-2 blocker** (mechanically greppable: every quoted value in an AT/LLR acceptance resolves to a defined constant or a spec'd NEW token). EXTENDS **C-15** (symbol IDENTITY) from dotted-symbol *objects* to enum/status/mode *values*, and the batches-05-11 symbol-citation rule from "the symbol exists" to "the value is a member of the defined set." **Rider — tabulate any matrix an AT keys on:** when an acceptance drives a multi-axis decision, the governing LLR MUST ship an explicit truth table (each cell's result), not prose — prose is where a phantom value hides. (Origin: batch-51 — see dev-flow-lessons)
- **Pre-execute every executable threshold (C-39) — a threshold that CAN be computed before the implementation exists MUST be, and its transcript recorded, before it is promoted to an acceptance criterion:** when an `AT`/`LLR`/gate names a concrete THRESHOLD about the change itself — a golden's drifting-line set, a blast radius ("N tests re-baseline", "the goldens move"), a file count, a cap's boundary, a count of affected sites — that number MUST be produced by an **executed** derivation over the CURRENT tree and pasted into the artifact, never predicted and never inherited from a reviewer's prose. Almost all such thresholds are computable pre-implementation (apply the transform to every value in the golden and diff; patch the helper and run the affected suite; grep the symbol), so "we'll find out in Phase 3" is a choice, not a constraint. **The failure is symmetric and that is the point: a predicted threshold false-fails a CORRECT implementation just as readily as it passes a wrong one** — so the discharge is not "be careful", it is *run it and paste the output*. Distinct from C-35 (which executes the PRODUCT's transform over a real input) and from C-31 (which derives a test's INPUT SET): C-39 governs the numbers the gate itself is keyed on. **Rider — re-measure the fold's OWN new thresholds, not only the inherited ones:** a refinement iteration that re-measures what the review disputed while asserting fresh numbers from reasoning simply relocates the defect. (Origin: batch-62 — see dev-flow-lessons)
- **Falsifiability-before-correctness (C-40) — "can this predicate go RED?" is a SEPARATE gate question from "is this predicate correct?", and it is answered at AUTHORING time, by EXECUTION:** every acceptance-bearing predicate — a black-box `AT`, an `LLR` acceptance clause, a `TC`, **and any measurement probe whose number a gate is keyed on** — MUST, in the artifact that introduces it, satisfy BOTH limbs and record the executed transcript for each. **LIMB 1 — the declared subject must be IN the expression.** Name the subject *the predicate itself declares* it certifies, then confirm that subject appears in the predicate's own expression; a predicate whose value is **invariant under the change it gates** cannot gate it, however exact its arithmetic — **see the corollary below before applying that sentence on its own.** **When the syntactic test (is the subject in the expression?) and the semantic test (does the predicate's value move?) DISAGREE, the semantic one governs, and its domain includes the platform** — a predicate whose subject is plainly in its expression can still be invariant on the host the merge gate runs on, which makes it inert exactly where it is relied upon. **The static half is free: read the expression and ask which symbol in it the implementation could move.** A predicate relating two pure functions of the same input certifies arithmetic, not the implementation. **Corollary, and it is the useful half:** when the declared subject is NOT the subject of the change being gated, the predicate is a **regression PIN, not a gate** — keep it and **label it so**; do not delete it and do not let it stand as the gate. **LIMB 2 — the set must come from the RULE, not from the implementation.** If the predicate quantifies over a set, that set MUST be drawn from the rule the predicate states, never from the implementation it certifies; a set derived from what the code currently handles makes the check a tautology that certifies a completeness the code does not have. **Two named instances:** *(i)* **a positive control shaped to the implementation** — deriving a detector's cases from the cases the detector already catches; shape them from the rule's own statement and establish each case's status independently of the detector. *(ii)* **a consolidation that drops observables** — when N artifacts merge, the **union of their observables** is the subject, so the merge MUST carry every observable forward or print an explicit retirement line naming what was dropped and why; an id-range table is a container, not evidence of preservation, and a green traceability count over the survivors cannot see the casualties. **DISCHARGE for both limbs:** name the mutation that reddens the predicate, **execute it, and paste the transcript**, including confirmation that the mutation actually applied (a typo'd mutation also "fails", for the wrong reason). Run the mutation where **no other session is reading** — your own increment tree or a `git archive`/worktree export, never a tree a concurrent review or a parallel batch is measuring — and **RESTORE it before the next gate**, confirming the restore in the same transcript **by the file's hash returning to its pre-mutation value** — `git status` alone is insufficient and is outright **vacuous for an untracked file**, which it reports identically whether or not the mutation was reverted. A mutation left applied contaminates every later measurement in that tree and is indistinguishable, to anyone else reading it, from a real defect. A predicate that stays GREEN under a mutation of what it claims to certify is **inert: rewrite it, do not re-argue it.** **Rider — the verdict is PER RESOLVED ARM, never the process exit code.** A test runner exits non-zero if ANY node fails, so a matrix that derives one verdict per mutant over a node set containing *parametrized* tests cannot express the thing a counterfactual is for: **which arms the mutation reddens.** An inert arm hides behind a sibling that failed, and the string `3 passed` sits unread in the transcript. Record one verdict per resolved node id and NAME the arms that stayed green. **Two failure modes of the harness itself, both of which reported a falsehood and both found only by running it:** a baseline that resolves ZERO arms (verbose and quiet flags cancelling) makes an all-green assertion compare `0 == 0` and pass — a vacuity detector, vacuous; and a whitespace-delimited node pattern silently drops every parametrized arm, reporting a live mutation as INERT. Assert the expected arm COUNT before trusting any verdict: **an arm the harness cannot see is an arm it cannot report inert.** **The DISCHARGE is declared in the increment packet's `**RED counterfactual**` field, which `V44` reads from flow rev68** — the ONE mutation that made this increment's own new assertion fail, where its transcript is stored, and the restore digest — and it is a row of its own rather than a limb of `V37`'s `**Mutation verdicts**` because the fold is the OBSERVED failure, not the remedy: of the 14 packets carrying the row, the **2** whose gate row still carried the words *and restored by hash* both named a restore digest and their mutation row named arms — no overlap — while the **12** that had lost those words named no digest at all and ten wrote a mutant tally instead, so **the restore half vanished from all twelve**. (Origin: batches 76/84 — see dev-flow-lessons)

- **Assert the EMITTED form, never the rendered one (C-42) — and it is the companion obligation to the one above, not a footnote to it:** executing the producer is **not enough** if the assertion is then written against the form a *human reads*. Producers escape, encode, wrap and substitute, so confirming a named output *exists* passes while a search for its readable form **false-fails a correct implementation** — a snapshot emitting `&#160;` returns **0** matches for a label plainly on screen and **29/29** for the emitted one, and a byte bound written against character arithmetic was wrong by up to **2.03×**. **Per artifact the increment emits, run the producer, paste what it actually emitted, and assert against THAT**, preferring the producer's own structured output to a substring search over serialized text: a substring search cannot tell a value from its own encoding. Declared in the increment packet's `**Emitted-form assertion**` field, which `V38` reads. (Origin: batches 60–63, fired at 75 and 77 — see dev-flow-lessons)

**DISTINCT from C-10** (mutates the CODE at the AT surface), **C-31** (mutates the INPUT SET) and **C-39** (executes the THRESHOLD the gate is keyed on) — a predicate can satisfy all three, be arithmetically exact, quantify over a derived complete set, carry a measured number, **and still be invariant under the change it gates**. **NOT orthogonal to C-35**, and say so honestly: running the producer over a real input *does* catch the round-trip-identity form of this defect; C-40's contribution over C-35 is that it applies where there is no product transform to run — a spec-layer algebraic predicate, a consolidation table, a hand-shaped case list. EXTENDS the §Objective-exit-criteria *Certainty* clause ("the counterfactual shown — the AT RED on the pre-fix tree") on three axes: from a **gate-exit** obligation to a **per-predicate authoring-time** one; from `AT-NNN` alone to **every acceptance-bearing predicate**, including `LLR` clauses, `TC`s and probes; and from "shown" to "**executed, with the transcript pasted**". (Origin: batch-63 — see dev-flow-lessons)
- **Project-specific UI-geometry gates** (C-13 reuse-transfer / C-13.1 fallback-ladder / C-23 driver-measure) live in the project's `docs/engineering-rules.md` — consult it at Phase 1 for any batch touching layout/sizing/geometry.
- **Prototype-fidelity check (C-16) — a cross-tech prototype's INTERACTIONS are UNVERIFIED for the target framework:** when a story's promise (esp. keyboard/pointer interaction, focus traversal, animation, layout behavior) is demonstrated in a throwaway prototype built in a DIFFERENT tech than the shipping target (an HTML/JS mock for a the UI framework/native the terminal UI, a Figma flow for a real widget), the requirement MUST flag that interaction `assumed — verify in target framework at Phase 3` — the prototype proves DESIGN INTENT, not implementability-for-free in the target — AND the black-box `AT-NNN` MUST exercise the REAL mechanism (press the actual arrow keys / drive the real pointer path), never a proxy that bypasses it (`.focus()` in place of arrow-nav, a direct setter in place of the gesture). Interaction-layer sibling of C-13 (geometry) and C-15 (runtime identity). (Origin: batch-27 — see dev-flow-lessons)
- **Untrusted-render-mode markup-safety (C-17) — a controlled-data prototype hides untrusted-input surfaces:** when an increment flips ANY render mode to interpret markup / ANSI / HTML / a template over strings that ORIGINATE in loaded or untrusted files (`markup=False→True`, enabling a template engine, rendering file-derived names/messages/symbols with styling), a markup-safety LLR (render via explicit-style `Text` construction or escape; never interpolate raw file text into a markup-parsed string) + a hostile-input `AT` (a bracket / ANSI / link payload rendered literally — no parse error, no style leak) is MANDATORY AT PHASE 1, not left to a Phase-2 catch — because the approving prototype rendered CONTROLLED sample data and structurally cannot reveal the injection sink. Do NOT trust an existing sanitizer without verifying it covers the NEW threat (an ANSI/control-char scrubber does not escape markup brackets and may not touch every file-derived field; it may be engine-frozen and thus not the fix site). (Origin: batch-27 — see dev-flow-lessons)
- **Information Flow Contract (C-54) — a requirement declares the VALUE a surface carries; it must also declare the ADDRESS by which consumers reach it:** every batch authors **Part A (Flow)** — `SOURCE → NODES → SINK`, each node naming the `owner` LLR that asked for it — because information flows always exist, whatever the stack; a node nobody owns is work no requirement asked for, and an LLR claiming a transform with no node is unimplemented. **Part B (boundary decomposition) is conditional on ONE deliberately stack-free question: does the system's boundary have components a consumer can address independently?** A the terminal UI with panels, a sensor array, a DAQ card with per-channel calibration: yes. A headless library with one entry point, a CLI emitting one report: no — those owe Part A and nothing else. When yes, each component declares `PARENT`, `INPUTS ⊆ PARENT.INPUTS` (*balancing* — the DFD/Structured-Analysis name, 45 years old; do not invent another), and per output an `address`, a `cardinality` when the address selects a set, an explicit `consumers` list, and an `owner`. **`consumers : none` is legal and MUST be written: an omitted field is a question nobody asked, and the validator treats the two differently.** Consumers are PATHS, optionally `::symbol` — trace to acceptance ids through the traceability matrix, which is the artifact that exists for it. **A dependant is not only something that reads the value; it is anything that would break if the address moved** — a stylesheet reads nothing and still breaks when the class is renamed, so it is a consumer. That sentence is the SCOPE of the field, it is what `V13` and `V14` parse `consumers` against, and it is normative: it stays here whatever happens to the story it was learned from. **Write `INDEXED POSITIONALLY` beside any `cardinality` whose consumers index the set:** cardinality alone does not catch a REORDER — the count holds, set equality holds, and a positional consumer breaks anyway. **Mechanised, each demonstrating RED in `--selftest`:** `V10` (every node owned by a requirement that exists), `V11` (every output declares address AND consumers), `V12` (balancing, reporting *could not be tested* separately from *holds* — the parent may not be declared here, or a list may be prose, and containment is a set operation with no members in free text), `V13` (**NOTICE** — greps each quoted literal `address` and names every file that reaches it and is not declared), `V14` (every declared consumer resolves to a file, and its `::symbol` is in it), `V21` (rev44 — every OUTPUT owned by a requirement that exists: V10's law over Part B, which had escaped it for one measured driver). Beside them, two NOTICE censuses serve the living-canon model (D-VII): `V22` (the living canon mirrors the batch record — unowned-LLR questions, the unreflected-id backlog aggregated, bare citations of retired test ids) and `V23` (every `PDR`/`DDR` citation parses under the id glue's grammar `PDR-<batch>#D<n>` — the vault side is deliberately out of reach). **`V13` is NOTICE by design so a retrofit across existing surfaces cannot gate unrelated work**; a project escalates it per surface as that surface's contract is written, and records that in its own `docs/engineering-rules.md` — as it records the taxonomy of COMPUTED-address sites, which no grep can follow and which is stack vocabulary, never flow. **And grep cannot tell a dependant from a mention**, so `V13` reports what reaches the literal and a human decides; that ambiguity is the price of being stack-free, and it is cheaper than a rule that must understand every stack's addressing. (Origin: batch-79 — see dev-flow-lessons)
- **Artifact:** TWO documents, created together (following `templates/req-template.md`): `.dev-flow/<batch_id>/01-requirements.md`, the **live contract**, holding current state only — no strikethrough, no amendment bullets, no measurement inside a normative sentence — and `.dev-flow/<batch_id>/01-requirements-ledger.md`, the **append-only ledger**, which is never edited and holds the reason each requirement says what it says. Every requirement declares a `**Ledger:**` field, every entry declares a `**Requirement:**` field, and `V26` compares the two sets of pairs BOTH WAYS. The live contract carries the Information Flow Contract per `templates/ifc-template.md` — Part A always, Part B when the trigger question is yes.
- **Gate:** present summary — total US, HLR, LLR, critical assumptions, gaps detected. Gate per §Objective exit criteria.

### Phase 2 — Cross-agent review
- **Input:** `.dev-flow/<batch_id>/01-requirements.md` approved in phase 1.
- **Agents (in parallel):**
  - `architect`: completeness, ambiguity, contradictions, correct US→HLR→LLR derivation.
  - `qa-reviewer`: testability of each requirement, viability of the chosen validation method.
  - `security-reviewer`: requirements with attack surface, sensitive data, auth/authorization.
- **Findings:** classified as `blocker` / `major` / `minor`. Verify `shall`/`should` usage — misuse is a blocker.
- **Two-layer review (blockers):** (a) every story has a black-box `AT`; (b) every output-producing requirement names its observable deliverable + observation method; (c) BOTH traceability chains are complete (behavioral + functional); (d) acceptance tests are genuinely black-box — drive the surface, assert the outcome, reference NO internal symbol.
- **Supersession census = principle, not a fixed grep list:** run it change-first against the batch's planned new/moved/edited files, keyed on the CATEGORY of assertion (file path / module structure / import graph / git-diff), not specific patterns. Never stamp a census "VERIFIED COMPLETE" — re-running an incomplete checklist cannot detect its own gaps. Use "best-effort + gate-confirmed"; the increment gate is the completeness guarantee.
- **Location-move census sweep (C-14):** when a story changes a file's **on-disk location** (not just its contents), the supersession census MUST additionally sweep the **e2e / save-observing** tests — any test that reads the artifact back from disk — not only the white-box placement tests. Grep the save-path globs (`glob`/`rglob` over the workarea / output dir) and confirm each observer survives or is updated; count a rewritten-in-place (net-0) test as a touched node. (Origin: batch-21 — see dev-flow-lessons)
- **Report-golden census membership (C-24) — extends the writer-census family (C-14 / C-15.1):** when a batch changes any SOURCE that a byte-identity report/output golden captures (a legend table, a section template, a report-line formatter, a header), the supersession census MUST include the byte-identity goldens among the observers to sweep — grep the golden directory (`tests/goldens/**`) and reason about whether the changed source flows into each golden's captured bytes. A source whose output reaches a golden legitimately drifts it; NAMING that drift in the census (and rebaselining surgically, double-proven per the golden control) is expected — MISSING it means the drift surfaces as a surprise failing golden mid-increment. (Origin: batch-36 — see dev-flow-lessons)
- **Touched-symbol reverse census (C-26) — generalizes C-14 and C-24:** forward traceability (every requirement → a test, 0 orphans) can be FULLY INTACT while impact analysis still misses a regression — because impact analysis is keyed FORWARD by requirement ("does my new LLR have a test?") and NOT REVERSE by symbol ("which EXISTING tests, from ANY requirement or batch, assert against the symbol my LLR touches?"). Therefore: every LLR that changes a code symbol or shared surface (a widget / container id, a CSS class, a file path, a constant, an enum value, an output format) MUST declare the touched symbol(s) in the LLR; and the Phase-2 / Phase-3 supersession census MUST then REVERSE-GREP each declared symbol across the ENTIRE `tests/` tree (`grep -rl <symbol> tests/`) and re-validate EVERY assertion it finds — independent of which requirement or batch owns that test. **C-14** (moved-file e2e/save-observers) and **C-24** (report byte-identity goldens) are NARROW named instances of this one rule; C-26 is its general form. **Declared in the increment packet's `**Reverse census**` field, which `V43` reads from flow rev68** — the five probes with their commands and verdicts, and the ones that did NOT fire named with their probe (C-48), or the declared empty. Measured 2026-09-10, case-sensitively because the reader is: the keyed ROW is absent from **246 of 246** increment packets and the section the template mints appears in **2**, none of them in the active batch — which is what a mandate with no reader costs. **The rule is keyed on the FIELD and never on the checklist row number** — the same obligation sits at row 4 in nine packets and at row 3 in five, across checklists shipped at four different lengths. (Origin: batch-37 — see dev-flow-lessons)
- **Scope-change re-routing:** if a requirement change after this phase closes adds a new external-write/output surface, explicitly re-invoke `security-reviewer` — do not rely on author self-routing.
- **Artifact:** `.dev-flow/<batch_id>/02-review.md`.
- **Gate:** if blockers exist, force **`iterate-to-refine`** back to phase 1. Otherwise, user decides. Gate per §Objective exit criteria.
- **ONE RETURN EDGE AT THIS STATION, AND THE OTHER CLASSES ARE ROUTED RATHER THAN SWALLOWED (flow rev72, `T07`).** This station's input is the approved `01-requirements.md`, so a **requirement defect is the only defect it can send anywhere** and `iterate-to-refine` is the only token it mints. An **implementation** finding — an existing symbol, test or surface the approved requirements oblige to change — is **carried into Phase 3 as a named finding with its owning increment**, never as a gate token: **`iterate-to-fix` is Phase 4's token** (§Phase 4 feedback edges), because Phase 4 is the only station that observes the implementation. A **security** finding on an existing surface re-invokes `security-reviewer` per §Scope-change re-routing. Anything outside those three is NAMED in the review's findings table with the station that owns it — `review-template.md` §Verdict carries the same table, and until rev72 it carried the contradiction instead: one arrow to Phase 1 labelled with both classifications.

### PDR — Preliminary Design Review *(gate, trigger-activated; fires with ARQ)*
- **When:** **after the Phase-2 cross-agent review approves the requirements, and before the first increment.** The blocking rule is the one below — *no increment starts without an approved PDR* — not a position in a list. **A batch may seal more than once, and then there is one record per seal:** batch-88 held two. What is forbidden is an increment running ahead of an approved record, never a second review.
- **Input:** the design proposal — `templates/design-proposal-template.md` — authored **between P2 and the PDR, from the Phase-2-reviewed requirements**: the approved `01-requirements.md` is the document it is written against.
- **Agents:** `architect` + `qa-reviewer` (+ `ux-reviewer` when family D fired). The tester's lens is not optional here: the proposed test cases are half of what is under review.
- **THE FORWARD-APPLICABILITY RULE — distilled from ISO/IEC/IEEE 15288.** 15288 separates *Architecture Definition* from *Design Definition*, whose outputs are the **design characteristics and design enablers necessary for implementation**, traceable to the architecture. Therefore: **everything the PDR produces must be NAMED as the input of a later activity; if an artifact of the PDR is nobody's input, it does not belong in the PDR.** This is what lets the PDR legitimately cost half the batch without being waste — that half *is* the literal input of the other half. And when it is not, this rule detects it.
- **The four outputs, each with its declared consumer:**

  | The PDR produces | Consumed by |
  |---|---|
  | design characteristics — what gets built, with which properties | the Phase-3 increments |
  | enablers — fixtures, test data, scaffolding, environment | Phase 3 and validation |
  | the **proposed test cases** | layers 0 / A / B, and the DDR |
  | design → requirement traceability | the matrix and the DDR |

- **Also reviewed:** does the design respect the ARQ boundaries · does every requirement have foreseen coverage · are the proposed test cases observable and **non-vacuous** (the mutation that would turn each RED is declared here, at authoring time) · which controls of the gauntlet apply and who pays for them · which interfaces are **FROZEN** for a fork.
- **Verdict:** `approved` / `approved with conditions` (listed, each individually dischargeable) / `rejected`. A rejection returns to **design**, not to implementation.
- **Blocks:** no increment starts without an approved PDR.
- **Re-opening:** an increment re-opens the PDR only when it changes a **design characteristic or an interface** — which is exactly trigger **A3**, and what 15288 would call touching the *definition* rather than the *realisation*.
- **Artifact home: the vault + Drive** (`artifact_homes.design_pdr`), sealed (date · verdict · participants · the ids approved) and **cited by id from the repo**. If it changes after the seal it is a new version with a new id — never a silent edit. **`/dev-flow` never writes the vault** (§Artifact homes, `Q22`). It writes the record to LOCAL STAGING under `.dev-flow/<batch_id>/`, and `/dev-flow-sync` publishes that staged file to the home above. The canonical copy is the vault one; the staged file is the input to the publishing act.

### Phase 3 — Implementation
- **Input:** approved requirements + review.
- **Agent:** `software-dev` (`agents/software-dev.md`), under this budget. **Precedence, declared rather than left to the reader:** inside a `/dev-flow` or `/fast-dev-flow` batch THIS budget governs; outside a batch, your runtime's own standing development rule does — and every document this flow ships states the SAME variable, SOURCE files, so the author is never handed two numbers. **Until rev85 both halves of that sentence named an operator-private skill that does not ship with this flow**, so a reader holding the publication alone was sent to a document they could not open; the flow is self-contained, and the budget is its own. Until rev67 the skill and the `software-dev` agent definition both said a flat "max 5 files" as a TOTAL and told the author to split above it, which is the variable `C-47` retired on 2026-08-10 and which `V9` has never counted. ⚠ **ONE member of this axis is outstanding and is named rather than absorbed:** the operator's own standing-instruction file on the authoring machine — a file this publication does not ship and does not name, because a reader holding the bundle has no such file to open — still states the retired flat total in its working-method section. It is the operator's instruction file and not flow surface, so no flow revision edits it; `CMD BUDGET-one-variable` carries it as **the single DECLARED exclusion**, and a SECOND violator reddens rather than joining it silently. ⚠ **`rev73` RETIRED the other two exclusions rather than defending them** (the docs-writing and marketing role definitions, declared *a different axis* at `rev67`; one of the two is outside the published set and is therefore named by role here rather than by a path a reader of this bundle cannot open): the objection recorded against that resolution was right that an exclusion-by-equality defers a question instead of answering it, and the answer turned out to be that **no exception was ever needed** — the cap binds SOURCE files, so an agent that writes no source is capped at zero of them and its deliverables are uncapped **by the rule itself**. Both files now state the one variable and the precedence clause; **seven documents carry it**, not four.
- **Hard constraints — the file budget counts SOURCE files only (measured 2026-08-10, replaces the flat "≤5 files"):**
  - **≤4 SOURCE files per increment.** Tests are **not capped**. Product docs and every `.dev-flow/**` artifact are outside the count.
  - **⚠ Warning at exactly 4 source files** — reaching the cap is not a violation, but §2 of the packet must state *why the increment could not be cut smaller*. Warnings are written in yellow with a `⚠` sign and **never block**; see §Notice convention.
  - **Exceeding 4 does not auto-block.** It requires (a) the reason declared in §2 of the packet and (b) the design/close review to look at it. Auto-blocking would have made 4.7 % of the historical corpus a violation and taught everyone to route around the rule instead of discussing it.
  - **There is NO total ceiling, deliberately.** Any cap on the *total* re-introduces the exact defect this replaced: it penalises writing tests.
  - Review packet at the end of each increment, following **the template this batch's `mode` owes** — `/dev-flow-init` step 4's seed-by-mode table, which is that fact's one home: the long `templates/increment-template.md` in `core`/`full`, the short `templates/fast-dev-flow/increment-template.md` in `fast`. Both fast rows are written from the flow ROOT, because no relative spelling is true in both layouts. `mode` is a field in `state.json`, so this bullet is reached by a fast batch too and may not name one template. No abstractions, helpers, or features not derivable from an approved LLR.
  - **Why 4, and why SOURCE-only — the derivation, which is part of the rule and not its provenance. Every figure in this bullet is the output of ONE script, `increment-file-history.py` in the authoring repository's analysis directory (canon-only; not shipped in the bundle), re-run over the record on 2026-09-10 — and **the run's own READING is on disk beside it**, `increment-file-history-2026-09-10.txt` (the transcript) and `-2026-09-10.json` (its 198 per-increment rows), because the corpus it walks GROWS: a figure whose producer is committed but whose output is not cannot be re-derived later, only re-measured against a different population — and the figures have exactly ONE other home, named here rather than left to be found: `C-47` in the lessons catalog, which states the 2026-08-10 corpus as DATED PROVENANCE and is not refreshed to today's, because an origin note that adopts a later measurement stops being an origin. `CMD BUDGET-derivation-consistent` reads BOTH.** It found **246** `increment-*.md`, parsed **198** as packets (40 excluded as non-packets, **8** failures enumerated rather than dropped, 96.1 % coverage) and reports the **SOURCE** distribution over the **192** packets whose path count is reliable: **median 2, p75 3, p90 4, p95 4, max 10**, with **95.8 % of increments at ≤4 source files** (8 of 192 exceed it). That is where the 4 comes from, and it is why exceeding it is a conversation rather than a block. **Source-only is the other half of the measurement:** of the **28** increments that break the old flat ≤5, **20 — 71 % — touch ≤4 SOURCE files** and break the cap by writing tests, not by sprawling (tests run median 1, p90 3, max 4). The old cap measured the wrong variable: 3 source + 3 tests was a violation while 5 source + 0 tests complied.
    - ⚠ **What this bullet published from rev5 to rev66, and what was actually wrong with it — recorded rather than silently overwritten.** It read *“median 3 source files, p90 6, max 12”* and, in the same sentence, *“95.3 % of all increments touch ≤4 source files”*, and an external review of 2026-09-08 was right that the two cannot describe one population. **Neither figure was arithmetically wrong; the LABEL was.** The script prints two distributions, and its **TOTAL DELIVERABLE** block reads verbatim *median 3 total files / p90 6 / max 12* — all files, tests and docs included — which the sentence relabelled *source*. Only the ≤4 share was ever a SOURCE figure (95.3 % over the 178-packet corpus of 2026-08-10; 95.8 % today). **The size of the mislabel, stated as a CROSS-CORPUS comparison because that is what it is:** rev66's figures describe the 178-packet corpus of 2026-08-10 and today's describe 198 packets, so 6-against-4 on p90, 12-against-10 on max and 3-against-2 on the median are *TOTAL-then* against *SOURCE-now* and not a drift in either. What is comparable within one run is the gap the label hid: over TODAY's corpus the same script returns TOTAL-deliverable p90 6 / max 12 against SOURCE p90 4 / max 10, so the rule's own justification overstated the spread of the variable it caps by **50 % on the p90**, measured on one population. **Re-run the script before changing any number here**; a figure with two homes is how this one drifted. (Origin: measured 2026-08-10, re-derived and re-labelled 2026-09-10 — see dev-flow-lessons)
- **Order:** implement LLRs in dependency order. If an LLR depends on another not yet implemented, report and stop.
- **Toolchain entry gate:** increment 1's first action verifies-and-installs the declared dev toolchain (linter, type-checker, test runner). A missing tool is a Phase-3 entry blocker, not a silent skip. (Origin: batches 02-04 — see dev-flow-lessons)
- **Frozen-file dual-guard (C-27) — the engine freeze has TWO guards; run BOTH:** every increment's frozen-file check (and the Phase-4 / final PR pass) MUST run the frozen-SOURCE guard (`test_engine_unchanged.py` / `test_tc031`) AND the frozen-TEST-file guard (`test_tc032_engine_test_files_unmodified_vs_main`, which diffs `_ENGINE_TEST_FILES` vs `main`) — a single-guard check is INCOMPLETE. The freeze covers engine SOURCE (`core.py`/`hexfile.py`/`range_index.py`/`validation/`/`<ui-package>/a2l.py`/`<ui-package>/mac.py`/`<ui-package>/color_policy.py`) **and** engine TEST files (`test_tui_a2l.py`, `test_tui_mac.py`, `test_validation_a2l/engine/mac.py`, `test_core_srecord_validation.py`, `test_hexfile.py`, `test_range_index.py`, `test_color_policy_round_trip.py`). A new test — including an `AT-NNN`/`TC-NNN` for the current story — can land in a frozen TEST file, pass the SOURCE-only guard, and surface only at a later whole-suite run; route any new test that would touch a frozen test file to a NON-frozen sibling (e.g. `test_tui_a2l_issue_recolor.py`, `test_validation_service_supplemental.py`). (Origin: batch-38 — see dev-flow-lessons)
- **Test-run evidence discipline (C-19):** gate evidence (pass/fail counts, the RED counterfactual, coverage) comes from ONE COMPLETE test run, with the exit code and tail read from THAT run's own output — never stitched across partial runs, never inferred from a killed or backgrounded call. If the harness backgrounds a run, read that one run's output; do not re-run and splice. A briefed "single blocking-foreground call" whose runtime exceeds the harness tool cap is a **spec bug in the brief**, not a test failure — specify "one complete run, evidence read from its own output" instead of "blocking foreground". (Origin: batch-35 — see dev-flow-lessons)
- **Net-new-file RED via move-aside, never stash (C-20):** to capture the trigger-absent RED counterfactual for a story that adds a NET-NEW file (module or test), make the file absent by MOVING IT ASIDE (rename out of the tree, run, restore) — never `git stash`. `git stash push -- <untracked path>` silently stashes NOTHING (untracked files need `-u`), and a subsequent bare `git stash pop` can resurrect an unrelated parked stash into a mid-increment conflict. Verify the file is restored (exists) before continuing. (Origin: batch-35 — see dev-flow-lessons)
- **Tests:** every test has a `TC-NNN` and maps to an LLR/HLR.
- **Layer 0 — unit tests, with an operable threshold.** Layers A (`TC`, white-box over the LLR) and B (`AT`, black-box over the story) both look *past* the unit, so bugs inside a single function are visible to neither. Layer 0 closes that, and it is **additive — it replaces nothing**. It applies when **either** criterion holds, both checkable before writing the test:
  - **decision criterion** — the unit has 2+ paths (`if` / `elif` / `for` / `while` / `except` / a comprehension with a condition) → **cyclomatic complexity ≥ 3**. Measurable with the standard `ast` module; nothing to install.
  - **boundary criterion** — the unit **transforms data crossing a boundary declared in the module map**: parses, serialises, computes an offset, validates, converts units. Layer 0 applies even with a single path, because that is where the bugs neither TC nor AT looks at actually live.
  - **Explicitly out:** pure delegations (one call and a return) · getters · UI wiring · constructors that only assign · one-line branchless functions.
  - **Anti-theatre:** layer 0 is measured by **mutation**, never by line coverage. High coverage made of vacuous assertions is the dominant defect of this whole catalog.
- **Parallel lanes — fork at the PDR, join at the DDR.** When ARQ declared parallelisable lanes, one agent runs the trunk (intake → ARQ → requirements → PDR) and forks into one agent per lane; the DDR is the join. **The lanes do not negotiate with each other — they consult the PDR.** Four conditions, and if one is missing you do not fork:
  1. **Frozen contract** — no shared interface is touched inside a lane. If one must change, the work returns to the trunk (trigger A3).
  2. **Disjoint FILE sets, not just modules** — two lanes may not edit the same file, not even different regions of it. Checked against the map and the plan **before** forking.
  3. **Crossed reverse census** — family B is run per lane and shared *before* starting: a symbol lane A touches may carry tests lane B also touches. This is the one check that structurally cannot be made from inside a lane.
  4. **One owner of the trunk** — requirements, traceability, backlog and SPEC are never written from a lane. Lanes propose; the trunk integrates.
  - **DECLARED, and from flow rev69 READ: `V46`**, on the `**Fork preconditions**` field in §2.8 of the requirements document — four rows, one per condition, each with a verdict and its executed evidence, or the legal empty `none — this batch runs one lane`, which MUST be written when there is no fork. **§2.8 is where condition 3 lives because it is the only place it CAN live:** `V43` reads the per-lane `Reverse census` in each lane's own increment packet, and the crossed census is by definition not any lane's to declare. *Measured 2026-09-10: 17 of this project's 66 live requirement documents carry lane/fork language; **0** declare the four conditions as a block.*
  - **Not parallelised, deliberately:** the complete validation run (it is ONE, owned by the orchestrator — stitched across lanes it stops being evidence), the close and the backlog (one writer), and the requirements (defined before the fork; a lane that needs them changed raises `iterate-to-refine` back to the trunk).
  - **Each lane needs its own worktree.** Not for convenience: **C-40 requires capturing the RED counterfactual where no other session is reading.** With one agent that was a precaution; with N lanes it is a correctness condition — mutating the shared tree contaminates a neighbour's measurement.
- **Coverage-claim discipline:** before a review packet marks an LLR "covered," `Glob` / read the exact test file path named in the LLR's Executed-verification line and confirm the test function exists on disk. Coverage signed off from intent (not from the artifact) is a false claim. (Origin: batch-08 — see dev-flow-lessons)
- **"Covered" = BOTH layers.** (a) white-box `TC-NNN` for the LLRs AND (b) the story's `AT-NNN` black-box acceptance test driving the shipped surface and asserting the deliverable is produced — a test that FAILS if the output is silently absent. Service/data-layer unit tests alone NEVER satisfy an output-producing story.
- **Spec-AT realization gate (C-18):** at each Phase-3 increment that lands a surface named by an `AT-NNN`, AND at the Phase-4 reconciliation, assert every `§3 AT-NNN` maps to **EXACTLY ONE distinct on-disk acceptance node** — never "covered by the combination of X + Y." An AT whose invariant holds only in parts (e.g. a seeded render test + a separate service-layer test) is **UNREALIZED** until a single node drives the whole named chain end-to-end through the shipped surface; folding an AT through Phase-2 does NOT realize it. (Origin: batch-29 — see dev-flow-lessons)
- **AT-amending-gate re-reconciliation (C-21):** whenever a gate amendment (a Phase-2 fold, an `iterate-to-refine`, or any review-driven change) ADDS, SPLITS, or REDEFINES an `AT-NNN` after the Phase-3 increment cut has been set, that cut is STALE — re-reconcile the AT registry and RE-DERIVE the increment plan BEFORE Phase 3 proceeds, so every AT (including the new / split ones) has an owning increment. C-18 *detects* an orphaned AT at end-of-phase; C-21 *prevents* it by re-cutting the moment the AT set changes. (Origin: batch-35 — see dev-flow-lessons)
- **Project-specific snapshot-drift gates** (C-22 per-cell prediction · C-28 shared-chrome/footer binding drift) live in the project's `docs/engineering-rules.md` — consult it at Phase 3 for any increment that changes snapshot-rendered UI or shared chrome (Footer/Header/rail bindings).
- **Test-count ledger:** track tests with a signed-balance ledger `post = base − D + A` (deletions, additions, rewrite-in-place), reconciled at each gate.
- **Requirement-amendment record (Before/After · Deleted/New):** if implementation surfaces a spec change (a baseline, a threshold, a symbol, a missing AC), edit the §3/§4 body first, then record the amendment in **§6.5 (Requirement amendments)** with explicit **Before → After** text and **Deleted / New** tokens, plus the parent-HLR re-read result and the re-derived TC/AT. Never silently edit a locked requirement during an increment. (Origin: batch-13 — see dev-flow-lessons; complements the §6.4 reconciliation log. §6.5 is also the record for `iterate-to-refine` from Phase 4.)
- **Artifacts:** code + tests + `.dev-flow/<batch_id>/03-increments/increment-NNN.md` (one review packet per increment, following the template the mode owes — see the budget bullet above). The packet lives in the **repo**, next to the diff it describes.
- **Independent review:** at each increment gate, `code-reviewer` reviews the diff (correctness, simplicity, reuse, convention conformance, test-intent) BEFORE user approval — independent of `software-dev`. HIGH findings block the increment until fixed; security concerns route to `security-reviewer`. **A RECOMMENDED fix does not discharge a HIGH (rev73).** A clean verdict requires the fix **applied AND verified**; until then the reviewer's verdict is the conditional form `BLOCK-UNTIL: <finding ids>`, which **names what is owed and authorises NOTHING** — it is not `OK-with-fixes` spelled differently, and the increment does not advance on it. Consistent with §Batch-kickoff authorization's third clause (*a HIGH finding blocks regardless*) and with `V50`'s conditional-gate discharge, which is where the re-read that closes it is recorded: a conditional verdict is discharged by RE-READING the artifact, never by trusting that the corrective pass ran. **THE AUTHORED SET IS FROZEN BEFORE THE REVIEWER IS DISPATCHED; A DIFF THAT MOVES UNDER THE REVIEWER IS RE-DISPATCHED; AND THE BUMP FOLLOWS THE VERDICT, NEVER PRECEDES IT (rev75).** `V36` records WHO reviewed; nothing recorded WHEN, and a verdict over a diff that has since moved names a tree that no longer exists — the reviewer's own `C-57` problem, since the instrument was shown an input other than the one being certified. **rev74 is the exhibit and it booked this rule itself:** its manifest hash and bundle were computed before the review returned, so folding five findings invalidated both and they were recomputed — the second figures were right and the first ones had been published to nothing, which is luck rather than process. **The order is: freeze → dispatch → fold (with RED proof per finding) → re-freeze and re-dispatch → bump, re-hash and bundle → run the battery once.** **AND THE RULE TERMINATES, which has to be said or it does not:** folding a round's OWN findings is the prescribed response to that round, not a fresh violation — it obliges a re-freeze and one more pass, discharged by that pass's verdict, the same way `V50` discharges a conditional gate by RE-READING the artifact rather than by trusting the corrective pass ran. **A revision closes when a pass over an unmoved set returns a verdict with no HIGH open.** What the rule forbids is editing the set **while a reviewer is still measuring it**: that reviewer's verdict then describes a tree that no longer exists, which is `C-57` pointed at the review itself, and the finding is against the author and never against the reviewer. rev75 was told this by its own round-2 reviewer, which kept measuring past its first report while the fold of that report landed — the fold was legitimate, the overlap was not, and the repair was the re-freeze already in flight. Derived artifacts — a manifest hash, a generated bundle, a `--sync-bundle` copy — are computed from the REVIEWED bytes, so they are the last step and never a parallel one. **What this does NOT claim:** no rule reads the ordering, and no mechanism can — it is a `C-65` obligation performed by the author, which makes it precisely the paragraph `C-58` warns about, said here rather than left implied.
  **Golden double-proof (batch-24):** when an increment mints a NEW byte-identical baseline (a golden capture asserting "default output unchanged"), the reviewer independently RE-DERIVES the golden from a clean worktree at the base ref and byte-compares — a golden captured by the author alone proves transcription, not provenance. (Origin: batch-24 I3 — see dev-flow-lessons)
- **Gate per increment:** user approves before advancing to the next. Phase ends when all approved LLRs are covered. Gate per §Objective exit criteria.

### DDR — Detailed Design Review *(gate; and the JOIN point when the batch forked into lanes)*
- **When:** detailed design closed, **before formal validation**.
- **Agents:** `architect` + `software-dev` + `qa-reviewer`.
- **Reviews:** what changed against the PDR **and why** · the reverse census of every touched symbol, **crossed between lanes** (a symbol lane A touches may have tests lane B also touches — this is the one check that structurally cannot be done from inside a lane) · that every `AT-NNN` realises in **exactly one** on-disk node (C-18) · the **summed** test ledger across lanes · whether the frozen interfaces are still intact · and **every condition the PDR left open, discharged one by one by RE-READING the artifact**, never by trusting that the corrective pass ran. A conditional verdict is not an authorisation.
- **Verdict:** same vocabulary as the PDR. A rejection returns to **design**, not to implementation.
- **Why it exists:** it is the gate that does not exist today. The flow goes from requirements straight to code without anyone ever having to *defend* a design — which is why design defects surface as gate surprises instead of as review findings.
- **Artifact home:** vault + Drive (`artifact_homes.design_ddr`), same sealing rule as the PDR — and the same writer: staged locally by `/dev-flow`, published by `/dev-flow-sync` alone (`Q22`).

### Phase 4 — Validation
- **Input:** implemented code + validation strategy from phase 1.
- **Agent:** `qa-reviewer` **evaluates** the strategy's results and writes the artifact — it does not execute the gate run. *(This bullet read `qa-reviewer executes the strategy` until flow rev73, three lines above the `C-25` paragraph that says the sub-agent never owns the run: the command contradicted itself inside one phase, and the census over this axis is what found it — the backlog item named the AGENT's veto and not this site.)*
- **Orchestrator owns the Phase-4 gate run (C-25) — refines C-19:** the ONE complete CI-equivalent gate suite run (`pytest -q -m "not slow"`) that produces the Phase-4 pass/fail evidence is launched and COLLECTED BY THE ORCHESTRATOR, not delegated to the `qa-reviewer` sub-agent — because a suite whose wall-time exceeds the harness tool cap gets backgrounded, and a sub-agent that launched it will END before it finishes, leaving `04-validation.md` unwritten. The orchestrator runs it (in the background if long), waits for the summary line, then hands the tail to `qa-reviewer` to reconcile the two layers + write the artifact. The sub-agent CONSUMES the result; it does not own the run. (Origin: batches 35-36 — see dev-flow-lessons) **And what `qa-reviewer` therefore writes is an ATTRIBUTION, not a claim (rev73):** it records the state of each result from §Evidence states and **names WHO executed it** — the orchestrator, a named agent, or `human:<name>` — because a QA that could only sign off on what it ran personally could, under this very rule, never sign off on anything. Evaluating a traceable result it did not launch is the job; asserting it launched it is the defect.
- **Methods:**
  - `test`: run suite, capture pass/fail.
  - `demo`: document observed flow and result.
  - `inspection`: produce review checklist and result.
  - `analysis`: reasoning or calculation supporting compliance.
- **Two validation layers:**
  - **Layer A — functional (white-box):** `TC-NNN` ↔ LLR/HLR (the methods above).
  - **Layer B — behavioral (black-box) acceptance:** exercise the system as the user — the UI framework the UI test driver end-to-end (`App.run_test()`), CLI invocation, or artifact-on-disk inspection — and assert the story's outcome with **representative + boundary + negative** inputs PLUS the **actual deliverable observed**. This is the `test (driver)` / e2e idiom, never `demo`. Reconcile `AT-NNN` to the real collected node per V-5. **Apply the spec-AT realization gate (C-18): every `§3 AT-NNN` must reconcile to exactly ONE distinct on-disk node driving the whole named chain — an AT satisfied only "in parts" is UNREALIZED and blocks the gate until a single joined node exists.**
- **Bidirectional surface-reachability matrix:** every named input dimension AND every named output/deliverable is exercised/observed through the handler (not only the service API). (Extends the A-5 surface-reachability rule, batch-11, to the output side.)
- **Feedback edges (gate vocabulary):** black-box FAILS + white-box PASSES ⇒ the requirement is wrong ⇒ **`iterate-to-refine`** (Phase 1), recorded via the §6.5 Before/After amendment (which re-derives HLR/LLR + their TC/AT); black-box fails from a wrong LLR ⇒ **`iterate-to-fix`** (Phase 3).
- **Escaped-bug regression:** a fix for a defect the suite missed ships a shipped-surface regression that demonstrably FAILS pre-fix (capture the failing run as evidence) then passes; its id is provisional per V-5, reconciled at Phase 4 with the pre-fix evidence captured against the reconciled node. (Origin: batches 11/14 — see dev-flow-lessons)
- **Artifact:** `.dev-flow/<batch_id>/04-validation.md` — both layers, the bidirectional matrix, evidence, gaps.
- **Blocker:** a story with no black-box deliverable observation is a Phase-4 blocker.
- **Gate:** blocker fails force `iterate-to-fix` (Phase 3) or `iterate-to-refine` (Phase 1) per the feedback edges. Otherwise, user decides. Gate per §Objective exit criteria.

### Phase 5 — Post-mortem
- **Input:** the entire batch (phases 1-4).
- **Agents:** `architect` + `qa-reviewer` co-author.
- **Structure:** what worked, what didn't, scope drift, metrics (iterations per phase, findings open vs. closed), root causes if multiple iterations, items proposed for the next batch.
- **Artifact:** written to `.dev-flow/<batch_id>/05-postmortem.md`, which in `full` is **LOCAL STAGING and not the home**: the canonical copy is `artifact_homes.postmortem` in the vault, and **`/dev-flow-sync` is the only command that writes it** (§Artifact homes, `Q22`). In `core` there is no post-mortem — the close record is `.dev-flow/<batch_id>/05-close.md`, it is canonical **in the repo**, and the vault `README` is a generated view of it.
- **Gate:** user decides — `close batch`, `open new batch` (back to phase 0 with a new `batch_id` — **run §Batch rollover first; it is a procedure, not a rename**), or `iterate` current. Gate per §Objective exit criteria.

### Phase 6 — Documentation
- **Input:** entire batch + final code.
- **Agents (in parallel):**
  - `docs-writer`:
    - `06-docs/traceability-matrix.md` (following template, no gaps).
    - `06-docs/functionality.md` (functional description accessible to a technical stakeholder).
    - `06-docs/diagrams/` (Mermaid: architecture, sequence, data as applicable).
  - `presentation-builder`:
    - `06-docs/executive-summary.md` (1-2 pages for non-technical stakeholder — context → problem → solution → outcomes → next steps).
- **Gate:** user reviews and approves. State moves to `awaiting-sync`. Gate per §Objective exit criteria.
- **PR + merge (per the batch-kickoff authorization):** commit/push, then open the PR.
  - **If merge authority was granted at kickoff:** once CI is green, run the **final PR-level `qa-reviewer` pass** over the whole merged diff vs `main` (dual traceability intact · 0 engine-frozen diffs · no cross-increment regression · every gate carry discharged). On a clean result the agent merges, then proceeds to sync; a HIGH finding blocks the merge and returns to the operator.
  - **Otherwise:** stop at "PR opened, CI green" and instruct the operator to merge. Never self-merge without the kickoff grant.
- **Backlog reconciliation (MANDATORY close step — the carry-over contract).** Before the batch is marked complete, reconcile the project's canonical cross-batch backlog — **the file, or lane files, that its `docs/engineering-rules.md` designates; absent such a designation, `.dev-flow/BACKLOG.md`** (create that default if neither exists — a prioritized cross-batch queue, never a per-batch file). **If the project routes to lanes, reconcile the lane this batch belongs to**, and the router only when the batch closes. Three moves, all required:
  1. **Mark shipped** — every backlog item this batch closed → strike it / mark `DONE` with its PR number + merge SHA.
  2. **Carry forward — drop nothing.** Append every still-open item PLUS every NEW carry, deferred finding, review-fold, or "suggested next task" this batch surfaced — pulled from the per-increment review packets (§6 Pending + §7 Suggested-next) and the `05-postmortem.md` "items proposed for the next batch". If the batch surfaced it, it lives in the backlog now.
  3. **Refresh the header** — update the recorded `origin/main` tip SHA + a "last refresh: <date> (<batch_id> close)" line.
  **A deferral written anywhere carries the `⏸ DEFER` marker, and this step reads the census** — `V42` reports every marker in `.dev-flow/design/**`, in an ADR or in the batch record that is keyed to no backlog entry, and reconciliation is where they are filed (see §*A deferral carries the marker*). This is a gate, not a nicety: **the batch is NOT closed until the canonical backlog reflects it.** (The SAME file — or the same lane file — is read at Phase 0 as the source of candidate stories and feeds the RC-1 already-shipped check, so a stale backlog corrupts the next batch's intake.) Record the reconciliation in the postmortem + carry it to the vault at sync.
- **Post-approval reminder:** instruct the user (or note it, if the agent merged under the grant):
  > "Documentation ready. Once the PR is merged, run `/dev-flow-sync` to upload artifacts to the Obsidian vault."

## Hard rules

- Never advance phase without explicit approval.
- Never assume the content of a prior artifact — always read it.
- Never allow `should`/`debería` as a modal verb inside an HLR/LLR statement. Flag it as an error.
- Never derive an HLR from a story that has not passed the Phase-0 Definition of Ready gate.
- Never sign off LLR coverage from intent — verify the named test exists on disk (Phase 3).
- **No story is "done" until a black-box test (`AT-NNN`) observes its user-verified outcome through the shipped surface, with boundary + negative evidence — independent of the white-box `TC-NNN` that validate the internal HLR/LLR mechanism. A green white-box suite that never observes the behavior is not acceptance.** (Origin: batch-14 — see dev-flow-lessons)
- **A phase gate never accepts an artifact still in unfilled-template form.** Remaining template placeholders (`<P>`, `TC-NNN`, `<...>`, empty required rows) or a `04-validation.md` with no executed results mean the phase did not actually run — block the gate. "Phase 4 never ran" must be impossible to pass. (Origin: batch-14 — see dev-flow-lessons)
- Every phase gate requires the responsible agent's completed **evidence checklist** (each item ✓/✗ + a one-line evidence: file:line, command output, or finding link) attached to the phase artifact. An unchecked or evidence-less item blocks the gate — a checklist marked mentally is not evidence.
- Offering `iterate` without a named gap against an exit-criteria axis (Coverage / Certainty / Evidence), or stamping `approve` below the bar because it "looks tested," is a process violation. See **§Objective exit criteria**.
- If you detect scope creep during a phase, stop and report.
- Any destructive action (deleting increments, resetting state) requires explicit approval.
- **A batch is not closed until the project's canonical backlog is reconciled** (shipped items marked done, every new carry/finding/deferred item appended, base ref + refresh-date bumped). **Every open item lives in exactly ONE canonical file.** A project MAY partition its queue (e.g. a code lane and a process lane) — a partition is a split, not a copy, so an item is **moved** between lane files and never duplicated, and the routing is declared in the project's `docs/engineering-rules.md`. What is forbidden is a second *de-facto* source (a memory note, a postmortem list) drifting alongside the canonical one; those may point to it, not replace it. A close that skips the backlog reconciliation is an incomplete batch. (Origin: 2026-07-20 operator audit, extended 2026-07-28 — see dev-flow-lessons)
- Do not touch the Obsidian vault from this command — that is `/dev-flow-sync`'s job.

## `state.json` schema

**Backward compatibility — do not break the 60+ batches already on disk.** Batches created before the
station model carry `current_phase` (numeric) and `iterations_per_phase`; **read whichever pair is
present and never rewrite an old batch's schema to the new one.** A migration that touches closed batches
would make their records assert something they never said. New batches use `current_station` /
`iterations_per_station`; the station ids are the ones in the phase map, with `ARQ`, `PDR` and `DDR`
present **only when a trigger turned them on** (`stations_active` is the authority on which exist in
*this* batch — and, when `guided: true`, the gate list `V55` derives the guided ledger's owed set from).

**`guided` is a PREFERENCE, seeded by `/dev-flow-init` step 3 and settable by hand**, and it is the one key here that changes what a GATE does rather than what a station holds: `SKILL.md` §*Guided first run* is its one home.

```json
{
  "project": "<name>",
  "language": "en | es",
  "batch_id": "<YYYY-MM-DD>-batch-NN",
  "batch_objective": "<short description>",
  "owner": "<absolute path of the checkout that opened this batch — `git rev-parse --show-toplevel`>",

  "mode": "fast | core | full",
  "mode_history": [
    {"from": "core", "to": "full", "date": "YYYY-MM-DD",
     "reason": "trigger A3 fired: a shared interface changed"}
  ],

  "guided": true,
  "current_station": "P0 | ARQ | P1 | P2 | PDR | P3 | DDR | P4 | P5 | P6",
  "phase_status": "not-started | in-progress | awaiting-gate | iterating | approved | awaiting-sync",
  "stations_active": ["P0", "P1", "P2", "P3", "P4", "P5", "P6"],
  "iterations_per_station": {"P0": 0, "P1": 0, "P2": 0, "P3": 0, "P4": 0, "P5": 0, "P6": 0},

  "triggers": {
    "evaluated_at": "<ISO8601>",
    "fired":     ["A2", "A3", "B1", "C8", "D1", "E1"],
    "not_fired": ["A1", "B2", "B3", "C2"],
    "record": ".dev-flow/<batch_id>/PLAN.md#triggers"
  },

  "artifact_homes": {
    "...": "the default homes are declared ONCE, in /dev-flow-init step 3, which is the command that writes them. How many there are is stated there too, beside the block, and an arm compares the two -- it is not restated here, because a figure with two homes is the drift this note is about. Not repeated here: this block and that one were hand-kept side by side until rev62 and had already drifted, <batch> against <batch_id>. The repo:/vault: convention and what vault: resolves to are above."
  },

  "artifacts": {
    "P1": ".dev-flow/<batch_id>/01-requirements.md",
    "P1_ledger": ".dev-flow/<batch_id>/01-requirements-ledger.md",
    "P2": ".dev-flow/<batch_id>/02-review.md"
  },
  "decisions_log": [
    {"station": "P1", "date": "YYYY-MM-DD", "decision": "approved", "notes": "...",
     "guided": true}
  ],
  "standing_authorization": {"autonomous": false, "merge": false,
                             "asked_on": "YYYY-MM-DD", "operator_words": "<verbatim>"},
  "obsidian_synced": false,
  "created_at": "<ISO8601>"
}
```

**`guided` on a `decisions_log` ENTRY is written only on a batch whose top-level `guided` is true**, and then on every gate entry — it is half of what `V55` reads, the other half being the gate's name, spelled `station` here and `gate` in a mode that has no stations. On a batch that is not guided the field is simply absent, as it is in every entry already on disk. `SKILL.md` §*Guided first run* is that obligation's one home.

**Every field above except `project`, `language` and `mode_history` is SINGLE-SLOT — it describes
the ACTIVE batch and nothing else.** `decisions_log` in particular is per-batch: at `open new batch`
it is MOVED to `.dev-flow/<outgoing_batch_id>/decisions-log.json` and reset to `[]`. **§Batch
rollover holds the full retire-or-carry table and is mandatory** — the field list here declares the
shape, not what happens to it when a batch ends.
