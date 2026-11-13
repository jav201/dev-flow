---
name: dev-flow
description: dev-flow — runs a software batch design-first. The batch opens with user stories and splits into small increments; each increment goes through strict EARS / ISO/IEC/IEEE 29148 requirements, a Code-Wire graph prototype reviewed with no code, parallel build and test design, and validation of the change; the batch closes with the full test suite, the requirements canon and the trace. Use when the operator asks for dev-flow, a design-first increment, or a graph prototype before code ("con prototipo en grafo").
---

# Design-first dev-flow

Design defects are cheapest before code: on a real project this flow took the MAJOR/HIGH findings on code from 8 in a code-first increment to 0–2 per increment, for about 50 % more model output. This file speaks to the orchestrator; worker rules are in `roles/`. A single increment is a batch of one.

## Records

Kept current under `.dev-flow/<increment>/`:
- **User stories (US)** and **requirements** (canon ids, each naming its US) — in `01-requirements.md`.
- **Test cases** — in `02-test-cases-<group>.md`, one row per alternative of a requirement (format in `roles/tester.md`). A case's result comes from the test run, never a typed column. [case: 918 rows still said not_run]
- **Evidence** — RED, GREEN, mutant and capture transcripts made by the tools, committed (force-add what `.gitignore` excludes); a result counts only for its commit and platform.

`trace_check.py` (this folder) checks the trace: US to requirement to test, changed function to requirement. Commit each stage's work, rulings, graphs and reviews included, when it ends.

## Stages

