---
command: docker run
title: The Travelling Trunk
chapter: 9
order: 5
risk: medium
metaphor: >
  A travelling trunk with a small, complete study packed inside, unpacked and set to work without disturbing the rest of the house.
related: [ssh, pip install, sudo]
sketch: >
  A steamer trunk standing open on end, its inside fitted like a tiny study with drawers, a fold-down desk and a hanging lamp, travel labels on the lid.
exercise:
  question: "docker run -v ~/study:/data ... What does the -v part do?"
  choices:
    - "Makes the trunk bigger"
    - "Lets the trunk's study reach into your real study drawer"
    - "Shows the version"
  answer: 1
  explanation: "-v opens a passage between a drawer of your house and the trunk. Whatever runs inside can then read, change or erase those sheets."
---

## In one line

`docker run` starts a program inside a container: a packaged, separate copy of everything it needs.

## The picture

The trunk arrives with a tiny, complete study packed inside: its own drawers,
its own clerks, its own tools. You open it and set it to work. Whatever
happens inside stays inside, unless you open a passage to one of your own
drawers or rooms.

## What really happens

`docker run image` creates a container from an image, downloading the image
if needed, and runs its command with an isolated filesystem, processes and
network. `-v` mounts host paths into it, `-p` publishes ports, `--rm` deletes
the container when it stops, `-it` gives an interactive terminal.
`--privileged` removes most isolation.

## Try it

```console
$ docker run --rm python:3.12 python -c 'print("hello from the trunk")'
hello from the trunk
```

## Margin notes

| Write                  | It means                                        |
|------------------------|-------------------------------------------------|
| `docker run image`     | Unpack this trunk and set it to work            |
| `--rm`                 | Throw the trunk away when it's done             |
| `-v ~/a:/data`         | Open a passage from my drawer a into the trunk  |
| `--privileged`         | Take the walls off the trunk                    |

## When an agent asks

Containers are a good way to run things at a distance from your files. Check
the `-v` passages (which of your drawers it can reach), and refuse
`--privileged` unless you know why it's needed.

## Careful

- `-v /:/host` hands the whole house to whatever is in the trunk.
- Images come from strangers too. Prefer official, well-known ones.
