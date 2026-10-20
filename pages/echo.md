---
command: echo
title: The Parrot
chapter: 3
order: 1
risk: low
metaphor: >
  The study's parrot, which repeats back exactly what you tell it, after filling in any notes from the pinboard.
related: [">", export, cat]
sketch: >
  An African grey parrot on a brass perch stand beside the writing desk, beak slightly open, a small seed cup hanging from the perch.
exercise:
  question: "You type echo \"My drawer is $HOME\". What does the parrot say?"
  choices:
    - "My drawer is $HOME"
    - "My drawer is /home/you"
    - "Nothing, $HOME is not a word"
  answer: 1
  explanation: "Inside double quotes, $HOME is replaced by the note pinned under that name before the parrot speaks. In single quotes it would say $HOME as written."
---

## In one line

`echo` prints back the text you give it.

## The picture

The parrot by the desk repeats whatever you say. If your sentence mentions a
note from the pinboard, like `$HOME`, the parrot reads the note first and says
what's written on it instead. On its own it changes nothing in the Study.

## What really happens

`echo` writes its arguments to standard output, separated by spaces and
followed by a newline. The shell expands variables like `$HOME` and patterns
like `*` before `echo` runs. Its real power comes from combining it with `>`
or `>>` to write text into a file.

## Try it

```console
$ echo "Hello, Study"
Hello, Study
$ echo "My drawer is $HOME"
My drawer is /home/you
```

## Margin notes

| Write             | It means                                     |
|-------------------|----------------------------------------------|
| `echo text`       | Say this back to me                          |
| `echo $NAME`      | Say what is pinned on the board under NAME   |
| `echo -n text`    | Say it without starting a new line           |
| `echo text > a`   | Write it onto sheet a instead (see `>`)      |

## When an agent asks

`echo` alone is harmless. Look at what follows it: `> file` writes over a
sheet, and `echo $SECRET` can print a password into the conversation.

## Careful

- `echo $API_KEY` shows your secret to anyone who can see the screen or the agent's log.
