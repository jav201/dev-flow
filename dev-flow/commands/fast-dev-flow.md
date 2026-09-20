---
description: Fast development flow for own repos — 3 compressed phases (minimal spec → supervised implementation → validation + close). Balances speed and quality without skipping security.
---

# /fast-dev-flow

Intermediate flow between working directly — your runtime's own default, which this flow does not define — and `/dev-flow` (full V-model). Designed for 30-90 minutes of work in own repos where we want minimal discipline without paying the full V-model ceremony.

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

BLUF / inductive: lead with the conclusion, then context. Technical, concrete, concise. **That is the whole of it, stated here**: this flow ships self-contained and inherits no tone from a file it does not carry. A runtime whose own standing instructions say something narrower may follow those; nothing here points at a document you were not given.

## Notice convention (operator-set, 2026-08-10)

`⚠` **yellow — notice**: does not block, obliges you to DECLARE the reason in the artifact. · `✗` red — **block**. · `✓` green — satisfied **with its evidence cited**; without a citation it is asserted, not satisfied. A notice that repeats for three consecutive batches becomes a rule or is retired — decided at the close. (Canonical statement in `/dev-flow`.)

## The reader's map — one row per step, and where its operative rule lives

**POINTERS ONLY. No rule is restated here** (`C-50`): every cell names the ONE file and section
that is that obligation's home, and the last column names the reserved field(s) the step produces
— the names a rule parses literally. Read this once before Phase A and you never have to guess
which of five documents a step's rule is in; the cross-referential sprawl both readers of the
2026-09-19 publication test named is a navigation problem, and this is the navigation.
**Every pointer below resolves to a heading that EXISTS in what this flow ships** — re-derived at
every selftest by `MAP POINTERS-resolve`, which reddens on a file this bundle does not carry and
on a heading no shipped file holds.

| Step | The rule's ONE home | Reserved field(s) it produces |
|---|---|---|
| Pre-check 3 — declare the batch | `commands/dev-flow-init.md` §*The `fast` declaration* | `mode` · `batch_id` · `flow_version` · `stations_active` · `guided` · `artifact_homes` |
| Every gate — the guided first run, when `guided: true` | `SKILL.md` §*Guided first run* | one `decisions_log` entry per gate, carrying `gate` and `guided: true` |
| Pre-check 4 — create the declared homes | `commands/dev-flow-init.md` §*Actions* | — (directories and the backlog lane) |
| Pre-check 5 — runtime absences | `SKILL.md` §*What refuses an invocation here* | the absences, named in the spec's §0 |
| Phase A · 2 — write the spec | `templates/fast-dev-flow/spec-template.md` §*0. Batch header* | flow revision · base ref · `PULL` outcome · standing authorization |
| Phase A · 4 — acceptance criteria | `templates/fast-dev-flow/spec-template.md` §*3. Acceptance criteria* | `AC-<n>` |
| Phase A · 5 — Information Flow Contract, Part A | `templates/fast-dev-flow/spec-template.md` §*3c. Information Flow Contract* | `SOURCE` · `NODES` · `SINK` · `owner : AC-<n>` |
| Phase A · 6 — sensitive-pattern scan | `commands/fast-dev-flow.md` §*Patterns that trigger `security_required`* | `security_required` |
| Every gate — premises | `commands/fast-dev-flow.md` §*Premise evaluation at every gate* | one verdict per premise, in the spec's §3b |
| Phase B · 1 — security pass, if fired | `agents/security-reviewer.md` §*Output format* | the four answers, in the spec's §6 |
| Phase B · 2 — implement under the budget | `agents/software-dev.md` §*Hard caps* | `SOURCE files` |
| Phase B · 3 — the packet, per increment | `templates/fast-dev-flow/increment-template.md` §*4 · Test results* | `RED counterfactual` · `Reverse census` · `Mutation verdicts` · `Instrument RED-proof` · `Emitted-form assertion` · `Correction population` |
| Phase B · 3 — the packet's evidence | `templates/fast-dev-flow/increment-template.md` §*Evidence files* | `Evidence files` |
| Phase B · 3 — the packet's review cell | `templates/fast-dev-flow/increment-template.md` §*4b · Independent review* | `Independent review` |
| Phase C · 1 — validation pass | `agents/qa-reviewer.md` §*Output formats* | the per-criterion verdicts, with their evidence states |
| Phase C · 1 — naming a result's state | `commands/dev-flow.md` §*Evidence states* | the state of every result reported, from that table's seven — named there and nowhere else |
| Phase C · 4 — closing artifact | `templates/fast-dev-flow/spec-template.md` §*8. Close* | the close block, and the spec marked `closed` |
| Phase C · 6 — backlog reconciliation | `commands/dev-flow.md` §*A deferral carries the marker* | `⏸ DEFER` |

