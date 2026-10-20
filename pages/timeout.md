---
command: timeout
title: The Egg Timer
chapter: 4
order: 7
risk: medium
metaphor: >
  An egg timer turned over beside a clerk's task: when the sand runs out, the clerk is told to stop, finished or not.
related: [kill, ps]
sketch: >
  A glass egg timer between two turned wooden posts and round wooden ends, standing on the floor, a little sand left in the upper bulb, most of it heaped in the lower one and a thin stream still falling.
exercise:
  question: "timeout 60 pytest stops after a minute and $? is 124. What does that mean?"
  choices:
    - "The tests all passed"
    - "The sand ran out: the tests were cut off before they finished, so you don't know yet"
    - "Exactly 124 tests failed"
  answer: 1
  explanation: "124 is timeout's own signal that time was up. The task was stopped part way, so there is no verdict on the tests, only that they took too long."
---

## In one line

`timeout` runs a command and stops it if it takes longer than you allow.

## The picture

You give a clerk a slip and turn the egg timer over beside them. If the clerk
finishes first, nothing more happens. If the last grain of sand falls while
they are still at work, the hand bell rings for them and they must put the
task down where it is.

## What really happens

`timeout DURATION COMMAND` starts the command and sends it `TERM` if it is
still running after the duration (seconds by default, or `m`, `h`, `d`). If it
was stopped, `timeout` exits with status 124. Otherwise it returns the
command's own status. `-s` picks another signal, and `-k` sends `KILL` later if
`TERM` was ignored.

## Try it

```console
$ timeout 2 sleep 10
$ echo $?
124
$ timeout 5 cat notes.txt
buy flour
call grandma
pay the bank
buy ink
$ echo $?
0
```

## Margin notes

| Write                  | It means                                      |
|------------------------|-----------------------------------------------|
| `timeout 30 cmd`       | Stop the clerk after thirty seconds           |
| `timeout 5m cmd`       | Five minutes of sand                          |
| `timeout -k 10 60 cmd` | Ring at one minute, send them out ten seconds later |
| `timeout -s INT 30 cmd`| Ring the Ctrl+C bell instead of the usual one |

## When an agent asks

Agents wrap long or uncertain tasks in `timeout` so they don't wait forever on
a test run, a server or a network call. That is a good habit. The seal belongs
to the slip inside, so read that part as if it stood alone:
`timeout 60 rm -rf build` erases just as thoroughly. Check the time is long
enough for the task to finish.

## Careful

- A task stopped half way may leave half-written sheets behind.
- Exit status 124 means "ran out of time", not "failed" or "passed".
