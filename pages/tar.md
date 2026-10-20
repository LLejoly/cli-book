---
command: tar
title: The Bundle and String
chapter: 3
order: 5
risk: medium
metaphor: >
  Tying a stack of sheets into one bundle with string, and later untying it to spread them back out.
related: [cp, mv, ls]
sketch: >
  A neat stack of papers tied crosswise with twine in a bow, a ball of string and a pair of scissors beside it.
exercise:
  question: "Which instruction ties the letters drawer into a bundle?"
  choices:
    - "tar -xzf letters.tar.gz"
    - "tar -czf letters.tar.gz letters"
    - "tar -tzf letters"
  answer: 1
  explanation: "c means create a bundle. x unties (extracts) one, and t lists what's inside without untying it."
---

## In one line

`tar` packs many files into one archive file, or unpacks one.

## The picture

To send a drawer to someone, you take all its sheets, stack them, and tie them
with string into one bundle. Squeezing the bundle tight, `z`, makes it smaller
to post. At the other end someone unties it and the sheets go back into
drawers, exactly as they were arranged.

## What really happens

`tar` (tape archive) writes files and directories into a single archive and
reads them back. The first letters say what to do: `c` create, `x` extract,
`t` list. `z` adds gzip compression and `f` names the archive file.
Extracting writes files into the current directory and overwrites ones with
the same name.

## Try it

```console
$ tar -czf letters.tar.gz letters
$ tar -tzf letters.tar.gz
letters/
letters/to-the-bank.txt
letters/to-grandma.txt
```

## Margin notes

| Write                 | It means                                  |
|-----------------------|-------------------------------------------|
| `tar -czf b.tar.gz d` | Tie drawer d into a squeezed bundle b      |
| `tar -tzf b.tar.gz`   | Tell me what's in the bundle, don't untie  |
| `tar -xzf b.tar.gz`   | Untie the bundle here                      |
| `tar -xzf b -C dir`   | Untie it inside another drawer             |

## When an agent asks

Agents use `tar` to back up a folder or to unpack something they downloaded.
Before untying a bundle from outside, list it first with `-t`. Untying can
replace sheets you already have.

## Careful

- Untying a bundle from a stranger can scatter sheets anywhere it names. List it before you extract it.
