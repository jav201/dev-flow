---
description: Syncs the batch documentation (.dev-flow/) to the Obsidian vault. Run AFTER commit/push/merge of the PR.
---

# /dev-flow-sync

Upload the final batch documentation to the Obsidian vault. This is a deliberate manual step — it does not run automatically.

## Argument — `/dev-flow-sync [<batch_id>]`

**`state.json` is the DEFAULT source of the batch under sync, never the only one.** It is
single-slot (see §Batch rollover in `/dev-flow`), so it names the ACTIVE batch and nothing else —
and a batch that rolled over before it closed was therefore **unsyncable by any supported path**.
Measured on batch-88, 2026-08-29: it had to be synced by hand out of
`git show 0f40624:.dev-flow/state.json`, and the only workaround this command's own text suggested
was to roll `state.json` back, which would corrupt live work. Recorded in
`.dev-flow/2026-08-24-batch-88/05-close.md` §4 (`S-3`).

Resolve the batch under sync in this order, and **say which branch you took in the report**:

1. **`<batch_id>` given** → the batch under sync is `<batch_id>`. Require `.dev-flow/<batch_id>/` to
   exist; if it does not, list the batch-shaped directories that do and STOP. `state.json`'s
   `batch_id`, `mode`, `current_station`, `phase_status` and `obsidian_synced` are **not** read —
   they describe a different batch, and answering from them is answering about the wrong subject.
2. **No argument** → read `state.json.batch_id`. If it is absent, unreadable, or names a directory
   that is not on disk, STOP and say which of the three it was. Do not fall back to a directory walk.

Call the result `<batch>`. `<batch> == state.json.batch_id` is the **ACTIVE** case; anything else is
the **SUPERSEDED** case, and the two differ wherever a field of `state.json` is single-slot.

## Pre-requisites (verify in order, stop if any fails)

1. **`.dev-flow/` exists** in the current directory and `.dev-flow/<batch>/` is a directory. If not,
   error: "I'm not inside a project with dev-flow initialized", or "there is no such batch on disk".
