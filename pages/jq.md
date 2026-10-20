---
command: jq
title: The Cut-Out Card
chapter: 2
order: 7
risk: low
metaphor: >
  A stiff card with windows cut in it, laid over a printed form so that only the boxes you asked for show through.
related: [cat, grep, "|", curl]
sketch: >
  A sloping wooden writing box standing on the floor; on its lid lies a printed form ruled into boxes, half covered by a cross-hatched card with two windows cut out, the form's handwriting showing through them.
exercise:
  question: "What does jq '.items[0].name' order.json read back?"
  choices:
    - "The first line of the sheet"
    - "\"flour\", the name in the first box of the items list"
    - "Every name in the list"
  answer: 1
  explanation: "jq counts boxes, not lines, and lists start at 0. .items[].name, with empty brackets, would read every name."
---

## In one line

`jq` picks out and reshapes pieces of a JSON file, the format most programs use to exchange data.

## The picture

Some sheets are not written in lines but laid out like a printed form: boxes
with labels, and lists of boxes inside boxes. You lay a cut-out card over the
form. Its windows show only the boxes you named, and the clerk reads you just
those. The form underneath is never touched.

## What really happens

`jq` reads JSON (JavaScript Object Notation, labelled values in braces and
lists in square brackets) and applies a filter to it. `.to` takes the value
labelled `to`, `.items[0]` the first entry of a list, and `.items[]` every
entry in turn. Filters are chained with `|`, and `-r` prints plain text
without quotes. It writes to standard output and never changes the file.

## Try it

`order.json` is the grocer's order in the example drawer.

```console
$ jq '.items[0]' order.json
{
  "name": "flour",
  "qty": 2
}
$ jq -r '.items[].name' order.json
flour
yeast
ink
$ jq '.items | length' order.json
3
```

## Margin notes

| Write                        | It means                                      |
|------------------------------|-----------------------------------------------|
| `jq . sheet`                 | Read the whole form back, neatly laid out     |
| `jq '.to'`                   | Only the box labelled `to`                    |
| `jq -r '.items[].name'`      | Every name in the list, as plain words        |
| `jq '.items[] \| select(.qty > 1)'` | Keep only the entries that pass the test |
| `jq -c`                      | Each answer on one compact line               |

## When an agent asks

Agents reach for `jq` to pull one value out of a long answer, often poured
through the funnel from `curl` or `gh`, or to read settings from
`package.json`. It only reads. Check where the JSON comes from: a sheet from the post is a paper from
outside the house. And watch for `env` or `$ENV` in the filter: they read out
every note on the pinboard, keys included.

## Careful

- `jq ... order.json > order.json` empties the sheet before jq can read it. Write to a new name, then `mv` it back.
