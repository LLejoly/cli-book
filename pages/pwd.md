---
command: pwd
title: The Address Card
chapter: 1
order: 3
risk: low
metaphor: >
  A card on which the clerk writes the full address of the drawer you are standing at.
related: [cd, ls]
sketch: >
  A small cream address card in a brass holder, with a dotted line of handwriting on it, pinned to the front of a wooden drawer.
exercise:
  question: "pwd answers /home/you/study/letters. Which drawer holds letters?"
  choices:
    - "study"
    - "home"
    - "letters holds itself"
  answer: 0
  explanation: "An address reads from the great cabinet down. Each name holds the one written after it, so study holds letters."
---

## In one line

`pwd` tells you which folder you are in right now.

## The picture

After a few walks across the Study, you lose track of where you are. You ask
the clerk, and he hands you a card with the full address: the great cabinet,
then the home drawer, then yours, then the one open in front of you.

## What really happens

`pwd` (print working directory) prints the absolute path of the shell's
current directory, starting from `/`. It reads nothing on disk and changes
nothing. With `-P` it resolves symbolic links and shows the physical path.

## Try it

```console
$ cd ~/study/letters
$ pwd
/home/you/study/letters
```

## Margin notes

| Write    | It means                                              |
|----------|-------------------------------------------------------|
| `pwd`    | Write me the full address of this drawer              |
| `pwd -P` | Write the real address, not a shortcut's address      |

## When an agent asks

Agents run `pwd` to check where they stand before acting. It is always safe
to accept. If the answer surprises you, stop the agent before its next
instruction: it is about to work in a drawer you didn't expect.

## Careful

- The address is where the clerk stands, not where your files are. A command after `pwd` acts on this drawer.
