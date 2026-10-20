---
command: ps
title: The Duty Roster
chapter: 4
order: 3
risk: low
metaphor: >
  The duty roster on the wall listing every clerk at work right now, with their number and the task in hand.
related: [kill, grep, "|"]
sketch: >
  A framed duty roster hanging on a wall hook, with handwritten rows of names and numbers, a small slate and chalk on a ledge below.
exercise:
  question: "What is the PID column in ps?"
  choices:
    - "How busy each clerk is"
    - "Each clerk's own number, used to call on that clerk later"
    - "The price of the task"
  answer: 1
  explanation: "PID is the process ID. It's how you name one particular clerk, for example to tell it to stop with kill."
---

## In one line

`ps` lists the programs that are running right now.

## The picture

Every task given to the Study is handled by a clerk. The duty roster on the
wall lists the clerks at work: each one's number, how long it has been busy and
what it's doing. Reading the roster disturbs nobody.

## What really happens

`ps` reports a snapshot of running processes. By default it shows those in
your current terminal. `ps aux` (BSD style) or `ps -ef` (Unix style) list every
process on the system with its PID, owner, CPU and memory use, and command
line. For a live view, `top` refreshes continuously.

## Try it

```console
$ sleep 300 &
$ ps
  PID TTY          TIME CMD
 4120 pts/0    00:00:00 bash
 4188 pts/0    00:00:00 sleep
 4190 pts/0    00:00:00 ps
```

## Margin notes

| Write              | It means                                      |
|--------------------|-----------------------------------------------|
| `ps`               | Clerks working at my desk                     |
| `ps aux`           | Every clerk in the whole house                |
| `ps aux \| grep x` | Find the clerks whose task mentions x         |
| `top`              | A roster that keeps updating                  |

## When an agent asks

Agents use `ps` to check whether something they started is still running, or
to find a clerk that's stuck. It only reads and is safe. A `kill` often follows
it, so look at what comes next.

## Careful

- `ps aux` shows full command lines, which sometimes include passwords someone typed into a command.
