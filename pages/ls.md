---
command: ls
title: The Lantern
chapter: 1
order: 1
risk: low
metaphor: >
  A lantern you hold up to an open drawer, so you can read the labels of everything inside.
related: [cd, pwd]
sketch: >
  A small brass oil lantern held over an open wooden drawer, its light falling on folded sheets and smaller drawers.
exercise:
  question: "You type ls in your study drawer and don't see .secret-diary.txt. Why?"
  choices:
    - "It was deleted."
    - "It is tucked behind the false back. ls -a would show it."
    - "ls only shows drawers, not sheets."
  answer: 1
  explanation: "Names starting with a dot are hidden. ls leaves them out unless you add the -a margin note."
---

## In one line

`ls` shows you what is inside a folder.

## The picture

You are standing at an open drawer, but it is dark. You lift a lantern and read
the labels: two smaller drawers, one sheet of notes. Nothing is moved and
nothing is touched. You only look.

## What really happens

`ls` lists the entries of a directory, by default the current one. It reads
the directory but changes nothing. Entries whose names start with `.` are
hidden unless you pass `-a`. With `-l` it also prints permissions, owner,
size and modification time for each entry.

## Try it

```console
$ ls
letters  notes.txt  recipes
$ ls -a
.  ..  .secret-diary.txt  letters  notes.txt  recipes
$ ls letters
to-grandma.txt  to-the-bank.txt
```

## Margin notes

| Write     | It means                                         |
|-----------|--------------------------------------------------|
| `ls -a`   | Show hidden sheets too (names starting with `.`) |
| `ls -l`   | Long list: locks, owner, size and date           |
| `ls -lh`  | Long list with sizes in KB, MB, GB               |
| `ls -R`   | Look inside every smaller drawer as well         |

## When an agent asks

An agent runs `ls` to find its way around before it does anything else. It
only looks, so it is safe to accept. It does mean the agent will see the names
of your files, so think twice if folder names are private.

## Careful

- `.` means "this drawer" and `..` means "the drawer that holds this one". They are not real sheets.
