---
command: printenv
title: The Board Read Aloud
chapter: 10
order: 5
risk: high
metaphor: >
  A clerk who stands at the pinboard and reads every note on it aloud, including the keys to the strongbox hanging there.
related: [export, echo, which]
sketch: >
  A cork pinboard in a wooden frame standing on the floor, three written cards and an iron strongbox key hanging from its brass pins; a brass speaking trumpet lies at its foot, bell turned outward, with sound lines spreading from it.
exercise:
  question: "Hobbs wants to check that a tool can find its settings and proposes printenv. Your API key is pinned on the board. What is the better slip?"
  choices:
    - "printenv, then delete the transcript afterwards"
    - "printenv TOOL_HOME, or printenv | cut -d= -f1 to see only the names"
    - "printenv is fine, because it only reads"
  answer: 1
  explanation: "printenv only reads, but it reads aloud: every value lands in the transcript, and from there in logs you don't control. Asking for one note by name, or for the names alone, gets the answer without saying the keys."
---

## In one line

`printenv` shows the settings every program you start can read, secrets included.

## The picture

The pinboard holds notes for every clerk you send out: where things are kept,
which language to write in, and sometimes a key to the strongbox, pinned there
so a clerk can fetch something. `printenv` sends a clerk to the board to read
every note aloud. Anyone within earshot hears the keys too.

## What really happens

`printenv` prints the environment variables of the current shell, as
`NAME=value` lines. Given names, it prints only those values. It changes
nothing, but API keys, tokens and passwords often live in the environment, so
its output is a secret. When an agent runs it, the output lands in the
conversation and possibly in logs or a provider's records.

## Try it

```console
$ printenv HOME
/home/you
$ export GREETING="good morning"
$ printenv GREETING
good morning
```

## Margin notes

| Write                     | It means                                       |
|---------------------------|------------------------------------------------|
| `printenv`                | Read every note aloud, keys and all            |
| `printenv HOME`           | Read me only the note called HOME              |
| `printenv \| cut -d= -f1` | Read me the names on the notes, not what they say |
| `env`                     | The same as `printenv` with no names           |

## When an agent asks

Agents run `printenv` or `env` to debug a tool that can't find its settings.
Ask Hobbs to name the note he needs, or to list names only. Refuse a bare
`printenv` or `env` if any key is pinned on your board: it will be written into
the transcript.

## Careful

- A key read aloud once has left the house. Treat it as exposed, and change it.
- `env`, `set` and `export -p` also read the board aloud.
