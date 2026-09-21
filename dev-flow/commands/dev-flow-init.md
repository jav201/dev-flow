---
description: Initializes the .dev-flow/ structure in the current project with state.json and templates. Run once when starting a new batch.
---

# /dev-flow-init

Initialize the engineering workflow in the current project.

## Pre-checks

1. Verify you are at the project root (look for signals: `.git/`, `package.json`, `pyproject.toml`, `README.md`). If unclear, **ask** the user before creating anything.
2. If `.dev-flow/` already exists:
   - Read `state.json` and report the current batch.
   - **Ask** explicitly whether to overwrite, archive the current batch, or cancel. Do not overwrite without confirmation.

## Actions

1. Ask (or detect) the **project name**, a **short description of the batch objective**, the **development language** (`en` | `es`; default `en` unless the user asks for Spanish), and the **mode** (`--mode fast|core|full`, default `full`; see §Modes in `/dev-flow`). **Where each answer is recorded is decided by the MODE, and step 3 is where that is written:** in `core` and `full` all four go into `state.json`, which the orchestrator reads to generate the artifacts. **In `fast` only `mode` and `batch_id` reach `state.json`** — the six-key declaration below carries neither `project` nor `batch_objective` nor `language`, because no rule reads them there in that mode and a seeded key nothing reads is a fact nobody maintains (`C-58`); the project's name, the objective and the language live in `.fast-dev-flow/spec.md`, whose §1 and §0 are their home. Until rev85 this step said *record all of them in `state.json`* against a block that omits three of them, and both readers of the 2026-09-18 publication test had to choose between the two.

**Seed only the artifacts the mode requires.** `fast` → the spec alone. `core` → `01` · `02` · `03-increments/` · `04` · `05-close.md`. `full` → everything below. Promotion later fills in what is missing; it never migrates anything.

**Write `artifact_homes` into `state.json`, in step 3 below, and nowhere else.** Until rev62 this step also wrote them into `.dev-flow/config.json`, and the defaults block was hand-kept HERE and again in `/dev-flow` — two inventories of one fact, already drifted (`<batch>` here against `<batch_id>` there) and neither of them read: `V2` takes `artifact_homes.tests` from `state.json` alone. **`config.json` is retired.** No rule ever read it, and no project on disk ever held one. **No command may write a FLOW ARTIFACT to a path that is not declared in `artifact_homes`** — if a flow artifact needs a new location, it is declared first. **That rule's one home is `/dev-flow` §*Artifact homes*, which states what it binds and what it does not**; this line does not restate the bound.

2. Create the structure:
   ```
   .dev-flow/
   ├── state.json                  (PROJECT-level and SINGLE-SLOT — it describes the ACTIVE batch)
   └── <batch_id>/                 (the batch RECORD — a directory, named by state.json's batch_id)
       ├── 01-requirements.md       (skeleton from template — the LIVE CONTRACT)
       ├── 01-requirements-ledger.md (skeleton from template §7, FIRST fence — APPEND-ONLY, never edited)
       ├── 02-review.md             (skeleton from template)
       ├── 03-increments/           (empty folder)
       ├── 04-validation.md         (skeleton from template)
       ├── 05-postmortem.md         (skeleton from template — in `full` this is **LOCAL STAGING**, not the home: the canonical copy is `artifact_homes.postmortem` in the vault and `/dev-flow-sync` alone writes it, `Q22`)
       └── 06-docs/
           ├── traceability-matrix.md  (skeleton from template)
           ├── functionality.md         (skeleton from template)
           ├── diagrams/                (empty folder)
           └── executive-summary.md     (skeleton from template)
   ```
   **`<batch_id>/` is a directory, and never a flat `.dev-flow/`.** A `state.json` that declares a `batch_id` with no directory of that name is the *ghost* state: `V18` reports it, and `V1`-`V9` fall back to walking the tree and judge whichever historical document the walk reaches first. Until rev62 this command created the flat shape, so **every project it ever initialised started life as a ghost.**
