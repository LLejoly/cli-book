---
command: git stash
title: The Bill Spike
chapter: 5
order: 7
risk: medium
metaphor: >
  A bill spike on the desk where you push your half-finished sheets to clear the desk, newest on top, to take back off later.
related: [git status, git reset, git switch, git restore]
sketch: >
  A tall bill spike on a round weighted base standing on the floor, a small stack of loose sheets pushed down onto it and resting on the base, the top sheet slightly askew.
exercise:
  question: "You run git stash with a changed notes.txt and a brand-new letters/to-aunt.txt. What is left on the desk?"
  choices:
    - "Nothing, both went on the spike"
    - "Only to-aunt.txt, because the letter book has never seen it"
    - "Only notes.txt"
  answer: 1
  explanation: "A plain stash takes only changes to sheets the book already knows. A brand-new sheet stays where it is unless you add -u."
---

## In one line

`git stash` puts your unsaved changes aside so you can work on something else, and brings them back later.

## The picture

You are halfway through a letter when something urgent arrives. You push the
half-finished sheets onto the bill spike, and the desk is clean again. Later
you lift the top bundle off the spike and lay it back where it was. Several
bundles can wait on the spike, the newest always on top.

## What really happens

`git stash` (short for `git stash push`) saves the staged and unstaged changes
to tracked files as a stash entry, then resets the working tree to `HEAD`.
Untracked files stay unless you pass `-u`. `git stash pop` reapplies the
newest entry and drops it. `git stash list` shows entries as `stash@{0}`,
`stash@{1}` and so on.

## Try it

```console
$ git status --short
 M notes.txt
?? letters/to-aunt.txt
$ git stash
Saved working directory and index state WIP on main: 2412c63 Add stamps to the list
$ git status --short
?? letters/to-aunt.txt
$ git stash list
stash@{0}: WIP on main: 2412c63 Add stamps to the list
$ git stash pop -q
$ git status --short
 M notes.txt
?? letters/to-aunt.txt
```

## Margin notes

| Write                   | It means                                      |
|-------------------------|-----------------------------------------------|
| `git stash`             | Push my unsaved changes onto the spike        |
| `git stash -u`          | New sheets too, not only known ones           |
| `git stash pop`         | Take the top bundle back and lay it out       |
| `git stash list`        | Count the bundles waiting on the spike        |
| `git stash drop` / `clear` | Throw one bundle away / every bundle. No undo |

## When an agent asks

Agents stash to get a clean desk before switching branch, pulling, or testing
whether a problem was already there. It is a gentle step, and much safer than
`git reset --hard`. Check the agent pops the stash afterwards, so your work
doesn't sit forgotten on the spike. Refuse `drop` or `clear` unless you know
what is on it.

## Careful

- `pop` can clash with changes made since, leaving conflict marks. The entry is then kept on the spike.
- `git stash clear` throws away every bundle, with no easy way back.
