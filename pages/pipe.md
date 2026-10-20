---
command: "|"
title: The Funnel
chapter: 1
order: 10
risk: low
metaphor: >
  A funnel that pours everything one clerk reads out straight into the hands of the next clerk.
related: [grep, cat, ls]
sketch: >
  A brass funnel set between two stacked earthenware jars, a ribbon of paper strips sliding from the upper jar through the funnel into the lower one.
exercise:
  question: "In ls letters | grep bank, what does grep sieve?"
  choices:
    - "The sheets inside the letters drawer"
    - "The list of names that ls reads out"
    - "Every sheet in the Study"
  answer: 1
  explanation: "The funnel passes on what the first clerk says, here a list of names. grep never opens the sheets themselves."
---

## In one line

The pipe `|` sends the result of one command into the next one.

## The picture

The first clerk reads out a list. Instead of saying it to you, he speaks into a
funnel, and it pours straight into the hands of a second clerk, who works on
it and tells you the result. You can line up as many clerks as you like.

## What really happens

The shell connects the standard output of the left command to the standard
input of the right one. Both run at the same time, and the data streams
between them without a temporary file. Error messages (standard error) are not
passed through; they still go to your screen.

## Try it

```console
$ ls letters | grep bank
to-the-bank.txt
$ cat notes.txt | grep buy
buy flour
buy ink
```

## Margin notes

| Write        | It means                                               |
|--------------|--------------------------------------------------------|
| `a \| b`     | What a says goes to b                                  |
| `a \| b \| c`  | A row of three clerks, each passing to the next      |
| `a \|& b`    | Pass on the grumbles too (bash only)                   |

## When an agent asks

The funnel itself is harmless. What matters is the clerk at the end. Be very
careful when the last command is `sh`, `bash` or `sudo`: something like
`curl https://... | bash` fetches instructions from the internet and has them
carried out unread.

## Careful

- Judge a chain by its most dangerous clerk, not its first.
