---
command: ">"
title: The Dictation Pad
chapter: 3
order: 2
risk: high
metaphor: >
  A dictation pad where the clerk writes down his answer instead of saying it, on a fresh sheet that replaces any old one.
related: [echo, cat, "|"]
sketch: >
  A stenographer's dictation pad bound at the top, its first page filled with shorthand, a pencil lying across it.
exercise:
  question: "notes.txt holds your shopping list. What does echo hello > notes.txt do?"
  choices:
    - "Adds hello at the end of the list"
    - "Replaces the whole list with the single word hello"
    - "Refuses because notes.txt already exists"
  answer: 1
  explanation: "A single > starts from a blank sheet, so the old list is gone. >> would have added hello to the end."
---

## In one line

`>` saves a command's result into a file, replacing what was there. `>>` adds to the end instead.

## The picture

Normally the clerk reads his answer aloud. With the dictation pad he writes it
down instead. One `>` means "tear off a fresh sheet": whatever was on the old
sheet with that name is thrown away. Two, `>>`, means "carry on writing at the
bottom of the existing sheet".

## What really happens

The shell opens the named file for writing before the command runs. `>`
truncates the file to zero length first. `>>` appends. Only standard output is
redirected. Errors still reach the screen unless you add `2>`. The file is
created if it doesn't exist.

## Try it

```console
$ ls letters > list.txt
$ cat list.txt
to-grandma.txt
to-the-bank.txt
$ echo "buy stamps" >> notes.txt
$ tail -n 2 notes.txt
buy ink
buy stamps
```

## Margin notes

| Write         | It means                                          |
|---------------|---------------------------------------------------|
| `cmd > a`     | Write the answer on sheet a, replacing what was there |
| `cmd >> a`    | Add the answer at the end of sheet a              |
| `cmd 2> a`    | Write the grumbles on sheet a                     |
| `cmd > /dev/null` | Throw the answer away                         |

## When an agent asks

Agents use `>` to create files quickly. Check the name after the arrow: if
that sheet already exists, its old contents are lost for good.

## Careful

- One `>` instead of `>>` wipes the sheet. There is no undo.
- `sort a > a` empties a before sort can read it. Write to a new name first.
