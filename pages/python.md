---
command: python
title: The Translator
chapter: 9
order: 2
risk: medium
metaphor: >
  A clerk who reads orders written in the Python language and carries out every line, whatever it says.
related: [pip install, make, which]
sketch: >
  A clerk's high desk with a bilingual dictionary lying open, a sheet of orders pinned to the slope, and a pair of spectacles folded on top.
exercise:
  question: "An agent asks to run python3 cleanup.py. How risky is it?"
  choices:
    - "Never risky, python only reads"
    - "As risky as what cleanup.py says. Read the sheet or ask what it does."
    - "Always dangerous"
  answer: 1
  explanation: "python carries out whatever the script says. The seal belongs to the script, not to python."
---

## In one line

`python` runs a program written in the Python language.

## The picture

The translator clerk reads orders written in Python. Hand him a sheet and he
carries out every line, in order: reading sheets, writing them, posting
letters, even erasing. He doesn't judge the orders. That is your job, before
you hand him the sheet.

## What really happens

`python3 script.py` starts the interpreter, which compiles and executes the
script with your user's permissions. `-c 'code'` runs a short snippet, `-m
module` runs an installed module like `pytest` or `http.server`. With no
arguments it opens an interactive prompt. `python` may mean version 2 or 3
depending on the system.

## Try it

```console
$ python3 count.py
4 things to do
$ python3 -c 'print(2 + 2)'
4
```

## Margin notes

| Write                  | It means                                      |
|------------------------|-----------------------------------------------|
| `python3 sheet.py`     | Carry out the orders on this sheet            |
| `python3 -c '...'`     | Carry out this one short order                |
| `python3 -m pytest`    | Ask the clerk who checks everything works     |
| `python3 -m venv .venv`| Set up a separate workroom for this project   |

## When an agent asks

Running tests or a script the agent just showed you is normal. For a script
you haven't seen, ask what it does. For `-c` with a long line, read the line:
it can do anything.

## Careful

- A one-line `python3 -c` can erase or post things just like a long script.
