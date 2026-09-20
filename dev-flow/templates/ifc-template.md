# Information Flow Contract (IFC) — <PROJECT> — Batch <BATCH_ID>

> **Artifact language:** canonical English scaffold. Generate the artifact in the batch's
> development language; for Spanish batches translate the prose — headers and guidance — and
> **never a label**. **Where that language is declared depends on the mode:** `state.json`'s
> `language` key in `core` and `full`; in `fast` the five-key declaration carries no such key by
> design, and the spec's §0/§1 is where the batch's language is fixed. This template is owed in
> all three modes, so it owes both readings.

> **Reserved field names.** The **field names and block keywords below are language-independent** — the
> validator parses them literally and they are never translated:
> `FLOW` · `COMPONENT` · `fn` · `id` · `owner` · `address` · `consumers` · `cardinality` · `inputs` · `outputs` · `parent` · `⏸ DEFER`
> Everything else on this page — headings, guidance, the prose in every cell — is translated with the batch.
> **One strategy, not two:** the flow ships no alias table, so a translated label is read as an ABSENT one and the rule keyed on it reports a true-sounding silence.
> **And one FLOW-WIDE reserved token, read out of this artifact by `V42` no matter which template minted it:** `⏸ DEFER`. It is a MARKER rather than a field name, which is why it is stated here *and* in `/dev-flow` §Language of artifacts rather than in a per-template list — a deferral can be written in any batch artifact, including the ones that carry no block at all. Measured: `⏸ DIFERIDO` returns the empty declaration list AND the empty near-spelling list, so a translated marker is indistinguishable from a batch that deferred nothing.

> **Where this lives.** Inside `.dev-flow/<batch_id>/01-requirements.md`, authored in Phase 1 with the
> HLR/LLR set. Give it its own section; the validator anchors on the `FLOW:` and `COMPONENT:`
> keywords inside fenced blocks, not on a heading, so placement is free but the block syntax
> is not.

> **Owed in.** `fast` ✓ · `core` ✓ · `full` ✓
> **In `fast`, PART A ONLY** — `SOURCE → NODES → SINK` with each node naming the requirement that owns it, written inside `.fast-dev-flow/spec.md` rather than in a requirements document. **Part B — addresses, `cardinality`, `consumers` — is NOT owed there**, and its trigger question is that flow's escalation signal: a change that moves how a consumer REACHES something belongs in `/dev-flow`. `/fast-dev-flow` Phase A step 5 is that obligation's one home; this row records that the artifact is owed, and §*Part B* below records where it stops. Until rev84 this row read `fast —` against a command that has required Part A since `C-54`, and a reader following the header alone wrote no contract at all.
> **Source:** this row is DERIVED and is not read off a table, and rev85 says so here rather than pointing at a home that does not hold it. The IFC is not a seeded FILE: it is a SECTION of the artifact each mode already owes — `01-requirements.md` in `core` and `full`, `.fast-dev-flow/spec.md` §3c in `fast` — so it is owed wherever its HOST is, which is why all three cells read `✓` while `/dev-flow-init` step 4's seed-by-mode table has no row for it and correctly does not mention it. That table remains the one home for the templates it DOES seed (flow rev72, `T05`), and every other template's `Owed in` line is read off it. A mode marked `—` **does not owe this artifact, and its absence is not an omission**; `by trigger` means the station exists only when the `triggers` block fired, and `stations_active` in `state.json` is the authority for *this* batch. Where a SECTION or a gate row is owed more narrowly than the artifact, it says so on the row. ⚠ **This template has no row of its own in that table**, because it is not seeded as a file: it is a SECTION of the artifact the mode already owes — `01-requirements.md` in `core` and `full`, where it is owed exactly where `req-template.md` is, and `.fast-dev-flow/spec.md` in `fast`, where `/fast-dev-flow` Phase A step 5 owes Part A. That is why this row is `✓` in all three modes while the seed table has no row to read it off: a template with no file of its own is owed wherever its HOST is.