3. Generate the initial `state.json`. **THE SCHEMA BELOW IS `core` AND `full`'s. `fast` writes the SIX-KEY declaration in §*The `fast` declaration* further down this step and nothing else** — the two blocks are not alternatives to choose between, they are one block per mode, and this sentence is the pointer that says so where a reader first meets the long one. **This block is the flow's ONLY inventory of the `artifact_homes` defaults** — `/dev-flow` §`state.json` schema declares the shape and points here for those **twelve** keys, so the fact has one home and there is no second copy to drift. Every value below is either a literal or a substitution step 1 already asked for; nothing here is filled in later:
   ```json
   {
     "project": "<name>",
     "language": "en",
     "batch_id": "<YYYY-MM-DD>-batch-01",
     "batch_objective": "<short description>",
     "owner": "<the absolute path of this checkout, as `git rev-parse --show-toplevel` prints it>",

     "mode": "full",
     "mode_history": [{"from": null, "to": "full", "date": "<YYYY-MM-DD>",
                       "reason": "initial mode, declared at /dev-flow-init"}],

     "guided": true,

     "current_station": "P0",
     "phase_status": "not-started",
     "stations_active": ["P0", "P1", "P2", "P3", "P4", "P5", "P6"],
     "iterations_per_station": {"P0": 0, "P1": 0, "P2": 0, "P3": 0, "P4": 0, "P5": 0, "P6": 0},

     "triggers": {
       "evaluated_at": null,
       "fired": [],
       "not_fired": [],
       "record": "NOT EVALUATED. /dev-flow evaluates the triggers at P0 and rewrites this block with the timestamp of THAT evaluation. An empty `fired` list here is an absence, not a verdict that nothing fired."
     },

     "artifact_homes": {
       "requirements": "repo:.dev-flow/<batch_id>/01-requirements.md",
       "requirements_ledger": "repo:.dev-flow/<batch_id>/01-requirements-ledger.md",
       "traceability": "repo:.dev-flow/<batch_id>/06-docs/traceability-matrix.md",
       "tests": "repo:tests/",
       "module_map": "repo:docs/ARCHITECTURE.md",
       "increments": "repo:.dev-flow/<batch_id>/03-increments/",
       "evidence": "repo:.dev-flow/<batch_id>/evidence/",
       "backlog": "repo:.dev-flow/BACKLOG.md",
       "design_pdr": "vault:<project>/design/PDR-<batch_id>.md",
       "design_ddr": "vault:<project>/design/DDR-<batch_id>.md",
       "postmortem": "vault:<project>/dev-flow-batches/<batch_id>/",
       "metrics": "vault:<project>/dev-flow-batches/<batch_id>/README.md"
     },

     "artifacts": {},
     "decisions_log": [],
     "standing_authorization": {"autonomous": false, "merge": false, "asked_on": null,
                                "operator_words": "NOT ASKED. Authorization is per-batch and is never carried. /dev-flow asks at P0 per §Batch-kickoff authorization; until it does, the flow's stated default applies — the operator approves every gate and merges the PR."},
     "obsidian_synced": false,
     "created_at": "<ISO8601>"
   }
   ```
   - `batch_id` uses today's date and auto-increments the suffix if there were already batches on the same date. **`.dev-flow/<batch_id>/` is created in the same act** — see step 2.
   - **`owner` is FILLED IN BY THIS STEP, like `<PROJECT>` and `<BATCH_ID>` are** — run `git rev-parse --show-toplevel` in the checkout you are initialising and write its output verbatim. It records WHICH CHECKOUT opened this batch, and `V40` compares it against the tree being gated: one checkout holds ONE active batch, and parallel work takes a git worktree with its own `state.json` (`/dev-flow` §Batch rollover). **Leaving the angle-bracket literal in place is not a silent no-op** — `V40` compares it against the tree and raises the RELATIVE-path NOTICE (`_V40_RELATIVE`: a checkout identity must be ABSOLUTE and fully qualified, and the angle-bracket literal is neither), which is the correct reading of a field nobody filled. A project with no git root writes the project root's absolute path and says so in `PLAN.md`.
   - **A `vault:` HOME IS NOT A PATH THIS COMMAND WRITES (`Q22`, flow rev72).** `design_pdr`, `design_ddr`, `postmortem` and `metrics` name the CANONICAL home of four artifacts, and **`/dev-flow-sync` is the only command that writes any of them**; `/dev-flow-init` and `/dev-flow` write the repo and the batch record only. The batch-record copies of the post-mortem and the design records are **local staging** — the input `/dev-flow-sync` publishes from — and staging is not a home, so it needs no key here. In `core` the direction reverses: `05-close.md` in the batch directory is canonical and `metrics` is a **generated view** of it. §Restrictions below is the same rule said once more, and until rev72 it contradicted step 4's own table.
   - **`repo:` and `vault:` are the two prefixes, and neither is optional.** `repo:` resolves against the project root; `vault:` against the flow's declared `vault_root` and against nothing else — `/dev-flow` §Artifact homes is that definition's one home. A command that cannot read that row STOPS and asks; it never guesses a path.
   - **`artifact_homes.evidence` is READ by a rule, and it is where EVIDENCE BYTES LIVE** (rev66, `C-59`). A transcript, a capture, a snapshot or a `.PRE` copy that a packet cites as proof is written HERE, byte for byte, and the packet cites it with its SHA-256. `V41` reads the declaration and re-hashes the bytes on disk against every digest a packet publishes. **A session-scoped scratch directory is not a home:** the three destinations outside version control at batch-66 had their only rollback copy under the agent session's temp directory, which does not survive the session. **And if the store is git, the path is marked `-text` in `.gitattributes` and never `text eol=lf`** — `core.autocrlf` silently normalised four `.PRE` files on the way in and one was stored as `d46bb314…` against a recorded `e103af29…`, so the commit looked healthy and a rollback from it would have restored bytes that do not hash to the original. Evidence carries mixed line endings by nature; only `-text` is correct.
   - **`artifact_homes.tests` is READ by a rule** — it is the node corpus `V2` resolves acceptance ids against, from `state.json` alone. `repo:tests/` is the default; a project whose acceptance arms live elsewhere declares it here and nowhere else.
   - **Every `<batch_id>`-templated home is re-pointed at batch rollover**, per `/dev-flow` §Batch rollover. A `repo:` home still naming the previous batch's directory sends this batch's writes into a closed batch's record.
   - `mode`, `stations_active` and `iterations_per_station` are written for the mode step 1 chose: `fast` → `["P1", "P3"]`, `core` → `["P0", "P1", "P3", "P4", "P5"]`, `full` → the seven above. `ARQ`, `PDR` and `DDR` are absent until a trigger turns one on — `stations_active` is the authority on which stations exist in *this* batch.
   - **`guided` is SEEDED BY MEASUREMENT, not asked, and it is a PREFERENCE rather than a station fact.** Write `true` when `.dev-flow/` holds **no batch directory yet** — this project's FIRST batch — and `false` on every batch after it. It turns on the guided gate, and **`SKILL.md` §*Guided first run* is that gate's ONE home** — what the gate does, what the ledger entry carries, and when the key may be turned off again are stated there and nowhere else, this bullet included (`C-50`). `V55` is the reader. **The operator may set either value by hand at any time, and NOTHING flips it automatically.** It is seeded in **all three modes**, which is why it also stands in the `fast` declaration below.
   - **`current_phase` and `iterations_per_phase` are NOT written.** They are the pre-station pair, kept in the schema only so the 60+ batches already on disk still read; a project created today uses the station names, and `V27`/`V29` read `current_station`. Writing both would make a fresh project assert two schemas at once.
   - **`triggers` and `standing_authorization` are seeded as DECLARED ABSENCES, not as empty objects.** A carried or blank `triggers` block asserts an evaluation that never ran; the `record` string above says in words that none has, so nobody reads `"fired": []` as *nothing fired*. Same for the authorization: the flow's default is stated, and `asked_on: null` says it was never asked.

