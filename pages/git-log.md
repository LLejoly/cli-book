---
command: git log
title: The Letter Book
chapter: 5
order: 4
risk: low
metaphor: >
  Leafing back through the bound letter book, newest copy first, reading who pressed each one, when, and why.
related: [git commit, git status, diff]
sketch: >
  A thick leather-bound letter-copy book lying open, its thin tissue pages fanned, the visible page showing a handwritten letter and a date in the corner.
exercise:
  question: "git log --oneline shows two lines. Which copy was pressed most recently?"
  choices:
    - "The top line"
    - "The bottom line"
    - "You can't tell from the list"
  answer: 0
  explanation: "git log reads the book from the newest page backwards, so the most recent commit is always first."
---

## In one line

`git log` lists the saved versions, newest first, with who made them and why.

## The picture

You open the letter book at the latest page and leaf backwards. Each copy
carries a number, a name, a date and the note written when it was pressed.
Reading the book changes nothing in it.

## What really happens

`git log` walks the commit history from the current commit backwards, showing
each commit's hash, author, date and message. `--oneline` shortens each to one
line, `-p` shows the diff, `-n 5` limits the count, and `--graph` draws
branches. It opens in a pager for long output. Press `q` to leave.

## Try it

```console
$ git log --oneline
2412c63 Add stamps to the list
244d512 Start my study
```

## Margin notes

| Write                | It means                                     |
|----------------------|----------------------------------------------|
| `git log`            | Read the book from the newest page           |
| `git log --oneline`  | One line per copy                            |
| `git log -p a`       | Show what changed on sheet a in each copy    |
| `git log -n 3`       | Only the last three copies                   |

## When an agent asks

Agents read the log to learn a project's history and how its messages are
written. It only reads and is safe to accept.

## Careful

- If the screen seems frozen, the book is open in a pager. Press `q` to close it.
