---
command: git push
title: The Post Bag
chapter: 5
order: 5
risk: medium
metaphor: >
  The post bag that carries your newly pressed copies to the shared letter book kept in another house.
related: [git commit, git log, ssh]
sketch: >
  A canvas post bag with a leather strap and brass buckle, stencilled with a number, a bundle of letters tied with string peeking from its mouth.
exercise:
  question: "Your push is rejected with 'fetch first'. What does that mean?"
  choices:
    - "The other house's book has copies you don't have yet"
    - "Your password is wrong"
    - "Your copies are lost"
  answer: 0
  explanation: "Someone else pressed copies into the shared book. You need to bring theirs home (git pull) before your bag can be added."
---

## In one line

`git push` sends your saved versions to a shared copy of the project elsewhere.

## The picture

Your letter book sits in your study. A second one, shared with others, is kept
in another house. The post bag carries your newly pressed copies there and adds
them after the last page. If someone else added pages since you last
looked, the house sends your bag back until you've read theirs.

## What really happens

`git push` uploads commits from a local branch to a remote repository (often
`origin` on a host like GitHub) and moves the remote branch forward. It is
rejected if the remote has commits you don't have. `--force` overwrites the
remote branch anyway, discarding other people's commits there.

## Try it

```console
$ git push
To github.com:you/study.git
   244d512..2412c63  main -> main
```

## Margin notes

| Write                     | It means                                  |
|---------------------------|-------------------------------------------|
| `git push`                | Send my new copies to the shared book     |
| `git push -u origin new`  | Send a new branch and remember where it goes |
| `git pull`                | Bring home copies others added            |
| `git push --force`        | Replace the shared book's pages with mine |

## When an agent asks

Pushing makes your work visible to others, so it is a step to agree to
knowingly. Check the branch name. Refuse `--force` on a shared branch like
`main` unless you're sure: it can erase colleagues' work.

## Careful

- A pushed secret has left the house. Change the password, don't just delete the file.
- `--force-with-lease` is the safer cousin of `--force`.