## Pre-checks

> **THESE PRE-CHECKS ARE THIS MODE'S INIT. You do not run `/dev-flow-init` as a separate act for a
> fast batch.** That command is the HOME of two blocks these pre-checks use — the six-key `fast`
> declaration (its step 3) and the two creation steps (5 and 6) — and this flow reads them from
> there rather than carrying a second copy. Running `/dev-flow-init` on its own would ask the
> mode question these pre-checks have already answered and seed nothing extra. A reader of the
> 2026-09-19 publication test had to cross-read three sections to settle this.

1. Verify you are at a project root (signals: `.git/`, `package.json`, `pyproject.toml`, etc.). If unclear, **ask**.
2. If `.fast-dev-flow/` does NOT exist, create it. If it already exists with an unclosed prior spec, warn and ask whether to resume or start fresh (archiving the previous one as `.fast-dev-flow/archive/<timestamp>-spec.md`).
3. **Declare the batch in `.dev-flow/state.json` — the MINIMAL `fast` declaration, and it is not optional.** *Lightweight* means **few artifacts, not no declaration**: this flow writes six keys and nothing else. **Its one home is `/dev-flow-init` step 3 §*The `fast` declaration*, which lists them**; this command does not restate the block, because a seed with two spellings drifts on its first edit (`C-50`). Write it before Phase A's gate. **Measured on a state-less `fast` tree, and re-derived at every selftest by `TPL FAST-STATE-reaches-the-readers`: THIRTEEN rules — `V27`, `V28`, `V31`, `V32`, `V36`, `V37`, `V38`, `V40`, `V41`, `V43`, `V44`, `V52`, `V54` — report *read nowhere; this is not a pass*, so the gate exits 0 over a batch it cannot inspect.** With those keys written, **all thirteen answer**: eight READ the batch's own artifacts (`V41` re-hashes the evidence it cites), three say the batch owes what they read and why (`V27`, `V52`, `V54` — `C-53`), and two record what they did NOT compare and why — `V40`, because `owner` is a rollover fact this flow does not carry, and `V28`, which since rev85 reads the `<YYYY-MM-DD>-fast-NN` id this flow mandates instead of calling it not batch-shaped.
4. **Create the homes pre-check 3 just DECLARED, in the same act that declares them** — the two directories `artifact_homes.increments` and `artifact_homes.evidence` name (`/dev-flow-init` step 5), and the lane `artifact_homes.backlog` names (`/dev-flow-init` step 6). Those two steps are those rules' one home, for every mode.
   - **Two consequences of git, stated so you do not read either as a defect.** (a) **git does not track an empty directory**, so the two directories exist on disk now and enter the repository with their first content in Phase B — the packet and the evidence. Do not plant a `.gitkeep`: nothing reads one, and the homes are declared in `state.json`, which IS committed. (b) Until that content lands, **`V42` reports that no tracked file falls in the deferral corpus** and says so in those words. That is the honest reading of an empty corpus, not a failure; the lane is on disk from this pre-check and the census answers from the first commit that carries a packet. An empty lane with its header is the artifact; Phase C step 6 reconciles it, it does not mint it. **Why the ordering is a rule and not a preference:** until rev85 the home was declared at this pre-check and the file was created three phases later, so `V42` reported *the DECLARED lane is not on disk · the census was NOT taken* at every gate of every fast batch until the last one, and both readers of the 2026-09-18 publication test recorded it and had to decide for themselves that it was benign. A declared home with no file is a `C-55` emptiness nobody declared.
5. **If this runtime has no named sub-agent roles and cannot prompt the user, say so once and run the fallback the adapter declares** — `SKILL.md` step 5 is that fallback's one home, and this line deliberately does not restate it.

## Phase A — Minimal spec (5-10 min)