---

## 0 · Why this artifact exists — the defect it was written from

**Definition — a MISADDRESSED OBSERVABLE.** A check is misaddressed when it is **not vacuous**
— the predicate can fail, and it measures a property that is genuinely *true in the failing
case* — because the requirement declared the **value** a surface carries while the change moved
the **address** by which that value is reached. The classic shape is an oracle that discards the
dimension the failure lives in: set equality over rows whose consumers index them positionally.

| | |
|---|---|
| What the requirement declares | the **value** displayed |
| What such a change actually moves | the **address** by which the value is reached |
| The oracle that misses it | one that discards the dimension the failure lives in — set equality against a positional consumer |

**The missing sentence is always the same one:** the requirement never stated the surface's
contract with its consumers. *"Shall not alter X"* — altered **for whom?** For a human reading
the panel, nothing was altered; for the two readers indexing it, everything was.

(Origin: batch-79 — see dev-flow-lessons)

> **A `shall not alter X` is not verified by observing X. It is verified by observing the
> contract by which others depend on X — and that contract has to be written down, with its
> consumers named.**

This template is that contract. **`address` and `consumers` are the two fields the flow never
had, and the two that would have caught it.**

---

## 1 · Part A — Flow. **Always owed.**

Information flows always exist. Every batch declares them, whatever the stack.

```
FLOW: <id>
  SOURCE : <where information enters the system boundary>
  NODES  :
    - fn    : <the function that performs this transform>
      owner : <the LLR that owns this transform>
      in    : <shape in>
      out   : <shape out>
  SINK   : <where information leaves the system boundary>
```

**One field per line.** A node begins at `- fn :`; every following indented `key : value` line
belongs to it until the next `- fn :` or the next block keyword.

**Two obligations that make this more than documentation:**

- a node with **no `owner`** is unowned work — it exists in code and no requirement asked for it;
- an LLR that claims a transform with **no node** is unimplemented.

Both are mechanically checkable, and neither was checkable before this artifact existed.

---

## 2 · Part B — Boundary decomposition. **Conditional, on one question.**

> **Does the system's boundary have components that a consumer can address independently?**

| System | Part B? | Why |
|---|---|---|
| the terminal UI with screens and panels | ✅ | a consumer selects a panel and indexes its children |
| Sensor array | ✅ | channel 3 is addressable independently of channel 4 |
| DAQ card with per-channel calibration | ✅ | each channel has its own I/O and its own transform chain |
| Headless library, one entry point | ❌ | no decomposable boundary — Part A alone |
| CLI emitting one report to stdout | ❌ | one sink, no addressable sub-components |

**If the answer is no, the batch owes Part A and nothing else.** The question is deliberately
stack-free: it names no UI, no framework, no language.

```
COMPONENT: <id>
  PARENT : <parent component | SYSTEM>
  SURFACE: <the user-facing surface this component belongs to>   (optional)
  INPUTS : <name>: <type> ; <name>: <type>     ⊆ PARENT.INPUTS
  OUTPUTS:
    - id          : <name>
      value       : <what it carries>
      address     : <HOW A CONSUMER REACHES IT — selector, index, channel, offset>
      cardinality : <expected count, when the address selects a set>
      consumers   : <who depends on this address; `none` is legal and MUST be written>
      owner       : <LLR>
```

### The fields, and what each one is for

