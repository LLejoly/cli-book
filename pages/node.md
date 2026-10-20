---
command: node
title: The Phrase Book
chapter: 9
order: 8
risk: medium
metaphor: >
  A clerk with a pocket phrase book for the JavaScript language, who reads orders written in it and carries out every line, whatever it says.
related: [npm run, npm install, python]
sketch: >
  A small cloth-bound pocket phrase book lying open on a round tripod side table, a folded sheet of orders peeking out from under it and a pair of folded spectacles beside it.
exercise:
  question: "Hobbs wants to run node -e with a long line full of require(\"child_process\"). What should you do?"
  choices:
    - "Sign it; -e only evaluates, it cannot change anything"
    - "Ask him what the line does, and read it: child_process lets JavaScript start any other command"
    - "Sign it, but only if it fits on one line"
  answer: 1
  explanation: "A one-line order can do as much as a whole sheet. child_process lets node hand slips to other clerks, including rm and curl, so the line deserves the same reading as a script."
---

## In one line

`node` runs a program written in JavaScript, outside a web browser.

## The picture

This clerk carries a phrase book for JavaScript. Hand him a sheet of orders in
that language and he carries out every line, in order: reading sheets, writing
them, posting letters, starting other clerks. Like the translator who reads
Python, he does not judge the orders. That is your job.

## What really happens

`node file.js` starts the Node.js runtime, which runs the script with your
user's permissions, including access to files, the network and other programs.
`-e 'code'` runs a short snippet, and `-p 'code'` runs it and prints the
result. `--check` only tests the script's grammar without running it. With no
arguments it opens an interactive prompt.

## Try it

```console
$ node count.js
4 things to do
$ node -p '2 + 2'
4
```

## Margin notes

| Write                  | It means                                         |
|------------------------|--------------------------------------------------|
| `node sheet.js`        | Carry out the orders on this sheet               |
| `node -e '...'`        | Carry out this one short order                   |
| `node -p '...'`        | Carry it out and read me the answer              |
| `node --check sheet.js`| Read the sheet for mistakes, but do nothing      |

## When an agent asks

Agents run `node` to try a script they just wrote, to start a project's server,
or to test a quick idea with `-e`. For a sheet the agent showed you, it is
routine. For a sheet that came from outside the house, or a long `-e` line,
read it first, and look for `child_process`, `fs` or addresses of other houses.

## Careful

- A one-line `node -e` can erase or post things just like a long script.
- A server started with `node` keeps running until you stop it.