### Actions
1. If the user hasn't given enough context, **ask** in a single short round: objective, loose user stories, what is OUT of scope.
2. Generate `.fast-dev-flow/spec.md` following `templates/fast-dev-flow/spec-template.md` — the template ships with the flow, at that path, and its §0 header is where the flow revision, the base ref, the `PULL` outcome and the batch's standing authorization are recorded.
3. **If the design decision is not obvious** (e.g. structural change, new integration, real ambiguity), briefly delegate to `architect` for a 1-2 paragraph recommendation. If it's obvious, do NOT delegate — unnecessary overhead.
4. Write **observable acceptance criteria**. Pattern: `When <input>, the system shall <observable output>`. Don't write "the system works well" or similar. **If it's not observable, it's not a criterion — it's a wish.**
5. **Information Flow Contract — Part A ONLY (C-54), written into the spec's §3c, which is that block's HOME in this flow.** Declare the flow this change touches. **`templates/ifc-template.md` §1 is the grammar's one home and the spec's §3c ships that same fence**, field for field — `SOURCE → NODES → SINK`, one field per line, a node beginning at `- fn :` — so there is one shape to follow and §3c is where you write it. **`owner` here is an ACCEPTANCE-CRITERION id — `AC-<n>` from §3 — and never an invented `LLR-`**: the full flow owns an LLR, this flow mints none, and a requirement id that names no requirement is worse than the gap. Until rev85 the obligation was stated here with no section to hold it and no answer for `owner`, and the reader of the 2026-09-18 re-run had to mint both. Information flows always exist, whatever the stack, and a node nobody owns is work nobody asked for. **Part B — addresses, `cardinality`, `consumers` — is NOT owed here**; it belongs to the full flow. **Its trigger question is this phase's escalation signal:** if the change alters *how a consumer reaches* something rather than *what it carries* — a selector, an index, a channel, an offset — stop and run `/dev-flow` instead. That is exactly the class of change that looks small, passes a value-based check, and breaks every reader indexing the surface positionally.
6. **Scan the spec for sensitive patterns — YOU run it; this command is its SPECIFICATION, not its implementation.** No scanner ships with this flow: the section below defines the scope, the matching, the pattern list and the four controls precisely enough to implement in a few lines of grep, and that definition is what makes your result checkable by someone else. Flag each detected pattern in section 6 of the spec. If at least one flag is positive, set `security_required: true` in the spec.

### Patterns that trigger `security_required`

**SCOPE — sections 1–4 of the spec** (objective, user stories, acceptance criteria, validation strategy), and **nothing else — §3b AND §3c INCLUDED IN THAT EXCLUSION**. §6 is where the answer is written, §0 and §7–8 carry the header, the batch status and the close, §3b is the premise table, whose *executed evidence* column is commands, digests and file paths, and §3c is the Information Flow Contract, whose node names are the change's own vocabulary; scanning any of them makes the spec's own record fire the scan that produced it. The four scanned sections are the ones a human WROTE ABOUT THE CHANGE; everything numbered around them is the record OF the batch.

**AND WITHIN THOSE FOUR SECTIONS THE SCAN READS AUTHORED TEXT, NOT THE SCAFFOLD — and the line between them is UNTOUCHED, not BRACKETED.** A `<…>` span is skipped **only while its contents are still the template's own words**, exactly as `templates/fast-dev-flow/spec-template.md` ships them: `<role>`, `<goal>`, `<input>`, `<output>` and their siblings. An unfilled placeholder is the template talking, not the author — `As a <role>, I want <goal>` fires `role` on a spec nobody has written yet, and a flag a blank template can raise carries no information about the change.

**The moment you type your own words between the brackets, it is authored text and it is scanned.** `When <a session token expires>, the system shall <re-issue it>` FIRES, and it must: the template models three of its four in-scope sections as a single bracketed slot (§1, §3's criteria pattern, §4), so a rule that skipped every bracket would let an author switch the security scan off by leaving two characters in place — which is the same control failing in the opposite direction, and `C-53` prices the two the same. Deleting the brackets is tidier and changes nothing. **This is the scope's one home** — the template's §6 points here rather than restating it, and its §2 states the consequence for the reader filling that section in.

**MATCHING — case-insensitive, on WORD BOUNDARIES, never as a substring — written `(?<!\w)<pattern>(?!\w)`.** ⚠ **Not `\b<pattern>\b`** — a pattern that BEGINS with a non-word character can never match under `\b`: `\b\.env\b` matches nothing, because there is no word boundary before a `.` that follows whitespace, and `.env` is on the list below. The lookaround form behaves like `\b` for word-initial patterns and still matches the others, which is why it is the rule. (Origin: the 2026-09-19 publication test — a reader implementing the stated rule literally found it could not match a stated pattern, and implemented the intent instead.) A substring match fires `form` inside the mandatory *In**form**ation Flow Contract* and `auth` inside `author`, which sets `security_required: true` on every conforming spec and teaches the operator to ignore the flag (`C-53`). A multi-word pattern is bounded the same way at each end.

**FOUR CONTROLS, run before the scan's own verdict is believed** — the probe must be shown able to return every answer it can return (`C-55`'s rider):

