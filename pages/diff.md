---
command: diff
title: The Two Candlesticks
chapter: 2
order: 5
risk: low
metaphor: >
  Two sheets laid side by side under a pair of candlesticks, compared line by line to spot what differs.
related: [cat, git status, cp]
sketch: >
  Two handwritten recipe cards laid side by side on a desk between a pair of brass candlesticks, one line on the right card underlined.
exercise:
  question: "diff answers 4a5 > 1 spoon honey. What does it mean?"
  choices:
    - "After line 4 of the first sheet, the second sheet adds 1 spoon honey"
    - "Line 4 was deleted"
    - "Both sheets contain 1 spoon honey"
  answer: 0
  explanation: "a means added. The > arrow points to a line that only the second sheet has."
---

## In one line

`diff` compares two files and shows only the lines that differ.

## The picture

You lay your bread recipe beside grandma's, light the two candles, and read
them together line by line. You say nothing about the lines that match. You
only point at the differences: this line changed, that line was added.

## What really happens

`diff` prints the changes that would turn the first file into the second.
Lines marked `<` come from the first file and `>` from the second. Codes like
`2c2` (changed), `4a5` (added) and `3d2` (deleted) give line numbers. `-u`
prints the "unified" format with `-` and `+` that code reviews use. It
exits with 1 when the files differ.

## Try it

```console
$ diff recipes/bread.txt recipes/bread-grandma.txt
2c2
< 350ml water
---
> 300ml water
4a5
> 1 spoon honey
```

## Margin notes

| Write        | It means                                          |
|--------------|---------------------------------------------------|
| `diff a b`   | What is different between sheets a and b          |
| `diff -u a b`| Show it with - and + and a few lines of context   |
| `diff -r a b`| Compare two whole drawers                         |
| `diff -q a b`| Only tell me whether they differ                  |

## When an agent asks

Agents use `diff` to check what an edit really changed, which is a habit
worth encouraging. It only reads, so it is safe to accept.

## Careful

- The order matters: `diff a b` and `diff b a` show the same changes with the arrows reversed.
