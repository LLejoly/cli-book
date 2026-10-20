---
command: npx
title: The Travelling Salesman
chapter: 11
order: 4
risk: high
metaphor: >
  A salesman at the door who fetches a tool from the catalogue that very minute and demonstrates it inside your study at once.
related: [npm install, source, eval]
sketch: >
  A salesman's open sample case on the doorstep, a mail-order catalogue tucked in its lid, one tool lifted out mid-demonstration.
exercise:
  question: "Hobbs suggests npx creat-react-app to start a project. What should catch your eye?"
  choices:
    - "Nothing, npx always fetches the newest version"
    - "The spelling: creat- is not create-. A near-name may be a different, hostile parcel"
    - "npx cannot run project tools"
  answer: 1
  explanation: "npx fetches whatever name you give it, including a look-alike someone registered to catch typos. One wrong letter can run a stranger's tool in your study. Check the name against the real package."
---

## In one line

`npx` fetches a JavaScript tool and runs it in one step, without installing it first.

## The picture

A salesman knocks. You name a tool; he fetches it from the catalogue there and
then, opens his case on your desk, and runs it inside your study straight away.
No parcel is kept, no packing list is signed. If you muddle the name, a
different salesman answers, and you have let his tool loose in the room.

## What really happens

`npx <pkg>` runs a package's command, downloading it to a cache first if it is
not already present, then executing it with your permissions. It is meant for
one-off tools and project binaries. The fetched code runs immediately, so a
mistyped or malicious package name runs its code at once.

## Try it

```console
$ npx cowsay hello
 _______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Margin notes

| Write              | It means                                              |
|--------------------|-------------------------------------------------------|
| `npx pkg`          | Fetch this tool and run it now                        |
| `npx pkg arg`      | Run it with an argument                               |
| `npx --no pkg`     | Run only if already present; don't fetch              |
| `npx -y pkg`       | Fetch and run without the confirm prompt              |

## When an agent asks

Agents use `npx` to run a scaffolding or build tool once. Read the package name
letter by letter: typosquatted near-names are a common trap. Be wary if the
name was suggested by a README, an issue or a web page Hobbs just read rather
than by you, and beware `-y`, which skips the one prompt that would let you look.

## Careful

- The fetched tool runs with your permissions the instant it arrives, before you can inspect it.
- A name one letter off a popular tool may be a hostile look-alike. Confirm the exact package.
