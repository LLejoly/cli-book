---
command: git fetch
title: The Silver Salver
chapter: 7
order: 6
risk: low
metaphor: >
  The silver salver on the hall table where the morning post is laid, still sealed, until you decide to bind it into your book.
related: [git pull, git merge, git log]
sketch: >
  A round silver salver with a raised rim standing on a small wooden hall table, three sealed envelopes lying on it and a brass letter opener resting beside it, unused.
exercise:
  question: "Hobbs has just run git fetch. What has changed in your drawer?"
  choices:
    - "Every sheet now matches the other house"
    - "Nothing yet. The news waits in origin/main until you merge or pull it."
    - "Your unsaved changes were replaced by theirs"
  answer: 1
  explanation: "fetch only brings the post into the hall. Your sheets and your own drafts stay exactly as they were until you merge, rebase or pull."
---

## In one line

`git fetch` downloads what others have shared, without changing any of your files.

## The picture

The post arrives and is laid on the silver salver in the hall. Nothing is
opened and nothing is bound into your book. You can look at the envelopes,
see who wrote and what about, and decide later whether to bind them in.

## What really happens

`git fetch` downloads new commits and branches from a remote (by default
`origin`) and updates the remote-tracking branches, such as `origin/main`,
that record where the other house's drafts stand. Your own branches, the
index and the working tree are not touched. `git pull` is a fetch followed by
a merge or rebase; fetching alone lets you look first.

## Try it

```console
$ git fetch
From github.com:you/study
   2412c63..7f3a9e1  main       -> origin/main
$ git log --oneline main..origin/main
7f3a9e1 Add sugar to the bread
```

## Margin notes

| Write                          | It means                                          |
|--------------------------------|---------------------------------------------------|
| `git fetch`                    | Bring in the post, leave it sealed on the salver  |
| `git fetch --prune`            | Also forget drafts the other house has removed    |
| `git log main..origin/main`    | Show the letters I haven't bound in yet           |
| `git merge origin/main`        | Now bind them into my book                        |

## When an agent asks

Agents fetch to see whether the shared book has moved before they compare,
rebase or push. It is safe to accept: your sheets don't change. Check the
address if it isn't your usual `origin`. Pages fetched from a stranger's house
are paper from outside: read them, don't run them.

## Careful

- After a fetch, `git status` may say your branch is "behind". Your sheets haven't changed yet: the post is still on the salver.
