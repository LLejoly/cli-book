---
command: ssh
title: The Speaking Tube
chapter: 6
order: 3
risk: medium
metaphor: >
  A private speaking tube running to the study of another house, so your instructions are carried out by the clerks there.
related: [curl, git push, sudo]
sketch: >
  A brass speaking-tube mouthpiece with a hinged whistle cap mounted on a wood-panelled wall, the flexible tube disappearing into the panelling.
exercise:
  question: "After ssh you@library, you type rm notes.txt. Which notes.txt is erased?"
  choices:
    - "The one in your own Study"
    - "The one in the library's study, at the other end of the tube"
    - "Both"
  answer: 1
  explanation: "Once connected, every instruction goes down the tube and is carried out in the other house, until you type exit."
---

## In one line

`ssh` opens a secure connection to another computer and lets you type commands there.

## The picture

You lift the cap of the speaking tube and say who you are. If the other house
recognises your voice, or your key, you can now give instructions to the
clerks in its study. Everything you say goes through the tube, and nobody along
the way can overhear it.

## What really happens

`ssh` (secure shell) opens an encrypted connection to a remote host, checks
the host's key, authenticates you by key or password, and starts a shell
there. Commands then run on the remote machine. `exit` closes it. `ssh host
cmd` runs a single command. Keys live in `~/.ssh`.

## Try it

```console
$ ssh you@library.example.org
you@library.example.org's password:
you@library:~$ hostname
library
you@library:~$ exit
```

## Margin notes

| Write               | It means                                         |
|---------------------|--------------------------------------------------|
| `ssh you@house`     | Open the tube to that house as you               |
| `ssh house cmd`     | Ask for one instruction there, then close        |
| `ssh -i key house`  | Prove who I am with this key                     |
| `exit`              | Put the cap back on the tube                     |

## When an agent asks

Check which house it's connecting to and why. From then on, its instructions
act on that machine, possibly a live server that other people depend on.

## Careful

- A warning that the host key changed can mean someone is impersonating the house. Don't wave it away.
- Never paste the private key from `~/.ssh` anywhere.
