<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/dev-flow-mark-dark.svg">
    <img src="brand/dev-flow-mark-light.svg" alt="dev-flow — the V that verifies" width="160">
  </picture>
</p>

<h1 align="center">dev-flow</h1>

<p align="center"><a href="https://github.com/jav201/dev-flow/actions/workflows/flow-selftest.yml"><img src="https://github.com/jav201/dev-flow/actions/workflows/flow-selftest.yml/badge.svg" alt="flow selftest"></a></p>

**A supervised engineering flow for AI coding agents whose record cannot be faked.**

Most agent workflows tell the model *what to write*. dev-flow also governs *how the work is recorded and checked*, the way software engineering has done it for decades: a V-model of stations, requirements traced to acceptance tests, increments with review packets, independent review, evidence that names its source, and a close with a post-mortem. That artifact structure is the control surface — the same one that regulated software practice relies on — carried over to agent-driven development and enforced rather than recommended.

Every batch leaves that record (requirements, increments, evidence, close), a validator reads it back, and the validator is itself tested by mutation — 1,594 self-test arms at the current revision, each proven able to fail. If a claim in the record has no reader, the flow treats it as a paragraph, not a control.

It works from **Claude Code, Codex, Kimi Code CLI or any runtime that can read a skill folder and run Python**. Outside Claude Code it runs *unguarded* — no named reviewer roles, no hooks — and the adapter says so rather than implying parity.

## Authorship and AI assistance

Copyright 2026 José Javier Granados Hernández. Licensed under the Apache License, Version 2.0 (see `LICENSE` and `NOTICE`).

This flow was developed with AI assistance (Claude), under the author's direction and review: the controls were distilled from the author's own project post-mortems, every design decision is the author's ruling, and every revision passed an independent review and a self-test before landing. The record of that process is the author's; the assistance is disclosed here because a flow whose thesis is an honest record should say how it was made.

## What you get

- **Two flows.** `/dev-flow` — a six-station V-model (requirements → review → implement → validate → close → docs) with supervised gates and independent review. `/fast-dev-flow` — three compressed phases for small changes in a repository you own.
- **A gate you can run anywhere.** `python scripts/devflow-validate.py <project root>` reads the batch record and reports BLOCK / NOTICE / not-applicable per rule, exits non-zero on a block, and verifies the bundle you are running against its own manifest — one changed byte in a shipped file is a BLOCK with the file named.
- **A control catalog.** `dev-flow-lessons/` — 31 numbered controls distilled from 54 post-mortems of one supervised, multi-agent flow: vacuous-check detection, acceptance-test oracles, gates and evidence, test hygiene, multi-agent orchestration, the security lens on "just text". The consultable `SKILL.md` is ~20k tokens; the forensic `REFERENCE.md` keeps every origin.
- **Templates that the validator reads.** Reserved field names, legal empties (`none — <reason>`), and a per-mode table of what each artifact owes. A row nothing reads is a defect here, and an arm checks that both ways.
- **A human review ledger.** The close artifact records what a human actually read, at what depth, and what was deliberately not reviewed — because a human review without a record is indistinguishable from one that never happened.

## Install — copy two folders

There is no installer. Copy `dev-flow/` and `dev-flow-lessons/` into the place your runtime discovers skills:

| Runtime | Where |
|---|---|
| Claude Code | the `skills/` directory of your Claude Code home. Invoke the `dev-flow` skill and follow its routing; do **not** copy the files under `dev-flow/commands/` out as standalone slash commands — copied out, they no longer know where the bundle lives, and their references to `init`, the templates and the scripts stop resolving |
| Codex CLI | the `skills/` directory of your Codex home (the `.codex` folder in your user directory) |
| Kimi Code CLI | your project's `.agents/skills/` (symlink or copy), or `kimi --skills-dir <path to this repo>` |

Then verify the copy from inside it:

    cd dev-flow
    python scripts/devflow-validate.py --selftest      # exits 0; canon-only checks SKIP by name
    python scripts/devflow-validate.py <your project>  # 0 block on an empty project

Requires Python 3.11+ and git. Windows, macOS and Linux.

## The record, and the gate's voice

What a batch leaves behind, and what each part is for:

    .fast-dev-flow/spec.md               WHAT the batch claimed
    .dev-flow/state.json                 WHICH batch is active, and its decisions ledger
    .dev-flow/<batch>/03-increments/     WHAT each increment proved
    .dev-flow/<batch>/evidence/          THE BYTES every digest cites
    .dev-flow/BACKLOG.md                 WHAT carries to the next batch

