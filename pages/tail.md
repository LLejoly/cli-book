---
command: tail
title: The Last Page
chapter: 2
order: 2
risk: low
metaphor: >
  Turning straight to the last page of a ledger to read the newest entries.
related: [head, cat, grep]
sketch: >
  A thick bound ledger lying open at its last written page, a fountain pen resting beside the newest entry, the earlier pages thick under the left hand side.
exercise:
  question: "An agent runs tail -f server.log and the command never seems to finish. Why?"
  choices:
    - "It is stuck and should be killed at once"
    - "-f keeps watching the sheet and reads out each new line as it is written"
    - "The file is too big to read"
  answer: 1
  explanation: "-f means follow. tail keeps the ledger open at the last page and reads new entries as they arrive, until you stop it with Ctrl+C."
---

## In one line

`tail` shows the last few lines of a file, which is where the newest entries are.

## The picture

A ledger fills up from front to back, so the newest entries are always at the
end. You open it straight at the last page and read the final lines. With a
margin note, you can even stay at that page and watch new entries appear as
the clerk writes them.

## What really happens

`tail` prints the last 10 lines of each file. `-n N` sets the number of lines,
and `-n +N` prints from line N to the end. `-f` keeps the file open and prints
new lines as they are appended, which is how people watch log files live.

## Try it

```console
$ tail -n 1 notes.txt
buy ink
$ tail -n 2 recipes/bread.txt
10g salt
7g yeast
```

## Margin notes

| Write          | It means                                           |
|----------------|----------------------------------------------------|
| `tail sheet`   | Read me the last 10 lines                          |
| `tail -n 50`   | Read me the last 50 lines                          |
| `tail -n +5`   | Read from line 5 to the end                        |
| `tail -f`      | Stay at the last page and read new lines as they come |

## When an agent asks

Agents use `tail` to read the end of a log after something went wrong, since
the newest error is at the bottom. It only reads. With `-f` it runs until
stopped, so the agent may seem to wait.

## Careful

- With `-f`, stop it with Ctrl+C. Nothing is lost when you do.
