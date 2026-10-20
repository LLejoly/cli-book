---
command: pytest
title: The Tasting Spoon
chapter: 9
order: 7
risk: medium
metaphor: >
  The cook's tasting spoon, dipped into every dish after each change, to check it still tastes the way the recipe says it should.
related: [python, make, npm run]
sketch: >
  A copper saucepan standing on a small wooden kitchen table, a long-handled tasting spoon resting across its rim, and a folded cloth beside it.
exercise:
  question: "pytest prints .F and 1 failed, 1 passed. What does it mean?"
  choices:
    - "The project is broken and pytest has repaired it"
    - "Two checks ran. The first held; the second found something different from what it expected"
    - "pytest itself failed to start"
  answer: 1
  explanation: "Each dot is a check that passed and each F one that failed. pytest only reports; it changes nothing to fix the failure. Reading the failure tells you, or Hobbs, what to look at."
---

## In one line

`pytest` runs a Python project's tests, small checks that the code still does what it should.

## The picture

After every pinch of salt, the cook dips the tasting spoon and checks the dish
against the recipe. Each taste is one check: right, or not right. She does not
fix anything with the spoon. She only tells you which dish to look at again.

## What really happens

`pytest` finds files named `test_*.py` or `*_test.py`, collects the functions
named `test_*` inside them, runs each one, and reports a dot for a pass and an
`F` for a failure, with details. Running tests means running the project's
code, along with any `conftest.py` files, with your permissions. It exits with
a non-zero status if anything fails, which is how agents and build tools notice.

## Try it

```console
$ pytest -q
..                                                                       [100%]
2 passed in 0.01s
$ pytest -q -k ink
.                                                                        [100%]
1 passed, 1 deselected in 0.01s
```

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `pytest -q`        | Taste everything, report briefly                 |
| `pytest -x`        | Stop at the first dish that tastes wrong         |
| `pytest -k word`   | Taste only the checks whose name contains word   |
| `pytest --lf`      | Taste again only what failed last time           |

## When an agent asks

Agents run `pytest` after every change, to see whether they broke something.
It is the most ordinary slip they write. In your own project, accept. In a
project from outside the house, the tests are orders like any others: glance at
`conftest.py` and the test files first. Watch also for an agent that changes a
test until it passes, rather than fixing the code.

## Careful

- Tests can write sheets, post letters or erase things, if that is what someone wrote in them.
- A pass only means the written checks held. A dish nobody tasted can still be wrong.
