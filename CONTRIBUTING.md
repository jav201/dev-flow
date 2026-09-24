# Contributing

Thank you for reading this far. Two things make this repository unusual, and both shape how a change lands.

## The record is the product

Every rule in the flow has a reader: a validator arm that fails when the rule is not honored, and a mutant that proves the arm can fail. A change that adds prose without a reader, or a reader that cannot go red, is not finished. If you propose a rule, propose with it the arm that reads it and the mutation that kills the arm.

## How a change lands

1. **Open an issue first** for anything beyond a typo: what the change closes, and how a reader would notice if it were missing.
2. **Freeze, review, bump.** A change is frozen, reviewed independently of its author, and only then does the manifest's revision and per-file hash move. Changing a shipped file without a new revision is a BLOCK by design: the published copy verifies itself against its own manifest.
3. **The fresh-reader test is the acceptance criterion** for anything that touches what a user reads. A runtime with no prior context (a second CLI, a fresh install) is given a toy repository and asked to run a batch with the skill alone, logging every point where it had to guess. A change to the fast path is accepted when that reader closes the batch and its verdict names no obstacle the change was meant to remove. The protocol, the prompt and the classification of findings (skill defect / runtime artifact / reader deviation) are the same for every revision.
4. **One home per fact.** State a rule once, in the file the reader has open at that step; everywhere else, point. A script that checks for duplicated sentences across the fast-path files runs at every revision and must report zero.
5. **No identity in the tree.** Shipped files carry no person, organization, project, path or credential. A scan runs before every export; a hit blocks the export.

## The validator's anatomy, for anyone adding an arm

`python dev-flow/scripts/devflow-validate.py --selftest` prints every arm; each line starts with its family. Counts below are from one run at the current revision — re-derive them, do not trust them:

| Family | Subject | Example |
|---|---|---|
| `V<n>` rules | your project's batch record (the gate itself) | `V41` re-hashes every cited evidence file |
| `ART` (34), `IFC` (28), `TPL` (14), `MD` (13), `LANG` (13) | the artifacts and templates the rules read: reserved fields, interface contracts, template shapes, markdown grammar, translated-plane literals | `TPL FAST-PACKET-reaches-the-rules` |
| `MUT` (33) | the mutation registry: every arm provably able to fail, every mutant anchored | `MUT REGISTRY-anchors-live` |
| `FV` (16), `MAP` (5), `BUN` (2), `SELF` (2) | the manifest's own figures, the file map, canon→bundle staging, the selftest's exit | `FV CONTROLS-count-declared` |
| `CMD` (12), `DFI` (12), `SCR` (4), `CAT` (10) | the shipped commands, the init command, the scripts, the control catalog | `SCR EVIDENCE-rows-and-check` |
| `PRE` (12), `ENC` (4), `DET` (6), `SEL` (6) | preflight probes (git, encoding, case folding), verdict encoding, determinism, exemptions | `ENC VERDICT-live` |
| `ATL` (12), `REV` (11), `INT` (9), `DEP` (9), `SYN` (8), `PUB` (7) | atlas derivation, reviews, integrity, deployment record, bundle sync, publication (no identity in the tree) | `PUB no-declared-names` |

An arm states what it expected and what it got on one line, and a mutant in `scripts/devflow-mutants.json` names the arm it must redden. Add both, or neither.

## Contributions and license

By submitting a contribution you agree that it is licensed under the Apache License, Version 2.0, as stated in Section 5 of the License (see `LICENSE` and `NOTICE`). Keep the copyright and attribution notices intact; do not add names to shipped files — attribution lives in `NOTICE` and in the commit history.

## What we will not merge

- A rule with no reader, or a reader with no mutant.
- A second wording of a rule that already has a home.
- A change that makes a fresh reader's verdict worse, even if it makes the author's life easier.
- Anything that requires a specific machine, account or project to run.
