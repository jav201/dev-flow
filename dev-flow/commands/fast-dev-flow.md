---
description: Fast development flow for own repos — 3 compressed phases (minimal spec → supervised implementation → validation + close). Balances speed and quality without skipping security.
---

# /fast-dev-flow

A compressed engineering flow for own repos: minimal spec → supervised implementation → validation + close. Built for 30-90 minutes of work that wants discipline without the full V-model ceremony of `/dev-flow`.

**How to read this file: top to bottom, in order.** When a step says *open X §Y*, that section is the operative rule's one home — open it, follow it, come back here. **Every path this file names outside your project — `templates/…`, `agents/…`, `scripts/…`, `SKILL.md`, `FLOW-VERSION.md` — is FLOW-RELATIVE: written from the flow's own root, in the layout the published bundle uses.** In that bundle the root is the `dev-flow/` folder this command was installed from, and it holds `SKILL.md`, `FLOW-VERSION.md`, `scripts/` and the rest. `/dev-flow` §*Where the flow's own files live* is that rule's one home and names where the canon↔bundle pairing is machine-readable; if a path below does not resolve from your install, resolve it there first. Paths inside your project are relative to the project root.

## When to use this flow

The canonical routing matrix lives in `/dev-flow` ("When to use this flow"). This command is the **"small feature / risky refactor / non-trivial fix"** lane:

```
Trivial fix (typo, one-liner)?              → work directly, no flow
Client deliverable / regulated context?     → /dev-flow (full V-model)
Spike / exploratory experiment?             → free, no ceremony
Anything else (small feature, risky         → HERE (/fast-dev-flow)
refactor, non-trivial fix, internal improvement)
```

If invoked for a case that doesn't fit, warn and suggest the right route.

## Language of artifacts

If the user hasn't specified the development language, **ask** — one short question — before generating the spec. Default English; Spanish when requested. The spec and closing artifact are produced in that language; this command's instructions stay English.

## Communication style

BLUF / inductive: lead with the conclusion, then context. Technical, concrete, concise.

## Notice convention

`⚠` **yellow — notice**: does not block, obliges you to DECLARE the reason in the artifact. · `✗` red — **block**. · `✓` green — satisfied **with its evidence cited**; without a citation it is asserted, not satisfied. A notice that repeats for three consecutive batches becomes a rule or is retired — decided at the close. (Canonical statement in `/dev-flow`.)

## The reader's map — one row per step, and where its operative rule lives

Every operative rule of a fast batch has exactly ONE home. This table names, for each step, the file and section that holds it, the reserved field(s) the step produces — the names a rule parses literally — and the gate the step belongs to. Read it once before Phase A.

| Step | The rule's ONE home | Reserved field(s) it produces | Gate id |
|---|---|---|---|
| Pre-check 3 — declare the batch (`scripts/devflow-init-fast.py` writes it) | `commands/dev-flow-init.md` §*The `fast` declaration* | `mode` · `batch_id` · `flow_version` · `stations_active` · `guided` · `artifact_homes` | `A` |
| Every gate — the guided first run, when `guided: true` | `SKILL.md` §*Guided first run* | one `decisions_log` entry per gate, carrying `gate` and `guided: true` | `A` · `increment-NNN` · `C` |
| Pre-check 4 — create the declared homes | `commands/dev-flow-init.md` §*Actions* | — (directories and the backlog lane) | `A` |
| Pre-check 5 — runtime absences | `SKILL.md` §*What refuses an invocation here* | the absences, named in the spec's §0 | `A` |
| Pre-check 6 — run the gate command, which is not an approval | `SKILL.md` §*What refuses an invocation here* | the verdict, recorded in the spec's §0 gate record | `A` |
| Phase A · 2 — write the spec | `templates/fast-dev-flow/spec-template.md` §*0. Batch header* | `Batch` · flow revision · base ref · `PULL` outcome · standing authorization | `A` |
| Phase A · 4 — acceptance criteria | `templates/fast-dev-flow/spec-template.md` §*3. Acceptance criteria* | `AC-<n>` | `A` |
| Phase A · 5 — Information Flow Contract, Part A | `templates/fast-dev-flow/spec-template.md` §*3c. Information Flow Contract* | `SOURCE` · `NODES` · `SINK` · `owner : AC-<n>` | `A` |
| Phase A · 6 — sensitive-pattern scan | `commands/fast-dev-flow.md` §*Patterns that trigger `security_required`* | `security_required` | `A` |
| Every gate — premises | `commands/fast-dev-flow.md` §*Premise evaluation at every gate* | one verdict per premise, in the spec's §3b | `A` · `increment-NNN` · `C` |
| Phase B · 1 — security pass, if fired | `agents/security-reviewer.md` §*Output format* | the four answers, in the spec's §6 | `increment-NNN` |
| Phase B · 2 — implement under the budget | `agents/software-dev.md` §*Hard caps* | `SOURCE files` | `increment-NNN` |
| Phase B · 3 — the packet, per increment | `templates/fast-dev-flow/increment-template.md` §*4 · Test results* | `RED counterfactual` · `Reverse census` · `Mutation verdicts` · `Instrument RED-proof` · `Emitted-form assertion` · `Correction population` | `increment-NNN` |
| Phase B · 3 — the packet's evidence (`scripts/devflow-evidence.py` prints the rows) | `templates/fast-dev-flow/increment-template.md` §*Evidence files* | `Evidence files` | `increment-NNN` |
| Phase B · 3 — the packet's review cell | `templates/fast-dev-flow/increment-template.md` §*4b · Independent review* | `Independent review` | `increment-NNN` |
| Phase C · 1 — validation pass | `agents/qa-reviewer.md` §*Output formats* | the per-criterion verdicts, with their evidence states | `C` |
| Phase C · 1 — naming a result's state | `commands/dev-flow.md` §*Evidence states* | the state of every result reported, from that table's seven — named there and nowhere else | `C` |
| Phase C · 4 — closing artifact | `templates/fast-dev-flow/spec-template.md` §*8. Close* | the close block, and the spec marked `closed` | `C` |
| Phase C · 6 — backlog reconciliation | `commands/dev-flow.md` §*A deferral carries the marker* | `⏸ DEFER` | `C` |