| Field | Why it exists |
|---|---|
| **`address`** | Changing it is a **breaking change even when the value is unchanged**. That is the batch-79 failure exactly, and declaring it turns an accident into a contract change |
| **`cardinality`** | Adding a fourth element where three were declared violates the **declared** contract, measured against the provider's own declaration — **no knowledge of consumers required**. ⚠ **NOTHING EXECUTES THIS COMPARISON.** The field is parsed, transcribed into the derived Atlas column (`V20` holds the Atlas and the corpus together) and read by **no rule**. **Measured by derivation rather than by a grep count, so the claim cannot go stale the way a number does:** an AST walk over the ten IFC readers finds the STRING CONSTANT `cardinality` in `_atlas_component_rows` alone — the Atlas column — and in no `v*_outcome` decision. *Constants, not prose:* a rule that merely MENTIONS the field in its docstring still does not read it, and the claim is about reading. The walk is `LANG RESERVED-ifc-derived`'s, and it is why the field is listed as reserved: translating it would move the derived Atlas and reopen `V20`, while changing no verdict. It is a contract an author and a reviewer compare against the surface **by hand**, and §5 says what that costs |
| **`consumers`** | Turns *"shall not alter X"* from unverifiable prose into a mechanical question: *do these consumers still resolve?* Entries are **paths**, optionally `::symbol` — see §3. Write `none` explicitly when there are none: **an omitted field is not the same claim as an empty one**, and the validator treats them differently |
| **`owner`** | Binds the output to the requirement that asked for it |
| **`SURFACE`** *(optional, rev42)* | Names the user-facing surface the component belongs to, so the derived Atlas can group by surface instead of by source file. **Decided by execution before the second surface existed** — the measurement is recorded in the originating project's own design record, which this publication does not carry, and the reasoning is restated here in full so nothing rests on a document you cannot open: with no field, a per-surface view is not derivable, and retrofitting after N surfaces costs N records — a one-way door priced at 1 record when it was opened |
| **`⊆` (balancing)** | A component cannot consume or emit what its parent does not declare. Called *balancing* after DFD / Structured Analysis, where it is a 45-year-old idea — do not invent a new name for it |

**`OUTPUTS` is a SECTION, and its emptiness is a claim — write `OUTPUTS: none` when a component
emits nothing.** Same rule as `consumers`, one level up: an omitted section is a question nobody
asked and `V12` reports it as *balancing NOT checked*, while a declared-empty one is a claim the
rule can test — and a parent declaring `none` makes any child emit **unbalanced**. Leaving the
section out to mean "nothing" is the shape `R-87-1` names: from batch-87 until rev74 the two
states were indistinguishable to the rule, so a parent with no outputs switched the emits half
of the check off for every child it had.

**`INPUTS` is a named list, not prose**: `;`-separated items, each `name: type`. This is not
formatting taste — **containment is a set operation and free text has no members.** An `INPUTS`
the validator cannot parse as a named list yields a `NOTICE` saying balancing was *not checked*,
which is worth more than a pass over something unreadable. The first draft of the worked example
below wrote `loaded-file state`, and it took writing `V12` to notice that nothing could ever
compare it to anything.

### Ordering commitments — write them now, enforced later

When an address selects a **set that consumers index positionally**, say so:

```
      address     : query(".loaded-detail"), INDEXED POSITIONALLY
      cardinality : 3
```

⚠️ **`cardinality` alone does not catch a REORDER** — the count holds, set equality holds, and a
positional consumer breaks anyway. That is the batch-79 defect wearing its other face. Closing it
is a separate control, deferred by operator ruling until the rule that would enforce it is
written. **Write `INDEXED POSITIONALLY` anyway from today**: it costs a phrase, and when the
control lands there will already be a corpus to enforce it against instead of a retrofit.

---

## 3 · Worked example — the defect, contracted

**Every value below was measured against the shipped code, not copied from the postmortem.**
That distinction turned out to matter — see the note after the block.

```
COMPONENT: loaded_panel
  PARENT : screen_workspace
  INPUTS : current_file: LoadedFile|None ; project_label: str|None
  OUTPUTS:
    - id          : artifact_slots
      value       : slot texts for primary, mac, a2l
      address     : query(".loaded-detail"), INDEXED POSITIONALLY
      cardinality : 3
      consumers   : tests/test_unload_feature.py::_detail_texts
                    tests/test_help_toggle_and_a2l_panel.py
                    tests/test_ui_commandbar.py
                    <project>/<ui-package>/styles.css
      owner       : LLR-120.2
    - id          : project_row
      value       : project string in its display form
      address     : query(".loaded-project-detail")
      cardinality : 1
      consumers   : tests/test_ui_commandbar.py
                    <project>/<ui-package>/styles.css
      owner       : LLR-120.2
```

