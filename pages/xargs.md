---
command: xargs
title: The Foreman
chapter: 9
order: 3
risk: medium
metaphor: >
  A foreman who takes a list of names and hands each one to a clerk as part of the same instruction.
related: ["|", find, rm]
sketch: >
  A foreman's clipboard with a long list of names, a pencil behind a brass clip, and a row of identical instruction slips fanned out beside it.
exercise:
  question: "What does find . -name '*.tmp' | xargs rm do?"
  choices:
    - "Lists the .tmp sheets"
    - "Erases every .tmp sheet that find names"
    - "Nothing, rm can't read from a funnel"
  answer: 1
  explanation: "rm doesn't read the funnel itself, but xargs turns each name it receives into an argument for rm. Every found sheet is erased."
---

## In one line

`xargs` turns a list of items into arguments for another command.

## The picture

Some clerks, like the eraser, don't listen to the funnel. They need names
written on their instruction slip. The foreman stands at the end of the
funnel, takes each name that arrives, writes it on the slip, and hands the
slip to the clerk. A short list becomes a lot of work very quickly.

## What really happens

`xargs` reads items from standard input, separated by whitespace or newlines,
and runs the given command with those items appended as arguments, batching
them. `-n 1` passes one item per run, `-I {}` places each item where `{}`
appears, `-0` reads NUL-separated input (pair it with `find -print0`), and
`-P` runs several at once.

## Try it

```console
$ ls letters | xargs -n 1 echo "write to"
write to to-grandma.txt
write to to-the-bank.txt
```

## Margin notes

| Write                 | It means                                        |
|-----------------------|-------------------------------------------------|
| `... \| xargs cmd`    | Hand every name to cmd                          |
| `xargs -n 1`          | One name per slip                               |
| `xargs -I {} cp {} b/`| Put each name where {} is                       |
| `xargs -p`            | Ask me before each slip                         |

## When an agent asks

Look at the command after `xargs`: that is what will be done to every item.
`| xargs rm` or `| xargs sed -i` can change hundreds of sheets at once.

## Careful

- Names with spaces get split in two. Use `find ... -print0 | xargs -0`.
- Run the left side alone first to see the list the foreman will receive.