> **THE `Gate id` COLUMN IS WHERE THE THREE GATE NAMES ARE DECLARED, AND IT IS THEIR ONE HOME.** A `fast` batch has exactly three gates, spelled `A`, `increment-NNN` and `C` — the per-increment gate carries its own number, so a batch with two increments writes `increment-001` and `increment-002`. These literal strings go in the `gate` field of each `decisions_log` entry, and `V55` accepts them and nothing else: `Phase A` is not `A`. In `core` and `full` the gate's name is its station id — see `SKILL.md` §*Guided first run*.

## Pre-checks

**These pre-checks ARE this mode's init — do not run `/dev-flow-init` as a separate act.** They read two blocks out of that file (the six-key declaration and the two creation steps) instead of running it.

1. Verify you are at a project root (signals: `.git/`, `package.json`, `pyproject.toml`, etc.). If unclear, **ask**.
2. If `.fast-dev-flow/` does NOT exist, the init script in pre-check 3 creates it — nothing to make by hand. If it already exists with an unclosed prior spec, warn and ask whether to resume or start fresh (archiving the previous one as `.fast-dev-flow/archive/<timestamp>-spec.md` — the script's `--force` does that for you).
3. **Declare the batch — run `python <the flow root>/scripts/devflow-init-fast.py` FROM YOUR PROJECT'S ROOT.** With no argument the script takes the current working directory as the project root, prints the absolute root it resolved on its FIRST line, and **refuses the flow's own folder** (exit 2, nothing written) — so the one way to get the wrong tree is to read past a line naming it. Name the root as an argument instead when you cannot `cd` to it. This sentence is that invocation's ONE home; the script's own `--help` carries the rest. It writes what `commands/dev-flow-init.md` §*The `fast` declaration* specifies — that section is the six keys' one home and this command does not restate them — filling every placeholder as it writes, the `<batch_id>` inside BOTH `artifact_homes.increments` and `artifact_homes.evidence` included: a bracket left in place is a literal directory name, not a default. It refuses to overwrite an existing batch unless `--force`. Lightweight means few artifacts, not no declaration: measured on a state-less `fast` tree, THIRTEEN rules — `V27`, `V28`, `V31`, `V32`, `V36`, `V37`, `V38`, `V40`, `V41`, `V43`, `V44`, `V52`, `V54` — report *read nowhere; this is not a pass*, so the gate exits 0 over a batch it cannot inspect.
4. **The same script creates the homes the declaration names, in the same act** — the two directories `artifact_homes.increments` and `artifact_homes.evidence` name, the backlog lane `artifact_homes.backlog` names (`commands/dev-flow-init.md` §*Actions*, steps 5 and 6), and the evidence home's `-text` mark in `.gitattributes`. Git does not track an empty directory, so the two directories enter the repository with their first content in Phase B; do not plant a `.gitkeep`. Until then `V42` reports that no tracked file falls in the deferral corpus — the honest reading of an empty corpus, not a failure.
5. **If this runtime has no named sub-agent roles and cannot prompt the user, say so once and run the fallback** — `SKILL.md` §*What refuses an invocation here* step 5 is that fallback's one home.
6. **Run the gate now, before Phase A, and read its verdict out loud** — `SKILL.md` §*What refuses an invocation here* steps 1 and 2 are that run's one home: they carry the command, the working directory, and the rule that a non-zero exit is a refusal you stop on. **Add `--brief` to any gate run and it prints the verdict first, then only the BLOCK and NOTICE lines, then one line counting the rest** — the exit code is the same one, so the refusal rule is unchanged; `python scripts/devflow-validate.py --help` is that flag's home and this command does not restate it. This first run proves the TOOL and the bundle — the batch pre-check 3 just declared is read too, and the rules that have no subject on it yet say so; the final gate runs it again over the completed batch record. **Running the command is not an approval**: the `A` gate has exactly one approval moment and it is the Gate paragraph at the end of Phase A.

## Phase A — Minimal spec (5-10 min)

### Actions
1. If the user hasn't given enough context, **ask** in a single short round: objective, loose user stories, what is OUT of scope.
2. Generate `.fast-dev-flow/spec.md` following `templates/fast-dev-flow/spec-template.md` (it ships at that path in the bundle). Its §0 header records the batch id, the flow revision, the base ref, the `PULL` outcome and the batch's standing authorization. **Write the `Batch` row with the id pre-check 3 declared**: `.fast-dev-flow/spec.md` is single-slot and `state.json` is not, so that row is what tells `V45` and `V55` this spec is THIS batch's record and not the previous one's.
3. **If the design decision is not obvious** (e.g. structural change, new integration, real ambiguity), briefly delegate to `architect` for a 1-2 paragraph recommendation. If it's obvious, do NOT delegate — unnecessary overhead.
4. Write **observable acceptance criteria**. Pattern: `When <input>, the system shall <observable output>`. Don't write "the system works well" or similar. **If it's not observable, it's not a criterion — it's a wish.**
5. **Information Flow Contract — Part A ONLY (`C-54`), written into the spec's §3c, which is that block's home in this flow.** Declare the flow this change touches. `templates/ifc-template.md` §1 is the grammar's one home and the spec's §3c ships that same fence, field for field — `SOURCE → NODES → SINK`, one field per line, a node beginning at `- fn :`. **`owner` here is an ACCEPTANCE-CRITERION id — `AC-<n>` from §3 — and never an invented `LLR-`**: the full flow owns an LLR, this flow mints none. **Part B — addresses, `cardinality`, `consumers` — is NOT owed here.** Its trigger question is this phase's escalation signal: if the change alters *how a consumer reaches* something rather than *what it carries* — a selector, an index, a channel, an offset — stop and run `/dev-flow` instead.
6. **Scan the spec for sensitive patterns — a scanner ships with this flow and you run it:**
   ```
   cd <the flow root>                 # the FLOW ROOT — see the opening
   python scripts/devflow-scan-spec.py <the project root>/.fast-dev-flow/spec.md
   ```
   Same working directory as the gate command (`SKILL.md` §*What refuses an invocation here* step 1), so one `cd` serves both tools. With NO argument the scanner reads `.fast-dev-flow/spec.md` under the CURRENT directory. **Exit `0` means nothing fired, `1` means at least one pattern fired — a verdict, not a breakage — and `2` means the scan could not run and claims nothing about the spec.** Copy the printed flags into section 6 of the spec; if at least one fired, set `security_required: true`. **The section below is the pattern list's one home and the script reads it from here at every run** (`C-50`) — deleting a pattern here stops the scanner matching it.

### Patterns that trigger `security_required`

**SCOPE — sections 1–4 of the spec** (objective, user stories, acceptance criteria, validation strategy), and **nothing else — §3b AND §3c INCLUDED IN THAT EXCLUSION**. §6 is where the answer is written, §0 and §7–8 are the record OF the batch, §5 is the non-goals list — the one section where naming a sensitive surface means the opposite of touching it — and §3b/§3c hold commands, digests and the change's own vocabulary. The four scanned sections are the ones a human WROTE ABOUT THE CHANGE.

**WITHIN THOSE FOUR SECTIONS THE SCAN READS AUTHORED TEXT, NOT THE SCAFFOLD.** A `<…>` span is skipped **only while its contents are still the template's own words**, exactly as `templates/fast-dev-flow/spec-template.md` ships them — an unfilled placeholder is the template talking, not the author. **The moment you type your own words between the brackets, it is authored text and it is scanned** — otherwise leaving two characters in place would switch the security scan off. Deleting the brackets is tidier and changes nothing.

**MATCHING — case-insensitive, on WORD BOUNDARIES, never as a substring — written `(?<!\w)<pattern>(?!\w)`.** ⚠ **Not `\b<pattern>\b`** — a pattern that BEGINS with a non-word character can never match under `\b`, and `.env` is on the list below. A substring match fires `form` inside the mandatory *In**form**ation Flow Contract* and `auth` inside `author`, which sets `security_required: true` on every conforming spec.

**FOUR CONTROLS, run before the scan's own verdict is believed** — the probe must be shown able to return every answer it can return (`C-55`'s rider):

