---
command: sed
title: The Proofreader's Pen
chapter: 3
order: 4
risk: medium
metaphor: >
  A proofreader's red pen that goes down a sheet line by line, swapping one word for another wherever it appears.
related: [grep, cat, diff]
sketch: >
  A dip pen with red ink resting on a printed page, one word struck through and a correction written in the margin with a caret mark.
exercise:
  question: "What is the difference between sed 's/water/milk/' bread.txt and sed -i 's/water/milk/' bread.txt?"
  choices:
    - "None, both change the sheet"
    - "The first only reads out a corrected copy. The second rewrites the sheet itself."
    - "The second asks for confirmation"
  answer: 1
  explanation: "Without -i, sed reads you a corrected version and leaves the sheet alone. With -i it writes the corrections into the sheet, with no undo."
---

## In one line

`sed` edits text: it finds words or lines and replaces, deletes or prints them.

## The picture

The proofreader runs her red pen down the sheet. Wherever she sees "water" she
writes "milk". Normally she reads you the corrected version and leaves the
original untouched. Add the margin note `-i` and she corrects the sheet itself,
in ink.

## What really happens

`sed` (stream editor) applies a small script to each input line. The most
common script is `s/old/new/`, which substitutes the first match on each line,
or every match with `/g`. `-n` with `p` prints selected lines, so
`sed -n '2,3p'` prints lines 2 and 3. `-i` edits files in place.

## Try it

```console
$ sed 's/water/milk/' recipes/bread.txt
500g flour
350ml milk
10g salt
7g yeast
$ sed -n '2,3p' notes.txt
call grandma
pay the bank
```

## Margin notes

| Write              | It means                                    |
|--------------------|---------------------------------------------|
| `sed 's/a/b/'`     | Read it with the first a on each line swapped for b |
| `sed 's/a/b/g'`    | Swap every a, not just the first            |
| `sed -n '5,9p'`    | Only read me lines 5 to 9                   |
| `sed -i ...`       | Make the corrections in the sheet itself    |

## When an agent asks

Agents use `sed -n` to read part of a file, which is harmless, and `sed -i` to
edit files quickly. For `-i`, check the pattern: a pattern that is too broad
rewrites far more than intended.

## Careful

- `-i` keeps no copy. Use `-i.bak` to keep the old sheet as `name.bak`.
- On a Mac, `sed -i` needs an argument: `sed -i '' 's/a/b/' file`.
