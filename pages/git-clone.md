---
command: git clone
title: The Borrowed Book
chapter: 7
order: 1
risk: medium
metaphor: >
  Borrowing another house's letter-copy book and making your own complete copy of it, every page and every draft.
related: [git pull, git log, cd]
sketch: >
  Two identical leather-bound letter books side by side on a desk, one closed with a library ribbon, the other open with fresh pages being filled.
exercise:
  question: "You clone a project from a stranger. What has happened to your Study so far?"
  choices:
    - "Their orders have already been carried out"
    - "A new drawer holds a copy of their book. Nothing in it has run yet."
    - "Your own letter book was replaced"
  answer: 1
  explanation: "Cloning only copies sheets into a new drawer. The danger comes later, when you or an agent run something found inside."
---

## In one line

`git clone` downloads a complete copy of a project, with all its history, into a new folder.

## The picture

Another house keeps a letter-copy book you'd like to work on. Instead of
reading it there, you make a complete copy of it: every pressed page, every
draft, every note. The copy goes in a new drawer of your Study, and it
remembers which house it came from so you can fetch news later.

## What really happens

`git clone` creates a new directory, downloads every object of the remote
repository, sets up a remote named `origin` pointing back to it, and checks
out the default branch. `--depth 1` fetches only the latest commit, which is
faster for big projects.

## Try it

```console
$ git clone git@github.com:you/study.git
Cloning into 'study'...
$ cd study
$ git log --oneline
244d512 Start my study
```

## Margin notes

| Write                     | It means                                      |
|---------------------------|-----------------------------------------------|
| `git clone address`       | Copy that book into a new drawer here         |
| `git clone address name`  | Call the new drawer name instead              |
| `git clone --depth 1 ...` | Only copy the latest pages                    |

## When an agent asks

Cloning is how an agent fetches a project to work on. It's usually fine. Check
the address. The risk is not the copy itself but running its install steps or
scripts later without reading them.

## Careful

- A cloned project can contain orders that run when you build or install it. Treat code from strangers as unread mail.
