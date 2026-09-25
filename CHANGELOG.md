# Changelog

One entry per flow revision shipped to this repository. The flow's full revision log stays in the private canonical repository; this file records what a user of the published skill receives.

## 2026-09-24-rev92 — the selftest passes on a machine that has never held a canon home
- `scripts/devflow-validate.py --selftest` now exits 0 from a clean checkout of this repository. It did not before: on GitHub Actions, ubuntu-latest, Python 3.11, it printed 50 failing arms and then died with `FileNotFoundError` on a path under `~/.claude`. Every one of those arms passed on the author's machine, because that machine has the private authoring tree the arms were silently reading.
- One resolver now answers "where does this flow live" for both layouts. Templates, commands, agent roles, the manifest and the control catalog are read from the bundle you installed. A subject that only the authoring tree can hold — a live project record, a second checkout, the whole Python file set, the diagram directory — makes the arm print a named SKIP saying what was not measured and why, and a closing line counts those skips by subject. None of them is scored as a pass.
- The adapter publishes the full list of arms that skip in a bundle (28 names over 30 lines, grouped by the missing subject), and an arm compares both numbers against a real bundle run in both directions.
- The selftest checks its own flow home before its first arm. A skill install is `dev-flow/` and `dev-flow-lessons/` side by side; if something is missing, the run says which folder, says it measured nothing, and exits non-zero — instead of running every check against a population that is not there.
- The selftest's own bundle run is now started with an empty `HOME` and no `DEVFLOW_*` variables, so the authoring tree cannot stand in for the tree being measured, and a new arm requires that no arm be red in that run and green in the parent's.
- Continuous integration on this repository runs the selftest in bundle mode and the gate on an empty tree on every push — and its first run found a second problem of the same kind: the checks assumed the machine they were written on. Two of those were real defects in the flow, not in the tests. `V40` rejected every checkout identity on any system without drive letters, so on Linux and macOS it refused what it was supposed to accept; and the loader that resolves a batch's artifacts walked the directory in whatever order the filesystem returned, so two copies of one repository could resolve different documents for the same filename. Both are fixed, and the checks that would have caught them are now written against the rule rather than against one machine.
- The list of arms that skip in a bundle differs by platform, and the adapter now publishes both counts.

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
