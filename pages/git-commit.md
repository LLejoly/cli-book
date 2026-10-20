---
command: git commit
title: The Copying Press
chapter: 5
order: 3
risk: medium
metaphor: >
  The iron copying press that presses the letters in the tray into the letter book as a permanent, signed and dated copy.
related: [git add, git log, git push]
sketch: >
  A cast-iron letter-copying press with a large turning wheel on top, a thick bound letter book lying open on its bed beneath the plate.
exercise:
  question: "Does git commit send your work to anyone else?"
  choices:
    - "Yes, everyone sees it at once"
    - "No, it presses the copy into your own letter book only"
    - "Only if the message says so"
  answer: 1
  explanation: "A commit stays in your Study. Sending your new copies to the shared book in another house is a separate step: git push."
---

## In one line

`git commit` saves the chosen changes as a new version, with a message saying what changed.

## The picture

You turn the wheel of the copying press. Everything in the tray is pressed into
the letter book as one new copy, signed with your name, dated, and labelled
with a short note about why. Earlier copies are never pressed over. Each new
one goes on the next page.

## What really happens

`git commit` records the staged snapshot as a new commit, with author, date,
message, and a pointer to its parent, and moves the current branch to it. The
commit gets a unique ID (a hash such as `2412c63`). `-m` gives the message
inline. `-a` stages modified tracked files first. `--amend` replaces the last
commit.

## Try it

```console
$ git commit -m "Add stamps to the list"
[main 2412c63] Add stamps to the list
 1 file changed, 1 insertion(+)
```

## Margin notes

| Write                | It means                                      |
|----------------------|-----------------------------------------------|
| `git commit -m "..."`| Press the tray into the book with this note   |
| `git commit -a -m`   | Put every changed known sheet in the tray, then press |
| `git commit --amend` | Redo the last pressing                        |

## When an agent asks

Committing is a safe habit, since every pressed copy can be returned to later.
Read the message: it should say plainly what changed. Be careful with
`--amend` on copies already sent to another house.

## Careful

- A commit is local. Until you push, nobody else has it, and a lost laptop loses it too.