- **Positive:** `session token` in a criterion **FIRES** (`session`, `token`).
- **Negative:** `Information Flow Contract` anywhere in sections 1–4 **DOES NOT FIRE** — no bounded pattern matches it.
- **Placeholder:** `As a <role>, I want <goal>, so that <benefit>` — the template's own untouched words — **DOES NOT FIRE**. The same line with the brackets removed **FIRES** (`role`), which is what makes the skip a rule rather than a hole.
- **Authored-in-brackets:** `When <a session token expires>, the system shall <re-issue it>` **FIRES** (`session`, `token`). The brackets are still there and the words inside them are yours, so the scan reads them.

A scan that cannot produce the negative is matching as a substring; a scan that cannot produce the placeholder pair is reading the scaffold; a scan that cannot produce the authored-in-brackets answer has turned the skip into a hole; a scan that cannot produce the positive is not running. Report all four with the flags.

**KEEP PROCESS PROSE OUT OF THE FOUR SCANNED SECTIONS.** A sentence about how the batch was RUN — *"the `qa-reviewer` role was self-executed"* — trips `role` or `auth` and sets the flag on work that touches no sensitive surface. Put the process note in §7 or §8, which are out of scope; if it belongs in §1–§4, declare the flag and answer Phase B step 1's four questions.

