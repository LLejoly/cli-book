---
command: which
title: The House Directory
chapter: 8
order: 5
risk: low
metaphor: >
  The house directory in the hall, telling you exactly which room the clerk called by a given name works in.
related: [export, python, ls]
sketch: >
  A wall-mounted wooden directory board in a hallway with rows of slide-in name plates, a hand pointing to one row.
exercise:
  question: "python3 behaves strangely. Why might which python3 help?"
  choices:
    - "It repairs python3"
    - "It shows which python3 answers, in case a different one is found first"
    - "It shows the python3 version"
  answer: 1
  explanation: "Several clerks can share a name. The house sends whoever appears first on the PATH list. which tells you who that is."
---

## In one line

`which` shows where the program behind a command name lives.

## The picture

When you call for "python3", the house sends one clerk. But which one? The
directory in the hall lists the rooms in the order the house checks them.
`which` reads it for you and names the room of the clerk who will answer.

## What really happens

`which` searches the directories listed in the `PATH` environment variable,
in order, and prints the first executable with that name. `-a` prints every
match. Shell builtins and aliases aren't files, so `type` or `command -v` is
more complete inside bash.

## Try it

```console
$ which python3 git
/usr/bin/python3
/usr/bin/git
```

## Margin notes

| Write           | It means                                         |
|-----------------|--------------------------------------------------|
| `which name`    | Which room does the clerk called name work in    |
| `which -a name` | Every room with a clerk of that name             |
| `type name`     | Is it a clerk, a house rule or a nickname        |

## When an agent asks

Agents use `which` to check a tool is installed before using it. It only
reads and is safe.

## Careful

- If `which` finds a program in an odd drawer you don't recognise, ask how it got there.
