# Integrator — one increment

1. Bring the groups to GREEN and apply the orchestrator's rulings on the interfaces.
2. The requirement wins. Never weaken an assertion. Change an old test only where a requirement or an
   accepted proposal asks.
3. With an editable install, `python -m pytest` imports from the cwd first. Run RED with the base tree as cwd
   and GREEN with the worktree, and print the package's `__file__` at the top of every transcript.
4. After GREEN, have a mechanical worker run every negative control in a copy of the tree and return the
   table: control, killed or survived. A survivor is a finding. [case: 12 of 32 final MAJOR were tests that
   could not fail]
5. Run `python <skill folder>/trace_check.py --req <requirements file> --base <increment base> --src <package>`.
   Before E5 an EVID line is expected; every other line is a finding.
   [case: in 0.3 s it finds a gap a review found by hand]
6. In your notes, give each failure's cause, its side (code, test or requirement) and its requirement. End
   with at most 3 lines "for the next workers" (experimental). [case: one test defect in three increments]
7. Hand back with the suite output, the mutant table and the `trace_check.py` output pasted. Without them
   the hand-back is not done.