**A FLAG ON ORDINARY VOCABULARY IS STILL A FLAG — declare it, never reword around it.** If a criterion trips a pattern without touching a sensitive surface, the answer is to set `security_required: true` and answer Phase B step 1's four questions, not to reword the spec until the scan goes quiet. A scan an author can phrase their way past is the control failing in the expensive direction (`C-53`).

Patterns — case-insensitive, bounded:

- **Auth / identity:** `login`, `logout`, `signin`, `password`, `token`, `jwt`, `oauth`, `oidc`, `saml`, `session`, `cookie`, `auth`, `authn`, `authz`, `permission`, `role`, `rbac`, `mfa`, `2fa`
- **Secrets / config:** `secret`, `apikey`, `api_key`, `api key`, `.env`, `env var`, `credential`, `vault`
- **External integrations:** `webhook`, `composio`, `mcp`, `n8n`, `third-party`, `external api`, `sdk`
- **Sensitive data:** `pii`, `personal data`, `payment`, `credit card`, `billing`, `gdpr`, `ccpa`, `hipaa`, `encrypt`, `decrypt`, `hash`
- **Destructive DB:** `drop table`, `delete from`, `truncate`, `migration`, `schema change`
- **Input / surface:** `user input`, `file upload`, `form`, `sanitize`, `escape`, `xss`, `sqli`, `csrf`, `ssrf`, `cors`
- **Network / exposure:** `expose`, `public endpoint`, `new route`, `webhook receiver`

Any match → `security_required: true`. Report to the user which flags fired and why.

### Gate
- Present the full spec (summary).
- List detected security flags (if any).
- Ask for approval: `approve` / `iterate` / `cancel`.
- **Do not advance to phase B without explicit approval.**
- **If `state.json` declares `guided: true`, this is a GUIDED gate and takes four further steps before it closes** — `SKILL.md` §*Guided first run* states them and is that gate's ONE home. `V55` reads the ledger they leave.

## Phase B — Supervised implementation (the bulk)

