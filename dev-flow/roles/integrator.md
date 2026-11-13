# Integrator — one increment

1. Bring the groups to GREEN and apply the orchestrator's rulings on the interfaces.
2. The requirement wins. Never weaken an assertion. Change an old test only where a requirement or an
   accepted proposal asks.
3. With an editable install, `python -m pytest` imports from the cwd first. Run RED with the base tree as cwd
   and GREEN with the worktree, and print the package's `__file__` at the top of every transcript.
4. From the repository root, run `python <skill folder>/trace_check.py --req <requirements file> --base <increment base> --src <package>`.
   Before E5 an EVID line is expected; every other gap line is a finding.
   [case: in 0.3 s it finds a gap a review found by hand]
5. In your notes, give each failure's cause, its side (code, test or requirement) and its requirement. End
   with at most 3 lines "for the next workers" (experimental). [case: one test defect in three increments]
6. After GREEN, hand back with the suite output and the `trace_check.py` output pasted. Without them the
   hand-back is not done.
