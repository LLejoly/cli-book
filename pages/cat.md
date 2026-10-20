---
command: cat
title: The Lectern
chapter: 1
order: 4
risk: low
metaphor: >
  A lectern where the clerk reads a sheet aloud to you from the first line to the last.
related: [ls, grep, "|"]
sketch: >
  A wooden reading lectern with a single sheet of handwritten paper resting on its slanted top, lit by a gas lamp.
exercise:
  question: "What does cat notes.txt letters/to-grandma.txt do?"
  choices:
    - "Glues the two sheets together for good"
    - "Reads both sheets aloud, one after the other"
    - "Only reads the first sheet"
  answer: 1
  explanation: "cat reads every sheet you name, in order, without changing any of them. Its name comes from conCATenate: to chain together."
---

## In one line

`cat` shows you everything written in a file.

## The picture

You hand the clerk a sheet. He places it on the lectern and reads it aloud,
every line, from top to bottom. Hand him two sheets and he reads one after the
other without a pause. The sheets go back in the drawer exactly as they were.

## What really happens

`cat` reads each named file in order and writes its bytes to standard output.
Its name comes from "concatenate". It does not change the files. On a binary
file, such as an image, it prints unreadable characters. For long files, a
pager like `less` is easier to read.

## Try it

```console
$ cat notes.txt
buy flour
call grandma
pay the bank
buy ink
$ cat -n notes.txt
     1	buy flour
     2	call grandma
     3	pay the bank
     4	buy ink
```

## Margin notes

| Write                | It means                                 |
|----------------------|------------------------------------------|
| `cat sheet`          | Read this sheet aloud                    |
| `cat -n sheet`       | Read it with a number before each line   |
| `cat a b`            | Read sheet a, then sheet b               |
| `cat a b > c`        | Copy both onto a new sheet c, in order   |

## When an agent asks

Agents use `cat` to read a file before changing it, which is good practice
and safe to accept. Remember that what it reads, the agent now knows. Think
twice before letting it read files with passwords or private keys.

## Careful

- `>` is not part of `cat`. It writes onto a sheet and wipes what was on it first, so `cat a > a` leaves you with an empty sheet.
