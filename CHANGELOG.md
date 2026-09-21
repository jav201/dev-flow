# Changelog

One entry per flow revision shipped to this repository. The flow's full revision log stays in the private canonical repository; this file records what a user of the published skill receives.

## 2026-09-21-rev91 — authorization on runtimes that cannot prompt
- On a runtime with no prompts, the operator's initial commission is the batch's standing authorization, declared in the spec header at Phase A; the guided gate records its decision instead of waiting for one, and a gate that was actually asked writes `asked at the gate`. On runtimes with prompts nothing changes.
- The validator's guided-ledger rule gains a fourth obligation: the spec header and the decisions ledger must agree on which authorization model the batch ran under.

## 2026-09-21-rev90 — the fast path's mechanical steps ship as tools
- `scripts/devflow-init-fast.py`: writes the fast batch declaration (batch id, minimal `state.json`, spec from the template with its header filled, evidence and increment homes, `.gitattributes`, an empty decisions ledger). Defaults to the current directory as the project root, prints the resolved root, and refuses to scaffold inside a flow installation.
- `scripts/devflow-evidence.py`: SHA-256 rows for the increment packet, `-text` marking, and `--check` against the committed blob and the packet's recorded digest.
- `scripts/devflow-validate.py --brief`: verdict first, BLOCK and NOTICE lines only, one summary line for rules with no subject; same exit code.
- The short fast packet states one legal empty for every field a fast increment may not owe; the adapter shows an example decisions-ledger entry.

## 2026-09-21-rev89 — the fast path says each rule once
- `commands/fast-dev-flow.md`, the fast templates and the adapter's fast sections rewritten so every operative rule of a fast batch is stated once, plainly, in the file the reader has open at that step; other files point. Revision citations and defensive prose removed; nothing became weaker (56 imperatives audited: 49 kept, 5 merged, 2 discharged).
- The opening declares that every flow path is relative to the `dev-flow/` folder the skill was installed from; the close says "record the `C` decision, then run the gate".

## 2026-09-20-rev88 — gaps a weak reader found
- Gate ids for the fast batch (`A`, `increment-NNN`, `C`) declared once in the reader's map; the decisions-ledger date form stated where the entry is defined.
- The validator's closing-gate witness reads the spec's close cell; two rules stop refusing the fast batch-id grammar and read the premise table from the fast spec.
- `scripts/devflow-scan-spec.py` ships: the security-pattern scan the fast command specifies, reading its pattern list from the command at every run.

## 2026-09-20-rev87 — first public-ready export
- Guided first run: `guided: true` on a project's first batch; at every gate the agent shows the next step's rule and command and records the decision; the validator checks that every reached gate carries a decision.
- Runtime-agnostic adapter (`SKILL.md`), bundle-run gate that refuses a manifest whose files were altered, self-contained publication with no references to the flow's origin project or author environment, control catalog split into a consultable `SKILL.md` and a forensic `REFERENCE.md`, human review ledger in the close artifact.
