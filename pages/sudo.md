---
command: sudo
title: The Master Key
chapter: 4
order: 2
risk: high
metaphor: >
  The head librarian's master key, which opens every lock in the house for one instruction.
related: [chmod, rm, pip install]
sketch: >
  A large ornate iron master key on a ring hanging from a hook, its bow decorated with a scrolled crest, casting a long shadow on the wall panel.
exercise:
  question: "An agent asks to run sudo rm -rf /var/cache/app. What changes because of sudo?"
  choices:
    - "Nothing, it is just politer"
    - "The erasing is done with the master key, so no lock in the house can stop it"
    - "It makes rm ask before erasing"
  answer: 1
  explanation: "sudo runs the rest of the instruction as the all-powerful root user. Every safety lock is bypassed, so a wrong path can damage the whole Study."
---

## In one line

`sudo` runs the rest of the command with full administrator power.

## The picture

Most drawers in the house have locks you can't open, and that's what keeps the
house safe. The head librarian has a master key that opens them all. `sudo`
borrows that key for a single instruction, after you show you're trusted by
giving your password.

## What really happens

`sudo` runs a command as another user, root by default, if the security
policy in `/etc/sudoers` allows it. It asks for your own password and caches
it for a few minutes. Everything the command does then happens with root
privileges, outside the normal permission checks.

## Try it

```console
$ whoami
you
$ sudo whoami
[sudo] password for you:
root
```

## Margin notes

| Write          | It means                                           |
|----------------|----------------------------------------------------|
| `sudo cmd`     | Carry out cmd with the master key                  |
| `sudo -u ann cmd` | Carry it out as Ann instead                     |
| `sudo -k`      | Forget my password now, ask again next time        |
| `sudo -i`      | Hand me the master key until I give it back        |

## When an agent asks

Treat every `sudo` as a red seal. Ask why it's needed. Installing system
software can need it. Editing your own files never should. Read the whole
instruction after `sudo`, because nothing will stop it.

## Careful

- An agent should almost never need your password. Typing it hands over the master key.
- `sudo` with `rm`, `chmod -R` or `curl ... | sh` is where the worst accidents happen.