**E0 — Plan and split (batch open).** Goal: increments each small enough for one focused pass.
- The commission (the operator's written request; draft it with them if missing) gives stories and scope. A change the user sees gets a UI prototype round with the operator's verdict before E1.
- Cap an increment at about 80 requirements and a worker group at 4 source files; split along boundaries the user can see. [case: 40 nodes passed in 6 of 7, none split]
- Done when: each increment has stories, scope, order and shared interfaces.

**E1 — Requirements.** Goal: each requirement is one EARS sentence that meets ISO/IEC/IEEE 29148 (necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, conforming).
- One `shall`, one response, "the system" as subject; split until it cannot be split; an "only when" becomes two requirements. Five forms only:
  - Ubiquitous — `The system shall …` (always true)
  - Event — `When <trigger>, the system shall …` (something happens; a command option is an event)
  - State — `While <state>, the system shall …` (a lasting state of the system, never a property of the input)
  - Unwanted — `If <condition>, then the system shall …` (a defect, a missing file, a bad argument)
  - Optional — `Where <feature>, the system shall …` (a feature a build or configuration may leave out)
- Every failure path gets its own `If` requirement; alternatives in one condition share the response. Each input from outside (file, argument, clipboard, environment) gets `If` requirements for hostile content: size, depth, control characters, paths. [case: 7 BLOCKER/MAJOR were unspecified hostile input]
- A statement names what can be observed, never the function, file or test that does it. A message requirement fixes its exact text, with `<placeholders>`. Definitions hold terms and formats only; anything the system does is a requirement.
- Each requirement carries a numeric pass threshold (`3/3` for yes-or-no behaviour) and a negative control: a mutant that turns its test RED.
- Examples computed by a script are committed as data, with the script. [case: lost script, 27 retyped positions off by one]
- Before a requirement depends on an input — a key, a terminal feature, a system call — check that it reaches the app on the target platform.
- Done when: defects in existing requirements are fixed in place, with a ruling each (a split keeps the parent id with `.1`, `.2`), and the slice of functions to change is mapped to requirements.

**E2 — Prototype as a Code-Wire graph.** Goal: the design as contracts and examples from the requirements, before code. Method, extractor and lint: https://github.com/jav201/code-wire.
- Extractor marks go only in a throwaway clone, never in the source. Build a baseline graph of the code in scope during E1; the prototype writes only the differences.
- From an earlier increment's graph, mark a clone (`python codewire_marks.py --repo <clone> --graph <g1> --graph <g2>`), extract the slice (`python codewire_extract.py --repo <clone> --layered --graph <g1> --graph <g2> --path <slice> --out <dir>`; `--layered`: a later graph replaces a node of an earlier one only when both have a node with the same module and name), rule on the list and update the graph before designing. Not a gate. [case: run in 0 of 12; five graphs stale]
- Over about 8 nodes, split the graph by file ownership after pinning the shared interfaces in one file; an agent proposes interface changes there, never makes them.
- The graph's author runs the lint and fixes every line it lists; nothing is kept. [case: exit 0 in 13 of 13]
- Done when: every requirement has a concrete example, and every requirement and every edit to a shared file has one owner group. [case: half a shared edit had no owner]

**E3 — Code-free design review**, when the increment pins an interface another increment will use, or reads or writes outside the program. Goal: no open MAJOR or worse.
- One reviewer, design and security lens, one round on the graph, requirements and callers. [case: one round found 3 to 8 MAJOR]
- An interface later increments will use is reviewed against their stories in the increment list. [case: a contract could not carry a later increment's fields]
- Rule on every finding in a rulings file. Prefer removing a feature over guarding it. One agent corrects with targeted edits, never a rewrite. Minor findings go to E4 as addenda.

**E4 — Build ∥ test design.** Goal: the approved graph as code, proven by independent tests.
- Launch an implementer and a tester per file group, a tester for the black-box ATs across groups (keys and dialogs), then an integrator.
- Done when: GREEN on the tree; RED on base for each fix and each behaviour that exists on base; no mutant survivor is unruled. [case: 26 of 26 RED files were import errors]

**E5 — Validate the change.** Goal: the change proven and reviewed; regression is the batch end's.
- Run the tests of new and changed requirements, the changed tests, and the law guards (project-wide source scans named in `CLAUDE.md` or `AGENTS.md`).
- One reviewer, code and security, one pass. BLOCKER and MAJOR are fixed in the increment, test first; re-review only a fix that touches an interface; MINOR goes to the backlog.
- Done when: no MAJOR or worse is open, real captures exist if the UI changed, and `04-validation.md` gives the verdict, each run with its evidence path, the mutant score, the review verdicts and what was not run.

**Batch end.** Goal: a whole batch the operator can judge.
- Run the full suite once, in sequential chunks. Each failure gets a corrective pass, RED first, recorded with its cause, requirement and files; never weaken a law guard.
- Run the E2 extraction on the whole batch and rule on its list.
- Fold the requirements into the canon (`REQUIREMENTS.md`, in its existing form).
- Build one review page for the operator: captures, a change map, what they must know, and a decision form.
- Push only on approval, then compare the remote CI's failing tests with the previous run's; a local green run is not the CI's verdict.
- Done when: each failure is fixed or ruled, `trace_check.py` with `--fixes` and `--canon` passes on the batch, and the operator has decided.

## Running it

- **Gates.** The operator approves the increment list, rules on prototype rounds and decides at the batch end; stop only for their decisions.
- **Conducting.** The main session conducts every stage and reads every report; never one conductor agent per increment: its context fills and its children outlive it.
- **Briefs.** Brief each worker with its card verbatim (text, or path when it reads files) plus only the increment's pointers: its files, requirement ids, graph nodes, `interfaces.md`. Refuse a hand-back without the pasted output its card asks for. Paste the integrator's lines "for the next workers" into the next briefs (experimental). [case: a check skipped "because it was not in the brief"]
- **Models.** The strongest model (Opus class) designs E1–E3, reviews, integrates and corrects. E4 implementation from the approved graph and mechanical work (mutant runs, records, captures) go to a Sonnet-class model — Sonnet, DeepSeek v4 Pro, Kimi K2.7 or K2.8 — always behind an independent tester or reviewer. When a model's work costs an extra pass or loses content, move that task up a class.
- **Log.** `steps.log` gets one line per stage (stage, model, result), committed with its work; a stage's time is its commit's (`git log --date=iso --format="%ad %s"`). Never type a time or a date. [case: log 35 h, commits 9.5 h]
- **Agents.** Parallel agents own disjoint files. Before launching an agent, stop whatever still writes in its worktree; an agent is done when its process ends, never when its log says so. Every headless agent gets a timeout and a closed stdin; watch every long job for stalls. Change no source or scope during a long run.