- **Positive:** `session token` in a criterion **FIRES** (`session`, `token`).
- **Negative:** `Information Flow Contract` anywhere in sections 1–4 **DOES NOT FIRE** — no bounded pattern matches it.
- **Placeholder:** `As a <role>, I want <goal>, so that <benefit>` — the template's own untouched words — **DOES NOT FIRE**. The same line with the brackets removed **FIRES** (`role`), which is what makes the skip a rule rather than a hole.
- **Authored-in-brackets:** `When <a session token expires>, the system shall <re-issue it>` **FIRES** (`session`, `token`). The brackets are still there and the words inside them are yours, so the scan reads them. This is the control that keeps the skip from becoming an off switch.

A scan that cannot produce the negative is matching as a substring; a scan that cannot produce the placeholder pair is reading the scaffold; a scan that cannot produce the authored-in-brackets answer has turned the skip into a hole an author can hide a change in; a scan that cannot produce the positive is not running. Report all four with the flags.

**THE FOUR SCANNED SECTIONS ARE ABOUT THE CHANGE, SO KEEP PROCESS PROSE OUT OF THEM.** A sentence about how the batch was RUN — *"the `qa-reviewer` role was self-executed"*, *"the reviewer approved"* — trips `role` or `auth` and sets the flag on work that touches no surface at all. That is the scan behaving exactly as specified, and the answer is never to reword around it: **put the process note in §7 or §8, which are the record OF the batch and out of scope, and if it belongs in §1–§4 then declare the flag and answer Phase B step 1's four questions.** Gaming a scan is the one response this control cannot survive; moving a sentence to the section it belonged in is not gaming it. Measured 2026-09-19, when a reader wrote a self-execution note into §4 and correctly refused to reword it.

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
- **If `state.json` declares `guided: true`, this is a GUIDED gate and takes four further steps before it closes.** **`SKILL.md` §*Guided first run* states them and is that gate's ONE home; this line points and does not restate them** (`C-50`). `V55` reads the ledger they leave.

## Phase B — Supervised implementation (the bulk)

### Actions
1. **If `security_required: true`**, BEFORE any code, run the four questions below and record their answers in the spec's §6 risk summary. **They are written here rather than cited, because this flow ships self-contained: every document it sends you to is one of its own files.** Delegate the pass to `security-reviewer` (`agents/security-reviewer.md`); where no named roles exist, execute that role's text yourself and record that you did (`SKILL.md` step 5).
   - **New outbound surface?** Name every external system this change can now reach, and who authorized each. A tool that can act on an outside system is a decision, not a dependency.
   - **Secrets?** Name where each credential is read from, and show that none is written into the repository, the artifacts or a transcript. `not-run` is not an answer here; `none — this change reads no credential` is.
   - **Blast radius?** Name what this change can destroy or expose if it is wrong — data, accounts, published surface — and what bounds it.
   - **Authorization?** Name the narrowest permission the change actually needs, and say whether it asks for more.
   - Report the identified risks and, unless the batch carries a standing authorization covering them, ask for confirmation before proceeding.
2. Delegate to `software-dev` (`agents/software-dev.md`), under the budget and the packet obligation below — which are this flow's own and are stated here.
3. **Hard constraints:**
   - **≤4 SOURCE files per increment. Tests are NOT capped**; product docs and `.fast-dev-flow/**` are outside the count. **⚠ at exactly 4** — declare in the packet why it could not be cut smaller; exceeding 4 does not auto-block but must be declared. **No total ceiling** (a total cap penalises writing tests — that is the defect this replaced). Same rule and same measured origin as `/dev-flow`; see its §Phase 3 for the data. **Precedence:** inside a batch of either flow THIS budget governs; outside a batch, your runtime's own standing development rule does — and every document this flow ships states the same variable, SOURCE files, so the author is never handed two numbers.
   - **Review packet at the end of EACH increment, following `templates/fast-dev-flow/increment-template.md` — the SHORT packet, which is this flow's own — written into the home `artifact_homes.increments` declares** (`.dev-flow/<batch_id>/03-increments/increment-NNN.md`, the template's own §*Where this lives*). **Every row in it is read by a rule that evaluates on a `mode: fast` tree, and nothing else is in it**: no `Owed in` column, no 16-row gate checklist, no `n/a — not owed in fast` cell. The long `templates/increment-template.md` stays for `core` and `full`. Until rev86 this line pointed at that long template — 489 lines, of which a fast batch could fill ten rows and had to recover the safe subset by cross-reading a dense ⚠ paragraph — and both readers of the 2026-09-19 publication test named the ceremony-to-code ratio as the single biggest obstacle to running a fast batch at all.
   - Tests written in the same increment as the code they cover.
   - No abstractions, helpers, or features not derivable from an approved acceptance criterion.
