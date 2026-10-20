---
command: git merge
title: The Bookbinder's Needle
chapter: 7
order: 7
risk: medium
metaphor: >
  A bookbinder's needle and thread that sew the pages of one draft into another, with a new signed page recording where the two were joined.
related: [git pull, git switch, git rebase]
sketch: >
  An open letter book lying flat on a wooden desk, a curved bookbinder's needle with linen thread passing through the gutter where two bundles of pages meet, and a spool of thread standing beside the book.
exercise:
  question: "git merge stops with 'CONFLICT (content): Merge conflict in notes.txt'. What is the safest next step?"
  choices:
    - "Run git reset --hard to make the message go away"
    - "Open notes.txt, choose between the marked lines, then git add and git commit"
    - "Delete notes.txt and merge again"
  answer: 1
  explanation: "A conflict means both drafts changed the same lines. Git marks both versions and waits for a person. If you would rather stop, git merge --abort puts everything back as it was before the merge."
---

## In one line

`git merge` joins the work of another branch into the one you are on.

## The picture

Two drafts have grown in separate folios. The bookbinder's needle sews the
pages of one into the other, so both lines of work sit in the same book.
Where the drafts had gone their own ways, a new page is pressed and signed:
"these two were joined here". If both changed the same lines, the binder
stops and waits for you to choose.

## What really happens

`git merge name` brings that branch's commits into the current branch. If
the current branch hasn't moved since they split, git fast-forwards: it moves
the branch forward without a new commit. Otherwise it makes a merge commit
with two parents, opening an editor for its message unless you pass
`--no-edit`. On conflicting lines it stops, writes `<<<<<<<` and `>>>>>>>`
markers into the file and waits.

## Try it

```console
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
$ git merge --no-edit birthday-letter
Merge made by the 'ort' strategy.
 letters/to-grandma.txt | 2 ++
 1 file changed, 2 insertions(+)
$ git log --oneline --graph -4
*   3e6a0b5 Merge branch 'birthday-letter'
|\
| * c41d7e9 Write to grandma for her birthday
* | 7f3a9e1 Add sugar to the bread
|/
* 2412c63 Add stamps to the list
```

## Margin notes

| Write                        | It means                                         |
|------------------------------|--------------------------------------------------|
| `git merge name`             | Sew that draft into the one on my desk           |
| `git merge --no-edit name`   | Use the usual message for the joining page       |
| `git merge --abort`          | Stop, and put everything back as it was          |
| `git merge --ff-only name`   | Only if no joining page is needed; else refuse   |

## When an agent asks

Agents merge to bring `main`'s news into their own branch, or to finish a
piece of work. Check which branch you are on and which one is coming in:
merging into `main` changes the shared draft. If there was a conflict, ask
how each one was settled, because the agent chose between two people's lines.
Be wary of `-X ours` or `-X theirs`, which settle every conflict one way.

## Careful

- Commit or set aside unsaved changes first. A merge on a messy desk may refuse, or mix two kinds of mess.
- Once a merge is pushed, undo it with `git revert -m 1`, not with a reset.
