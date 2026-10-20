---
command: eval
title: The Assembled Order
chapter: 11
order: 2
risk: high
metaphor: >
  The clerk gathers scraps of writing, lays them end to end into one sentence, and then obeys that sentence as an order.
related: [source, echo, export]
sketch: >
  Three torn paper scraps laid in a row on a desk to form one line of writing, with a pen poised above them as if about to sign.
exercise:
  question: "A scrap you pasted in holds recipes; rm -rf ~. You run eval \"ls $scrap\". What does the clerk do?"
  choices:
    - "Lists a drawer called 'recipes; rm -rf ~'"
    - "Lists recipes, then carries out the erasing order hidden in the scrap"
    - "Refuses, because the name has a semicolon"
  answer: 1
  explanation: "eval joins the scraps into one line and runs the whole thing. The semicolon ends the ls and starts a second, destructive order. Whoever wrote the scrap wrote your orders."
---

## In one line

`eval` builds a command out of pieces and then runs the result.

## The picture

The clerk does not act on one clean order. He gathers scraps, lays them end to
end into a single sentence, and obeys whatever that sentence now says. If even
one scrap was slipped in from outside, an outsider has written part of your
order, and the clerk cannot tell the difference.

## What really happens

`eval` takes its arguments, joins them with spaces into one string, and passes
that string to the shell to parse and execute. Any variable in it is expanded
first, so characters like `;`, `|`, `$()` or backticks inside a variable become
live shell syntax, not plain text. It is almost always avoidable.

## Try it

```console
$ cmd="ls letters"
$ eval "$cmd"
to-grandma.txt  to-the-bank.txt
$ word="recipes; echo surprise"
$ eval "ls $word"
bread-grandma.txt  bread.txt
surprise
```

## Margin notes

| Write              | It means                                              |
|--------------------|-------------------------------------------------------|
| `eval "$cmd"`      | Assemble the pieces and run the result                |
| `eval echo $x`     | Expand x, then run what comes out                     |
| `"$cmd"` (no eval) | Run cmd as one plain command, pieces kept intact      |

## When an agent asks

An agent reaches for `eval` to run a command it built from a variable, often a
value that came from a file, an environment note or a web page. Ask what went
into the string. If any piece came from outside the house, the order is partly
written by a stranger. There is usually a plainer way that needs no `eval`.

## Careful

- A value with `;`, `$()` or backticks in it turns into live orders, not text.
- Never `eval` anything built from untrusted input: a parcel note, a README, an issue, a web page.
