---
command: git switch
title: The Folio Tabs
chapter: 7
order: 4
risk: medium
metaphor: >
  Coloured tabs marking separate drafts in the letter book, so you can turn to another draft and lay its sheets on the desk.
related: [git status, git commit, git reset]
sketch: >
  The fore-edge of a thick letter book with several coloured cloth tabs sticking out at different heights, one tab pulled so the book falls open there.
exercise:
  question: "What does git switch -c birthday-letter do?"
  choices:
    - "Deletes the birthday-letter draft"
    - "Starts a new draft called birthday-letter from where you are, and turns to it"
    - "Sends the draft to another house"
  answer: 1
  explanation: "-c means create. The new draft begins as a copy of the current one, and you can work on it without touching main."
---

## In one line

`git switch` moves you to another branch: a separate line of work in the same project.

## The picture

The letter book can hold several drafts at once, each marked with its own
tab. Turning to another tab lays that draft's sheets on your desk in place
of the current ones. The other draft is safe in the book, unchanged,
waiting for you to come back.

## What really happens

`git switch` changes `HEAD` to another branch and updates the working tree to
match. `-c name` creates the branch first. If you have uncommitted changes
that would be overwritten, it refuses. The older `git checkout name` does the
same, but `checkout` also restores files, so it's easier to misuse.

## Try it

```console
$ git switch -c birthday-letter
Switched to a new branch 'birthday-letter'
$ git branch
* birthday-letter
  main
```

## Margin notes

| Write                  | It means                                      |
|------------------------|-----------------------------------------------|
| `git switch name`      | Turn to the draft with that tab               |
| `git switch -c name`   | Start a new draft here and turn to it         |
| `git branch`           | List every tab; * marks the open one          |
| `git switch -`         | Go back to the draft I was on before          |

## When an agent asks

Agents usually make their own branch so their work stays apart from `main`
until you approve it. That's good practice. Watch for `git checkout -- .`,
which isn't switching at all: it throws away your unsaved changes.

## Careful

- `git checkout -- file` restores a sheet from the book and erases your unsaved edits to it.
