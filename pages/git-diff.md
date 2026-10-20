---
command: git diff
title: The Tracing Paper
chapter: 7
order: 3
risk: low
metaphor: >
  A sheet of tracing paper laid over the last pressed copy, showing exactly which words have changed since.
related: [diff, git status, git add]
sketch: >
  A translucent sheet of tracing paper half laid over a handwritten letter, one line on the letter crossed through and a new line traced above it.
exercise:
  question: "In git diff, what does a line starting with + mean?"
  choices:
    - "A line that was added since the last pressed copy"
    - "A line that is extra important"
    - "A line that was deleted"
  answer: 0
  explanation: "+ marks a line that is new in the drawer. - marks a line that was in the last pressed copy and is now gone or changed."
---

## In one line

`git diff` shows the exact lines you changed since the last saved version.

## The picture

You lay tracing paper over the last pressed copy of a sheet and compare.
Lines that vanished are marked with a minus, new lines with a plus.
Everything that didn't change is left plain, so the changes stand out.

## What really happens

`git diff` compares the working tree with the index and prints a unified
diff. `--staged` compares the index with the last commit, which is what will
be committed. `git diff main..branch` compares two branches. `--stat` gives
only a per-file summary. It changes nothing.

## Try it

```console
$ git diff
diff --git a/notes.txt b/notes.txt
--- a/notes.txt
+++ b/notes.txt
@@ -1,4 +1,4 @@
 buy flour
 call grandma
 pay the bank
-buy ink
+buy blue ink
```

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `git diff`         | Changes not yet in the tray                      |
| `git diff --staged`| Changes waiting in the tray                      |
| `git diff --stat`  | Just tell me how many lines changed per sheet    |
| `git diff a..b`    | Compare two drafts                               |

## When an agent asks

An agent that shows you `git diff` before committing is letting you check its
work. It only reads. This is the best moment to look over what it changed.

## Careful

- If `git diff` shows nothing, the changes may already be in the tray. Try `--staged`.
