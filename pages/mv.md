---
command: mv
title: The Satchel
chapter: 1
order: 7
risk: medium
metaphor: >
  A satchel you use to carry a sheet to another drawer, or to bring it back with a fresh label.
related: [cp, rm, ls]
sketch: >
  A worn leather satchel with its flap open and a folded sheet of paper half out of it, resting against a cabinet of drawers.
exercise:
  question: "What does mv to-grandma.txt to-granny.txt do?"
  choices:
    - "Makes a copy called to-granny.txt"
    - "Renames the sheet, keeping it in the same drawer"
    - "Creates a drawer called to-granny.txt"
  answer: 1
  explanation: "Moving a sheet to a new name in the same drawer is how you rename it. Only one sheet remains."
---

## In one line

`mv` moves a file somewhere else, or gives it a new name.

## The picture

You slip a sheet into your satchel, walk to another drawer, and put it there.
Nothing is copied: the sheet is simply somewhere else now. Renaming is the
same walk without leaving the drawer: you take the sheet out and put it back
under a new label.

## What really happens

`mv` renames or moves files and directories. Within one file system it just
changes the entry, so it's instant even for huge directories. Across disks it
copies, then deletes the source. Like `cp`, it overwrites an existing
destination without asking unless you pass `-i` or `-n`.

## Try it

```console
$ mv notes.txt letters/
$ ls letters
notes.txt  to-grandma.txt  to-the-bank.txt
$ mv letters/to-grandma.txt letters/to-granny.txt
```

## Margin notes

| Write            | It means                                       |
|------------------|------------------------------------------------|
| `mv a drawer/`   | Carry sheet a into that drawer                 |
| `mv a b`         | Rename sheet a to b                            |
| `mv -i a b`      | Ask me before covering an existing sheet       |
| `mv -n a b`      | Never cover an existing sheet                  |

## When an agent asks

Agents use `mv` to rename or tidy up. Read both names: the first is what moves,
the last is where it lands. If the last name already exists, that sheet is
replaced and gone.

## Careful

- `mv a b` when b is a sheet replaces b. When b is a drawer, a goes inside it. One letter of difference, two outcomes.
