---
command: touch
title: The Date Stamp
chapter: 3
order: 3
risk: medium
metaphor: >
  A rubber date stamp pressed on a sheet to mark it as seen today, or on a blank sheet to start a new one.
related: [ls, ">", mkdir]
sketch: >
  A wooden-handled rubber date stamp with its turning date bands, beside an ink pad and a blank sheet bearing a fresh round stamp.
exercise:
  question: "postcard.txt doesn't exist. What does touch postcard.txt do?"
  choices:
    - "Grumbles that the sheet is missing"
    - "Creates an empty sheet called postcard.txt"
    - "Opens the sheet for writing"
  answer: 1
  explanation: "If the sheet doesn't exist, touch puts a new blank one in the drawer. If it does, it only updates its date."
---

## In one line

`touch` creates an empty file, or updates the date of one that exists.

## The picture

You take the date stamp and press it on a sheet. If the sheet is already in
the drawer, only the date in its corner changes and the writing stays as it
was. If there was no such sheet, you stamp a blank one and put it in the drawer.

## What really happens

`touch` sets a file's access and modification times to now. If the file
doesn't exist, it creates it with zero length. `-c` prevents creation. Build
tools such as `make` compare these times, so touching a file can make them
rebuild things.

## Try it

```console
$ touch postcard.txt
$ ls -l postcard.txt
-rw-r--r-- 1 you you 0 Oct 19 09:30 postcard.txt
```

## Margin notes

| Write          | It means                                         |
|----------------|--------------------------------------------------|
| `touch a`      | Stamp sheet a with today's date, or start it blank |
| `touch a b c`  | Stamp three sheets at once                       |
| `touch -c a`   | Stamp it only if it already exists               |

## When an agent asks

Agents use `touch` to create an empty file before filling it in. It never
erases writing, so it is mild. The only change you might notice is a new
blank sheet or a newer date.

## Careful

- Touching files can trick tools that decide what to redo by date into doing work again.
