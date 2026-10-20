---
command: cp
title: The Carbon Paper
chapter: 1
order: 6
risk: medium
metaphor: >
  Carbon paper slipped under a sheet, so you end up with the original and an exact copy.
related: [mv, rm, mkdir]
sketch: >
  Two sheets of paper stacked with a dark sheet of carbon paper between them, the top sheet slightly lifted at the corner to show the copy beneath.
exercise:
  question: "notes-copy.txt already exists. What does cp notes.txt notes-copy.txt do?"
  choices:
    - "Asks you first"
    - "Writes over notes-copy.txt without a word"
    - "Makes notes-copy-2.txt instead"
  answer: 1
  explanation: "cp quietly replaces a sheet with the same name. Add -i to make it ask, or -n to make it refuse."
---

## In one line

`cp` makes a copy of a file or folder.

## The picture

You slip carbon paper under a sheet, trace it once, and now have two sheets
with the same words. The original stays where it was. If a sheet with the new
name was already there, the copy goes on top of it and the old words are lost.

## What really happens

`cp` copies a source file to a destination path, or several sources into a
destination directory. An existing destination file is overwritten without a
prompt. Directories need `-r`. `-a` keeps timestamps and permissions, which
is what you want for backups.

## Try it

```console
$ cp notes.txt notes-copy.txt
$ cp -r letters letters-backup
$ ls
letters  letters-backup  notes-copy.txt  notes.txt  recipes
```

## Margin notes

| Write          | It means                                         |
|----------------|--------------------------------------------------|
| `cp -i a b`    | Ask me before writing over an existing sheet     |
| `cp -n a b`    | Never write over an existing sheet               |
| `cp -r a b`    | Copy a whole drawer and everything inside it     |
| `cp -a a b`    | Copy a drawer exactly, dates and locks included  |

## When an agent asks

Agents copy files to make a backup before an edit, or to start from a
template. Both are good habits. Check the destination: if that name is already
taken, the old sheet will be replaced.

## Careful

- Overwriting is silent. Copying onto the wrong name destroys that sheet.
- `cp -r` on a big drawer can fill up your Study. Check its size first.