### The `fast` declaration — six keys, and the reason each one is there

**`/fast-dev-flow` writes THIS and nothing else, and this block is the fact's one home** (`C-50`): the command points here and does not restate the keys. *Lightweight* means few artifacts, not no declaration — a `fast` batch with no `state.json` is a batch the gate cannot inspect, which is what the 2026-09-18 publication test measured on two runtimes.

```json
{
  "mode": "fast",
  "batch_id": "<YYYY-MM-DD>-fast-01",
  "flow_version": "<the revision `FLOW-VERSION.md` declares>",
  "stations_active": ["P1", "P3"],
  "guided": true,
  "artifact_homes": {
    "spec": "repo:.fast-dev-flow/spec.md",
    "increments": "repo:.dev-flow/<batch_id>/03-increments/",
    "evidence": "repo:.dev-flow/<batch_id>/evidence/",
    "backlog": "repo:.dev-flow/BACKLOG.md"
  }
}
```

- **Every key but one is here because a READER reads it** (`C-58` — a seeded key nothing reads is a fact nobody maintains); the exception is named at the end of this bullet rather than left to contradict its opening: `mode` decides `V36`'s accepted reviewer forms and `V27`/`V52`/`V54`'s applicability; `batch_id` resolves the batch directory `V18` and every `S1` rule walk from; `stations_active` is what `V52` asks before deciding a design proposal is owed and is also the gate list `V55` derives the owed set from in `core` and `full`; `guided` is `V55`'s own subject and the reason the sixth key joined at rev87 — the fence above carries `true` because a FIRST batch is the case this seed is copied for, and step 3's bullet says when to write `false` instead; `artifact_homes.evidence` is `V41`'s only source, and `artifact_homes` is read from `state.json` **alone** by every rule keyed on it. `flow_version` is the `C-45` PULL identity the spec header also carries — the one key here that no rule reads, named as such rather than left to look like one.
- **The key names are the SAME as the other two modes'** — `artifact_homes`, `increments`, `evidence`, `backlog` — so no reader needs a `fast` spelling. `spec` is the fast flow's own home and is declared for the same reason the others are: and no command writes a FLOW ARTIFACT to a path `artifact_homes` does not declare (`/dev-flow` §*Artifact homes*, that rule's one home).
- **What is deliberately ABSENT, and what that costs, said out loud:** no `owner`, so `V40` reports that no checkout comparison was made — `owner` records which checkout opened a batch for rollover, and this flow has one batch and no rollover; no `current_station`, `phase_status`, `iterations_per_station` or `triggers`, because nothing in this flow advances them and a seeded empty would assert an evaluation that never ran; and **no `decisions_log` in the seed** — which is not the same as never having one. `guided: true` is the ONE key that asks this flow to write the ledger back, and it does so at the FIRST gate it closes, one entry per gate and nothing else in it (`SKILL.md` §*Guided first run*, that gate's one home; `V55` is the reader). Seeding `[]` would still be wrong, for the reason above: it asserts a ledger that records no decision (the same reason step 3 seeds those as declared absences in `full`). `V27` and `V54` read `mode` and say a `fast` batch owes neither ledger — `V27` keyed on the SUBJECT since rev87, so a guided fast batch whose ledger names GATES is not charged for naming no increment.
- **`fast` still uses `.dev-flow/<batch_id>/` for the packet and the evidence**, exactly as `core` and `full` do; what it does not create is `01-`…`06-`. `/fast-dev-flow` §Structure lists the resulting footprint.

4. Copy each template from the flow's `templates/` directory — every row below names it relative to that directory, except the one row that says otherwise and gives its path from the flow root → its artifact, **into `.dev-flow/<batch_id>/`**, replacing `<PROJECT>` and `<BATCH_ID>`:
   **Seed by mode — copy only what the mode requires.** A template that is not seeded is not "missing": promotion fills it in later, without migrating anything.

   | Template | → artifact | `fast` | `core` | `full` |
   |---|---|:--:|:--:|:--:|
   | `req-template.md` | `.dev-flow/<batch_id>/01-requirements.md` | — | ✓ | ✓ |
   | **`req-template.md` §7, FIRST fence only** | `.dev-flow/<batch_id>/01-requirements-ledger.md` — the append-only ledger, seeded with **no entries**. §7's second fence is the SHAPE of an entry and is documentation, not seed: copying it seeds two entries that name no requirement and one live `<YYYY-MM-DD>`, which is 2 BLOCKs (`V26`, `V1`) on the project's first gate. **Seeded in the same act as the contract, never later:** a batch whose ledger is absent has not adopted the lean shape, and `V26` says so at every gate | — | ✓ | ✓ |
   | `review-template.md` | `.dev-flow/<batch_id>/02-review.md` | — | ✓ | ✓ |
   | **`increment-template.md`** — the LONG packet | copied per increment into `03-increments/increment-NNN.md` | — | ✓ | ✓ |
   | **`templates/fast-dev-flow/increment-template.md`** — the SHORT packet, written from the flow root for the same reason the row below is: **no relative spelling is true in both layouts**. It carries ONLY the rows a rule reads on a `mode: fast` tree, so a fast batch fills what is read and nothing else; `core` and `full` take the long one above | copied per increment into `03-increments/increment-NNN.md` | ✓ | — | — |
   | `validation-template.md` | `.dev-flow/<batch_id>/04-validation.md` | — | ✓ | ✓ |
   | **`close-template.md`** | `.dev-flow/<batch_id>/05-close.md` | — | ✓ | — |
   | `postmortem-template.md` | `.dev-flow/<batch_id>/05-postmortem.md` | — | — | ✓ |
   | **`phase-checklists.md`** | `.dev-flow/<batch_id>/00-checklists.md` | — | ✓ | ✓ |
   | **`architecture-template.md`** | `docs/ARCHITECTURE.md` — **only if it does not already exist**; it is a standing project artifact, not a per-batch one | by trigger | by trigger | ✓ |
   | **`design-proposal-template.md`** | the PDR input — seeded to **local staging** under `.dev-flow/<batch_id>/design/`, published by `/dev-flow-sync` to `artifact_homes.design_pdr` (**vault**). **This command never writes the vault** (`Q22`; see §Restrictions, which has said so since rev1) | by trigger | by trigger | ✓ |
   | **`design-review-template.md`** | the PDR and DDR records — same rule: **local staging** here, `artifact_homes.design_pdr` / `design_ddr` (**vault**) published by `/dev-flow-sync` alone | by trigger | by trigger | ✓ |
   | `templates/fast-dev-flow/spec-template.md` — one of the TWO rows of this table that are not under the templates directory named above (the other is the short packet), each written from the flow root for that reason: **no relative spelling is true in both layouts** — a canonical home and the bundle spell the OTHER templates' directory differently, so a sibling in one layout is a child in the other, and `FLOW-VERSION.md`'s mapping table is where that pairing lives | `.fast-dev-flow/spec.md` | ✓ | — | — |
   - **`fast` also writes `.dev-flow/state.json`** — the six-key declaration above, not the full seed of step 3. It is a `state.json` like any other, so every reader keyed on `artifact_homes` or on `mode` reads a `fast` batch too.
   - **The three rows below are `full` ONLY** — they seed `06-docs/`, which is `P6`'s station and which `core` and `fast` do not open. They are written as a list rather than as table rows for layout alone, and a mode reads them exactly as it reads the table above: a mode the row does not name does not owe the artifact.
   - `traceability-matrix.md` → `.dev-flow/<batch_id>/06-docs/traceability-matrix.md` — `full`
   - `functionality-template.md` → `.dev-flow/<batch_id>/06-docs/functionality.md` — `full`
   - `executive-summary-template.md` → `.dev-flow/<batch_id>/06-docs/executive-summary.md` — `full`
5. Create the empty folders **the mode owes**: `.dev-flow/<batch_id>/03-increments/` and `.dev-flow/<batch_id>/evidence/` — the two directories `artifact_homes` declares — in all three modes, and `.dev-flow/<batch_id>/06-docs/diagrams/` in `full` alone. **A declared home with no directory is the state `V41` reads as an absence**, and the two are created in the same act as the declaration for the same reason the backlog lane is (step 6). **`fast` creates these two and nothing else under `.dev-flow/<batch_id>/`**; `/fast-dev-flow` §Structure lists the resulting footprint.
6. **Create the backlog lane `artifact_homes.backlog` declares** — `.dev-flow/BACKLOG.md` by default, or the lane the project's `docs/engineering-rules.md` designates — in **all three modes**, as an empty prioritized queue carrying the four fields Phase C's reconciliation reads back. No template is seeded for it because it is four lines; this IS its shape:

   ```markdown
   # Backlog — <project>

   The cross-batch queue, shared by `/dev-flow` and `/fast-dev-flow`. Every open item lives
   in exactly ONE canonical file; a project MAY partition it into lanes declared in its
   `docs/engineering-rules.md`, which is a split and never a copy.

   Base ref: <the commit this queue was last reconciled against>
   Last refresh: <YYYY-MM-DD>

   ## Open
   ## Done
   ```

   It is created in the same act that declares it, and that ordering is the rule: a home declared here and filled three phases later is a home `V42` reports as *the DECLARED lane is not on disk · the census was NOT taken* at every gate in between, which is what both readers of the 2026-09-18 publication test hit and had to rule benign by themselves.

## Report to user

After the structure is created, report:
- Created structure (tree).
- Location of `state.json`.
- Suggested next step — **it is mode-dependent, because the artifact it names is**:
  > **`core` / `full`:** "Paste your user stories into `.dev-flow/<batch_id>/01-requirements.md` (section 2.6 — Source user stories) and then run `/dev-flow` to start phase 0 (story intake & refinement). Or just hand them to me and I'll insert them."
  > **`fast`:** "Write the objective and the observable acceptance criteria into `.fast-dev-flow/spec.md` and run `/fast-dev-flow` from Phase A. There is no `01-requirements.md` in this mode, and its absence is not an omission." 

## Restrictions

- Do not overwrite an existing `.dev-flow/` without explicit confirmation.
- **No git operations IN THIS COMMAND** (no `git init`, no `git add`, no commits). It scopes THIS command and nothing else: scaffolding is not a change worth a commit of its own, and a command that initialises a tree must not decide what enters history. **A BATCH may still commit** — `/fast-dev-flow` §*Hard rules* is that rule's one home, and Phase C step 6 requires the backlog edit to travel in the batch's commit. Until rev85 this line read as an absolute ban and every reader of the 2026-09-18 publication test recorded the contradiction and resolved it alone.
- Do not touch the Obsidian vault.
