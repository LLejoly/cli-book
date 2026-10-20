---
command: npm run
title: The Errand Book
chapter: 9
order: 6
risk: medium
metaphor: >
  A small book of named errands kept with the project's packing list: you call out a name, and the clerk carries out whatever orders are written under it.
related: [npm install, node, make]
sketch: >
  A small leather errand book lying open on top of an opened brown-paper parcel on the floor, its pages ruled into short entries that each begin with a heavy stroke, the paper flaps folded back and the loose string trailing down the front onto the floor.
exercise:
  question: "Hobbs asks to run npm test in a project he just cloned from a stranger's house. What do you know about what it will do?"
  choices:
    - "It runs the tests, so it only reads"
    - "Nothing yet. test is only a name; the orders under it are written in package.json, by whoever made the project"
    - "npm checks every errand before running it"
  answer: 1
  explanation: "npm run looks the name up and hands the line written there to a shell. The project's author chose that line. Plain npm run lists every errand with its orders, so you can read before you sign."
---

## In one line

`npm run` carries out a named task that a JavaScript project has written down for itself.

## The picture

The packing list, `package.json`, has a small errand book tucked behind it.
Each errand has a short name, like *test* or *build*, and a line of orders
under it. You call out the name, and the clerk carries out the line, whatever
it says. Whoever packed the parcel wrote the book, not you.

## What really happens

`npm run <name>` reads the `scripts` section of `package.json` and runs that
line in a shell, with `node_modules/.bin` added to the `PATH` so the project's
installed tools are found. If scripts called `pre<name>` or `post<name>` exist,
they run before and after it. With no name, `npm run` lists every script and
its command. Words after `--` are passed on to the script.

## Try it

```console
$ npm run
Lifecycle scripts included in study@1.0.0:
  test
    pytest -q
available via `npm run-script`:
  count
    grep -c buy notes.txt
$ npm run count

> study@1.0.0 count
> grep -c buy notes.txt

2
```

## Margin notes

| Write                  | It means                                          |
|------------------------|---------------------------------------------------|
| `npm run`              | Read me every errand and its orders               |
| `npm run build`        | Carry out the errand called build                 |
| `npm test`             | Short for `npm run test`                          |
| `npm run test -- -x`   | Pass `-x` on to the errand's own orders           |

## When an agent asks

Agents run `npm run build`, `npm run lint` or `npm test` after every change,
to see whether the project still works. In your own project that is routine.
In a project you just cloned or unpacked, the errand book came in the parcel:
run plain `npm run` first and read the lines, and look for a `pre` errand.

## Careful

- The name says nothing. An errand called `test` can post your keys to another house.
- A tool named in the errand is taken from `node_modules`, so a bad parcel installed there runs too.
