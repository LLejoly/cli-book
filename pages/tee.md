---
command: tee
title: The T-Joint
chapter: 3
order: 6
risk: high
metaphor: >
  A brass T-joint fitted below the funnel, so what pours through goes two ways at once: on to you, and onto a sheet.
related: ["|", ">", sudo]
sketch: >
  A low wooden stand holding a brass T-joint on an upright post, a tin funnel feeding it from above; one arm of the T drips into a teacup, the other into a small jar, both standing on the stand.
exercise:
  question: "What is the difference between sort notes.txt | tee sorted.txt and sort notes.txt > sorted.txt?"
  choices:
    - "None at all"
    - "Both write sorted.txt, but tee also reads the sorted list back to you"
    - "tee adds to the end of sorted.txt instead of replacing it"
  answer: 1
  explanation: "tee writes the sheet and says it aloud. Like a single >, it starts the sheet afresh. Only tee -a adds to the end."
---

## In one line

`tee` saves what passes through it into a file and shows it to you at the same time.

## The picture

The funnel carries one clerk's answer to the next. Fit a T-joint below it and
the stream splits in two. One arm carries on as before, to you or the next
clerk. The other pours onto a sheet, which is written out as the words arrive.
That sheet starts fresh, unless you say otherwise.

## What really happens

`tee` copies its standard input to standard output and to every file you
name. It truncates each file first, as `>` does, unless you pass `-a`
(append). Being a separate program, it runs with its own permissions, which is
why `| sudo tee file` can write where `sudo cmd > file` cannot: in the
second form the redirect is opened by your own shell, without the master key.

## Try it

```console
$ sort notes.txt | tee sorted.txt
buy flour
buy ink
call grandma
pay the bank
$ echo "buy stamps" | tee -a notes.txt
buy stamps
```

## Margin notes

| Write                  | It means                                        |
|------------------------|-------------------------------------------------|
| `cmd \| tee a`         | Show me the answer and write it on sheet a, replacing it |
| `cmd \| tee -a a`      | Show me, and add it to the end of sheet a       |
| `cmd \| tee a b`       | Write it on two sheets at once                  |
| `cmd \| sudo tee a`    | Write it with the master key. The riskiest form |
| `tee a > /dev/null`    | Write the sheet, but don't read it to me        |

## When an agent asks

Agents use `| tee build.log` to keep a long answer on file while still seeing
it. Read the name after `tee`: that sheet is wiped unless `-a` is there. Be
most careful with `sudo tee`, often aimed at a settings file such as
`/etc/hosts`, which it overwrites with the master key.

## Careful

- `tee` without `-a` is a single `>`: the old sheet is lost, with no undo.
- Everything that passes through is also read aloud, so `printenv | tee env.txt` shows your keys and stores them on a sheet.
