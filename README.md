# dev-flow

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
| Claude Code | the `skills/` directory of your Claude Code home (the commands under `dev-flow/commands/` can also be exposed as slash commands) |
| Codex CLI | the `skills/` directory of your Codex home (the `.codex` folder in your user directory) |
| Kimi Code CLI | your project's `.agents/skills/` (symlink or copy), or `kimi --skills-dir <path to this repo>` |

Then verify the copy from inside it:

    cd dev-flow
    python scripts/devflow-validate.py --selftest      # exits 0; canon-only checks SKIP by name
    python scripts/devflow-validate.py <your project>  # 0 block on an empty project

Requires Python 3.11+ and git. Windows, macOS and Linux.

## Your first batch in ten minutes (fast flow)

1. Open `dev-flow/SKILL.md` and follow its routing: the fast flow is `commands/fast-dev-flow.md`; its **reader's map** lists, for every step, the one file and section that holds the rule.
2. Pre-checks: run the gate on the project (it will pass with most rules *not applicable* — the batch does not exist yet).
3. Phase A: write `.fast-dev-flow/spec.md` from `templates/fast-dev-flow/spec-template.md`; the flow seeds a five-key `.dev-flow/state.json` so the gate can see the batch.
4. Phase B: implement in increments of at most four source files; each increment gets the short packet (`templates/fast-dev-flow/increment-template.md`, nine rows — exactly the fields a rule reads) with a RED counterfactual whose restore is proven by file hash.
5. Phase C: run the gate again; it now reads the batch (`V41` re-hashes every cited evidence file), reconcile the backlog, close.

Fresh readers on Codex and Kimi ran exactly this on a toy repository with no other context; their reports shaped revisions 84–86 of the flow.

## What it is not

- Not a spec format. It does not replace your requirements tool; it makes the record of a batch checkable.
- Not an enforcement layer outside Claude Code. On other runtimes the operator stands where the guard would stand, and the record says so.
- Not a code auditor. Confidence in code comes from the gates and the tests the flow makes you prove can fail, not from a human reading every line.

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

`FLOW-VERSION.md` carries the flow revision and a hash per shipped file. The validator verifies the copy you run against that manifest, both directions. Changing a shipped file without a new revision is a BLOCK by design.

## License

Apache License 2.0 — see `LICENSE`. Attribution notices are in `NOTICE`.