**Adding a fourth `.loaded-detail` cell now violates `cardinality: 3` on a declared contract.**
The value is untouched; the *address* moved. The eventual real fix — a separate class for the project
row — is what the schema forces you to write down **in advance**.

> ⚠ **AND NO RULE SEES IT. THREE THINGS ARE BEING CONFLATED HERE AND THIS BLOCK SEPARATES THEM**
> (flow rev72, `T02`; until then this sentence ended `the address moved; the validator sees it`, and
> a promise of detection is worse than silence because it retires the author's own caution):
>
> 1. **THE DECLARATION — mechanical, and all that `V11` performs.** `V11` BLOCKs on exactly two
>    conditions: an `OUTPUT` with no `address`, and an `OUTPUT` whose `consumers` was omitted. It
>    receives no surface and observes none. **Reproduced 2026-09-10:** two components differing only
>    in address and `cardinality` — `query(".a")`/`3` against `query(".b")`/`999` — return the
>    *identical* verdict, *"1 OUTPUT(s), each with an address and a declared consumer list"*; the rule
>    was shown firing on what it really reads before its silence was believed — remove the `address`
>    and the same call returns `BLOCK`.
> 2. **THE CONSUMER GREP — mechanical, `V13`/`V14`, and bounded.** `V13` greps each declared LITERAL
>    address across the tree and NOTICEs a reacher that is not in `consumers`; `V14` resolves each
>    declared consumer to a file and its `::symbol`. Neither reads the surface either — they read the
>    repository.
> 3. **THE EXECUTED SURFACE PROOF — performed by NO rule, and owed as PROJECT EVIDENCE.** That the
>    address still selects, that it selects `cardinality` elements, and that their ORDER is unchanged
>    are three claims about a running surface. The batch that declares them **cites its own executed
>    check** — the test id, the command and its output — in the increment packet's `Emitted-form
>    assertion` or `Evidence files`. A valid schema is not a compatible surface, and **no universal
>    detection is claimed for any stack.**
>
> If automation for limb 3 is ever built, it is accepted only when it distinguishes a **changed
> selector**, an **added element** and a **reorder at equal cardinality**, and reports which of the
> three it covers.

> **A hand-maintained list of dependants only ever does one thing: go short.** `V13` is the rule
> that exists to catch it — grep the declared literal, and any file that reaches it and is not
> listed is an undeclared consumer. **This block's own `consumers` list was corrected three
> times, each time by measuring rather than reading**, and the third correction is the one that
> fixes the definition below.
>
> *(Origin: this worked example's own `consumers` list, corrected three times — see dev-flow-lessons)*

### What a `consumers` entry may be

**A dependant is not only something that reads the value; it is anything that would break if the
address moved.** A stylesheet reads nothing and still breaks when the class is renamed — it is a
consumer and it is declared. **That sentence is the SCOPE of this field**, it is what `V13` and
`V14` parse `consumers` against, and it is normative: it stays here whatever happens to the story
it was learned from.

**A path**, optionally with `::symbol`. Not a test id, not a prose description.

The design's sketch mixed both forms in one block — `test_unload_feature.py::_detail_texts`
beside `AT-B78-09` — and they are not interchangeable for a machine. `V13` compares this list
against the files a grep of the `address` returns, so an entry has to be **the kind of thing
that grep returns**. Trace to acceptance ids through the traceability matrix, which is the
artifact that exists for it; name the file here.

## 4 · The same schema on a system with no UI at all

```
COMPONENT: thermocouple_array
  PARENT : SYSTEM
  INPUTS : raw_counts: int16[8] ; cjc_temp: float
  OUTPUTS:
    - id          : channel_temps
      value       : °C per channel
      address     : channels[0..7], INDEXED POSITIONALLY
      cardinality : 8
      consumers   : trend_logger ; alarm_evaluator
      owner       : LLR-SENSE-4

FLOW: channel_temps
  SOURCE : ADC raw counts
  NODES  :
    - fn    : apply_gain_offset
      owner : LLR-SENSE-2
      in    : int16
      out   : mV
    - fn    : cjc_compensate
      owner : LLR-SENSE-3
      in    : mV
      out   : mV
    - fn    : type_k_polynomial
      owner : LLR-SENSE-4
      in    : mV
      out   : °C
  SINK   : channel_temps
```

Adding a ninth channel breaks `cardinality: 8` and every positional consumer — **the identical
defect shape, in a system with no interface at all.** That is the evidence the generalisation is
real and not a retrofit of one UI bug.

---

## 5 · What the validator checks, and what it cannot

| | Checks |
|---|---|
| `V10` | every `FLOW` node declares an `owner`, and that requirement id exists |
| `V11` | every `OUTPUT` declares `address` **and** `consumers` (an explicit `none` is legal and must be written, not omitted) |
| `V12` | `INPUTS ⊆ PARENT.INPUTS` and `OUTPUTS ⊆ PARENT.OUTPUTS` — balancing. `NOTICE` when the parent is not declared here, a list is unparseable, or **either side omits `OUTPUTS` entirely**: containment against something absent is not a pass. **From rev74 both halves draw that line.** A component that emits nothing writes `OUTPUTS: none`, and a parent that declares no outputs BLOCKs any child that emits — until rev74 an omitted section and a declared-empty one arrived as the same falsy set and the emits check silently did not run |
| `V14` | every `consumers` entry resolves to a file that exists, and its `::symbol` appears in it |
| `V13` | greps each declared literal `address` across the tree; a file that reaches it and is not in `consumers` is an **undeclared consumer**. `NOTICE` |

| | **NOT checked — owed as project evidence** |
|---|---|
| `cardinality` | **read by no rule.** Parsed, transcribed into the derived Atlas column, compared against nothing. Whether the address still selects that many elements is limb 3 of §3 |
| ordering | `INDEXED POSITIONALLY` is a written commitment with no reader, by the operator ruling recorded in §2. `cardinality` alone cannot catch a reorder and neither can anything else here |
| the surface itself | no rule opens a browser, a socket or a process. **The declaration is compared to the surface by the batch's own executed check, cited in the increment packet**, or it is not compared at all |

> **`V13`'s bound, stated so nobody reads its silence as coverage.** It can only follow addresses
> that are **literals**. An address computed at runtime cannot be grepped, so a project that
> builds addresses dynamically must recognise those *sites* in its own
> `docs/engineering-rules.md` — that taxonomy is stack vocabulary and does not belong here.
>
> **This is tolerable by design, and the reason is worth understanding — restated at flow rev72 so it
> stops naming a detection nobody performs.** Discovery is not the guard, and a total grep failure
> degrades the reported **blast radius**. What it does NOT degrade is the **declaration**: `address`
> and `consumers` are still checked for presence by `V11`, needing no knowledge of consumers at all.
> **It does not follow that a MOVED address is detected.** `cardinality` is read by no rule
> (§*The fields*), and `V11` compares no declaration against a surface — so the sentence that stood
> here until rev72, `it never degrades the detection`, promised a detection that exists only as
> §3 limb 3: **the project's own executed check, cited as evidence.**

**The severity escalation is the project's call, not the flow's.** `V13` ships as `NOTICE` so a
retrofit across existing surfaces cannot gate unrelated work. A project raises it to a blocker
per surface as that surface's contract is written — and records that decision in its own rules.
