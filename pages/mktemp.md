---
command: mktemp
title: The Numbered Pad
chapter: 3
order: 7
risk: medium
metaphor: >
  A pad of blank scrap sheets, each stamped with its own serial number, so no two clerks ever take the same sheet.
related: [touch, mkdir, rm]
sketch: >
  A pad of tear-off scrap sheets lying on a small writing table, a gummed strip along its top and a stamped mark in the corner; one torn-off sheet lies beside it, with a ragged top edge and the same kind of mark.
exercise:
  question: "Hobbs writes tmp=$(mktemp) and later rm -rf \"$tmp\". What should you check?"
  choices:
    - "Nothing, rm is always safe on scrap sheets"
    - "That $tmp really holds the name mktemp gave, and nothing else changed it in between"
    - "That the scrap sheet is empty, or rm will refuse"
  answer: 1
  explanation: "rm erases whatever name the variable holds at that moment. If it were empty or changed, the eraser would land elsewhere. -rf is only needed for mktemp -d."
---

## In one line

`mktemp` creates a new, empty file (or folder) with a unique name, for scratch work, and tells you its name.

## The picture

By the back stairs there is a scrap drawer that every clerk in the house
shares. Its pad has a serial number stamped on each sheet. Tear one off and it
is yours: nobody else holds that number, so no one will write over your
work. The clerk reads you the number, so you can find the sheet again.

## What really happens

`mktemp` creates a file with a random name such as `/tmp/tmp.k3Jx9QbW2T`,
readable and writable only by you, and prints the name. `-d` creates a
directory instead. A template with at least three `X`s, like
`draft.XXXX`, sets the name and creates it in the current directory. The file
stays until someone deletes it. `/tmp` is often cleared when the computer
restarts.

## Try it

```console
$ tmp=$(mktemp)
$ echo $tmp
/tmp/tmp.k3Jx9QbW2T
$ sort notes.txt > "$tmp"
$ head -n 2 "$tmp"
buy flour
buy ink
$ rm "$tmp"
```

## Margin notes

| Write                     | It means                                      |
|---------------------------|-----------------------------------------------|
| `mktemp`                  | Give me a fresh scrap sheet and tell me its number |
| `mktemp -d`               | Give me a fresh scrap drawer instead          |
| `mktemp --suffix=.txt`    | Same, with `.txt` at the end of the name      |
| `mktemp draft.XXXX`       | A fresh sheet named after this pattern, here  |
| `tmp=$(mktemp)`           | Keep the number on a note named `tmp`         |

## When an agent asks

Agents use `mktemp` to get somewhere safe to put intermediate results, such
as a sorted copy or a downloaded file, without overwriting anything of yours.
Creating the sheet is harmless. Read the clean-up slip that comes later: it
should erase `"$tmp"` exactly, in quotes, and nothing wider.

## Careful

- If the variable (the note named `tmp`) is empty, `rm -rf "$tmp"/*` turns into `rm -rf /*`. Check that the name was set first.
- Scrap sheets are left behind unless something removes them. Secrets written there stay until then.