### Actions
1. **If `security_required: true`**, BEFORE any code, run the four questions below and record their answers in the spec's §6 risk summary. Delegate the pass to `security-reviewer` (`agents/security-reviewer.md`); where no named roles exist, execute that role's text yourself and record that you did (`SKILL.md` §*What refuses an invocation here* step 5).
   - **New outbound surface?** Name every external system this change can now reach, and who authorized each. A tool that can act on an outside system is a decision, not a dependency.
   - **Secrets?** Name where each credential is read from, and show that none is written into the repository, the artifacts or a transcript. `not-run` is not an answer here; `none — this change reads no credential` is.
   - **Blast radius?** Name what this change can destroy or expose if it is wrong — data, accounts, published surface — and what bounds it.
   - **Authorization?** Name the narrowest permission the change actually needs, and say whether it asks for more.
   - Report the identified risks and, unless the batch carries a standing authorization covering them, ask for confirmation before proceeding.
2. Delegate to `software-dev` (`agents/software-dev.md`), under the budget and the packet obligation below.
3. **Hard constraints:**
   - **≤4 SOURCE files per increment. Tests are NOT capped**; product docs and `.fast-dev-flow/**` are outside the count. **⚠ at exactly 4** — declare in the packet why it could not be cut smaller; exceeding 4 does not auto-block but must be declared. **No total ceiling** (a total cap penalises writing tests). **Precedence:** inside a batch of either flow THIS budget governs; outside a batch, your runtime's own standing development rule does.
   - **Review packet at the end of EACH increment, following `templates/fast-dev-flow/increment-template.md` — the SHORT packet, which is this flow's own — written into the home `artifact_homes.increments` declares** (`.dev-flow/<batch_id>/03-increments/increment-NNN.md`). Every row in it is read by a rule that evaluates on a `mode: fast` tree, and nothing else is in it. The long `templates/increment-template.md` stays for `core` and `full`. **Mark the evidence home `-text` in `.gitattributes` before the first evidence file lands** — the packet's §*Evidence files* is that rule's one home and says why.
   - Tests written in the same increment as the code they cover.
   - No abstractions, helpers, or features not derivable from an approved acceptance criterion.
4. **Gate per increment:** the user approves before advancing to the next. **If `state.json` declares `guided: true`, this is a GUIDED gate and takes four further steps before it closes** — `SKILL.md` §*Guided first run* states them and is that gate's ONE home; the last of those four steps writes this gate's `increment-NNN` entry in `decisions_log`, and you write it as the gate closes rather than at the end of the batch. `V55` reads the ledger they leave.
5. The phase ends when all acceptance criteria are covered by code + tests.

### Difference vs `/dev-flow` phase 3
- Here we don't require formal TC-IDs. Each test maps to an acceptance criterion by name or reference.
- **`state.json` is DECLARED and not MAINTAINED** — the six keys of pre-check 3 are written once and never advanced: no `current_station`, no `iterations_per_station`, no `phase_status`, and **no `decisions_log` UNLESS `guided: true`**, the one key that asks this flow to write the ledger back — one entry per gate, and nothing else in it (`SKILL.md` §*Guided first run*). Progress lives in the conversation, the commits and the spec's own status table.
- Code review is **lightweight**: a quick self-review, or a single `code-reviewer` pass on risky increments — not a mandatory per-increment gate like `/dev-flow`.
- **`tester` assignment is LIGHT here, and light means USUALLY ABSENT.** `software-dev` writes its own tests and **no delegation is owed**. Delegate to `tester` in this flow for exactly one case: an **escaped regression**, where the deliverable is the RED-on-base capture and the author of that capture should not be the author of the fix. Everything else belongs to `/dev-flow`.
- **A standing authorization is not re-asked.** If the batch already carries one, an agent proceeds inside its scope and neither re-requests it nor widens it; see `/dev-flow` §Batch-kickoff authorization, which is that rule's one home.
- **Evidence states:** every result this flow reports names its state from `/dev-flow` §*Evidence states* — `planned` · `executed` · `approved` · `failed` · `blocked` · `not-run` · `n/a — <reason>`. **A planned test is not a run one**, and the compressed flow does not get a compressed vocabulary.
- **Where `dev-flow-lessons` encourages more than this mode owes — a mutation battery, a reverse census — the mode is the authority in a fast batch**: the packet's declared empties are the truthful fast answer, and work done anyway is recorded as a real answer (the packet's §4 says which).

## Phase C — Validation + close (5-15 min)

