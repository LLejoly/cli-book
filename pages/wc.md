---
command: wc
title: The Tally Counter
chapter: 2
order: 3
risk: low
metaphor: >
  A brass tally counter clicked once for every line, word or letter on a sheet.
related: [cat, grep, "|"]
sketch: >
  A small brass hand tally counter with its numbered wheels showing, resting on a sheet of handwriting, a thumb-lever on top.
exercise:
  question: "wc notes.txt answers 4 9 44 notes.txt. What is the 9?"
  choices:
    - "The number of lines"
    - "The number of words"
    - "The size in kilobytes"
  answer: 1
  explanation: "wc always answers in the same order: lines, words, then bytes (roughly the letters, spaces and line ends)."
---

## In one line

`wc` counts the lines, words and characters in a file.

## The picture

The clerk takes a brass tally counter and goes through the sheet, clicking
once for each line, once for each word and once for each letter. Then he reads
you the three numbers. He doesn't read you the sheet itself.

## What really happens

`wc` (word count) prints newline, word and byte counts for each file, in that
order, followed by the name. `-l`, `-w` and `-c` print only one count. It is
often placed at the end of a pipe, as in `grep error log | wc -l`, to count
matching lines.

## Try it

```console
$ wc -l notes.txt
4 notes.txt
$ wc notes.txt
 4  9 44 notes.txt
```

## Margin notes

| Write           | It means                                  |
|-----------------|-------------------------------------------|
| `wc -l`         | Count the lines only                      |
| `wc -w`         | Count the words only                      |
| `wc -c`         | Count the bytes                           |
| `... \| wc -l`  | Count how many lines the clerk said       |

## When an agent asks

Agents use `wc -l` to see how long a file is before reading it, or to count
results. It only reads and is always safe to accept.

## Careful

- A last line without a line ending isn't counted by `-l`, so the count can be one short.
