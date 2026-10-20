---
command: mkdir
title: The Empty Drawer
chapter: 1
order: 5
risk: medium
metaphor: >
  A carpenter fitting a new, empty drawer into the cabinet, with a fresh brass label.
related: [cd, ls, rm]
sketch: >
  A new, empty wooden drawer half slid into an old cabinet, a blank brass label plate and a few small screws beside it.
exercise:
  question: "recipes/cakes doesn't exist yet. What does mkdir -p recipes/cakes/sponge do?"
  choices:
    - "Grumbles that cakes doesn't exist"
    - "Makes cakes, then sponge inside it"
    - "Makes a single drawer called cakes/sponge"
  answer: 1
  explanation: "The -p margin note builds every missing drawer along the way. Without it, mkdir refuses."
---

## In one line

`mkdir` creates a new, empty folder.

## The picture

You need somewhere to keep your poems. The carpenter fits a new drawer into
the cabinet, empty, with your label on the front. Nothing else in the Study is
touched. If a drawer with that label is already there, he refuses.

## What really happens

`mkdir` (make directory) creates one or more directories. It fails if the
name already exists or the parent directory is missing. `-p` creates any
missing parents and doesn't complain if the directory already exists. A new
directory can be removed with `rmdir` while it is still empty.

## Try it

```console
$ mkdir poems
$ ls
letters  notes.txt  poems  recipes
$ mkdir recipes/cakes/sponge
mkdir: cannot create directory 'recipes/cakes/sponge': No such file or directory
$ mkdir -p recipes/cakes/sponge
```

## Margin notes

| Write            | It means                                      |
|------------------|-----------------------------------------------|
| `mkdir name`     | Fit one new drawer here                       |
| `mkdir -p a/b/c` | Fit every missing drawer along the way        |
| `mkdir a b`      | Fit two drawers at once                       |

## When an agent asks

Agents make drawers to hold the work they're about to do. It's harmless and
easy to undo. Just check where: a new drawer in your home drawer or an
unfamiliar place tells you where the agent plans to write next.

## Careful

- Names with spaces need quotes: `mkdir "old letters"`, or you get two drawers, `old` and `letters`.
