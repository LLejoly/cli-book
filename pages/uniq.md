---
command: uniq
title: The Ditto Mark
chapter: 8
order: 6
risk: low
metaphor: >
  A clerk copying a list writes a ditto mark instead of a line that repeats the one just above it, so only a repeat directly under its twin is noticed.
related: [sort, cut, "|"]
sketch: >
  A list sheet lying on a wooden writing desk with a drawer, its handwritten lines showing pairs of ditto marks under a line that repeats the one above, and a pencil resting across the sheet.
exercise:
  question: "cut -d' ' -f1 notes.txt | uniq still prints buy twice. Why?"
  choices:
    - "uniq only removes repeats that sit next to each other, and the two buy lines are far apart"
    - "uniq ignores the first word of each line"
    - "The funnel loses the uniq margin notes"
  answer: 0
  explanation: "uniq only compares each line with the one just before it. The two buy lines have call and pay between them, so both stay. Put sort in front, and the repeats line up side by side."
---

## In one line

`uniq` removes a line when it repeats the line just before it.

## The picture

The clerk copies a list line by line. Before each line, he glances only at the
line just above. If it says the same thing, he writes a ditto mark („) instead.
He never looks further up the page, so a repeat that comes later, after a
different line, is copied out in full again. When he reads the copy back to
you, he skips the ditto marks.

## What really happens

`uniq` reads lines from a file or standard input and drops each line that is
identical to the line before it. It never looks further back, which is why it
is almost always used as `sort | uniq`. `-c` puts a count in front of each
line, `-d` prints only lines that were repeated, `-u` only lines that were not,
and `-i` ignores upper and lower case.

## Try it

```console
$ cut -d' ' -f1 notes.txt | uniq
buy
call
pay
buy
$ cut -d' ' -f1 notes.txt | sort | uniq -c
      2 buy
      1 call
      1 pay
```

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `sort \| uniq`     | Line the repeats up first, then keep one of each |
| `uniq -c`          | Count each line together with its ditto marks    |
| `uniq -d`          | Read me only the lines that have ditto marks     |
| `uniq -i`          | Treat capital and small letters as the same      |

## When an agent asks

Agents reach for `sort | uniq -c | sort -rn` to count things: the commonest
errors in a log, the words in a list, the authors in the letter book. It only
reads. Check that `sort` comes before `uniq`, or the counts will be wrong
without any grumble, and watch for a second file name after the first.

## Careful

- `uniq a b` does not compare two sheets: it reads `a` and writes the result over `b`, without asking.