### Actions
1. Delegate a light pass to `qa-reviewer`:
   - **The suite run is the ORCHESTRATOR's**, and `qa-reviewer` reconciles its output and **names who executed it** — a backgrounded suite outlives the sub-agent that launched it, so a `qa-reviewer` that reports pass/fail is reporting a result it consumed.
   - Verify acceptance criteria one by one (manual smoke if applicable), each carrying its evidence state.
2. **Coverage-claim discipline:** before reporting an acceptance criterion as "covered by test", confirm the named test function exists on disk (`Glob` / read the file). Coverage signed off from intent rather than the artifact is a false claim.
3. **If `security_required` was true**, final security pass:
   - Confirm the risks identified in phase B were mitigated.
   - If risks remain open, list them as pending in the close.
4. Produce the **closing artifact** — a markdown block ready to paste into the PR description or CHANGELOG:
   - **What changed** (1 paragraph).
   - **How it was tested** (list of tests + manual smoke performed).
   - **Open risks / pending** (if any).
   - **Security flags fired and how they were handled** (if applicable).
   - **Suggested commit message** (short, imperative).
5. Update `.fast-dev-flow/spec.md`, marking the spec `closed` with the date — the word goes in the **`Current phase`** cell of the spec's §7 status table, and **that cell is the close signal `V55` reads**: while it says anything else AND the ledger records no `C` decision, the `C` gate is one the batch has not reached and the rule excuses it instead of judging it. **Two witnesses, either one sufficient** — the cell, and a `decisions_log` entry naming `C`; the rule prints which one it used.
6. **Backlog reconciliation (MANDATORY — the carry-over contract).** Reconcile the project's canonical cross-batch backlog — **the file, or lane files, that its `docs/engineering-rules.md` designates; absent such a designation, `.dev-flow/BACKLOG.md`** — a prioritized cross-batch queue shared by BOTH flows, already on disk since pre-check 4. If the project routes to lanes, resolve the routing BEFORE you read anything and reconcile the lane this batch belongs to — `/dev-flow` §*Phase 0* Input is that ordering's one home — and create the lane now if pre-check 4 did not. Then: (a) mark every item this batch shipped `DONE` with its PR/SHA; (b) **carry forward, drop nothing** — append every open item plus every new carry / deferred finding / "Open risks / pending" from the closing artifact; (c) bump the recorded base ref + a "last refresh: <date>" line. **A deferral written anywhere carries the `⏸ DEFER` marker, and this step reads the census** — `V42` reports every marker keyed to no backlog entry; see `/dev-flow` §*A deferral carries the marker*, that rule's one home. **Include the backlog edit in this batch's commit/PR** so the backlog travels with the code that changed it.

### Final gate
- Present the closing block to the user and ask for confirmation to mark the batch complete.
- **Record the `C` decision, then run the gate.** If `state.json` declares `guided: true`, this is a GUIDED gate and takes four further steps before it closes — `SKILL.md` §*Guided first run* states them; at THIS gate they run in the order that section gives, so the `decisions_log` entry naming `C` is written BEFORE the closing run, not after it. Then — run the gate again now; it reads the batch this time:
  ```
  cd <the flow root>                 # the FLOW ROOT — see the opening
  python scripts/devflow-validate.py <the project root, as an absolute path>
  python scripts/devflow-validate.py --brief <the project root>   # the same verdict, only the lines that ask something
  ```
  The run at pre-check 6 read a batch that had just been declared and nothing else; this one proves the BATCH, because the packets and the evidence now exist for the rules to read as well. Record its verdict in the spec's §0 gate record.

## Escape hatch — promotion to `/dev-flow`

If during any phase you detect the batch grew beyond fast scope (e.g. more than 3 increments in phase B, serious requirements ambiguity, sustained scope drift), **stop and report**:

> "This batch exceeded fast-dev-flow scope. I recommend promoting to /dev-flow for formal traceability and validation. Do I proceed? On approval I run `/dev-flow-init --mode core` (or set the `mode` field in `state.json`) and continue — **nothing is archived, nothing is migrated, no history is lost**."

Do not promote without explicit approval. Project-level V-rules apply at and after promotion; where the runtime has the flow-guard hook, it blocks either flow on a BLOCK from `V7`, `V15` or `V16`.

## Premise evaluation at every gate (C-43, compressed)

