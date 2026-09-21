# Quick Spec — <PROJECT>

> Minimal spec for `/fast-dev-flow`. Goal: capture what's needed in 5-10 minutes without IEEE 830 overhead.
> **Hard rule:** acceptance criteria must be **observable** (input → verifiable output). If it's not observable, it's not a criterion.

> **Owed in.** `fast` ✓ · `core` — · `full` —
> **Source:** `/dev-flow-init` step 4's seed-by-mode table, which is this fact's one home. A mode marked `—` **does not owe this artifact, and its absence is not an omission**; `by trigger` means the station exists only when the `triggers` block fired, and `stations_active` in `state.json` is the authority for *this* batch. Where a SECTION or a gate row is owed more narrowly than the artifact, it says so on the row.

---

## 0. Batch header — identity, currency, authorization

| Field | Value |
|-------|-------|
| Batch | `<the `batch_id` state.json declares, e.g. 2026-09-20-fast-01>` |
| Flow revision | `<the revision FLOW-VERSION.md declares — the same value state.json's flow_version carries>` |
| Base ref | `<the commit this batch starts from>` |
| `C-45` PULL — currency | `<executed — compared against the remote manifest · or: not-run — no canon remote on this runtime>` |
| Standing authorization | `<the operator's own words, and what they authorize · or: none — every gate is asked>` |
| Runtime absences (`SKILL.md` step 5) | `<named roles unavailable and therefore self-executed · prompts unavailable · or: none>` |
| Gate record | `<the validator command, its exit code, and 0 block · date>` |

> **`Batch` IS READ BY A RULE, and it is what keys this file to a batch.** `.fast-dev-flow/spec.md`
> is SINGLE-SLOT — one spec at a time, the previous one archived (`/fast-dev-flow` §Pre-checks 2)
> — while `state.json` rolls over to a new `batch_id`. Between the two acts the spec on disk is
> the PREVIOUS batch's, and `V45` reads its premise roll-up and `V55` reads its close cell. With
> this row written, both compare it against the declared batch and say whose spec they found.
> **Leave the cell as it ships and nothing is compared**: a cell that is not a batch id declares
> no id, and the readers skip the comparison.
>
> **Every row is a DECLARED ANSWER or a declared absence, never blank.** `not-run — <why>` is an
> answer; an empty cell is a question nobody asked. The evidence-state vocabulary is `/dev-flow`
> §*Evidence states* and is not re-minted here.

---

## 1. Objective (1 line)

`<what this batch solves, in one sentence>`

---

## 2. User stories (1-3, Connextra format)

- As a `<role>`, I want `<goal>`, so that `<benefit>`.
- As a `<role>`, I want `<goal>`, so that `<benefit>`.

> ⚠ **`<role>` is a PLACEHOLDER, and the §6 scan does not read it — while it is still these
> words.** The scan skips a `<…>` span only while its contents are the ones this template ships,
> so the scaffold you are reading cannot set its own flag. **Type your own words between the
> brackets and they are scanned**, brackets or not — which is what stops the brackets from being
> an off switch for the security flag. `/fast-dev-flow` §*Patterns that trigger
> `security_required`* is that rule's one home and carries the four controls that prove it.

---

## 3. Acceptance criteria (3-7 bullets, observable)

> Suggested pattern: **"When `<input/context>`, the system shall `<observable output/behavior>`."**

- [ ] When `<input>`, the system shall `<output>`.
- [ ] When `<input>`, the system shall `<output>`.
- [ ] When `<input>`, the system shall `<output>`.

---

## 3b. Premise table (C-43)

> One row per premise the batch rests on, **executed against disk** before any code is written.
> Tiers: `AXIOM` (validated and verified already) · `HYPOTHESIS` (what this batch introduces)
> · `PREMISE` (a claim about the world — symbols, line numbers, "X already exists").
> Verdicts: ✅ TRUE with its executed probe · ❌ FALSE (blocks) · ❓ UNDECIDABLE (blocks).
> **A load-bearing emptiness (C-55) is a `PREMISE` row whose evidence is the SYNTHETIC instance**,
> not an argument that none exists.

| Premise | Tier | Verdict | Executed evidence |
|---|---|---|---|
| `<claim>` | `PREMISE` | `<✅/❌/❓>` | `<command + its output, or file:line>` |

- **Premise evaluation:** `<✅ TRUE | ❌ FALSE | ❓ UNDECIDABLE>` — `<N premise(s) evaluated, and the verdict that decides the gate>` · or `none — <why no premise applies>`

> **The roll-up is written in the same grammar as the full flow's** (`templates/req-template.md`
> §2.7), so a reader moving between the two reads one field, not two. **And `V45` READS IT HERE**:
> in `mode: fast` the rule resolves `artifact_homes.spec` and reads the roll-up out of THIS
> section, with the same four outcomes and the same verdict vocabulary it applies to the full
> flow's §2.7. The gate that reads it is the Phase A gate.

---

## 3c. Information Flow Contract — Part A (C-54)

