---
command: dd
title: The Whitewash Brush
chapter: 10
order: 4
risk: high
metaphor: >
  A whitewash brush that coats a whole surface with whatever is in the pail, from edge to edge, without asking what was there before.
related: [cp, sudo, df]
sketch: >
  A wooden pail of whitewash with a wide block brush laid across its rim, beside a chest of three drawers whose right half has been painted over in flat white, hiding the drawer fronts and knobs, a drip running down the edge.
exercise:
  question: "Hobbs wants to write a disk image to a USB stick with dd if=study.img of=/dev/sda. What should you check first?"
  choices:
    - "That study.img is not too big"
    - "That /dev/sda really is the stick and not your main disk"
    - "Nothing. dd asks before it overwrites anything."
  answer: 1
  explanation: "dd never asks. Whatever of= names is painted over from edge to edge. On many machines /dev/sda is the main disk, so check with lsblk which name the stick really has."
---

## In one line

`dd` copies raw data from one place to another, and can overwrite a whole disk in one go.

## The picture

The whitewash brush doesn't care what is on a wall. You name a pail and a
surface, and it coats the surface with whatever is in the pail, stroke after
stroke, from one corner to the other. Point it at a whole cabinet and every
drawer, label and sheet vanishes under the wash. Mix up pail and cabinet, and
you paint your good cabinet with the empty one.

## What really happens

`dd` copies bytes from `if=` (input file) to `of=` (output file), block by
block, with no idea of files or folders. It is used to write disk images to
USB sticks and to copy or wipe whole disks, named like `/dev/sdb`. Writing to a
disk replaces everything on it, with no confirmation. An existing output file
is emptied first. `/dev/zero` is an endless pail of blank bytes.

## Try it

```console
$ dd if=/dev/zero of=blank.sheet bs=1K count=4
4+0 records in
4+0 records out
4096 bytes (4.1 kB, 4.0 KiB) copied, 0.000102 s, 40.2 MB/s
$ wc -c blank.sheet
4096 blank.sheet
```

## Margin notes

| Write             | It means                                   |
|-------------------|--------------------------------------------|
| `if=a`            | The pail: read from a                      |
| `of=b`            | The surface: paint over b                  |
| `bs=4M`           | Paint in strokes of 4 megabytes            |
| `count=4`         | Stop after 4 strokes                       |
| `status=progress` | Tell me how far you've got as you go       |

## When an agent asks

Agents use `dd` to write a disk image to a USB stick, to make a test file of a
set size, or to wipe something. Read `of=` letter by letter: is it a sheet, or
a disk like `/dev/sda`? Ask Hobbs to run `lsblk` first and say which disk is
which. Refuse any `of=/dev/...` you can't name yourself.

## Careful

- `of=/dev/sda` instead of `of=/dev/sdb` paints over the wrong disk. One letter, everything gone, no undo.
- Swap `if=` and `of=`, and dd copies the stick over your disk instead of the other way round.
- dd is silent while it works, so a long pause is not a hang. On macOS disks are named like `/dev/disk2`.
