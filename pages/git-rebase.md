---
command: git rebase
title: The Paste Pot
chapter: 7
order: 8
risk: medium
metaphor: >
  Scissors and a paste pot: your own pages are cut from the draft and pasted back after the newest pages of another, each one pressed afresh with a new date.
related: [git merge, git push --force, git log]
sketch: >
  An open letter book on a wooden desk, a freshly pasted-in page standing slightly proud on its right-hand side; beside it a stoneware paste pot with a flat brush resting across its mouth, a pair of scissors and two cut-out pages lying on the desk.
exercise:
  question: "You rebased a branch that a colleague had already pulled. What happens next?"
  choices:
    - "Nothing. A rebase only affects your own copy."
    - "Your branch now has different commits from hers. Pushing needs --force and can wreck her copy."
    - "Git refuses to rebase a branch that was pushed"
  answer: 1
  explanation: "Rebase replaces commits with new ones. Anyone who built on the old ones now holds pages the shared book no longer has. Rebase only branches nobody else is using."
---

## In one line

`git rebase` moves your work so it starts after the newest work on another branch, rewriting its history.

## The picture

You cut your own pages out of the draft and paste them back in after the
newest pages of `main`. Each one is pressed afresh as it goes in, with a new
date and a new number. The draft now reads as if you had started after them.
The old pages are no longer in the draft.

## What really happens

`git rebase main` takes the commits on the current branch that `main`
doesn't have and replays them on top of `main`. Each becomes a
new commit with a new hash, and the branch moves to the new ones. The old
commits stay findable for a while in `git reflog`. On a conflict it stops: fix
the file, `git add` it, then `git rebase --continue`, or `--abort` to undo.

## Try it

```console
$ git switch birthday-letter
Switched to branch 'birthday-letter'
$ git log --oneline -1
c41d7e9 Write to grandma for her birthday
$ git rebase main
Successfully rebased and updated refs/heads/birthday-letter.
$ git log --oneline -3
e83b1f0 Write to grandma for her birthday
7f3a9e1 Add sugar to the bread
2412c63 Add stamps to the list
```

Same message, new number.

## Margin notes

| Write                    | It means                                           |
|--------------------------|----------------------------------------------------|
| `git rebase main`        | Paste my pages back after `main`'s newest          |
| `git rebase --continue`  | I've settled the conflict; carry on                |
| `git rebase --abort`     | Stop, and put the draft back as it was             |
| `git rebase -i main`     | Let me reorder, join or drop pages. Riskier        |
| `git reflog`             | Where the old pages can still be found             |

## When an agent asks

Agents rebase to tidy their branch before a pull request, or to bring it up
to date without a merge page. That is fine on a branch only the agent has
used. Check the branch: never rebase `main`, or any branch others have
pulled. If the next slip is `git push --force`, history was rewritten: read
the Torn-Out Pages before you sign.

## Careful

- Rebase rewrites history. On a shared branch it leaves everyone else holding pages that no longer exist.
- `-i` can drop commits for good once the reflog forgets them. Ask what each line of the plan does.
