---
command: git status
title: The Tally Sheet
chapter: 5
order: 1
risk: low
metaphor: >
  The clerk's tally sheet comparing the drawers with the last pressed copy in the letter book: what has changed, what is waiting in the tray, what is new.
related: [git add, git commit, diff]
sketch: >
  A tally sheet clipped to a small wooden board, with three ruled columns and a few ticks and crosses in ink, a pencil tucked under the clip.
exercise:
  question: "git status --short shows ?? letters/to-aunt.txt. What does ?? mean?"
  choices:
    - "The sheet is damaged"
    - "The letter book has never seen this sheet"
    - "The sheet is waiting in the tray"
  answer: 1
  explanation: "?? marks an untracked sheet: it exists in the drawer but has never been pressed into the letter book."
---

## In one line

`git status` shows what has changed since the last saved version.

## The picture

The Study keeps a letter-copy book with a pressed copy of every version. The
clerk compares the drawers with the last copy in the book and fills in a tally
sheet: these sheets changed, these are waiting in the tray to be pressed, and
these are new ones the book has never seen.

## What really happens

`git status` compares the working tree, the index (staging area) and the
latest commit. It lists files that are staged, modified but not staged, and
untracked, and says which branch you're on and whether it's ahead or behind
its remote. It changes nothing.

## Try it

```console
$ git status --short
 M notes.txt
?? letters/to-aunt.txt
```

## Margin notes

| Write              | It means                                      |
|--------------------|-----------------------------------------------|
| `git status`       | Fill in the full tally sheet                  |
| `git status -s`    | The short version, one line per sheet         |
| ` M` / `M `        | Changed, not yet in the tray / waiting in the tray |
| `??`               | A sheet the letter book has never seen        |

## When an agent asks

Agents run `git status` before and after working, to see what they changed.
It only reads, and it's a very good sign. An agent that checks status is
keeping track of its own edits.

## Careful

- Status only knows the drawers inside the letter book's project, not the whole Study.