> **Owed in `fast`, and this section is its home.** `/fast-dev-flow` Phase A step 5 is the
> obligation's one home and `templates/ifc-template.md` is the block's grammar; this section is
> where the ANSWER is written, so a fast batch never has to invent a place for it.
> **Part A only** — `SOURCE → NODES → SINK`, each node naming the requirement that owns it.
> **Part B — addresses, `cardinality`, `consumers` — is NOT owed here.** If the change alters
> *how a consumer reaches* something rather than *what it carries*, stop and run `/dev-flow`.

> **`owner` in `fast` is an ACCEPTANCE-CRITERION id from §3**, written `AC-<n>`, and that is this
> field's one home. The full flow owns an LLR and the fast flow mints none; a node with no owner is
> work nobody asked for, so the id it carries is the smallest one this flow really has. Do **not**
> invent `LLR-` ids here — a requirement id that names no requirement is worse than the gap.

> **ONE GRAMMAR, NOT TWO.** The block below is `templates/ifc-template.md` §1's Part A fence,
> field for field — `FLOW` / `SOURCE` / `NODES` with one field per line under each `- fn :`,
> a node beginning at `- fn :`. The ONLY substitution `fast` makes is the `owner` VALUE: an
> `AC-<n>` where the full flow writes an LLR.

```
FLOW: <id — what moves, in one line>
  SOURCE : <where information enters the system boundary>
  NODES  :
    - fn    : <the function that performs this transform>
      owner : AC-<n>
      in    : <shape in>
      out   : <shape out>
  SINK   : <where information leaves the system boundary>
```

- **Part B trigger question — answered, never skipped:** `<no — this change moves what the flow CARRIES / yes — it moves an address, a selector, an index or an offset, so this batch is promoted to /dev-flow>`

---

## 4. Validation strategy (1 paragraph)

`<which tests will be written (unit / integration / e2e), what manual smoke will be done, what evidence is enough to close the batch>`

---

## 5. Non-goals (what is OUT)

- `<what will explicitly NOT be done in this batch>`
- `<what is deferred for later>`

---

## 6. Detected security flags

> The orchestrator runs the scan `/fast-dev-flow` §*Patterns that trigger `security_required`* defines — **that command is the scope's and the matching's one home**, and this section is where its ANSWER is written. Mark `[x]` what applies. If at least one is marked, `security_required: true`; report the positive and negative control with the flags.

- [ ] Auth / identity (login, sessions, tokens, permissions)
- [ ] Secrets / config (.env, API keys, credentials)
- [ ] External integrations (webhooks, MCP, Composio, n8n, third-party)
- [ ] Sensitive data (PII, payments, health, encryption)
- [ ] Destructive DB (drop, delete, truncate, migrations)
- [ ] Input / attack surface (uploads, forms, sanitization, CORS)
- [ ] Network / exposure (new public endpoints, webhook receivers)

**`security_required`:** `<true | false>`

**Risk summary (if security_required = true):**
`<3-5 lines: which patterns fired, which areas they touch, what needs special attention in phase B>`

---

## 7. Batch status

| Field | Value |
|-------|-------|
| Current phase | A / B / C / closed |
| Started | `<YYYY-MM-DD HH:MM>` |
| Closed | `<YYYY-MM-DD HH:MM or ->` |
| Promoted to /dev-flow | yes / no |
| Gate self-approvals | `<one line per gate the standing authorization stood for: which gate, the date, and that it was self-approved under the words in §0 · or: none — every gate was asked>` |
| Notes | `<if archived, promoted, or closed normally>` |

> **`Current phase` IS THE CLOSE SIGNAL, and it is read by a rule.** Writing `closed` in that
> cell at Phase C step 5 is what tells `V55` the `C` gate is BEHIND the batch; while it says
> anything else AND the `decisions_log` records no `C` decision, `C` is a gate still ahead and
> `V55` excuses it rather than accusing it. **It is one of TWO witnesses and either one is
> enough** — the other is that ledger entry — and the rule prints which one it used. Write the
> word, not a synonym: the cell is matched on `closed`.

> **The self-approval row is where an un-asked decision becomes a record.** `/dev-flow`
> §*Batch-kickoff authorization* is that obligation's one home and says that in `fast` the
> answers live here and in §0 — `state.json.standing_authorization`, `PLAN.md`,
> `decisions_log`, the post-mortem and the vault are not owed in this mode. Autonomy is never
> silent: a gate nobody asked about and nobody wrote down is indistinguishable from one nobody
> reached.

---

## 8. Close (filled in phase C)

### What changed
`<1 paragraph>`

### How it was tested
> **One line per acceptance criterion, and each line carries three things**: the criterion's
> `AC-<n>`, its evidence state from `/dev-flow` §*Evidence states*, and **who executed it**
> — the orchestrator, a named agent, or `human:<name>`. `agents/qa-reviewer.md` is that
> obligation's one home and this is where its light pass lands; a `fast` batch seeds no
> `04-validation.md`, and that absence is not an omission.

- `AC-<n>` — `<the test or smoke that covers it>` — `<evidence state>` — executed by `<who>`
- `AC-<n>` — `<the test or smoke that covers it>` — `<evidence state>` — executed by `<who>`

### Open risks / pending
- `<if any>`

### Security flags — handling
`<only if security_required was true: how the detected risks were mitigated>`

### Suggested commit message
```
<type>: <short imperative summary>

<optional body with detail>
```
