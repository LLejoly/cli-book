---
command: git add
title: The Letter Tray
chapter: 5
order: 2
risk: medium
metaphor: >
  Laying finished letters in the tray beside the copying press, chosen to go into the next pressed copy.
related: [git status, git commit]
sketch: >
  A two-tiered wooden letter tray on the desk, a few folded letters in the top tier, the corner of a copying press just visible behind it.
exercise:
  question: "You edited notes.txt and recipes/bread.txt, then ran git add notes.txt. What will the next commit contain?"
  choices:
    - "Both changes"
    - "Only the change to notes.txt"
    - "Nothing, add must be followed by a file list"
  answer: 1
  explanation: "Only sheets placed in the tray go into the next pressed copy. bread.txt stays changed in the drawer but is left out."
---

## In one line

`git add` chooses which changes go into the next saved version.

## The picture

Before pressing a copy into the letter book, you pick which sheets go in. You
lay them in the tray beside the press. Anything left on the desk stays as it
is, changed but not recorded. Nothing is pressed yet: the tray is a waiting
place, and you can still take sheets back out.

## What really happens

`git add` copies the current content of files into the index (staging area),
which is what `git commit` will record. New files become tracked. `git add .`
stages everything under the current directory, `-p` lets you choose parts of a
file. `git restore --staged` takes a file back out.

## Try it

```console
$ git add notes.txt
$ git status --short
M  notes.txt
?? letters/to-aunt.txt
```

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `git add a`        | Put sheet a in the tray                          |
| `git add .`        | Put every changed and new sheet here in the tray |
| `git add -p`       | Show me each change and let me choose            |
| `git restore --staged a` | Take sheet a back out of the tray          |

## When an agent asks

Agents add the files they changed before committing. Watch for `git add .` or
`git add -A`: they can sweep in sheets you never meant to share, like a file
with passwords.

## Careful

- Once a secret is pressed into the book and sent off, removing it later is hard. Keep it out of the tray.
