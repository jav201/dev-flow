# Increment `<NNN>` — `AC-<n>` · `<short title>`

> **This is the `fast` packet and it is the whole of it.** Every row is read by a rule that EVALUATES on a `mode: fast` tree — measured, re-derived at every selftest by `TPL FAST-PACKET-rows-derive`, which reddens BOTH ways: a rule added later with no row here, and a row here no rule reads. **TWO of those rules ask for a control `/dev-flow` §*Modes* does not activate in `fast` — the RED counterfactual and the reverse census — because the rules that read them are not mode-aware. Both rows LEAD with `none — not owed in fast`, which is the truthful answer, and §4 says so again beside them.** Nothing else full-flow-only appears: no `Owed in` COLUMN in a gate table (the one-line `Owed in.` declaration below is this page's own, and says which mode owes the artifact), no 16-row gate checklist, no `n/a — not owed in fast` cell to write. `core` and `full` use the long `templates/increment-template.md`; this file is `templates/fast-dev-flow/increment-template.md`.
> **Owed in.** `fast` ✓ · `core` — · `full` —
> **Where this lives:** the repo, at the home `artifact_homes.increments` declares — `.dev-flow/<batch_id>/03-increments/increment-<NNN>.md`. Synced nowhere.
> **Reserved field names.** The **field names and block keywords below are language-independent** — the
> validator parses them literally and they are never translated:
> `SOURCE files` · `Instrument RED-proof` · `Correction population` · `Mutation verdicts` · `Emitted-form assertion` · `Reverse census` · `RED counterfactual` · `Independent review` · `Evidence files` · `⏸ DEFER`
> Everything else on this page — headings, guidance, the prose in every cell — is translated with the batch (the batch's language is fixed in the spec's §0/§1).
> **One strategy, not two:** the flow ships no alias table, so a translated label is read as an ABSENT one and the rule keyed on it reports a true-sounding silence.
> **Each name above carries its declared empty in its own cell**: an empty DECLARED is an answer, an empty OMITTED is a gap, and the two must never read alike. `⏸ DEFER` is the one FLOW-WIDE marker — `V42` reads it out of any batch artifact, whichever template minted it.
> `⚠` notice — does not block, obliges you to declare the reason here. `✗` block. `✓` satisfied **with its evidence cited**.

| Field | Value |
|---|---|
| Batch | `<batch_id>` |
| Increment | `<NNN>` |
| Criterion | `AC-<n>` — the acceptance-criterion ids this increment closes (`fast` mints no `R-`, `LLR-`, `AT-` or `TC-`) |
| Date | `<YYYY-MM-DD>` |

## 1 · What changed

*(BLUF: the outcome first, then the mechanism. Name the shipped surface the user reaches.)*

## 2 · Files modified

| File | Kind | Change |
|---|---|---|
| `<path>` | source / test / doc | `<what changed in it>` |

| Field | Value |
|---|---|
| **SOURCE files** | **`<N>` / 4** |

⚠ **At exactly 4, and at every count above it, state here why this increment could not be cut smaller.** Tests are not capped; docs and `.dev-flow/**` are outside the count.

## 3 · How to test

```bash
<the exact commands, copy-pasteable>
```

## 4 · Test results

One complete run: the exit code and the tail come from THAT run's own output, never stitched across partial runs or inferred from a backgrounded call.

| Layer | Nodes | Result |
|---|---|---|
| **black-box** — `AC-<n>` ↔ criterion, through the shipped surface | `<nodes>` | `<N passed>` |

| Field | Value |
|---|---|
| **RED counterfactual** | ``none — not owed in fast (`/dev-flow` §Modes)`` — or, when the increment made a new assertion anyway: `<the mutation that made THIS increment's OWN new assertion fail, by position and operation · where its transcript is stored · the restore digest that returned the file to its pre-mutation bytes>` — or: `none — no new assertion in this increment` |
| **Reverse census** | ``none — not owed in fast (`/dev-flow` §Modes)`` — or, when the increment ran the sweep anyway: `<per probe, its command and its verdict, N hits, and where every hit was re-validated>` — or: `none — this increment touches no code symbol or shared surface`. The probe grammar is `/dev-flow` §*Trigger evaluation*, cited for the SHAPE of a probe only — which controls are live in this mode is §*Modes*' question, and it answers `—`. |
| **Mutation verdicts** | `<per resolved node: the mutation by position and operation · KILLED / CRASH / SURVIVED / BAD (the mutation's anchor did not apply, so nothing was measured) · the arms that stayed GREEN, named · the transcript's path under artifact_homes.evidence and the restore digest — or: none — no mutation battery in this increment>` |
| **Instrument RED-proof** | `<N instruments, each shown RED before its first PASS was believed — or: none — no instrument beyond the suite>` |
| **Emitted-form assertion** | `<N artifacts, each asserted against the form its producer emitted — or: none — this increment emits no artifact>` |
| **Correction population** | `<N corrections, each enumerated with its method BEFORE its first site was edited — or: none — no correction>` |

**`RED counterfactual` AND `Reverse census` ARE ASKED IN EVERY MODE AND OWED IN NONE OF THEM HERE.** `/dev-flow` §*Modes* does not activate the RED counterfactual or the reverse census in `fast`, and it is the one authority for that; the rules that read these rows are not mode-aware, so they ASK every packet and a notice is all they can raise. The truthful fast answer is therefore the first declared empty — `none — not owed in fast` — and writing it is a declaration, not a skip. Write the second empty, or a real answer, when the increment did the work anyway.

✗ **Describe a mutation by position and operation; never spell the corrupted token here** — this packet is scanned as corpus, so a verbatim mutant makes the restore prove the wrong plane. ✗ A verdict per battery is not a verdict: one per resolved node, and name the arms that stayed green.

### Evidence files

Bytes at the home `artifact_homes.evidence` declares, verbatim, hash-verified. **Cite each path from the ROOT OF THE STORE the home declares — the repository root for a `repo:` home, the vault root for a `vault:` one — so the citation BEGINS with the home's own path and continues to the file.** With `artifact_homes.evidence` at `repo:.dev-flow/<batch_id>/evidence/`, that is `.dev-flow/<batch_id>/evidence/transcript-001.txt`, NOT `transcript-001.txt`: a path relative to the home itself resolves outside it and `V41` verifies none of those digests. No `./`, no `..`, no absolute or volume-rooted path. `V41`'s own finding prints the accepted shape with an example built from the home this batch declared, and is that rule's one home — and take the digest by re-reading the bytes *where they landed* (for git, from the index blob). Mark the home `-text` in `.gitattributes` before the first evidence file, or a normalising git stores bytes that do not hash to what you recorded.

| Evidence artifact | Path — under `artifact_homes.evidence` | SHA-256 |
|---|---|---|
| `<transcript / capture / snapshot>` | `<the path, as stored>` | `<the 64-hex digest of the bytes AT THAT PATH>` |

*(Delete the row above when the field reads `none` — a placeholder beside a declared empty is the one contradiction this page can still print.)*

| Field | Value |
|---|---|
| **Evidence files** | `<N artifacts, each at the declared home and cited with the digest of its stored bytes — or: none — this increment cites no evidence file>` |

## 4b · Independent review

In `fast` the reviewer is the author, and that is DECLARED — not omitted and not waived. Write the reserved token **`SELF-REVIEW — fast mode`** followed by the verdict and how every HIGH was resolved. `V36` accepts that token only while `state.json` says `mode: fast`. The one other legal empty, in every mode, is `WAIVED-BY-OPERATOR — <reason>`, and the reason is not optional: it says the review was owed and skipped, which is a different fact from a self-review. `ABSENT` is the empty state, never a value. Escalate to a `code-reviewer` pass on a risky increment — the named forms `V36` accepts are `code-reviewer`, `security-reviewer`, `qa-reviewer`, `ux-reviewer`, `tester`, `human:<name>`.

| Field | Value |
|---|---|
| **Independent review** | `<SELF-REVIEW — fast mode · the verdict · how every HIGH was resolved — or: WAIVED-BY-OPERATOR — and the reason, in the operator's own words>` |

## 4c · Evidence checklist (`software-dev`, five lines)

*(The five checks `agents/software-dev.md` §*Evidence checklist* lists — each ✓/✗ with one line of evidence: `file:line`, command output, or a finding link. THIS is their home; they are not the long packet's 16-row gate checklist, which `fast` does not owe.)*

| Check | ✓/✗ | Evidence |
|---|:--:|---|
| `<the check, from that role's list>` | | `<file:line · command output · finding link>` |

## 5 · Risks

*(What could break that this increment does not cover. Specific enough to act on.)*

## 6 · Pending items

*(Anything surfaced and not closed here. Every line lands in the batch's backlog at close. A deferral carries the reserved marker `⏸ DEFER` and is keyed to a backlog entry — `V42` reports every marker that is not.)*

## 7 · Suggested next task

*(The next increment, or the reason this batch is ready to close.)*
