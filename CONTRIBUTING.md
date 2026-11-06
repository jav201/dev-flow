# Contributing

Thank you for trying dev-flow. The flow is kept small on purpose, and that shapes how a change lands.

## A change cites a real defect

A new line in the skill, a new check in `trace_check.py` or a new field in a record lands only if it names a defect it caught, or would have caught, in a real run. Without that, it is an experiment, not part of the flow. A change that removes a line is welcome when nothing reads that line.

## How a change lands

1. Open an issue first for anything beyond a typo: what failed, in which run, and which line would have prevented it. The *reader report* template is the easiest way.
2. Keep `dev-flow/SKILL.md` short: one sentence per practice, with its reason when the reason is not obvious.
3. A change to `trace_check.py` comes with a test that fails without it: `python -m pytest dev-flow/test_trace_check.py`.