4. **Gate per increment:** the user approves before advancing to the next. **If `state.json` declares `guided: true`, this is a GUIDED gate and takes four further steps before it closes.** **`SKILL.md` §*Guided first run* states them and is that gate's ONE home; this line points and does not restate them** (`C-50`). `V55` reads the ledger they leave.
5. The phase ends when all acceptance criteria are covered by code + tests.

### Difference vs `/dev-flow` phase 3
- Here we don't require formal TC-IDs. Each test maps to an acceptance criterion by name or reference.
- **`state.json` is DECLARED and not MAINTAINED** — the six keys of pre-check 3 are written once and never advanced: no `current_station`, no `iterations_per_station`, no `phase_status`, and **no `decisions_log` UNLESS `guided: true`**, which is the one key that asks this flow to write the ledger back — one entry per gate, and nothing else in it (`SKILL.md` §*Guided first run*). Progress lives in the conversation, the commits and the spec's own status table. Until rev84 this bullet said *no `state.json`*, and the fast batch it described was one the gate could not inspect, the evidence home was undeclared, and every reader keyed on `artifact_homes` read nothing.
- Code review is **lightweight**: a quick self-review, or a single `code-reviewer` pass on risky increments — not a mandatory per-increment gate like `/dev-flow`.
- **`tester` assignment is LIGHT here, and light means USUALLY ABSENT (rev73).** `software-dev` writes its own tests and **no delegation is owed** — a trivial change adds its test and moves on. Delegate to `tester` in this flow for exactly one case: an **escaped regression**, where the deliverable is the RED-on-base capture and the author of that capture should not be the author of the fix. Everything else (wide matrices, E2E acceptance, independent authorship as a standing rule) belongs to `/dev-flow` — if you want it here, that is the escape hatch below, not a heavier fast flow.
- **A standing authorization is not re-asked.** If the batch already carries one, an agent proceeds inside its scope and neither re-requests it nor widens it; see `/dev-flow` §Batch-kickoff authorization, which is that rule's one home.
- **Evidence states:** every result this flow reports names its state from `/dev-flow` §*Evidence states* — `planned` · `executed` · `approved` · `failed` · `blocked` · `not-run` · `n/a — <reason>`. **A planned test is not a run one**, and the compressed flow does not get a compressed vocabulary.

## Phase C — Validation + close (5-15 min)

### Actions
1. Delegate a light pass to `qa-reviewer`:
   - **The suite run is the ORCHESTRATOR's**, and `qa-reviewer` reconciles its output and **names who executed it** — the same ownership `/dev-flow` §Phase 4 states under `C-25`, for the same mechanical reason (a backgrounded suite outlives the sub-agent that launched it). A `qa-reviewer` that reports pass/fail is reporting a result it consumed.
   - Verify acceptance criteria one by one (manual smoke if applicable), each carrying its evidence state.
2. **Coverage-claim discipline:** before reporting an acceptance criterion as "covered by test", confirm the named test function exists on disk (`Glob` / read the file). Coverage signed off from intent rather than the artifact is a false claim. (Same lesson as `/dev-flow` Phase 3, origin batch-08.)
3. **If `security_required` was true**, final security pass:
   - Confirm the risks identified in phase B were mitigated.
   - If risks remain open, list them as pending in the close.
4. Produce the **closing artifact** — a markdown block ready to paste into the PR description or CHANGELOG:
   - **What changed** (1 paragraph).
   - **How it was tested** (list of tests + manual smoke performed).
   - **Open risks / pending** (if any).
   - **Security flags fired and how they were handled** (if applicable).
   - **Suggested commit message** (short, imperative).
