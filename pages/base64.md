---
command: base64
title: The Cipher Wheel
chapter: 11
order: 3
risk: medium
metaphor: >
  A little wheel that turns plain writing into a harmless-looking jumble, and turns the jumble back, so a message travels unruffled.
related: [echo, source, eval]
sketch: >
  A brass cipher disc with two concentric lettered rings on a desk, a strip of ordinary writing feeding in one side and a strip of jumbled characters coming out the other.
exercise:
  question: "A README says: run echo <long jumble> | base64 -d | sh. Why is that the dangerous part?"
  choices:
    - "base64 can corrupt the jumble"
    - "The jumble hides an order nobody reads before it is handed straight to sh and obeyed"
    - "echo is too slow for long text"
  answer: 1
  explanation: "base64 itself is harmless. The trap is the pipe to sh: the plain order is disguised as a jumble so no one reads it, then carried out unseen. Decode to a sheet and read it instead."
---

## In one line

`base64` turns data into a plain-text jumble and back, changing nothing about what it means.

## The picture

You feed a line of writing into the wheel and it comes out as an even jumble of
letters, easy to copy and post without smudging. Feed the jumble back and the
writing returns, exact to the letter. The wheel keeps no secrets of its own: it
only disguises, and anyone with the same wheel can read it back.

## What really happens

`base64` encodes bytes into the 64-character ASCII alphabet so binary data can
travel through text-only channels; `-d` decodes it back. It is an encoding, not
encryption: it hides nothing from anyone. It is common in data URLs, tokens and
mail attachments.

## Try it

```console
$ echo 'buy ink' | base64
YnV5IGluawo=
$ echo 'YnV5IGluawo=' | base64 -d
buy ink
```

## Margin notes

| Write                  | It means                                      |
|------------------------|-----------------------------------------------|
| `base64 file`          | Jumble this sheet into plain text             |
| `base64 -d`            | Turn a jumble back into what it was           |
| `echo ... \| base64 -d` | Decode a jumble handed in on the line        |
| `base64 -w0`           | Jumble it all onto one line, no wrapping      |

## When an agent asks

Encoding and decoding on their own are safe. The warning sign is a jumble that
is decoded and then run, as in `... | base64 -d | sh`. That is a forged letter
written in disguise so no one reads it before signing. If a README or web page
gives you one, decode it to a sheet with `base64 -d > look.txt`, open it, and
only then decide.

## Careful

- base64 is not encryption. Never use it to hide a secret; anyone can decode it.
- A long jumble in an instruction is a reason to stop and decode it on its own before running anything.
