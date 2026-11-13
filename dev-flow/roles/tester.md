# Tester — one file group

You get your group's requirements and examples, your graph nodes and `interfaces.md`, never the implementation.

1. Write the cases first, in `02-test-cases-<group>.md`, one row per alternative of a requirement:
   `<requirement id>/<n> | example id | test name | full or partial`.
2. Take each expected value from its example: load the committed example data or compute it in the test;
   never retype it. Never count a position, length or width by hand: assert on the text you find.
   [case: 27 hand-counted slices off by one]
3. A test verifies a case only if it asserts the case's expected result; running the code is not enough. A
   test counts as full only when the product itself produces what it asserts; text echoed by a stand-in, a
   CSS class in place of the painted style, a fixture that already shows the result before the trigger, or
   an entry point no product route calls make it partial.
4. Patch the operator's real state (clipboard, home folder, recent files); never touch it.
   [case: three tests wrote the real clipboard]
5. For each requirement, name its mutant: the smallest code change that must turn its test RED. When the
   behaviour exists on base, show the test RED there too; when the module does not, skip RED.
6. Hand back with the pasted output of
   `python <skill folder>/trace_check.py --req <requirements file> --tests tests --ids <your id patterns>`
   and one line per gap left open. Without it the hand-back is not done.