5. Update `.fast-dev-flow/spec.md`, marking the spec `closed` with the date.
6. **Backlog reconciliation (MANDATORY — the carry-over contract).** Reconcile the project's canonical cross-batch backlog — **the file, or lane files, that its `docs/engineering-rules.md` designates; absent such a designation, `.dev-flow/BACKLOG.md`** — a prioritized cross-batch queue shared by BOTH flows, never a per-batch file, and **already on disk since pre-check 4, which creates the declared lane**; if the project routes to a lane this batch had not resolved then, create that lane now. **If the project routes to lanes, reconcile the lane this batch belongs to** — resolve the routing before reading, because a partitioned queue keeps no open work in the original file and reading that file alone returns an empty queue that looks like "nothing pending". Then: (a) mark every item this batch shipped `DONE` with its PR/SHA; (b) **carry forward, drop nothing** — append every open item plus every new carry / deferred finding / "Open risks / pending" from the closing artifact; (c) bump the recorded base ref + a "last refresh: <date>" line. **A deferral written anywhere carries the `⏸ DEFER` marker, and this step reads the census** — `V42` reports every marker in `.dev-flow/design/**`, in an ADR or in the batch record that is keyed to no backlog entry; see `/dev-flow` §*A deferral carries the marker*, which is that rule's one home. **Include the backlog edit in this batch's commit/PR** so the backlog travels with the code that changed it. The batch is not complete until the backlog reflects it — a fast-flow ships small, but the backlog still updates every time.

### Final gate
- Present the closing block to the user.
- Ask for confirmation to mark the batch as complete.
- **Run the gate again now; it reads the batch this time.** The run at Phase A proved the TOOL over a tree with no batch declared; this one proves the BATCH, because `state.json`, the packets and the evidence now exist for the rules to read. `SKILL.md` §*What refuses an invocation here* step 1 carries the command and the reason.
- **If `state.json` declares `guided: true`, this is a GUIDED gate and takes four further steps before it closes.** **`SKILL.md` §*Guided first run* states them and is that gate's ONE home; this line points and does not restate them** (`C-50`). `V55` reads the ledger they leave.

## Escape hatch — promotion to `/dev-flow`

If during any phase you detect the batch grew beyond fast scope (e.g. >3 increments in phase B, serious requirements ambiguity, sustained scope drift), **stop and report**:

> "This batch exceeded fast-dev-flow scope. I recommend promoting to /dev-flow for formal traceability and validation. Do I proceed? On approval I run `/dev-flow-init --mode core` (or set the `mode` field in `state.json`) and continue — **nothing is archived, nothing is migrated, no history is lost**."

Do not promote without explicit approval. Project-level V-rules apply at and after promotion to `/dev-flow`; the flow-level rules `V7`/`V15`/`V16`/`V17` fire via the flow-guard hook on **any** invocation of either flow, and the hook blocks the command on a BLOCK from `V7`, `V15` or `V16` — `V17` runs there too but is not in that blocking set.

## Premise evaluation at every gate (C-43, compressed)

At each of the three gates, alongside checking the work against the spec, **evaluate the PREMISES the stage rests on as explicit propositions.** Checking work against a spec answers *"does this match?"*, not *"is what the spec ASSERTS ABOUT THE WORLD true?"* — a stage can be perfectly compliant with a false premise. Verdicts: ✅ **TRUE** (an **executed** probe — command output, a `file:line`; citing another document is NOT evidence) · ❌ **FALSE** (counterexample recorded — blocks) · ❓ **UNDECIDABLE** (missing verification, or the requirement is ambiguous/incomplete — blocks until decided or declared out of scope in writing).

**Three tiers.** **Axioms** = requirements already validated AND verified — law by default, but **re-openable** on an executed counterexample or a logical invalidation (in practice almost always **INCOMPLETENESS**); a successful challenge **ENLARGES** the requirement, never deletes it. **Hypotheses** = what this batch introduces, *including anything inherited from a prior design batch* — written down ≠ verified. **Premises** = claims about the world (symbols, line numbers, sizes, "X already exists") — executed against disk, never trusted.

**ARTIFACT** — a short premise table in `.fast-dev-flow/spec.md`, added at Phase A beside the acceptance criteria: `| Premise | Tier | Verdict | Executed evidence |`. Four columns, one row per premise. Without the table the control degrades to *"I thought about it"*; with it, the next session can re-check the batch's foundations in seconds.

This is the cheapest control in the fast flow: it is greps and one-line probes, and it runs before any code is written — and it is the flow where an unverified premise is most likely to survive, precisely because the ceremony is light.

## An emptiness is doing work — say which kind (C-55, compressed)

**Whenever a claim or a guard depends on the tree containing NO instance of some case, that emptiness is LOAD-BEARING and must be declared.** Nothing is wrong today — that is the whole problem. C-40 asks whether a predicate *can* go red; C-43 asks whether a premise is *true*; C-55 asks what the result is resting on that is only accidentally the case right now.

