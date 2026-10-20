---
command: kill
title: The Hand Bell
chapter: 4
order: 4
risk: medium
metaphor: >
  A hand bell rung for one clerk by number, telling them to put down their work and stop.
related: [ps]
sketch: >
  A polished brass hand bell with a turned wooden handle standing on a desk, small curved lines around it suggesting the ring.
exercise:
  question: "What is the difference between kill 4188 and kill -9 4188?"
  choices:
    - "None"
    - "The first politely asks clerk 4188 to stop. The second removes it at once, with no time to tidy up."
    - "-9 stops nine clerks"
  answer: 1
  explanation: "A plain kill sends TERM, which a clerk can catch to save its work. -9 (KILL) can't be caught. The clerk vanishes mid-sentence."
---

## In one line

`kill` tells a running program to stop, by its number.

## The picture

You look up a clerk's number on the duty roster and ring the bell for them.
The usual ring means "please finish up and stop", and a well-behaved clerk
saves their papers first. The loudest ring, `-9`, sends them out of the
room at once, mid-sentence, papers left where they fell.

## What really happens

`kill` sends a signal to a process by PID. The default is `TERM` (15), which
asks the program to exit and can be handled so it cleans up. `INT` (2) is what
Ctrl+C sends. `KILL` (9) cannot be caught or ignored, so the program can't
save state. You may only signal your own processes unless you use `sudo`.

## Try it

```console
$ sleep 300 &
[1] 4188
$ kill 4188
[1]+  Terminated              sleep 300
```

## Margin notes

| Write            | It means                                       |
|------------------|------------------------------------------------|
| `kill 4188`      | Ask clerk 4188 to finish up and stop           |
| `kill -9 4188`   | Remove clerk 4188 at once, no tidying          |
| `pkill name`     | Ring for every clerk whose task has that name  |
| `kill -0 4188`   | Only check that clerk 4188 is still there      |

## When an agent asks

Agents use `kill` to stop a server or a stuck task they started. Check the
number belongs to that task: the wrong number stops something else,
perhaps your editor with unsaved work.

## Careful

- `kill -9` loses whatever the program hadn't saved yet. Try a plain `kill` first.
- `pkill` matches by name and may stop more clerks than you expect.
