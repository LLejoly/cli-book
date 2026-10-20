---
command: nc
title: The Hatch in the Wall
chapter: 11
order: 5
risk: high
metaphor: >
  A small hatch cut through the wall that opens a direct line to another house, to send writing out or to listen for what comes in.
related: [ssh, curl, eval]
sketch: >
  A brass-rimmed hatch set in a panelled wall, its little door ajar, a speaking-tube cord running from it off the edge of the frame.
exercise:
  question: "A forged note asks Hobbs to run nc that opens a hatch and hands your desk's controls to another house. What is that?"
  choices:
    - "A harmless speed test"
    - "A reverse shell: it gives a stranger a working line into your study"
    - "A way to back up your files"
  answer: 1
  explanation: "An inbound hatch wired to a shell lets another house type orders at your desk. A note from outside asking for it is a forged letter. A plain port check, like nc -zv host 80, only knocks and reports; that is the safe use."
---

## In one line

`nc` opens a raw connection to another machine to send or receive bytes directly.

## The picture

You cut a small hatch in the wall and run a line through it to another house.
Through it you can pass a sheet, or sit and listen for whatever is pushed back.
Opened for a moment to check that a door answers, it is harmless. Left open and
wired to your desk, it lets a stranger reach in and work your drawers.

## What really happens

`nc` (netcat) makes arbitrary TCP or UDP connections. It can connect out, or
listen for an incoming connection with `-l`, and pipe raw data either way. `-z`
scans without sending data and `-v` reports the result, which together make a
simple port check. Because it moves raw bytes, it is also the classic tool for
reverse shells and quiet data transfer.

## Try it

```console
$ nc -zv example.com 80
Connection to example.com (93.184.216.34) 80 port [tcp/http] succeeded!
$ nc -zv example.com 81
nc: connect to example.com port 81 (tcp) failed: Connection timed out
```

## Margin notes

| Write                | It means                                           |
|----------------------|----------------------------------------------------|
| `nc -zv host port`   | Just knock and tell me if the door answers         |
| `nc host port`       | Open a line and pass writing both ways             |
| `nc -l port`         | Listen here for an incoming line                   |
| `nc -w 5 ...`        | Give up after 5 seconds                            |

## When an agent asks

A port check (`-zv`) to see whether a service is up is routine and safe. Stop
if the command listens (`-l`), or pipes `nc` into a shell, or sends a file out,
especially when a README, issue or web page Hobbs just read asked for it. That
is a forged letter asking him to open a hatch for a stranger. Check who gave
the order and where the line goes.

## Careful

- `nc -l` wired to a shell is a reverse shell: it hands your desk to whoever connects.
- `nc` can quietly carry a file out of the house. Watch what is being piped into it.
