# Batch close — <PROJECT> — Batch <BATCH_ID>

> **Artifact language.** Canonical **English scaffold**; generate in the batch's language — the **prose**,
> and never a label.

> **Owed in.** `fast` — · `core` ✓ · `full` —
> **Source:** `/dev-flow-init` step 4's seed-by-mode table, which is this fact's one home (flow rev72, `T05`). A mode marked `—` **does not owe this artifact, and its absence is not an omission**; `by trigger` means the station exists only when the `triggers` block fired, and `stations_active` in `state.json` is the authority for *this* batch. Where a SECTION or a gate row is owed more narrowly than the artifact, it says so on the row.

> **Reserved field names.** The **field names and block keywords below are language-independent** — the
> validator parses them literally and they are never translated:
> `Conditional-gate discharge` · `New controls` · `Human perimeter` · `Human review ledger` · `Gated tree` · `⏸ DEFER`
> **And the §6 DEPTH tokens — cell VALUES rather than field names, reserved for the same reason:**
> `light` · `rigorous` · `spot-check` · `none` · `✅` · `❌`. A CLOSED set, declared closed by the first
> revision that ships it — so the vocabulary a later promotion of `V54` to BLOCK will need already exists,
> instead of being introduced over a free-text field that six authors have by then written six ways.
> Everything else on this page — headings, guidance, the prose in every cell — is translated with the batch.
> **One strategy, not two:** the flow ships no alias table, so a translated label is read as an ABSENT one and the rule keyed on it reports a true-sounding silence.
> **And one FLOW-WIDE reserved token, read out of this artifact by `V42` no matter which template minted it:** `⏸ DEFER`. It is a MARKER rather than a field name, which is why it is stated here *and* in `/dev-flow` §Language of artifacts rather than in a per-template list — a deferral can be written in any batch artifact, including the ones that carry no block at all. Measured: `⏸ DIFERIDO` returns the empty declaration list AND the empty near-spelling list, so a translated marker is indistinguishable from a batch that deferred nothing.

> **Used by `mode: core`** in place of the full `05-postmortem.md` + `06-docs/`. Six sections, all
> six required. **THIS FILE IS THE CANONICAL COPY** and its home is the **repo**
> (`.dev-flow/<batch_id>/05-close.md`) — operator ruling `Q22`, flow rev72. The vault
> `<batch_id>-README.md` (`artifact_homes.metrics`) is a **GENERATED VIEW of this file, never a second
> source**, and **`/dev-flow-sync` step 6 is the only thing that writes it**; `/dev-flow` never writes
> the vault. So the batch exists for the cross-batch Dashboard without paying for the docs layer, and
> when the two disagree **this file is the one that is true**.

> **Notice convention.** `⚠` yellow = declare and continue · `✗` red = block · `✓` green = satisfied
> **with its citation**.

---

## 0 · Gate record — which tree this close gated

| Field | Value |
|---|---|
| Gate record | `<the validator command, its exit code, and 0 block · date>` |
| Gated tree | `<the 40-hex HEAD at the gate · clean — or: dirty — the files>` |

> **`Gated tree` BINDS THE RECORD TO THE BYTES, and THIS ROW IS THAT RULE'S ONE HOME for `core`
> and `full` (flow rev94).** Write it at the close gate, from that run's own two commands —
> `git rev-parse HEAD` for the 40-hex ref, and `git status --porcelain` for the word after it:
> `clean` when it printed nothing, `dirty — <the files>` when it did. **`V57` reads it at every
> later run** and prints `record predates this tree by N commit(s)` when `HEAD` has moved — or
> says the record is AHEAD, or that the two have diverged — and names the files that are dirty
> against `HEAD`, which is what `git status --porcelain` measures. **It is a NOTICE and never a block:**
> a closed batch is allowed to be followed by work — the gate's job here is to say so instead of
> printing the same verdict over different bytes. In `full`, where this file is not seeded, the
> same two rows go in `05-postmortem.md` and `V57` reads them there. **Expect `predates this tree by
> 1 commit(s)` immediately after the close**, because the commit that carries this row is itself one
> commit later than the tree it names; the figure is the record's AGE, and that is what it is for.
> ⚠ **Declared bound:** the ref proves WHICH tree was gated, not that the tree was good.

---

## 1 · What changed

*(BLUF. What the user can now do that they could not before, and through which surface. Then the mechanism.)*

| Requirement | Version | Verified by | Verdict |
|---|---|---|---|
| `R-NNN` | `vN` | `AT-NNN` · `TC-NNN` | |

---

## 2 · New controls discovered — and where they landed (C-45)

A control found here is **not this project's property**. If it is portable it must reach every project
that runs this flow, or each one re-learns the same lesson at full price.

| Control | What failure it closes | Measured origin |
|---|---|---|

**The four landings — record which ones actually happened. Command-but-not-template is *half-encoded*, and the missing half is the enforceable one:**

