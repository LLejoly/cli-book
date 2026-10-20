---
command: head
title: The Ribbon Marker
chapter: 2
order: 1
risk: low
metaphor: >
  A ribbon laid across a sheet a few lines down, so the clerk reads only what sits above it.
related: [tail, cat, wc]
sketch: >
  A long sheet of handwriting with a silk ribbon laid across it a few lines from the top; the lines below the ribbon are faded.
exercise:
  question: "A log sheet has 10,000 lines. What does head show you?"
  choices:
    - "All 10,000 lines, very fast"
    - "The first 10 lines"
    - "The 10 most important lines"
  answer: 1
  explanation: "head reads from the top and stops after 10 lines unless you say otherwise with -n. It has no idea what is important."
---

## In one line

`head` shows only the first few lines of a file.

## The picture

The sheet is long, and you only need the start. You lay a ribbon across it a
few lines down and ask the clerk to read up to the ribbon. Everything below it
stays unread. The sheet itself is not touched.

## What really happens

`head` prints the first 10 lines of each file, or of standard input. `-n N`
changes the number of lines, and `-c N` counts bytes instead. With GNU `head`,
`-n -N` prints everything except the last N lines. It stops reading early,
so it's quick even on huge files.

## Try it

```console
$ head -n 2 notes.txt
buy flour
call grandma
```

## Margin notes

| Write            | It means                                   |
|------------------|--------------------------------------------|
| `head sheet`     | Read me the first 10 lines                 |
| `head -n 3`      | Read me the first 3 lines                  |
| `head -c 100`    | Read me the first 100 characters           |
| `... \| head`    | Only show me the start of what the clerk says |

## When an agent asks

Agents use `head` to peek at a file before reading all of it, or to cut a
long answer short with `| head`. It only reads, so it is safe to accept.

## Careful

- The first lines are not a summary. A problem halfway down the sheet won't show.
