---
command: make
title: The Housekeeping Book
chapter: 9
order: 1
risk: medium
metaphor: >
  A household book of standing recipes, where each task lists what it needs, and only the tasks whose ingredients changed are done again.
related: [python, touch, chmod]
sketch: >
  A cloth-bound household book lying open, its pages ruled into numbered recipes with ingredients on the left and steps on the right, a ribbon marker across.
exercise:
  question: "You run make twice in a row. Why does the second time say 'is up to date'?"
  choices:
    - "make is broken"
    - "Nothing the task depends on changed since last time, so there's nothing to redo"
    - "The first run failed"
  answer: 1
  explanation: "make compares dates: if the result is newer than everything it's made from, the recipe isn't followed again."
---

## In one line

`make` runs the build steps written in a project's Makefile, redoing only what is out of date.

## The picture

The household book lists recipes: "the shopping list is made from the notes,
by copying out every line with *buy*". When you ask for the shopping list, the
housekeeper checks the dates. If the notes changed since the list was made,
she follows the recipe again. If not, she tells you it's already done.

## What really happens

`make` reads a `Makefile` of rules: a target, the files it depends on, and the
shell commands that build it. It compares modification times and runs only
the rules whose targets are missing or older than their dependencies. `make
name` builds a particular target. `-n` prints the commands without running
them.

## Try it

```console
$ make
grep buy notes.txt > shopping.txt
$ make
make: 'shopping.txt' is up to date.
$ cat shopping.txt
buy flour
buy ink
```

## Margin notes

| Write          | It means                                       |
|----------------|------------------------------------------------|
| `make`         | Follow the first recipe in the book            |
| `make test`    | Follow the recipe called test                  |
| `make -n`      | Read me the steps without doing them           |
| `make -j4`     | Let four helpers work at once                  |

## When an agent asks

`make`, `make build` or `make test` in a project you know is routine. The
real orders are in the Makefile, so in a project you don't know, run `make -n`
first or read it.

## Careful

- A Makefile is a set of shell orders. `make install` often needs `sudo` and writes outside the project.
