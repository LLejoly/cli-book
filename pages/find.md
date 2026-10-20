---
command: find
title: The Card Catalogue
chapter: 2
order: 4
risk: low
metaphor: >
  The library's card catalogue, whose cards tell you the exact drawer of every sheet matching what you ask for.
related: [ls, grep, rm]
sketch: >
  A wooden card-catalogue cabinet with rows of small brass-handled drawers, one drawer pulled out to show index cards with a single card raised.
exercise:
  question: "What does find . -name \"*.txt\" look through?"
  choices:
    - "Only the drawer you are in"
    - "The drawer you are in and every drawer inside it"
    - "Every drawer in the whole Study"
  answer: 1
  explanation: "The dot means 'start here'. find then searches every smaller drawer below it, but never above."
---

## In one line

`find` searches through folders, and all the folders inside them, for files that match a description.

## The picture

You don't remember where you put the recipes. Instead of opening every drawer,
you go to the card catalogue and ask for "every sheet whose name ends in .txt".
The clerk walks every drawer below where you stand and hands you a card with
the full directions to each one.

## What really happens

`find` walks a directory tree from each starting point and prints every path
that matches the tests you give, such as `-name`, `-type f` (files) or
`-type d` (directories), `-size` and `-mtime`. It can also run actions on each
match, like `-delete` or `-exec`.

## Try it

```console
$ find . -name "*.txt"
./.secret-diary.txt
./letters/to-grandma.txt
./letters/to-the-bank.txt
./notes.txt
./recipes/bread-grandma.txt
./recipes/bread.txt
$ find . -type d
.
./letters
./recipes
```

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `find . -name "x*"`| Find sheets whose name starts with x             |
| `find . -type d`   | Find drawers only                                |
| `find . -mtime -1` | Find sheets changed in the last day              |
| `find . -delete`   | Erase everything found. Treat it like `rm -r`    |

## When an agent asks

Agents use `find` to get the lie of a project. Plain searches only read. Look
at the end of the instruction: `-delete` or `-exec rm` turns a search into an
eraser.

## Careful

- `find / ...` searches the whole Study and can grumble about many locked drawers.
- Always run the search without `-delete` first to see what it would erase.
