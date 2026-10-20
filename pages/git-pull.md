---
command: git pull
title: The Morning Post
chapter: 7
order: 2
risk: medium
metaphor: >
  The morning post bringing the pages others pressed into the shared book, which are then bound into your own copy.
related: [git push, git clone, git diff]
sketch: >
  A bundle of letters tied with string on a hall table beside a brass letter opener and an open letter book, early light falling across them.
exercise:
  question: "git pull stops with 'CONFLICT in notes.txt'. What does that mean?"
  choices:
    - "notes.txt was deleted"
    - "You and someone else changed the same lines, and the clerk won't guess which wins"
    - "The other house refused the post"
  answer: 1
  explanation: "When two people rewrite the same lines, git marks both versions in the sheet and waits for a person to decide."
---

## In one line

`git pull` brings in the changes others have shared and merges them into your copy.

## The picture

Every morning the post brings pages that others have pressed into the shared
book. Your clerk binds them into your copy, after your own. If someone else
rewrote the very lines you also changed, the clerk sets both versions side by
side and waits for you to choose.

## What really happens

`git pull` is `git fetch` followed by an integration step: a merge by
default, or a rebase with `--rebase`. It fast-forwards when you have no local
commits. If the same lines changed on both sides it stops with a conflict and
writes `<<<<<<<`, `=======` and `>>>>>>>` markers into the file.

## Try it

```console
$ git pull
Updating 2412c63..7f3a9e1
Fast-forward
 recipes/bread.txt | 1 +
 1 file changed, 1 insertion(+)
```

## Margin notes

| Write                | It means                                         |
|----------------------|--------------------------------------------------|
| `git pull`           | Bring in the post and bind it into my book       |
| `git pull --rebase`  | Bind theirs first, then re-press mine after      |
| `git fetch`          | Collect the post but don't bind it yet           |

## When an agent asks

Pulling before starting work is a good habit. If it ends in a conflict, the
agent has to choose between two people's lines, so ask it what it chose
and why.

## Careful

- With unsaved changes in the drawer, a pull may refuse to start. Commit or set them aside first.
