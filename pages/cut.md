---
command: cut
title: The Paper Cutter
chapter: 8
order: 7
risk: low
metaphor: >
  A board paper cutter with a ruled bed and a hinged blade, set once and brought down so that every line keeps only the same column.
related: [uniq, sort, grep]
sketch: >
  A wooden board paper cutter standing on the floor, its long hinged blade raised, a ruled sheet lying on the bed against the guide, and a narrow cut strip fallen beside the board.
exercise:
  question: "You want the second word of each line in notes.txt. Which slip is right?"
  choices:
    - "cut -f2 notes.txt"
    - "cut -d' ' -f2 notes.txt"
    - "cut -c2 notes.txt"
  answer: 1
  explanation: "Without -d, cut splits lines at tabs, and notes.txt has none, so -f2 prints every line whole. -c2 gives the second letter, not the second word. -d' ' tells it the words are separated by spaces."
---

## In one line

`cut` keeps only one part of every line, such as the first word or the first ten letters.

## The picture

The clerk lays the sheet on the paper cutter, sets the guide at the right
column and brings the blade down. Every line loses the same part at once, and
he reads you what is left. The sheet in the drawer is untouched. Only his
reading is trimmed.

## What really happens

`cut` prints selected parts of each input line. `-f` picks fields, which are
separated by a tab unless `-d` names another single character. `-c` picks
characters by position. Ranges look like `2`, `1,3`, `2-` (to the end of the
line) or `-4`. Fields come out in their original order, whatever order you list
them in.

## Try it

```console
$ cut -d' ' -f1 notes.txt
buy
call
pay
buy
$ cut -d' ' -f2- notes.txt
flour
grandma
the bank
ink
```

## Margin notes

| Write              | It means                                          |
|--------------------|---------------------------------------------------|
| `cut -d, -f2`      | Words are parted by commas; keep the second       |
| `cut -f1,3`        | Keep the first and third columns (tab-separated)  |
| `cut -c1-10`       | Keep the first ten letters of each line           |
| `cut -s`           | Leave out lines that have no separator at all     |

## When an agent asks

Agents use `cut` to pull one column out of a table: names from a list,
the second field of a CSV (a sheet of values parted by commas), the user names
in `/etc/passwd`. It only reads. Check the `-d` character against what the
sheet really uses: if it is wrong, you get whole lines back and the agent may
draw the wrong conclusion.

## Careful

- Two spaces in a row count as two separators, so the next field comes out empty. For spacing that wanders, `awk '{print $2}'` is safer.
- `cut` splits a CSV at every comma, even one inside quotes like `"Smith, Ada"`.
