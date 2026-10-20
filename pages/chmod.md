---
command: chmod
title: The Locksmith
chapter: 4
order: 1
risk: medium
metaphor: >
  A locksmith who changes who may read a sheet, who may write on it, and who may set it to work as a set of orders.
related: [sudo, ls]
sketch: >
  A locksmith's leather roll opened on the desk, showing a row of small keys and picks, with an old brass padlock sprung open beside it.
exercise:
  question: "ls -l shows -rwxr-xr-x for tidy.sh. Who may change what is written on it?"
  choices:
    - "Everyone"
    - "Only you, the owner"
    - "Nobody"
  answer: 1
  explanation: "The letters come in three groups: owner, group, everyone else. Only the first group has w (write). The other two can read and run it."
---

## In one line

`chmod` changes who is allowed to read, change or run a file.

## The picture

Every sheet has three little locks: one for you, one for your household, one
for everyone else. Each lock can allow reading, writing or "carrying out as
orders". The locksmith resets those locks. A sheet of instructions can't be
handed to a clerk as orders until its "run" lock is opened.

## What really happens

`chmod` sets permission bits for user, group and others: `r` read, `w` write,
`x` execute. Use letters (`u+x`, `go-w`) or octal numbers, where 4 is read,
2 is write and 1 is execute: `755` is `rwxr-xr-x` and `600` is `rw-------`.
`-R` applies the change to a whole directory tree.

## Try it

```console
$ ls -l tidy.sh
-rw-r--r-- 1 you you 20 Oct 19 09:30 tidy.sh
$ chmod +x tidy.sh
$ ./tidy.sh
tidy
$ chmod 600 notes.txt
$ ls -l notes.txt
-rw------- 1 you you 44 Oct 19 09:30 notes.txt
```

## Margin notes

| Write            | It means                                        |
|------------------|-------------------------------------------------|
| `chmod +x a`     | Let sheet a be carried out as orders            |
| `chmod 600 a`    | Only I may read and write it; nobody else may look |
| `chmod 755 a`    | I may do anything; others may read and run      |
| `chmod -R ...`   | Change the locks on a whole drawer and its contents |

## When an agent asks

Agents often run `chmod +x` on a script they just wrote so they can run it.
That's normal. Be wary of `chmod 777` or `chmod -R` on big drawers: they
throw locks open for everyone.

## Careful

- `777` means anyone may change the sheet. It is almost never the right fix.
- `chmod -R` on your home drawer can break keys that must stay private, like `~/.ssh`.