| # | Landing | Done? | SHA / path |
|---|---|---|---|
| 1 | the **command** (`commands/…`) — the rule itself | | |
| 2 | its **artifact** (a template section) — a control with no output degrades to "I thought about it" | | |
| 3 | the **catalog** entry (`dev-flow-lessons`) with its measured origin | | |
| 4 | **committed and pushed**, manifest re-hashed and bumped | | |

- **New controls:** `<N control(s) minted → C-NN, C-NN | none — the reason this batch minted none>`

**Read by `V51`.** The table above says where each control landed; this field says **how many there
were**, and it is the one a reader can count across batches without opening every close artifact in
the record one at a time. *A batch
that minted none says so in the field* — an absence DECLARED and an absence OMITTED do not render
alike, and only the declared one can be counted. Several consecutive batches finding none is a signal
the catalog has dried up, not that the system matured; that signal is only visible if each batch
answered.

> ⚠ **This field does NOT decide whether a lesson deserves to be minted.** It reads whether the batch
> ANSWERED. Encoding a control is the operator's sitting, under the project's own control-encode rule;
> a reader is not an approval. What the field removes is the condition that let the debt go
> **uncounted** between sittings — the condition under which this project reached four consecutive
> batches at zero before anybody wrote the number down.

---

## 3 · Working-file reconciliation (C-44)

**No file this batch touched may be left in limbo.** Run it as a mechanical sweep, never from memory:
`git status --short` in **every** repository touched — auxiliary repos outside the project tree included
(a skills / commands / config repo counts) — plus `git log <branch> --not --remotes` for commits that
exist and were never pushed.

| File | State | Evidence |
|---|---|---|
| `<path>` | ✅ committed **and landed** (PR / merge named) · 🗑️ deliberately reverted · 📋 left on purpose, path + remaining work in the backlog | |

- **Pre-existing dirt is reported as FOUND, never swept into this batch's commit** — committing another
  session's work in progress is its own defect.
- ⚠ Any commit that exists and never landed: work that is finished but unlanded is indistinguishable,
  to every later reader, from work never done.

### Conditional-gate discharge

Any gate that closed as *"once items 1–N land this is a PASS"* — each item listed, **discharged by
re-reading the artifact**, never by trusting the corrective pass ran. *A conditional verdict is not an authorisation.*

- **Conditional-gate discharge:** `<N condition(s) · ✅ all discharged | N condition(s) · ⚠ M outstanding, named below | none — no gate closed conditionally>`

| Condition | Discharged? | The artifact line that proves it |
|---|---|---|

**Read by `V50`.** The table carries the per-condition evidence; the field carries the **roll-up**, and
the roll-up is what a gate can read. *A cell that names conditions without saying whether they were
discharged is the empty state, never a value* — "the corrective pass ran" is the sentence this whole
section exists to refuse.

**The legal empty is a declaration.** `none — no gate closed conditionally` is an answer; a missing
field is not, and the two must not render alike. Write it whenever every gate this batch closed was
closed outright — that is the common case and it costs one line.

> ⚠ **Its one open failure, declared here rather than discovered later.** This closes the CLOSE-side
> half of the fix-gate question — the conditional verdict now has a reader at the close. The gate-side
> half is `C-14`/`V32`'s, and the deferred `F-8` question was retired as subsumed by them. Neither half
> grades: `V50` reads whether the roll-up was written, never whether the discharge is real. That stays
> the reviewer's, and it is why the third column asks for **the artifact line**, not for a claim.

---

## 4 · Backlog reconciliation — the carry-over contract

Three moves, **all three required**. The batch is **not closed** until the canonical backlog reflects it.

1. **Mark shipped** — every item this batch closed, struck / `DONE`, with its PR number and merge SHA.
2. **Carry forward — drop nothing.** Every still-open item **plus** every new carry, deferred finding
   and "suggested next task" the increments surfaced. If this batch surfaced it, the backlog owns it now.
3. **Refresh the header** — the recorded `origin/main` tip and a `last refresh: <date> (<batch_id> close)` line.

**Read the deferral census before move 2, and file what it names.** `V42` reports every ⏸ DEFER marker in `.dev-flow/design/**`, in an ADR or in the batch record that is keyed to no backlog lane — deferrals born BEFORE this batch, which move 2 cannot see because it sweeps what the batch produced. It is a READ and not a fourth move: three moves, still all three required. See `/dev-flow` §*A deferral carries the marker*, which is that rule's one home.

| Item | Move | Reference |
|---|---|---|

---

## 5 · Batch metrics — the 13 keys of `core`

Extract, do not invent: a key the artifacts did not record goes `null`, and the key is never dropped.

> **The number in that heading is DERIVED from the block below, by `KEYCOUNT-derived`, and it was
> wrong at three sites for as long as the block has existed.** It read *"the 12 keys"* over a block of
> **13** — in a section whose own instruction is *the key is never dropped*, so an implementation keyed
> on the number rather than on the block is one key short of a contract that forbids exactly that. The
> arm parses this fence, compares it to every prose site that names a count for it, and reddens on a
> planted fourteenth key. **Do not restate this figure in `commands/` or `templates/`:** the arm
> DISCOVERS every unquoted `N keys` claim across those two directories and requires each to be one a
> yaml fence backs, so a new site reddens instead of quietly becoming a second inventory (`C-50`).
> `docs/**` is a declared exclusion — the changelog records what was believed on a date, and rewriting
> those rows to satisfy a census would be editing the past to make the present measurable.

