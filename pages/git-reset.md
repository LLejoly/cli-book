---
command: git reset
title: The Ink Eradicator
chapter: 7
order: 5
risk: high
metaphor: >
  A bottle of ink eradicator that wipes the writing on your desk back to how the last pressed copy looked.
related: [git status, git diff, rm]
sketch: >
  A small two-bottle ink eradicator set in a tin case with a glass rod, beside a sheet whose last lines are fading away.
exercise:
  question: "You edited notes.txt but didn't commit, then ran git reset --hard. Can you get your edits back?"
  choices:
    - "Yes, from the wastebasket"
    - "No. They were never pressed into the book, so there is no copy to return to."
    - "Yes, with git log"
  answer: 1
  explanation: "--hard wipes the drawer back to the last pressed copy. Changes that were never committed are gone."
---

## In one line

`git reset --hard` throws away every change you haven't saved and returns the files to the last saved version.

## The picture

You dab ink eradicator on every sheet on your desk, and the writing vanishes
back to what the last pressed copy shows. Anything you wrote since that copy
is gone. Pressed copies in the book are safe; unpressed work is not.

## What really happens

`git reset` moves the current branch to another commit. `--soft` keeps your
changes staged, the default `--mixed` keeps them in the working tree, and
`--hard` overwrites the index and working tree to match the commit exactly.
Untracked files are left alone; `git clean -fd` removes those.

## Try it

```console
$ git diff --stat
 notes.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git reset --hard
HEAD is now at 244d512 Start my study
$ tail -n 1 notes.txt
buy ink
```

## Margin notes

| Write                 | It means                                          |
|-----------------------|---------------------------------------------------|
| `git reset --hard`    | Wipe my desk back to the last pressed copy        |
| `git reset --soft HEAD~1` | Unpress the last copy, keep the sheets in the tray |
| `git restore a`       | Wipe only sheet a back                            |
| `git stash`           | Put my unsaved changes aside instead of wiping them |

## When an agent asks

This is a red seal. An agent may use it to "start clean" after a mistake.
Before agreeing, check `git status`: anything not committed will be lost.
Suggest `git stash` instead, which sets the changes aside safely.

## Careful

- `git reset --hard origin/main` also discards commits you never pushed.
- `git clean -fd` after it erases new sheets too. Together they wipe a desk completely.