2. **The batch reached its closing station.** How that is decided depends on the case, and **neither
   case may be silently unevaluable**:
   - **ACTIVE** → read `mode` FIRST, because the closing station is a function of it: **`P6` for
     `full`**, **`P5` for `core`** (derived from `/dev-flow`'s mode table — `core` closes with
     `05-close.md` and owes no `06-docs/`), and **`fast` → this command does not apply**: say so and
     stop. Then read whichever of `current_station` / `current_phase` the file carries (both schemas
     are live and `/dev-flow` forbids rewriting an old batch's into the new one) and require **that**
     closing station — numeric schema `6` / `5` respectively — with `phase_status` in {`approved`,
     `awaiting-sync`}. If it carries NEITHER key, **that is an ERROR, not a pass**: report the keys
     the file actually has and stop. **`stations_active` is NOT consulted, and the three reasons are
     measured, not stylistic:** it is absent from **all 20** `state-snapshot-at-close.json` files —
     the numeric-schema class this fallback exists for; its order is **trigger-shaped** (`ARQ` /
     `PDR` / `DDR` interleave with the numbered stations, so "last element" is positional, not
     terminal); and its reset at rollover is **unreliable** — measured 2026-09-03 over the state
     ledger's own git history, the 87→88 rollover reset it and the 88→89 rollover did not. Deriving
     this condition from that array would reintroduce, inside the sentence that repairs this
     pre-requisite, the *silently unevaluable* defect the pre-requisite forbids by name.
     Until rev51 this step tested `current_phase >= 6` alone. the record's schema uses
     `current_station`, so the condition was **unevaluable for every batch in that project and
     always had been** — it never failed, never passed, and never ran (`S-4`).
   - **SUPERSEDED** → `state.json` cannot speak for it. Judge the DIRECTORY: it must hold a closing
     artifact (`05-*`). If it does not, **WARN with what is missing and ask the operator to confirm
     explicitly before continuing** — do not refuse. Recovering a batch that rolled over unclosed is
     the reason the argument exists, and a hard block here rebuilds the wall it was added to remove.
3. **Not already synced.**
   - **ACTIVE** → `obsidian_synced !== true`. If already synced, warn and ask whether to re-sync
     (overwrite).
   - **SUPERSEDED** → `obsidian_synced` is the ACTIVE batch's flag and says nothing about this one.
     **The vault destination folder is the flag**: if it already exists, warn and ask whether to
     re-sync. It is the stronger signal of the two — directly observable, and it cannot be left
     unlanded the way a boolean in a repo file can (C-44).
4. **Ask the user explicitly:** "Have you already done commit/push/merge of this batch to the repo?" If `no`, instruct:
   > "Do commit + push first (and merge the PR if applicable). Then re-run `/dev-flow-sync`. This ensures the documentation in Obsidian reflects code that's already on main."
   > Stop.

## Mode branch — establish the mode FIRST

**ACTIVE** → `state.mode`. **SUPERSEDED** → `state.mode` is single-slot and describes another batch;
read the mode off the directory instead — a `05-close.md` with no `06-docs/` is `core`, a
`05-postmortem.md` with `06-docs/` is `full` — and **state in the report which you inferred and from
what**. If the directory supports neither reading, ask the operator rather than guessing.

- **`mode: core`** → **light sync**: generate **only** the `<batch_id>-README.md` with its frontmatter (step 6's schema, filled from `04-validation.md` and `05-close.md`; `null` for every key those two did not record — **never a key dropped, and no count restated here**) and **skip the artifact copy entirely**. The batch still enters the cross-batch Dashboard without paying for `06-docs/`. The template-completeness detect of step 3 **still runs** over the requirements / review / validation / close roles of the step-4 table. **The `core` run then executes, in order: steps 1 (state/project read) → 2 (destination folder) → 3 (evidence checklist + template-completeness detect) → 6 (generate the index README) → 7 (dashboard) → 8 (record the sync) → 9 (land the `state.json` edit). Steps 4 (artifact copy) and 5 (visual evidence) do not run in `core`.** Until rev56 this read *"then jump to step 7"*, which skipped step 6 — the step that generates the README with its frontmatter contract, and the only artifact `core` produces.
- **`mode: full`** → everything below, unchanged.
- **`mode: fast`** → this command does not apply; the closing artifact lives in the PR/CHANGELOG.

**Respect `artifact_homes`.** Every destination this command writes comes from that block — including the vault ones. **Never write a FLOW ARTIFACT to a path that is not declared there** (`/dev-flow` §*Artifact homes*, that rule's one home and the statement of what it binds), and never copy an artifact whose declared home is the repo: an artifact has exactly one home, and the link crosses by id.

**THIS COMMAND IS THE ONLY WRITER OF THE VAULT — operator ruling `Q22`, 2026-09-11, flow rev72.** `/dev-flow` and `/dev-flow-init` write the repo and the batch record and nothing else; every vault byte in this flow is written here. Two consequences, and they run in opposite directions by mode. In **`full`**, the vault copies of the **PDR, the DDR and the post-mortem** are the **canonical** ones (`artifact_homes.design_pdr` · `design_ddr` · `postmortem`); what sits under `.dev-flow/<batch_id>/` is **local staging**, the input this command publishes from, and staging is not a home. In **`core`**, `.dev-flow/<batch_id>/05-close.md` is **canonical in the repo** and the `<batch_id>-README.md` this command generates at step 6 is a **generated VIEW of it, never a second source** — which is why step 6 fills `null` for every key the close record did not record rather than inventing one. When a view and its source disagree, the source is true; when a staged file and its published copy disagree in `full`, the published copy is true and the staging is stale. See `/dev-flow` §Artifact homes for the table.

## Actions

1. Read `state.project` and `state.language` from `state.json` (project identity is carried across
   batches, so it is the same for both cases), take `<batch>` and the mode from the two sections
   above, and read `artifact_homes`. **For a SUPERSEDED batch use `artifact_homes` only for the
   repo-vs-vault HOME decision, never for its paths** — its `<batch_id>`-templated entries were
   re-pointed at the active batch by the rollover.
2. **Destination folder:** `<vault_root>/<project>/dev-flow-batches/<batch>/`, where `<vault_root>`
   is the **`vault_root` row of the flow's deployment record** — the per-installation file of the canonical home that already declares
   this installation's per-machine paths. **That row is the definition of the `vault:` prefix** used
   throughout `artifact_homes`; resolve every `vault:` path against it and nothing else.
   - **If no `vault_root` row is declared, STOP and ask the operator for it.** Do not guess a path,
     and do not reuse one seen in another project. Until rev56 this step named one operator's
     absolute Drive path, so any other installation of this flow would have written into that
     operator's vault — an installation-specific fact living inside portable flow content, which is
     the defect the flow home's per-installation deployment record exists to prevent (*"a per-installation fact cannot live in a shared
     identity"*).
   - If the project folder under `<vault_root>` doesn't exist, **ask** before creating it.
   - `03-increments/` does not reach the vault (convention since batch-04). It is excluded by
     step 4's `repo:`-home rule rather than by name, so the convention holds without a second,
     drift-prone statement of it.
3. **Evidence-checklist check (before copying):** confirm each phase artifact carries its completed evidence checklist (each item ✓/✗ + one-line evidence). If any artifact is missing its checklist or has unchecked / evidence-less items, **WARN and list them** — the phase gate should have caught this; surface it, don't sync an incomplete record silently.
   - **Template-completeness DETECT (automated reject-check — RC-S1 backstop, not prose):** before copying, run a STRUCTURAL detect on each artifact to sync (the requirements / review / validation / close roles of the step-4 table, plus `06-docs`, matched by the same prefix families and never by basename). **Match unfilled *structure*, NOT token substrings** — legitimate prose, code fences, and frontmatter schema examples quote placeholder tokens (the batch-15 `<P>` / `TC-NNN` false positive). For each artifact:
     1. **Empty required structure → BLOCKER:** a required table reduced to its header + separator row with zero data rows — **and note the trap this arms:** since rev56 the templates prefix their illustrative rows with `*(example — delete)*`, so an author who deletes the only marked row of a **required** table produces exactly the header+separator shape this rule BLOCKs on. Delete the marker and fill the row; delete the row only when another data row remains; a required `##`/`###` section whose body is empty or contains ONLY the template's italic guidance `*(…)*`; a validation artifact carrying no verdict token (`PASS` / `FAIL` / `PASS-WITH-NOTES`) AND no per-requirement results table.
     2. **Live placeholder tokens → BLOCKER:** `<PROJECT>` / `<BATCH_ID>` / `<Short title>` / `<role>` / `<goal>` / `<str>` / `<N>` / `<YYYY-MM-DD>` appearing as the ACTUAL value of a heading, field, or table cell — NOT inside a backtick span, a fenced code block, or a frontmatter `schema` example.
     3. **Verify before blocking (anti-false-positive):** a raw grep hit for a placeholder token is a HINT only — confirm it sits in a live field, not quoted guidance, before declaring a blocker. Record hits that resolve to quoted-guidance as "checked — false positive" and do NOT block on them.
   - On a real blocker: **STOP, do not copy, and report the artifact + exact section/row/line.** **The id is `RC-S1`, not `RC-1`, and that is a naming ruling, not a note:** `RC-1` is the base-currency gate of `/dev-flow` §Phase 0, it holds that sense at 21 other sites in the flow (measured 2026-09-03), and **one token cannot carry two different reject-checks.** This is the sync-side net. (Origin: the 2026-06-23 black-box audit — see dev-flow-lessons)
   - **Repo-hygiene line (batch-23):** confirm the PRIMARY repo checkout is back on `main` and no stray agent/PR branches remain checked out in any worktree; list any found for the operator (don't switch branches yourself without approval). (Origin: batch-23 — see dev-flow-lessons)
4. **The copy list is DERIVED from the batch directory. It is not named here, and that is the fix.**

   **A silent name mismatch is the defect, not the names.** Until rev51 this step named six paths
   under `.dev-flow/` and three were wrong for this project: `02-review.md` where batch-88 writes
   `02-review-security.md`, and `05-postmortem.md` where batches 86, 87 and 88 all write
   `05-close.md` — so **two artifacts were dropped with no error and no warning**, and the `05`
   mismatch was live for EVERY batch (`S-1`). It named neither `PLAN.md` nor
   `01b-qa-validation-plan.md`, which are in every recent batch and could therefore reach the vault
   by **no mode at all** (`S-2`); it would have missed batch-86's `00-measurements.md` identically.
   And it named paths at `.dev-flow/<file>` while every batch since batch-01 keeps its record in
   `.dev-flow/<batch_id>/<file>`. **Correcting the three names fixes today's batches and leaves the
   next rename to fail exactly the same way, silently.** A list maintained beside the thing it
   describes is the defect `FLOW-VERSION.md` has now recorded five times, and rev15 already ruled on
   it: derived, not maintained.

   **COPY = every file under `.dev-flow/<batch>/`, recursively, MINUS the declared exclusions.**
   Each exclusion is a principle, never a filename:
   - **anything whose `artifact_homes` entry declares a `repo:` home.** An artifact has ONE home
     (C-50) and the link crosses by id. `03-increments/` is excluded by THIS rule and not by being
     named — its home is `repo:.dev-flow/<batch>/03-increments/` — which keeps the vault convention
     since batch-04 without stating it twice.
   - **derived directories** (`_derived/`), regenerated at gates and guarded by `V20`.

   Nothing else is excluded: a file that is in the batch directory is part of the batch record.

   **REPORT = that derived list classified by ROLE, and every unfilled REQUIRED role is a WARN.**
   This is the half a derived list cannot get for free — it can never miss a file that exists, and
   it can never notice one that is absent. **Match by PREFIX FAMILY, never by exact basename:**

   | Role | Prefix under `.dev-flow/<batch>/` | In the record |
   |---|---|---|
   | requirements contract | `01-requirements.md` | required |
   | requirements ledger | `01-requirements-ledger*` | required — the contract says what the batch obliges, the ledger says why. Omitting it syncs the conclusions and drops the reasoning: silent data loss, not a coverage gap |
   | QA / validation plan | `01b-*` | optional |
   | review | `02-*` | required |
   | validation | `04-*` | required |
   | close / post-mortem | `05-*` | required |
   | living plan | `PLAN.md` | optional |
   | phase-6 docs | `06-docs/` | required in `full`, absent in `core` |

   `02-review.md` and `02-review-security.md` both satisfy the review role; `05-close.md` and
   `05-postmortem.md` both satisfy the close role. **A required role that matched nothing is a WARN
   naming the role and the prefix that found nothing — never a silent skip, and never a blocker**:
   the batch record is what it is by the time sync runs, and refusing to copy it helps nobody. An
   absent OPTIONAL role is reported as absent, without a warning. A file matching no role is copied
   and listed under **unclassified** — it is part of the record, and the report says so rather than
   the command deciding on its own that it does not matter.

   The role table drives the WARN in BOTH modes; the COPY happens only in `mode: full`, per the mode
   branch above.
5. **Visual-evidence refresh (conditional — only for projects with a generated-evidence pipeline):** applies when the repo has a generated-evidence suite AND the vault project folder carries a `visual-evidence.md` gallery. **The three values are the PROJECT's, not the flow's** — the suite command, the directory it writes into, and the vault directory it lands in — so the prose below states the MECHANISM and the project states the paths. Skip for projects without a pipeline, and say so in the report rather than skipping silently (`C-55`).
   1. **Trigger check:** refresh if the batch diff touched the project's declared UI surface OR any vault evidence asset predates the batch merge date. If neither, note "visual evidence current — refresh skipped" in the report.
   2. **Regenerate:** run the project's evidence suite from the repo root. All cases must pass — a failing capture is a WARN in the report, never a silent skip.
   3. **Copy:** refresh the vault copies with the helper in the vault `visual-evidence.md` §5 (PowerShell: use `-LiteralPath` — filenames contain `[…]` that otherwise parse as wildcards and the copy silently does nothing). Overwrite in place; delete nothing.
   4. **Stamp:** update the "last refreshed" date line(s) in `visual-evidence.md`.
   5. **Scope guard:** baseline snapshots that require the canonical CI-matching environment are OUT of this step — never regenerate them here (env-sensitive drift; see the snapshot-regen-env rule). Only generated evidence is refreshed.
   - (Origin: the 2026-07-02 visual-evidence audit — see dev-flow-lessons)
6. **Generate index** `<batch>-README.md` in the destination subfolder. It MUST begin with YAML frontmatter (the machine-readable metrics contract — flat, typed, stable keys, for Obsidian Dataview / CSV export), then the human-readable body.

   **Frontmatter schema (fill every key; use `null` if genuinely unknown — never drop a key):**
   ```yaml
   ---
   type: dev-flow-batch
   project: <str>
   batch_id: <str>
   language: en | es
   verdict: pass | iterate
   date_start: <YYYY-MM-DD>     # first decisions_log date
   date_end: <YYYY-MM-DD>       # last decisions_log date
   duration_days: <int>
   iter_total: <int>
   iter_per_phase: "0:_ 1:_ 2:_ 3:_ 4:_ 5:_ 6:_"
   increments: <int>
   cap_trips: <int>
   files_touched: <int>
   findings_blocker: <int>
   findings_major: <int>
   findings_minor: <int>
   caught_p2: <int>
   caught_p3gate: <int>
   caught_p4: <int>
   pct_caught_p2: <float>       # caught_p2 / (caught_p2 + caught_p3gate + caught_p4) × 100 — shift-left signal
   findings_open: <int>
   findings_closed: <int>
   security_findings: <int>
   us_total: <int>
   us_ready: <int>
   us_covered: <int>
   llr_total: <int>
   llr_coverage_pct: <float>
   tests_base: <int>
   tests_deleted: <int>
   tests_added: <int>
   tests_post: <int>
   new_control: <str | none>
   controls_stress_tested: <int>
   open_items_next: <int>
   ---
   ```

   **Data sources (extract, don't invent — leave `null` if an artifact didn't record it):**
   - **project, language** → `state.json` (carried across batches, so correct in both cases).
   - **batch_id** → `<batch>`, as resolved by §Argument.
   - **iter_per_phase, iter_total, and the `decisions_log` dates** → for an **ACTIVE** batch,
     `state.json`. For a **SUPERSEDED** batch those fields are single-slot and describe the active
     batch: read the decisions from `.dev-flow/<batch>/decisions-log.json`, the archive §Batch
     rollover writes, and take the iteration counts from `PLAN.md`. **A batch superseded before
     rev51 has no archive.** Then set `date_start` / `date_end` / `duration_days` / `iter_*` to
     `null` and say so in the report — recovering them means reading
     `git show <merge>:.dev-flow/state.json` by hand, and a plausible date is worse than a missing
     one.
   - the **validation** artifact (`04-*`) → verdict, tests_base/deleted/added/post.
   - the **review** artifact (`02-*`) → findings_blocker/major/minor, caught_p2, security_findings.
   - `03-increments/` → increments, cap_trips, caught_p3gate, files_touched.
   - the **close** artifact (`05-*`) → caught_p4, findings_open/closed, new_control,
     controls_stress_tested, open_items_next.
   - `06-docs/traceability-matrix.md` → us_total/ready/covered, llr_total, llr_coverage_pct.

   **Body (below the frontmatter):**
   - Title: project + batch_id + batch objective.
   - Executive summary (3 lines from `executive-summary.md`).
   - Obsidian wikilink-style links to each artifact: `[[01-requirements]]`, `[[traceability-matrix]]`, etc.
   - Decision table from `decisions_log` (phase, date, decision, notes).
   - **Evidence-checklist summary:** per phase, completion (e.g. `P2 review 5/5 ✓`, `P3 increments N/N ✓`, `P4 validation 7/7 ✓`).
   - **## Batch metrics** — human-readable tables rendered from the frontmatter values above: Throughput · Quality/shift-left · Coverage · Process maturity.
   - **Cross-batch note** + live Dataview query:
     > "Queryable across batches via Dataview:"
     > ```
     > TABLE verdict, pct_caught_p2, llr_coverage_pct, open_items_next, duration_days
     > FROM "01 - Proyectos"
     > WHERE type = "dev-flow-batch"
     > SORT batch_id DESC
     > ```
7. **Ensure the cross-batch dashboard.** In the vault's `<project>/dev-flow-batches/` directory, if the cross-batch dashboard document does not exist, create it with the Dataview query from step 6 (tabulating all `type: dev-flow-batch` READMEs). **Its name is the installation's own choice** — this flow ships no vault and names no document there; whatever the vault already calls it is the name. Never overwrite an existing one — the user may have customized it.
8. **Record the sync — and WHERE depends on the case.**
   - **ACTIVE** → update `state.json`: set `obsidian_synced: true` and append to `decisions_log`
     `{"station": "P6", "date": "<YYYY-MM-DD>", "decision": "synced-to-obsidian", "notes": "<destination path>"}`.
   - **SUPERSEDED** → **do not touch `state.json`.** Both fields belong to the active batch, and
     writing them would make the live batch's record assert a sync it never had — the C-43 failure,
     caused by the very single-slot property this argument exists to work around. The vault
     destination folder is this batch's sync flag (pre-requisite 3), so the sync leaves no on-disk
     flag in the repo, and the report says that explicitly.
9. **LAND that `state.json` edit — C-44 (ACTIVE case only; a SUPERSEDED sync makes no such edit).** Setting the flag is not the same as persisting it. **Commit the `state.json` change and confirm it reaches `origin/main`** (merged, not merely pushed to a branch); if it cannot land immediately, say so explicitly and record the branch holding it. **Then re-read `origin/main`'s copy and confirm `obsidian_synced` is actually `true` there** — the step-3 pre-requisite reads the LOCAL file, so an unlanded sync leaves `origin/main` asserting the batch was never synced, and the next reader believes it. *(Origin: the unmerged close-out that made `origin/main` deny a finished sync — see dev-flow-lessons)*

## Report to user

Report:
- **Which batch was synced and how it was resolved** — argument or `state.json` — and whether this
  was the ACTIVE or the SUPERSEDED case.
- List of files copied with destination paths, **grouped by the role each filled**, plus the
  unclassified ones, plus **every required role that matched nothing** (the step-4 WARN).
- Path of generated index.
- **Visual-evidence freshness (reject-check):** for projects with a generated-evidence pipeline, after step 5 ran (or was skipped) verify no vault evidence asset still predates the batch merge date. If any does, **WARN loudly with the stale file list** — do not report the sync as clean. (This is the check that would have caught the 2026-05-22→2026-07-02 staleness at batch-05 instead of a manual audit.)
- **Final suggestion:**
  > "Open Obsidian. Verify the `<batch_id>-README.md` index links correctly from the project root note. If your root note doesn't link to the new batch, add it manually — I don't touch notes I didn't create."

## Restrictions

- **Only write inside the batch subfolder** — with ONE exception: the step-5 visual-evidence refresh may overwrite the project's own generated-evidence assets and the refresh-date line(s) of `visual-evidence.md`. Nothing else outside the batch subfolder.
- **Do not delete anything** in the vault — only create new files (or overwrite if re-sync is confirmed).
- **Do not run git operations.** Sync assumes the user has already committed/pushed.
- **Never write to `state.json` for a batch it does not declare.** Every field in it except
  `project`, `language` and `mode_history` is single-slot.
- **Do not modify the project's root note in Obsidian** — suggest changes to the user, do not apply them.
