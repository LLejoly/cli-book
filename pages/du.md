---
command: du
title: The Letter Scale
chapter: 8
order: 3
risk: low
metaphor: >
  A brass letter scale that weighs a drawer and everything in it, so you know which drawers are heaviest.
related: [df, ls, find]
sketch: >
  A brass postal letter scale with a curved weight arm and a small platform holding a bundle of papers, the pointer swung partway up its dial.
exercise:
  question: "Your disk is full. Which instruction helps find the heaviest drawers?"
  choices:
    - "du -sh * | sort -h"
    - "rm -rf *"
    - "ls -a"
  answer: 0
  explanation: "du -sh weighs each drawer, and sort -h orders them by size, so the heaviest come last. Then you decide what to remove."
---

## In one line

`du` shows how much disk space files and folders take up.

## The picture

You lift each drawer onto the letter scale and read its weight, contents
included. Weighing changes nothing. It just tells you where the bulk of the
Study is, before you decide what to clear out.

## What really happens

`du` (disk usage) walks directories and reports the space used by each.
`-s` prints one total per argument, `-h` uses readable units, and
`--max-depth=1` (or `-d 1`) shows one level down. Sizes are disk blocks used,
so tiny files still count as at least 4K.

## Try it

```console
$ du -sh letters recipes
4.0K	letters
8.0K	recipes
```

## Margin notes

| Write                | It means                                      |
|----------------------|-----------------------------------------------|
| `du -sh drawer`      | Weigh this drawer, in KB, MB or GB            |
| `du -sh * \| sort -h`| Weigh every drawer here, lightest first       |
| `du -d 1 -h`         | Weigh each drawer one level down              |

## When an agent asks

Agents use `du` to find what's filling a disk. It only reads and is safe.
What often follows is an `rm` of the biggest drawer, so read that step
carefully.

## Careful

- On a big Study, `du` on the great cabinet `/` takes a long time and grumbles about locked drawers.
