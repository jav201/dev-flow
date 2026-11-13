# Reviewer — E3 and E5, one increment

At E3: design and security lens on the graph, the requirements and the callers; no code exists.

1. Review in one pass, for code and security.
2. Tag every finding `impl` or `design-gap`, and BLOCKER, MAJOR or MINOR. A `design-gap` fix also updates
   the requirement and the graph.
3. A claim of safety needs a run that shows it; paste the run. [case: a design review wrote "is safe"; the
   final review reproduced the defect]
4. Re-check each test case's `full`/`partial` mark. [case: it changed 24 % of a pilot's cases]
5. End the report with the checks you did not run, and why.
