---
command: npm install
title: The Packing List
chapter: 6
order: 5
risk: high
metaphor: >
  A packing list kept with the project, from which every parcel it needs is ordered and unpacked in one go.
related: [pip install, curl]
sketch: >
  A long handwritten packing list on a clipboard, ticked down the margin, in front of a stack of brown-paper parcels tied with string.
exercise:
  question: "npm install with no name reports 'added 57 packages'. Where did 57 come from?"
  choices:
    - "npm picked popular parcels"
    - "The packing list names a few parcels, and each of those needs others"
    - "It is a mistake"
  answer: 1
  explanation: "Each parcel on the list can depend on others, which depend on others again. A short list easily becomes dozens of parcels."
---

## In one line

`npm install` downloads every JavaScript package a project lists as needed.

## The picture

The project keeps a packing list, `package.json`. You hand it to the supplier,
who sends every parcel on it, plus every parcel those parcels say they need.
They're unpacked into a drawer called `node_modules`. Some parcels run a
little setup routine of their own while being unpacked.

## What really happens

With no arguments, `npm install` reads `package.json` and the lockfile and
installs all dependencies into `node_modules`, resolving the full dependency
tree. With a name, it adds that package and records it. Packages can define
install scripts that run automatically, unless `--ignore-scripts` is given.

## Try it

```console
$ npm install
added 57 packages, and audited 58 packages in 3s
found 0 vulnerabilities
```

## Margin notes

| Write                     | It means                                       |
|---------------------------|------------------------------------------------|
| `npm install`             | Order everything on the packing list           |
| `npm install name`        | Order one more parcel and add it to the list   |
| `npm ci`                  | Order exactly what the lockfile says, nothing else |
| `--ignore-scripts`        | Unpack parcels without running their setup     |

## When an agent asks

`npm install` in a project you trust is routine. Be more careful when the
agent adds a new parcel by name: check the spelling and that the parcel
is well known.

## Careful

- Install scripts run with your permissions. A bad parcel can read your files.
- `npm install -g` with `sudo` puts parcels into the whole house. Avoid it.
