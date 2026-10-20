---
command: df
title: The Measuring Jug
chapter: 8
order: 4
risk: low
metaphor: >
  A graduated measuring jug for each cabinet, showing at a glance how full it is and how much room is left.
related: [du, ls]
sketch: >
  A glass measuring jug with engraved graduation marks, filled two-thirds with water, standing beside a small wooden cabinet.
exercise:
  question: "What is the difference between du and df?"
  choices:
    - "None"
    - "du weighs drawers you choose. df tells how full each whole cabinet (disk) is."
    - "df deletes files"
  answer: 1
  explanation: "df looks at whole disks and their free space. du adds up what particular folders use."
---

## In one line

`df` shows how full each disk is and how much space is left.

## The picture

Each cabinet in the house has a measuring jug beside it. A glance tells you
its size, how much is used, and how much room remains. You don't open any
drawers. The jug only gives the totals.

## What really happens

`df` (disk free) reports, for each mounted filesystem, its size, used and
available space, use percentage and mount point. `-h` prints readable sizes.
`df -h .` shows only the filesystem holding the current directory. `-i`
reports inodes, which can run out before space does.

## Try it

```console
$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       250G  120G  130G  48% /
```

## Margin notes

| Write        | It means                                        |
|--------------|-------------------------------------------------|
| `df -h`      | How full is every cabinet, in GB                |
| `df -h .`    | How full is the cabinet holding this drawer     |
| `df -i`      | How many more sheets can it hold                |

## When an agent asks

Agents check `df` when something fails with "No space left on device". It
only reads and is always safe.

## Careful

- A cabinet at 100% makes all sorts of tools fail strangely. Free space before anything else.
