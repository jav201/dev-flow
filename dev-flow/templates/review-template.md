# Review — <PROJECT> — Batch <BATCH_ID>

> **Artifact language:** canonical English scaffold. Generate in the batch's development language (`state.json` `language`).
> Phase 2 artifact. Reviewers (in parallel): `architect` ∥ `qa-reviewer` ∥ `security-reviewer`.

> **Owed in.** `fast` — · `core` ✓ · `full` ✓
> **Source:** `/dev-flow-init` step 4's seed-by-mode table, which is this fact's one home (flow rev72, `T05`). A mode marked `—` **does not owe this artifact, and its absence is not an omission**; `by trigger` means the station exists only when the `triggers` block fired, and `stations_active` in `state.json` is the authority for *this* batch. Where a SECTION or a gate row is owed more narrowly than the artifact, it says so on the row.

## ✅ Verdict (read first)

- **Gate:** `approve` → Phase 3  /  `iterate-to-refine` → Phase 1 (blockers present)
- **Out-of-scope findings:** `<N>` named and routed below  /  `none`

> **ONE RETURN EDGE, AND IT IS P1 — flow rev72, `T07`.** This station's input is the approved
> `01-requirements.md` and nothing else, so a **requirement defect is the only defect it can send
> anywhere**. Until rev72 this line carried one arrow with two classifications on it, naming the
> station of only one of them, so a
> reviewer reusing the format for an implementation finding was told to reopen requirements that are
> not wrong. (The retired arrow is recorded as `iterate → Phase 1` — wholly inside one span, because a
> history note spelled as live prose reads to a scanner exactly like the mandate it replaced.) The exits are now per class, and the routing agrees with `validation-template.md`
> §*Result* and with `/dev-flow` §*Gate decisions* rather than contradicting both.

| Finding class | Where it goes | Gate token |
|---|---|---|
| **requirement defect** — ambiguity, contradiction, a missing `AT`, an untestable validation method, a `should` inside a statement | **Phase 1**, via the §6.5 Before/After amendment | `iterate-to-refine` |
| **implementation defect** — an existing symbol, test or surface the approved requirements oblige to change | **carried into Phase 3** as a named finding with its owning increment; the increment gate closes it | *(none — this station mints no P3 token)* |
| **security finding on an existing surface** | `security-reviewer`, re-invoked per §*Scope-change re-routing*; recorded in §Security review summary. A blocker among them **is** a requirement defect and routes as one | per the row above |
| **anything else** | **named in §Findings with the station that owns it.** A finding nobody routed is a finding nobody owns — that is what the ⚠ line above counts | *(none)* |

> **`iterate-to-fix` (P3) is PHASE 4's token and is never minted here.** Phase 4 has both edges
> because it is the only station that observes the implementation: *black-box FAILS + white-box
> PASSES ⇒ the requirement is wrong ⇒ `iterate-to-refine`; black-box fails from a wrong LLR ⇒
> `iterate-to-fix`*. Phase 2 observes neither.
- **Findings:** `<B>` blocker · `<M>` major · `<m>` minor
- **shall/should check:** ✓ clean  /  ✗ misuse (blocker)
- **Two-layer (blockers):** ✓ every story has an `AT` · output reqs name deliverable+observation · both trace chains complete · ATs are genuinely black-box  /  ✗ `<which>`
- **Census (change-first):** done — best-effort + gate-confirmed  /  ⚠ incomplete   (NEVER stamp "VERIFIED COMPLETE")
- **Security:** ✓ no findings  /  ⚠ `<N>` findings
- **Evidence checklists (architect / qa / security):** ✓ all complete  /  ✗ `<missing>`

> If gate = `approve` and every line is ✓, the Detail below is reference. Any blocker/⚠ → read the matching part.

---

## Detail (reference)

### Findings
| ID | Reviewer | Severity | Area / Req | What | Recommendation | Status |
|----|----------|----------|------------|------|----------------|--------|
| *(example — delete)* F1 | architect | blocker / major / minor | | | | open / fixed |

### shall / should check
> Any modal `should` / `debería` inside an HLR/LLR statement is a writing error → blocker.

`<result>`

### Two-layer acceptance review (blockers)
> (a) every story has a black-box `AT`; (b) every output-producing requirement names its observable deliverable + observation method; (c) BOTH traceability chains complete (behavioral US→AT→outcome + functional US→HLR→LLR→TC); (d) each `AT` is genuinely black-box — drives the surface, asserts the outcome, references NO internal symbol.

| Story / Req | (a) AT present | (b) deliverable+method named | (c) both chains | (d) black-box pure | Status |
|-------------|----------------|------------------------------|-----------------|--------------------|--------|
| US-001 | yes/no | yes/no/n/a | yes/no | yes/no | ✓ / blocker |

### Supersession census (change-first)
> Planned new/moved/edited files checked against EVERY guard family (behavioral-placeholder · structural/placement · AST-composition · engine-frozen). State reservations; the increment gate is the completeness guarantee, not this census.

`<files × families run · reservations · what the I-gate must confirm>`

### Security review summary
`<security-reviewer findings + verdict, or "no attack surface this batch">`

### Evidence checklists (full) — architect · qa-reviewer · security-reviewer
> Attach each reviewer's completed evidence checklist (items in their agent files), ✓/✗ + one-line evidence.
