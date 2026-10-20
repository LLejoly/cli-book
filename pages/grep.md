---
command: grep
title: The Sieve
chapter: 1
order: 9
risk: low
metaphor: >
  A kitchen sieve that lets every line through and keeps only the ones containing your word.
related: [cat, "|", ls]
sketch: >
  A fine kitchen sieve resting over an earthenware bowl, a few short strips of paper caught in its mesh and the rest fallen below.
exercise:
  question: "What does grep -v buy notes.txt show?"
  choices:
    - "Only the lines with buy"
    - "Every line without buy"
    - "How many times buy appears"
  answer: 1
  explanation: "-v turns the sieve around: it keeps every line that does not contain the word. -c would count instead."
---

## In one line

`grep` finds the lines in a file that contain a word.

## The picture

You pour a sheet, line by line, through a sieve. Lines with your word stay in
the mesh and are shown to you. All the others fall through and are ignored.
The sheet itself is never changed. You just see what the sieve kept.

## What really happens

`grep` searches each input line for a pattern, a plain word or a regular
expression, and prints the lines that match. It reads files you name, or
standard input when you name none. It exits with status 0 if anything matched
and 1 if nothing did, which scripts use to make decisions.

## Try it

```console
$ grep buy notes.txt
buy flour
buy ink
$ grep -n bank notes.txt
3:pay the bank
$ grep -r grandma .
./notes.txt:call grandma
```

## Margin notes

| Write              | It means                                    |
|--------------------|---------------------------------------------|
| `grep -i word`     | Ignore capital letters                      |
| `grep -v word`     | Keep the lines without the word             |
| `grep -n word`     | Show the line number of each catch          |
| `grep -r word .`   | Sieve every sheet in every drawer below here |
| `grep -c word`     | Just count the lines that are caught        |

## When an agent asks

Agents use `grep` constantly to find where something is mentioned before
changing it. It only reads, so it is safe to accept. With `-r` on a large
drawer it can take a while and show the agent a lot of your files.

## Careful

- Some characters, like `.`, `*` and `[`, have special meanings in a pattern. Search for them with `grep -F`.
