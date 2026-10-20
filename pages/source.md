---
command: source
title: The Sealed Orders
chapter: 11
order: 1
risk: high
metaphor: >
  A sheet of sealed orders opened at your own desk and carried out on the spot, so every change it makes stays in your study.
related: [export, cd, python, eval]
sketch: >
  A folded sheet of orders on a writing desk, its red wax seal just broken, beside a brass letter opener and a small cork pinboard.
exercise:
  question: "go.sh contains the single line cd letters. You run bash go.sh, then pwd. Which drawer are you in?"
  choices:
    - "letters, because the sheet said so"
    - "Still study: a separate clerk opened the drawer, not you"
    - "Neither, bash go.sh closes every drawer"
  answer: 1
  explanation: "bash go.sh hands the sheet to a new clerk who works and then leaves. Only source go.sh carries the orders out at your own desk, where the change stays."
---

## In one line

`source` carries out the instructions written on a sheet as if you had typed them yourself.

## The picture

A sheet of orders arrives under seal. Usually you hand such a sheet to a clerk
who works in another room and then leaves. With `source`, you break the seal
at your own desk and carry the orders out right here. Whatever they change, the
open drawer, the notes on the pinboard, stays changed in your study.

## What really happens

`source file` (or `. file`) reads the file and runs each line in the current
shell, not in a child process. So `cd`, `export`, aliases and functions in it
change your session. Running `bash file` instead starts a new shell, and its
changes vanish when it exits. Startup files such as `~/.bashrc` are loaded this way.

## Try it

```console
$ echo 'cd letters' > go.sh
$ bash go.sh
$ pwd
/home/you/study
$ source go.sh
$ pwd
/home/you/study/letters
```

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `source file`      | Carry out this sheet's orders at my own desk     |
| `. file`           | The same, in the older short form                |
| `source ~/.bashrc` | Re-read my start-up orders now                   |
| `bash file`        | Hand the sheet to a new clerk instead            |

## When an agent asks

Agents source a sheet to set up a tool, such as `source .venv/bin/activate`.
Ask where the request came from. If a README, an issue or a web page Hobbs
just read told him to source a sheet, that is a paper from outside giving
orders. Open the sheet with `cat` first and read every line.

## Careful

- Sourced orders run with all your keys. They can read secrets on your pinboard and send them out.
- A sourced sheet can change `PATH` or define a function named `ls` or `sudo`, and the trick lasts for the whole session.
