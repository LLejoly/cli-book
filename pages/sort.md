---
command: sort
title: The Sorting Rack
chapter: 8
order: 1
risk: low
metaphor: >
  The post room's sorting rack of pigeonholes, where slips are put in alphabetical order before being read out.
related: [cat, "|", grep]
sketch: >
  A wooden post-room sorting rack of small pigeonholes, each with a tiny brass label holder, several holding folded slips.
exercise:
  question: "What does sort -n do differently from plain sort with 2, 10 and 9?"
  choices:
    - "Nothing"
    - "Plain sort gives 10, 2, 9 (letter by letter). -n gives 2, 9, 10 (by value)."
    - "-n removes the numbers"
  answer: 1
  explanation: "Plain sort compares characters, and '1' comes before '2'. The -n margin note tells it to compare the numbers' values."
---

## In one line

`sort` puts the lines of a file in order.

## The picture

The clerk cuts the sheet into slips, one per line, and files each slip in the
sorting rack in alphabetical order. Then he reads them back from the first
pigeonhole to the last. The original sheet is untouched. Only the reading
comes out in order.

## What really happens

`sort` reads all its input lines and writes them sorted, by default in the
locale's collation order. `-n` sorts numerically, `-r` reverses, `-u` drops
duplicates, `-k` sorts by a given field, and `-h` understands sizes like 2K or
1G. It's often paired with `uniq -c` to count repeats.

## Try it

```console
$ sort notes.txt
buy flour
buy ink
call grandma
pay the bank
$ sort -r notes.txt | head -n 2
pay the bank
call grandma
```

## Margin notes

| Write          | It means                                      |
|----------------|-----------------------------------------------|
| `sort -r`      | File them from last to first                  |
| `sort -n`      | Order numbers by their value                  |
| `sort -u`      | Keep only one of each repeated slip           |
| `sort -k 2`    | Order by the second word on each line         |

## When an agent asks

Agents sort to make long lists readable or to find the biggest or smallest
items. It only reads. Watch the `>` after it: `sort a > a` empties sheet a.

## Careful

- To sort a sheet into itself, use `sort -o a a`, not `sort a > a`.
