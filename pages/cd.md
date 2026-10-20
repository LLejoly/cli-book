---
command: cd
title: The Drawer Handle
chapter: 1
order: 2
risk: low
metaphor: >
  Walking over to another drawer and opening it, so it becomes the one in front of you.
related: [ls, pwd]
sketch: >
  A tall wooden cabinet of many drawers, one drawer pulled open, with a dotted line of footsteps on the floorboards leading to it.
exercise:
  question: "You are in ~/study/letters. Where does cd .. take you?"
  choices:
    - "To ~/study"
    - "To the great cabinet /"
    - "Nowhere, .. is not a real drawer"
  answer: 0
  explanation: ".. always means the drawer that holds the one you are in. Here that is ~/study."
---

## In one line

`cd` moves you into another folder.

## The picture

You close the drawer in front of you, walk across the Study, and open another
one. Nothing inside any drawer changes. Only your place in the room does.
Every instruction you write after that is carried out in the new drawer.

## What really happens

`cd` changes the shell's current working directory. It is built into the
shell, not a separate program. Paths can be absolute (starting at `/`) or
relative to where you are now. With no argument it returns to your home
directory. `cd -` jumps back to the previous directory.

## Try it

```console
$ cd ~/study/letters
$ ls
to-grandma.txt  to-the-bank.txt
$ cd ..
$ pwd
/home/you/study
```

## Margin notes

| Write    | It means                                     |
|----------|----------------------------------------------|
| `cd ..`  | Step back to the drawer holding this one     |
| `cd ~`   | Go back to your own drawer                   |
| `cd -`   | Go back to where you were just before        |
| `cd /`   | Go to the great cabinet that holds everything |

## When an agent asks

An agent uses `cd` to stand in the right place before working. It changes
nothing by itself. What matters is the **next** instruction: an `rm` after a
`cd` into the wrong drawer erases the wrong sheets. Check where it is going.

## Careful

- A path with spaces needs quotes: `cd "old letters"`.
