---
command: less
title: The Page Turner
chapter: 2
order: 6
risk: low
metaphor: >
  A long bone page turner that lets you leaf through a long sheet one page at a time, forwards or back, without ever marking it.
related: [cat, head, tail]
sketch: >
  A thick book lying open on a small writing table, one page half lifted by a long, slender bone page turner slipped beneath it, its handle resting on the table.
exercise:
  question: "Hobbs runs less notes.txt and then sits waiting, doing nothing. Why?"
  choices:
    - "The sheet is broken and less cannot finish reading it"
    - "less is waiting for a key: space to turn the page, q to close"
    - "less is quietly copying the sheet somewhere else"
  answer: 1
  explanation: "less stays open until someone presses q. That is fine for you at the desk, but a clerk who cannot press keys will wait forever."
---

## In one line

`less` shows a long file one screenful at a time, so you can read it at your own pace.

## The picture

The sheet is far too long to read in one glance. You take the bone page
turner and leaf through it: one page forward, one page back, a quick search
for a word. You set the pace, not the clerk. When you have finished, you close
it, and the sheet is exactly as it was.

## What really happens

`less` is a pager, a program that shows text one screen at a time and waits
for your keys. Space moves down a page and `b` moves back up. `/word` searches
forward, `n` jumps to the next match, `G` goes to the end and `q` quits. It
never changes the file. Tools like `git log`, `git diff` and `man` open it for
you when their answer is longer than the screen.

## Try it

```console
$ less notes.txt
buy flour
call grandma
pay the bank
buy ink
notes.txt (END)
```

Press `q` to close it and return to the desk.

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `less -N sheet`    | Number every line down the side                  |
| `less -S sheet`    | Cut long lines at the edge instead of wrapping   |
| `/word`, then `n`  | Find a word, then the next one                   |
| `q`                | Close the sheet                                  |
| `less +F sheet`    | Stay at the end and show new lines, like `tail -f` |

## When an agent asks

An agent rarely needs `less`. It waits for someone to press keys, and an
agent has no fingers, so the command just sits there until it is stopped. If
an agent asks for it, it probably wanted `cat`, `head` or `sed -n`.
When `git log` or `git diff` stalls in the same way, the fix is
`git --no-pager log` or adding `| cat`. It only reads, so it is safe to accept.

## Careful

- Inside `less`, `v` opens the sheet in an editor and `!` runs another command. Only plain keys like space, `b`, `/` and `q` are pure reading.