At each of the three gates, alongside checking the work against the spec, **evaluate the PREMISES the stage rests on as explicit propositions.** Checking work against a spec answers *"does this match?"*, not *"is what the spec ASSERTS ABOUT THE WORLD true?"* — a stage can be perfectly compliant with a false premise. Verdicts: ✅ **TRUE** (an **executed** probe — command output, a `file:line`; citing another document is NOT evidence) · ❌ **FALSE** (counterexample recorded — blocks) · ❓ **UNDECIDABLE** (missing verification, or the requirement is ambiguous/incomplete — blocks until decided or declared out of scope in writing).

**Three tiers.** **Axioms** = requirements already validated AND verified — law by default, but **re-openable** on an executed counterexample or a logical invalidation (in practice almost always **INCOMPLETENESS**); a successful challenge **ENLARGES** the requirement, never deletes it. **Hypotheses** = what this batch introduces, *including anything inherited from a prior design batch* — written down ≠ verified. **Premises** = claims about the world (symbols, line numbers, sizes, "X already exists") — executed against disk, never trusted.

**ARTIFACT** — a short premise table in `.fast-dev-flow/spec.md`, added at Phase A beside the acceptance criteria: `| Premise | Tier | Verdict | Executed evidence |`. Four columns, one row per premise. Without the table the control degrades to *"I thought about it"*; with it, the next session can re-check the batch's foundations in seconds.

This is the cheapest control in the fast flow: it is greps and one-line probes, and it runs before any code is written.

## An emptiness is doing work — say which kind (C-55, compressed)

**Whenever a claim or a guard depends on the tree containing NO instance of some case, that emptiness is LOAD-BEARING and must be declared.** C-40 asks whether a predicate *can* go red; C-43 asks whether a premise is *true*; C-55 asks what the result is resting on that is only accidentally the case right now.

**Limb 1 — the emptiness is the FINDING.** If the batch's result is an *absence* ("no X exists", "the blind spot is empty"), the property that made the search wide enough is **part of the result**. A negative result is sound only if the search was too WIDE; narrow it later and every derived claim weakens with the suite green. Guard the over-breadth and **say in the guard's own docstring that it protects a conclusion, not a behaviour** — otherwise the next reader files it as an implementation detail and "improves" it.

**Rider — an absence is admissible only if the probe can produce a NON-absence.** Run the same probe, unmodified, over a case known to be present. **Uniformity over heterogeneous inputs is the TRIGGER for that control, never the verdict** — the correct answer can be uniform too, and treating it as a verdict false-fails correct work, which **C-53** prices as high as passing wrong work. If no known-present case can be built, **say so and downgrade the claim**.

**Limb 2 — the emptiness is an ACCIDENT of today's data.** A guard clause that is a **no-op on the current tree** is untested however green the suite, and the tell is that mutating it changes nothing. Two consequences: **a conjunctive criterion needs one mutation per conjunct**, and **mutating a stage is not mutating the pipeline**.

**DISCHARGE — a synthetic instance, not an argument.** Construct the case the tree lacks (a fixture tree, an in-memory module) and assert against it. "There are none today" is the reason the guard is needed, never a reason to skip it.

**ARTIFACT** — one line per load-bearing emptiness in the spec's premise table (**§3b** — §6 is where the security-flag answer is written and holds no premises), tier `PREMISE`, with the synthetic instance as its executed evidence.

## The flow is a SHARED asset — changes flow both ways (C-45, compressed)

A control is discovered in one project but is **not that project's property**. Portable ones must reach every project running this flow, or each re-learns the same lesson at full price.

**PUSH** — a portable control is not encoded until it lands upstream: the **command** (the rule) · its **artifact** (a template section) · the **catalog** entry (`dev-flow-lessons`, with the measured origin) · **committed and pushed**, SHAs recorded at the close. Per **C-44** an unpushed control is indistinguishable from one never written. Say which of the four landed — command-but-not-template is *half-encoded*, and the missing half is the enforceable one.