```yaml
type: dev-flow-batch
project: <str>
batch_id: <str>
mode: core
verdict: pass | iterate
increments: <int>
source_files_max: <int>          # highest source-file count in any one increment
notices_raised: <int>            # ⚠ declared across the batch
rework_returns: <int>            # items that came back, per QA's phase checklists
triggers_fired: <str>            # e.g. "B1,B4,C8"
tests_base_to_post: "<base> -> <post>"
new_control: <str | none>
open_items_next: <int>
```

- ⚠ **A notice that has now repeated for three consecutive batches** must be resolved here: it becomes a
  rule (and then it blocks) or it is retired (and stops cluttering the checklist). Record which.
- **Declare what was NOT done** — e.g. evaluation with real users (ISO 9241-210). An omission that is
  stated is a limit; an omission that is silent is a false claim.

---

## 6 · Human review ledger — what a human audited, at what depth

The gates record the **machine's** verdicts. This section records the other half of the balance: what
a human actually read, at what depth, and — declared, never omitted — what was deliberately **not**
reviewed. **A human review without a record is indistinguishable from one that never happened.**
Depth is the reviewer's choice; the ledger does not force rigour, it makes the choice **visible**.

> **What the flow ALREADY records, and what this section adds — so that nothing here is re-minted.**
> WHO and WHEN have had readers for three revisions: every increment packet names its reviewer
> (`V36`), the validation artifact names who completed the evidence checklist (`V48`, in `V36`'s
> grammar reused), and `state.json`'s `decisions_log` carries every gate decision with its date.
> **Not one of them records the DEPTH of the reading, or a reading DECLINED.** That — depth, and the
> declared non-review — is the whole of what §6 adds. It is also why the name in the roll-up is
> `V36`'s identity grammar **reused and not re-minted**: the same question at a different station
> (`C-50`).

**Depth is a CLOSED token set, and `Human review` is a glyph. Both are declared ONCE — in the
Reserved field names block at the top of this file — and neither is ever translated;** re-listing
them here would be a second inventory of the same vocabulary (`C-50`). A depth that vocabulary
cannot say is a signal that the **row** is wrong, not that the set is too small.

| Artifact | Machine verdict (citation) | Human review | Depth | Deliberately NOT reviewed |
|---|---|---|---|---|
| *(example — delete)* `01-requirements.md` | gate §4 ✓ · `V26` green | ✅ | `rigorous` | |
| *(example — delete)* Test cases / ATs | `V37` 12/12 · mutants 9/9 KILLED | ✅ | `light` | the fixture matrix behind `AT-007` |
| *(example — delete)* Evidence view | `V41` — every cited file resolved | ❌ | `none — read the packet summaries instead` | |
| *(example — delete)* Code | gates + reviewer verdict `PASS` | ✅ | `spot-check` | not audited line by line |
| `<one row per human-auditable artifact this batch produced>` | | | | |

The second column carries a **citation**, never prose: the machine verdict already has a home and is
referenced from here, never copied (`C-50`).

- **Human perimeter:** `<what this flow does NOT cover and the operator owns — e.g. personnel selection, organisational environment, business judgement | none — why nothing lies outside>`
- **Human review ledger:** `<human:NAME — N artifact(s) reviewed, M rigorous · K declared not-reviewed | none — why this batch recorded no human review>`

**Read by `V54`** — NOTICE, under the three-batch convention: three batches carry it, then it BLOCKs
or it is retired. **Both fields are owed.** **The reviewer's name LEADS the roll-up**, in `V36`'s
accepted forms reused unchanged (`human:<name>`, a flow agent, or `WAIVED-BY-OPERATOR — <reason>`) —
a name at the END of a sentence whose subject is a count is read as no name at all, deliberately: the
ledger's claim is that a *person* did this reading. The perimeter field is not decoration — it is the
declaration that **green gates say nothing about what lies outside the flow**, and an absent
perimeter field is a finding for exactly that reason: a reader who cannot see the boundary reads the
gates as covering everything. `none — <reason>` is the legal empty on both (`C-55`): an absence
**declared** is an answer, an absence **omitted** is a gap, and the two must not render alike.

> ⚠ **What `V54` does NOT do, declared here rather than discovered later.** It does not judge the
> review's **quality** — a reviewer can write `rigorous` and have skimmed, and no keyed field can
> detect that; the quality stays with the reviewer and with whoever reads this artifact next. It
> does not count or grade the table's **rows**: the depth tokens are reserved so that a later
> promotion has a vocabulary, not because a rule reads a row today. And it audits nothing **inside**
> the perimeter it asks you to declare — declaring the boundary is the obligation; what lies beyond
> it is the operator's, which is the point of writing it down.

**If this table grows past about six rows, the batch is producing human-auditable artifacts that have
no name.** The symptom is in the artifact cut, not in the table.
