<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/dev-flow-mark-dark.svg">
    <img src="brand/dev-flow-mark-light.svg" alt="dev-flow — the V that verifies" width="160">
  </picture>
</p>

<h1 align="center">dev-flow</h1>

**A design-first engineering flow for AI coding agents: requirements, a graph prototype reviewed before any code, independent tests, and a record a script can check.**

**Status: beta (v0.3.0, dev-flow v3).** One skill file of about 75 lines for the orchestrator, four role cards for the workers, and one checker script. It replaces the rev94 flow, which stays available at tag `v0.1.1`.

## What it does

A batch opens with user stories and splits into small increments (**E0**). Each increment then goes through five stages:

1. **E1 Requirements.** Strict EARS sentences that meet ISO/IEC/IEEE 29148, each with a numeric pass threshold and a negative control.
2. **E2 Prototype.** The design as a [Code-Wire](https://github.com/jav201/code-wire) graph of contracts and examples, before any code.
3. **E3 Design review.** When the increment pins an interface that another increment will use, or reads or writes outside the program, one reviewer with the design and security lens reviews the graph in one round; no code exists yet.
4. **E4 Build ∥ test design.** Implementers work by file ownership. Independent testers write the test cases (one row per alternative of a requirement) and the tests, and prove them RED on the base where the behaviour exists there. An integrator brings the work to GREEN; then a mechanical worker runs every E1 negative control (a mutant) and hands back the table.
5. **E5 Validate the change.** The targeted tests, the project's law guards, `trace_check.py` on the increment, and one code and security review in one pass.

The batch end runs the full test suite once, folds the requirements into the project's canon, and checks the trace.

## Why

On a real project, MAJOR/HIGH findings on code dropped from 8 in a code-first increment to 0–2 per increment. The design review had caught most of them before code existed. The price is more model output: about 50 % more on the first increment.

## What it keeps

Four records define the software: user stories, requirements, test cases and evidence. `dev-flow/trace_check.py` checks that they stay linked:

- every story reaches a requirement;
- every requirement has a test case and a test;
- every changed source file is named by a requirement;
- every cited evidence file is committed;
- at the batch end, every requirement is in the canon.

## Install

Copy `dev-flow/`, with its `roles/` folder, into your agent's skills folder; for Claude Code that is `~/.claude/skills/dev-flow/`. Then ask for `/dev-flow` or for a design-first increment.

You need git, Python 3.11 or later for `trace_check.py`, and [Code-Wire](https://github.com/jav201/code-wire) v3.2 or later for E2.

## Check an increment

```
python dev-flow/trace_check.py --req .dev-flow/<increment>/01-requirements.md --base <base commit> --src <package>
```

Exit 0 means no gap; each gap is one line. `--help` lists the checks and the batch-end form. Before E5 the EVID line is expected; a tester adds `--ids <patterns>` to check its own requirements.

## Limits

- **Where it has run:** with Claude Code. Opus-class models did the design and the reviews; Sonnet-class models (Sonnet, DeepSeek v4 Pro, Kimi K2.x) did the implementation and the mechanical work, always behind an independent review. Other runtimes are untested with this version.
- **The worker roles** (implementer, tester, integrator, reviewer) are cards in `dev-flow/roles/`. The orchestrator pastes each card into the worker's brief, and each card names the output its hand-back must carry.
- **`trace_check.py` checks links by id and by file.** It does not judge whether a test is good; the review stages do that.
- **This is a beta.** The wording will change as real runs find gaps.

## Feedback

Open an issue with the *reader report* template and say where the skill made you guess.

## License

Copyright 2026 username_subject. Licensed under the Apache License, Version 2.0 (see `LICENSE` and `NOTICE`).
