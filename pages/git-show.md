---
command: git show
title: The Reading Glass
chapter: 5
order: 6
risk: low
metaphor: >
  A reading glass held over one pressed copy in the letter book, so you can read that single page in full and see what changed on it.
related: [git log, git diff, git commit]
sketch: >
  A thick letter-copy book lying open on the floor, a round reading glass with a turned wooden handle resting across the right-hand page, its lens enlarging the ruled lines beneath it.
exercise:
  question: "You want to read notes.txt exactly as it was in the first copy, 244d512. Which slip does that?"
  choices:
    - "git show 244d512"
    - "git show 244d512:notes.txt"
    - "git log notes.txt"
  answer: 1
  explanation: "git show 244d512 shows that copy's note and its changes. Adding :notes.txt reads the whole sheet as it was pressed then, without touching today's sheet."
---

## In one line

`git show` displays one saved version: its message and exactly what it changed.

## The picture

The letter book lies open in front of you. Instead of leafing through every
page, you hold the reading glass over a single pressed copy. You read who
signed it, when, the note written beneath, and every line that was added or
crossed out. Lifting the glass leaves the book as it was.

## What really happens

`git show` prints a commit's hash, author, date and message, followed by its
diff against its parent. With no argument it shows `HEAD`, the latest commit.
`git show <commit>:<path>` prints a file's whole content as it was in that
commit. `--stat` replaces the diff with a per-file summary. Like `git log`, it
opens in a pager for long output.

## Try it

```console
$ git show --oneline
2412c63 Add stamps to the list
diff --git a/notes.txt b/notes.txt
index 7cd3208..3966100 100644
--- a/notes.txt
+++ b/notes.txt
@@ -2,3 +2,4 @@ buy flour
 call grandma
 pay the bank
 buy ink
+buy stamps
$ git show 244d512:notes.txt
buy flour
call grandma
pay the bank
buy ink
```

## Margin notes

| Write                   | It means                                     |
|-------------------------|----------------------------------------------|
| `git show`              | Read the latest copy and what it changed     |
| `git show 244d512`      | Read that particular copy                    |
| `git show --stat`       | Only which sheets changed, and how much      |
| `git show HEAD~1:a.txt` | Sheet a.txt as it was one copy ago           |

## When an agent asks

Agents use `git show` to read one commit closely, for example to understand a
change before building on it or to recover an old version of a sheet. It only
reads and is safe to accept. Watch for `git show ... > file`: then the clerk
writes his answer over a sheet, which is a different slip.

## Careful

- If the screen seems frozen, the copy is open in a pager. Press `q` to close it.
