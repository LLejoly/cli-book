---
command: ln
title: The Forwarding Card
chapter: 8
order: 2
risk: medium
metaphor: >
  A card left in one drawer that says "this sheet is kept in drawer X", so anyone looking here is sent there.
related: [ls, cp, rm]
sketch: >
  A small printed card with a pointing hand and a ruled line of handwriting, propped in an otherwise empty drawer.
exercise:
  question: "bread is a forwarding card to recipes/bread.txt. You erase recipes/bread.txt. What happens to bread?"
  choices:
    - "It keeps the recipe"
    - "The card stays but now points to nothing"
    - "It is erased too"
  answer: 1
  explanation: "A symbolic link only holds directions. When the real sheet is gone, the card is left pointing at an empty place."
---

## In one line

`ln -s` creates a shortcut: a name in one place that leads to a file kept somewhere else.

## The picture

Rather than copying a sheet, you leave a forwarding card in another drawer:
"the bread recipe is kept in the recipes drawer". Anyone who opens the card is
sent straight to the real sheet. There is still only one sheet, so a change to
it is seen from both places.

## What really happens

`ln -s target name` creates a symbolic link, a small file that stores a path.
Most commands follow it transparently. Without `-s`, `ln` makes a hard link:
a second name for the same data on disk. `ls -l` shows links as
`name -> target`. Removing a link with `rm` doesn't touch the target.

## Try it

```console
$ ln -s recipes/bread.txt bread
$ ls -l bread
lrwxrwxrwx 1 you you 17 Oct 19 09:30 bread -> recipes/bread.txt
$ head -n 1 bread
500g flour
```

## Margin notes

| Write             | It means                                         |
|-------------------|--------------------------------------------------|
| `ln -s a b`       | Leave card b pointing to sheet a                 |
| `ln -sf a b`      | Replace card b if it's already there             |
| `ln a b`          | Give the same sheet a second name                |
| `readlink b`      | Read me where card b points                      |

## When an agent asks

Agents use links to make a tool or config file appear where a program expects
it. Check the direction: `ln -s target name`. With `-f`, an existing file
called `name` is replaced.

## Careful

- `ln -sf` over a real sheet replaces that sheet with a card. Its contents are lost.
