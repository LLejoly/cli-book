---
command: rm
title: The Eraser
chapter: 1
order: 8
risk: high
metaphor: >
  An eraser that rubs a sheet clean off the page, leaving no crumbs to sweep back.
related: [mv, ls]
sketch: >
  A worn pencil eraser resting beside a half-erased sheet of paper; where the writing was, the paper is perfectly clean.
exercise:
  question: "You run rm notes.txt by mistake. Where can you get it back from?"
  choices:
    - "The wastebasket, like on a desktop"
    - "Nowhere in the Study. Only a backup made earlier can help."
    - "Type rm -undo notes.txt"
  answer: 1
  explanation: "rm skips the wastebasket. Without a backup made beforehand, the sheet is gone."
---

## In one line

`rm` deletes files for good, with no wastebasket in between.

## The picture

You take the eraser and rub a sheet away. On a real desk you would find crumbs
and maybe a faint trace. Here there is nothing: no crumbs, no wastebasket, no
trace. The clerk doesn't ask "are you sure?" either. It just erases.

## What really happens

`rm` removes directory entries for the files you name. It does not move them
to a trash folder, so ordinary tools cannot restore them. Directories are
refused unless you pass `-r` (recursive), which deletes the directory and
everything inside it. `-f` (force) silences warnings and confirmation prompts.

## Try it

```console
$ ls
letters  notes.txt  recipes
$ rm notes.txt
$ ls
letters  recipes
$ rm recipes
rm: cannot remove 'recipes': Is a directory
```

## Margin notes

| Write       | It means                                            |
|-------------|-----------------------------------------------------|
| `rm -i`     | Ask me before erasing each sheet                    |
| `rm -r`     | Erase a drawer and everything inside it             |
| `rm -f`     | Don't warn me, don't ask me                         |
| `rm -rf`    | Erase the whole drawer, silently. The most dangerous form |

## When an agent asks

Agents often run `rm` to tidy up files they created themselves, like build
output or temporary files. Before accepting, read the exact path. Be very wary
of `-rf` together with `~`, `/`, `*` or a path you don't recognise.

## Careful

- `rm -rf` on the wrong drawer can erase years of work in a second.
- A stray space matters: `rm -rf ./build` erases one drawer, `rm -rf . /build` erases the one you are in.
- `*` matches every sheet in the drawer. Run `ls` with the same pattern first to see what it would erase.