**PULL** — at Phase A, alongside the pre-checks, confirm the local flow files are not behind their remotes. Compare against the published manifest (`FLOW-VERSION.md`, beside the flow's own files): version + per-file SHA256. **A batch run on a stale flow inherits a solved problem as an open one.** Record the flow revision in the spec header next to the base ref.

**On a runtime that has only the published bundle there is no canon remote to be behind, and the honest outcome is `not-run`, never a silent pass.** The manifest travels WITH the files, so comparing it against them proves the copy is internally consistent and says nothing about staleness. Record the currency half in the spec header as **`not-run — no canon remote on this runtime`**, next to the flow revision the manifest declares.

**Classification still decides placement** — portable → the global command; stack-specific → the project's `docs/engineering-rules.md`. Portability is the test, not convenience.

## Session-close working-file reconciliation (C-44, compressed)

**No file this session touched may be left in limbo at its close.** At the final gate, sweep `git status --short` in **every repo touched — including auxiliary repos outside the project tree** — plus any commit that exists but was never pushed, and report each file in exactly one terminal state: ✅ **committed** (and, where it only matters once integrated, **landed**) · 🗑️ **reverted / deleted, deliberately** · 📋 **left in place ON PURPOSE with its path + remaining work written into the canonical backlog**.

**This flow does not DECIDE to run git operations — that is the operator's call, and §*Hard rules* is that rule's one home** (a batch carrying a standing authorization commits as authorized; one without it prepares the change and reports). So C-44 here is a **reporting** obligation either way: produce the reconciliation for the user, name anything unlanded, and **report pre-existing uncommitted changes as found rather than folding them into your own work.**

## Hard rules

- Never advance a phase without explicit user approval — and where the runtime cannot prompt, what stands in its place is the batch's standing authorization, under which the gate records rather than waits (`SKILL.md` §*What refuses an invocation here* step 5, that rule's one home; no second wording of it stands here).
- Never skip security-flag detection — it's part of this flow's value.
- **Never close a HIGH with a recommended fix.** A clean verdict from `code-reviewer` or `security-reviewer` requires the fix **applied and verified**; until then the verdict is the conditional `BLOCK-UNTIL: <finding ids>`, which authorises nothing. This flow is faster, not laxer — see `/dev-flow` §Phase 3 *Independent review*, that rule's one home.
- Never generate the spec without observable acceptance criteria. If the criteria aren't observable, mark the spec invalid and ask the user again.
- Don't touch the Obsidian vault from this flow. Docs live in the repo (PR description / CHANGELOG).
- **Don't DECIDE to run git operations (commit, push, merge) — that is the user's call, and it is a rule about who decides, not a ban on the batch ever being committed.** When the operator has authorized commits for this batch (§*A standing authorization is not re-asked*, recorded in the spec header), commit as authorized. With no such authorization, prepare the change, report it, and let the user commit.
- **Never close a gate without evaluating its premises** (C-43): each is ✅ TRUE with an executed probe, ❌ FALSE, or ❓ UNDECIDABLE — the last two block. A requirement inherited from a prior design batch is a **hypothesis**, not an axiom.
- **Never end a session leaving a touched file in limbo** (C-44): every file is committed-and-landed, deliberately discarded, or recorded in the backlog with its path. Sweep every repo touched, auxiliary repos included; report pre-existing dirt as found, never fold it into your own work.
- **A batch is not complete until the project's canonical backlog is reconciled** (Phase C step 6): shipped items marked done, every carry/finding appended, base ref bumped, and the edit included in the batch's commit. **Every open item lives in exactly ONE canonical file**, and the backlog is shared with `/dev-flow` — a project MAY partition it into lanes (declared in its `docs/engineering-rules.md`), which is a split, not a copy: items MOVE between lane files and are never duplicated.

## Structure created in the project

The real footprint — five required entries plus one optional archive, across BOTH trees (the spec lives in `.fast-dev-flow/`, everything else in `.dev-flow/`):

```
.fast-dev-flow/spec.md                          the spec (Phase A → closed in Phase C)
.fast-dev-flow/archive/<timestamp>-spec.md      closed specs, optional
.dev-flow/state.json                            the MINIMAL fast declaration (pre-check 3)
.dev-flow/<batch>/03-increments/                the review packet per increment
.dev-flow/<batch>/evidence/                     the evidence bytes every digest is cited against
.dev-flow/BACKLOG.md                            the cross-batch backlog, shared with `/dev-flow` (pre-check 4)
```

**`<batch>` is `state.json`'s own `batch_id`, and the two `.dev-flow/<batch>/` paths are the ones its `artifact_homes` declares** — no command writes a FLOW ARTIFACT to a path `artifact_homes` does not declare (`/dev-flow` §*Artifact homes* is that rule's one home); your source and your tests are the WORK, not the record, and owe no key.

Lightweight on purpose: no requirements matrix, no per-phase subfolders, no post-mortem, no vault, and nothing in `.dev-flow/<batch_id>/` but the packets and the evidence.

## Tone

Keep the flow conversational and agile. The philosophy is: spec in 5 minutes, supervised code, clean close. If the user feels you're being slow or heavy, that's a signal you're applying `/dev-flow` overhead here — correct it.
