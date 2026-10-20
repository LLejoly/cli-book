---
command: export
title: The Pinboard
chapter: 4
order: 5
risk: medium
metaphor: >
  A cork pinboard by the door where you pin notes that every clerk you send out will read before starting work.
related: [echo, sudo]
sketch: >
  A small cork board in a wooden frame with three handwritten cards held by brass drawing pins, one card slightly curled at the corner.
exercise:
  question: "You run export GREETING=\"good morning\" then close the terminal window. What happens to the note?"
  choices:
    - "It stays pinned forever"
    - "It disappears with that desk session"
    - "It is written into every sheet"
  answer: 1
  explanation: "export only pins the note for this session and the clerks it sends out. To keep it, it has to be written into a start-up sheet like ~/.bashrc."
---

## In one line

`export` sets a named value that the programs you start can read.

## The picture

You pin a card to the board: GREETING says "good morning". Every clerk you send
out from now on glances at the board before starting, so they all know it.
Clerks who were already out don't see the card, and the board is cleared when
you leave the desk.

## What really happens

`export NAME=value` sets a shell variable and marks it for export, so it's
copied into the environment of every child process started afterwards.
Programs read settings like `PATH`, `HOME` or `API_KEY` this way. Changes last
only for the current shell session unless written into a startup file such as
`~/.bashrc`.

## Try it

```console
$ export GREETING="good morning"
$ echo $GREETING
good morning
$ sh -c 'echo "a new clerk hears: $GREETING"'
a new clerk hears: good morning
```

## Margin notes

| Write              | It means                                      |
|--------------------|-----------------------------------------------|
| `export A=b`       | Pin note A saying b, for every clerk I send   |
| `echo $A`          | Read me what's pinned under A                 |
| `unset A`          | Take note A off the board                     |
| `env`              | Read me every note on the board               |

## When an agent asks

Agents use `export` to set up a tool, for example pointing it at a folder or
giving it a key. Check what's being pinned. Changing `PATH` decides which
programs run when a name is typed.

## Careful

- A secret typed in `export API_KEY=...` is saved in your shell history. Prefer a protected file.
