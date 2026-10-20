---
command: git push --force
title: The Torn-Out Pages
chapter: 10
order: 2
risk: high
metaphor: >
  Tearing pages out of the shared letter book in another house and pasting yours in their place, so whatever others pressed there is lost.
related: [git push, git pull, git reset]
sketch: >
  An open letter-copy book lying on the floor, the ragged stubs of torn-out pages showing along its gutter and a fresh sheet pasted over the right-hand page; a torn page with a jagged edge and a crumpled ball of paper lie on the floor beside it.
exercise:
  question: "Your push is refused because a colleague pressed new pages into the shared book. Hobbs proposes git push --force. What happens to your colleague's pages?"
  choices:
    - "They are kept, and yours are added after them"
    - "They are torn out of the shared book's branch"
    - "Git asks your colleague first"
  answer: 1
  explanation: "--force makes the shared branch match yours exactly. Pages that only the other house had are dropped from it, and nobody is asked. Pull their pages home first, or at least use --force-with-lease, which refuses when someone has pressed new pages since you last looked."
---

## In one line

`git push --force` replaces the shared copy of a project with yours, even if that throws away other people's work.

## The picture

The second letter book, kept in another house, refuses your post bag when
someone has pressed pages there that you haven't read. `--force` is a note in
the margin that says: tear out whatever is in the way and paste my pages in.
The house obeys. Your colleagues' pages are torn out, and nobody in that house
keeps them.

## What really happens

`git push --force` (`-f`) moves the remote branch to your local commit even
when that discards commits on it. Commits that were only on the remote branch
disappear from it; teammates may still have copies in their own clones, but
git doesn't warn them. `--force-with-lease` overwrites only if the remote
branch is still where your last fetch saw it.

## Try it

```console
$ git push
To github.com:you/study.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:you/study.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
$ git push --force-with-lease --dry-run
To github.com:you/study.git
 ! [rejected]        main -> main (stale info)
error: failed to push some refs to 'github.com:you/study.git'
$ git push --force --dry-run
To github.com:you/study.git
 + 5b8e0c4...9a1f3d2 main -> main (forced update)
```

## Margin notes

| Write                         | It means                                          |
|-------------------------------|---------------------------------------------------|
| `git push --force`            | Tear out whatever is in the way, paste in mine    |
| `git push -f`                 | The same, written short                           |
| `git push --force-with-lease` | Only if nobody has pressed new pages since I looked |
| `git push --dry-run`          | Tell me what would happen, change nothing         |
| `git pull`                    | Bring their pages home first                      |

## When an agent asks

Agents usually ask after rewriting their own copies, for example with
`git commit --amend`, when an ordinary push is refused. On a branch only the
agent works on, that is often fine. On `main`, or any branch others share,
refuse and ask for `git pull` instead. Check the branch name on the slip, and
prefer `--force-with-lease`.

## Careful

- The torn pages may survive in a colleague's own book, or nowhere at all. Git won't tell you which.
- `--force-with-lease` trusts your last look. If something fetched in the background since, it lets the push through without you having read their pages.