**Limb 1 — the emptiness is the FINDING.** If the batch's result is an *absence* ("no X exists", "the blind spot is empty"), the property that made the search wide enough is **part of the result**. A negative result is sound only if the search was too WIDE; narrow it later and every derived claim weakens with the suite green. Guard the over-breadth and **say in the guard's own docstring that it protects a conclusion, not a behaviour** — otherwise the next reader files it as an implementation detail and "improves" it.

**Rider — an absence is admissible only if the probe can produce a NON-absence.** Run the same probe, unmodified, over a case known to be present. **Uniformity over heterogeneous inputs is the TRIGGER for that control, never the verdict** — the correct answer can be uniform too (a clean tree greps zero everywhere), and treating it as a verdict false-fails correct work, which **C-53** prices as high as passing wrong work. A plausible zero reads as data; only an impossible value betrays itself, and that is luck. If no known-present case can be built, **say so and downgrade the claim**. Same discipline as C-53's positive/negative fixture pair, applied to **diagnostic probes**, which nobody verifies because *"I am only looking"*.

**Limb 2 — the emptiness is an ACCIDENT of today's data.** A guard clause that is a **no-op on the current tree** is untested however green the suite, and the tell is that mutating it changes nothing. Two consequences: **a conjunctive criterion needs one mutation per conjunct** (*"classify it AND never drop it"* is two predicates), and **mutating a stage is not mutating the pipeline**.

**DISCHARGE — a synthetic instance, not an argument.** Construct the case the tree lacks (a fixture tree, an in-memory module) and assert against it. "There are none today" is the reason the guard is needed, never a reason to skip it.

**ARTIFACT** — one line per load-bearing emptiness in the spec's premise table (**§3b** — §6 is where the security-flag answer is written and holds no premises), tier `PREMISE`, with the synthetic instance as its executed evidence. This is the cheapest place to catch it: the fast flow is where a green suite is most likely to be mistaken for coverage.

*(Origin: batch-84, both limbs — see dev-flow-lessons)*

## The flow is a SHARED asset — changes flow both ways (C-45, compressed)

A control is discovered in one project but is **not that project's property**. Portable ones must reach every project running this flow, or each re-learns the same lesson at full price.

**PUSH** — a portable control is not encoded until it lands upstream: the **command** (the rule) · its **artifact** (a template section — a control with no output degrades to *"I thought about it"*) · the **catalog** entry (`dev-flow-lessons`, with the measured origin) · **committed and pushed**, SHAs recorded at the close. Per **C-44** an unpushed control is indistinguishable from one never written. Say which of the four landed — command-but-not-template is *half-encoded*, and the missing half is the enforceable one.

