---
command: git restore
title: The Fresh Sheet
chapter: 7
order: 9
risk: high
metaphor: >
  A fresh sheet written out from the last pressed copy and laid in the drawer in place of the one you scribbled on, which goes into the stove.
related: [git reset, git diff, git status]
sketch: >
  An open letter book lying on a wooden desk with a clean sheet laid across its right-hand page, and beside the book a crumpled ball of paper.
exercise:
  question: "You spent an hour editing notes.txt, without committing. Hobbs proposes git restore notes.txt. What happens to that hour?"
  choices:
    - "It is kept in the wastebasket, in case you change your mind"
    - "It is gone. The sheet goes back to what the book holds."
    - "It is pressed into the book first, then the sheet is restored"
  answer: 1
  explanation: "Edits that were never committed or stashed have no copy anywhere. restore overwrites them with the version from the book, and git cannot undo it."
---

## In one line

`git restore` puts a file back to its last saved version, throwing away your unsaved edits to it.

## The picture

You have scribbled all over a sheet and want the old one back. You open the
letter book at the last pressed copy, write out a fresh sheet from it, and
lay it in the drawer where the scribbled one was. The scribbled sheet goes
into the stove. Only that sheet changes; the rest of the desk is left alone.

## What really happens

`git restore file` overwrites the file in the working tree with its version
in the index, which is the last commit unless you have staged something.
`--staged` does something else: it takes the file out of the index and
leaves your edits alone, which is safe. `--source=` restores from any commit.
Untracked files are not touched. It is the clearer, newer form of
`git checkout -- file`.

## Try it

```console
$ git diff --stat
 notes.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git restore notes.txt
$ git status --short
?? letters/to-aunt.txt
```

## Margin notes

| Write                            | It means                                        |
|----------------------------------|-------------------------------------------------|
| `git restore a`                  | Put sheet a back as the book has it. Edits lost |
| `git restore --staged a`         | Take sheet a out of the tray; keep my edits     |
| `git restore .`                  | Put back every sheet in this drawer and below   |
| `git restore --source=HEAD~1 a`  | Bring back sheet a as it was one copy earlier   |

## When an agent asks

Agents use `restore` to undo their own edits after a wrong turn, or to take
a file out of the tray. Before accepting, run `git diff` on the same file:
if any of those lines are yours, they will be lost. `--staged` alone is safe.
`git restore .` is as sweeping as `git reset --hard`. If in doubt, suggest
`git stash`, which sets the edits aside instead.

## Careful

- There is no wastebasket. Edits never committed or stashed cannot be brought back by git.
- `git restore a` and `git restore --staged a` look alike but differ in danger. Read the slip twice.
