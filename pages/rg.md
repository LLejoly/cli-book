---
command: rg
title: The Rotary Sifter
chapter: 2
order: 8
risk: low
metaphor: >
  A crank-turned flour sifter, the Sieve's quicker cousin, that works through every drawer at once and leaves out the sheets you would not want sifted.
related: [grep, find, "|"]
sketch: >
  A tin rotary flour sifter with a loop handle and a side crank, standing on three short feet in a shallow earthenware dish on the floor, a little heap of sifted flour beneath its mesh.
exercise:
  question: "You type rg secret in the study. Nothing from .secret-diary.txt comes back, though the word is written in it. Why?"
  choices:
    - "rg cannot read sheets ending in .txt"
    - "The diary is behind the false back, and rg skips hidden sheets unless told --hidden"
    - "The diary is empty"
  answer: 1
  explanation: "rg leaves out hidden sheets, sheets the letter book ignores and unreadable binary files. Silence from rg only means silence among the sheets it looked at."
---

## In one line

`rg` (ripgrep) searches every file below a folder for a word, very fast.

## The picture

The Sieve takes one sheet at a time unless told otherwise. The rotary sifter
has a crank: turn it and every drawer below you goes through the mesh,
quickly. It is also choosy. Sheets behind the false back, and the ones the
letter book is told to ignore, are set aside unsifted. What stays in the mesh
is read back, grouped by sheet, each line with its number.

## What really happens

`rg` searches recursively from the current directory by default, using regular
expressions (patterns with special characters). It skips hidden files, files
listed in `.gitignore` and similar ignore files, and binary files. It searches
files in parallel, so results arrive in any order. Given a pipe and no path,
it searches what flows in. Like `grep`, it exits with 1 when nothing matched.

## Try it

```console
$ rg grandma
notes.txt
2:call grandma
$ rg -l flour
notes.txt
order.json
recipes/bread.txt
recipes/bread-grandma.txt
```

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `rg -i word`       | Ignore capital letters                           |
| `rg -l word`       | Only name the sheets that contain it             |
| `rg -F 'a.b'`      | Search for the exact characters, no pattern      |
| `rg -g '*.txt' word` | Only sift sheets whose names match             |
| `rg --hidden word` | Sift the sheets behind the false back too        |

## When an agent asks

`rg` is the search agents use most; Claude's own search tool is built on it.
Agents run it to find every place a name appears before changing it. It only
reads. Look twice at `--hidden`, `-u` or `-uu`: they reach behind the false
back and into ignored sheets, where `.env` files and keys tend to live, and
the matches land in the agent's conversation.

## Careful

- `-r` does not mean recursive here, as it does for `grep`. It means `--replace`, which only changes what is read back, never the sheet.
- "No matches" means none among the sheets rg looked at. Ignored and hidden sheets were never searched.