The gate never says more than it measured. Run it on an empty repository and it passes — and tells you what a pass means here (real output, `--brief`, trimmed):

    0 block · 5 notice · 49 not applicable
      [!] V18  .dev-flow/state.json: no `.dev-flow/state.json`, so nothing declares the active batch …
      [!] V27  .dev-flow/state.json: `state.json` holds no `decisions_log` list, so neither the coverage nor the currency of the record was checked …
      [!] V42  .dev-flow/: the tracked file set could not be enumerated …, so the deferral corpus is undefined …
    n/a: 49 rule(s) with no subject on this tree (no mode declared on this tree) — run without --brief to list them

A green with no subject is reported as *no subject*, never as a pass. That sentence is the whole design.

## Your first batch in ten minutes (fast flow)

1. Open `dev-flow/SKILL.md` and follow its routing: the fast flow is `commands/fast-dev-flow.md`; its **reader's map** lists, for every step, the one file and section that holds the rule.
2. Pre-checks: run the gate on the project (it will pass with most rules *not applicable* — the batch does not exist yet).
3. Phase A: write `.fast-dev-flow/spec.md` from `templates/fast-dev-flow/spec-template.md`; the flow seeds a five-key `.dev-flow/state.json` so the gate can see the batch.
4. Phase B: implement in increments of at most four source files; each increment gets the short packet (`templates/fast-dev-flow/increment-template.md`, nine rows — exactly the fields a rule reads) with a RED counterfactual whose restore is proven by file hash.
5. Phase C: record the closing gate's decision (`C`) first, then run the gate again; it now reads the batch (`V41` re-hashes every cited evidence file, `V55` sees every gate recorded), reconcile the backlog, close.

Fresh readers on Codex and Kimi ran exactly this on a toy repository with no other context; their reports shaped revisions 84–86 of the flow.

## What it is not

- Not a spec format. It does not replace your requirements tool; it makes the record of a batch checkable.
- Not an enforcement layer outside Claude Code. On other runtimes the operator stands where the guard would stand, and the record says so.
- Not a code auditor. Confidence in code comes from the gates and the tests the flow makes you prove can fail, not from a human reading every line.

## Limits — stated, not discovered later

- **Enforcement is a Claude Code property.** Named reviewer roles, prompt gates and the hook that refuses a stale invocation exist there and nowhere else. On any other runtime the flow runs *unguarded*: the operator's initial commission is the batch's standing authorization, the guided gate records its decision instead of waiting for one, and the record says so. The validator still refuses an altered bundle and still reads the batch record on every runtime.
- **The flow does not audit code line by line, and does not ask a human to.** Confidence comes from the gates, the tests the flow makes you prove can fail, and the evidence the record hashes. What a human actually read, at what depth, and what was deliberately not reviewed goes in the close artifact's human review ledger — a review with no record is indistinguishable from one that never happened.
- **It was distilled from one flow's post-mortems.** The controls carry their origin batches as anonymous indices, and the catalog's own honesty note says which controls are stack-specific. Treat them as a strong prior, not a law.
- **Fresh-reader verdicts are the acceptance test, and they are published with the flow.** At the current revision a weak reader with no context closes a fast batch with the skill alone; the obstacles it still names are listed in `CHANGELOG.md`, not smoothed.

## Layout

    dev-flow/
      SKILL.md              adapter: routing, what refuses an invocation, severity legend
      FLOW-VERSION.md       identity: revision, per-file hashes, control census (no history)
      commands/             dev-flow, fast-dev-flow, dev-flow-init, dev-flow-sync
      agents/               reviewer and implementer role texts
      templates/            dev-flow/ (full and core modes) · fast-dev-flow/ (spec + short packet)
      scripts/              devflow-validate.py · devflow-mutate.py · devflow-mutants.json
    dev-flow-lessons/
      SKILL.md              the control catalog (consultable)
      REFERENCE.md          origins, measurements, dispositions (forensic)

## Versioning

`FLOW-VERSION.md` carries the flow revision and a hash per shipped file. It travels with the flow because it is the identity contract the validator enforces. Some of its recipes name the canonical authoring home, which has paths a published bundle does not; if you are reading this repository, the recipe under *From inside a bundle* is yours, and the canon recipes belong to the authoring home. Nothing in the manifest is secret — the two recipes are two doors into the same contract. The validator verifies the copy you run against that manifest, both directions. Changing a shipped file without a new revision is a BLOCK by design.

## License

Apache License 2.0 — see `LICENSE`. Attribution notices are in `NOTICE`.