**PULL** — at Phase A, alongside the pre-checks, confirm the local flow files are not behind their remotes. Compare against the published manifest (`FLOW-VERSION.md`, beside the flow's own files): version + per-file SHA256. **A batch run on a stale flow inherits a solved problem as an open one.** Record the flow revision in the spec header next to the base ref.

**On a runtime that has only the published bundle there is no canon remote to be behind, and the honest outcome is `not-run`, never a silent pass.** The manifest travels WITH the files, so comparing it against them proves the copy is internally consistent and says nothing about staleness — that is `V7`'s bound, stated in `FLOW-VERSION.md`'s own question table. Record the currency half in the spec header as **`not-run — no canon remote on this runtime`**, next to the flow revision the manifest declares. An unanswerable question answered anyway is the vacuous check this flow exists to refuse.

**Classification still decides placement** — portable → the global command; stack-specific → the project's `docs/engineering-rules.md`. Portability is the test, not convenience: a stack-specific rule pushed upstream pollutes every other project, and a portable one kept local is a lesson paid for once and used once.

## Session-close working-file reconciliation (C-44, compressed)

**No file this session touched may be left in limbo at its close.** At the final gate, sweep `git status --short` in **every repo touched — including auxiliary repos outside the project tree** (skills / commands / config) — plus any commit that exists but was never pushed, and report each file in exactly one terminal state: ✅ **committed** (and, where it only matters once integrated, **landed** — a commit that never lands is not terminal) · 🗑️ **reverted / deleted, deliberately** · 📋 **left in place ON PURPOSE with its path + remaining work written into the canonical backlog**.

**This flow does not DECIDE to run git operations — that is the operator's call, and §*Hard rules* is that rule's one home** (a batch carrying a standing authorization commits as authorized; one without it prepares the change and reports). So C-44 here is a **reporting** obligation either way: produce the reconciliation for the user, name anything unlanded, and **report pre-existing uncommitted changes as found rather than folding them into your own work.**

*Why it is a gate: work that is finished but unlanded is indistinguishable from work never done, and the state files a later session reads to orient itself then assert something false — which the next batch inherits as a premise (C-43). Origin: batch-70, four instances of this exact pattern found inside one session, none of them a code defect.*

## Hard rules

- Never advance a phase without explicit user approval.
- Never skip security-flag detection — it's part of this flow's value.
- **Never close a HIGH with a recommended fix (rev73).** A clean verdict from `code-reviewer` or `security-reviewer` requires the fix **applied and verified**; until then the verdict is the conditional `BLOCK-UNTIL: <finding ids>`, which authorises nothing. This flow is faster, not laxer — see `/dev-flow` §Phase 3 *Independent review*, that rule's one home.
- Never generate the spec without observable acceptance criteria. If the criteria aren't observable, mark the spec invalid and ask the user again.
- Don't touch the Obsidian vault from this flow. Docs live in the repo (PR description / CHANGELOG).
- **Don't DECIDE to run git operations (commit, push, merge) — that is the user's call, and it is a rule about who decides, not a ban on the batch ever being committed.** When the operator has authorized commits for this batch (§*A standing authorization is not re-asked*, recorded in the spec header), commit as authorized — and Phase C step 6's *include the backlog edit in this batch's commit* is then exactly what it says. With no such authorization, prepare the change, report it, and let the user commit. Until rev84 this line read as an absolute ban beside a step that mandates a commit, and both readers of the 2026-09-18 publication test recorded the contradiction and resolved it by themselves.
- **Never close a gate without evaluating its premises** (C-43): each is ✅ TRUE with an executed probe, ❌ FALSE, or ❓ UNDECIDABLE — the last two block. A requirement inherited from a prior design batch is a **hypothesis**, not an axiom.
- **Never end a session leaving a touched file in limbo** (C-44): every file is committed-and-landed, deliberately discarded, or recorded in the backlog with its path. Sweep every repo touched, auxiliary repos included; report pre-existing dirt as found, never fold it into your own work.
- **A batch is not complete until the project's canonical backlog is reconciled** (Phase C step 6): shipped items marked done, every carry/finding appended, base ref bumped, and the edit included in the batch's commit. **Every open item lives in exactly ONE canonical file**, and the backlog is shared with `/dev-flow` — a project MAY partition it into lanes (declared in its `docs/engineering-rules.md`), which is a split, not a copy: items MOVE between lane files and are never duplicated. Never let a second *de-facto* source drift alongside it. (Origin: 2026-07-20 operator audit, extended 2026-07-28 — see dev-flow-lessons)

## Structure created in the project

**The real footprint — five required entries plus one optional archive, and it is NOT `.fast-dev-flow/` alone.** Until rev84 this section claimed it was, while the increment packet, the evidence bytes and the mandatory backlog all lived under `.dev-flow/`: a reader following this command literally had to invent the other tree, and two did, differently.

```
.fast-dev-flow/spec.md                          the spec (Phase A → closed in Phase C)
.fast-dev-flow/archive/<timestamp>-spec.md      closed specs, optional
.dev-flow/state.json                            the MINIMAL fast declaration (pre-check 3)
.dev-flow/<batch>/03-increments/                the review packet per increment
.dev-flow/<batch>/evidence/                     the evidence bytes every digest is cited against
.dev-flow/BACKLOG.md                            the cross-batch backlog, shared with `/dev-flow` (pre-check 4)
```

**`<batch>` is `state.json`'s own `batch_id`, and the two `.dev-flow/<batch>/` paths are the ones its `artifact_homes` declares** — they are not hard-coded here, and no command writes a FLOW ARTIFACT to a path `artifact_homes` does not declare — `/dev-flow` §*Artifact homes* is that rule's one home and says what it binds; your source and your tests are the WORK, not the record, and owe no key.

Lightweight on purpose: no requirements matrix, no per-phase subfolders, no post-mortem, no vault, and nothing in `.dev-flow/<batch_id>/` but the packets and the evidence. Five keys of state and four `.dev-flow/` entries is the whole of it.

## Tone

Keep the flow conversational and agile. The philosophy is: spec in 5 minutes, supervised code, clean close. If the user feels you're being slow or heavy, that's a signal you're applying `/dev-flow` overhead here — correct it.
