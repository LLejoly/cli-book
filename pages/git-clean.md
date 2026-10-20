---
command: git clean
title: The Housemaid's Broom
chapter: 10
order: 3
risk: high
metaphor: >
  A housemaid's broom that sweeps out of the drawers every sheet that was never pressed into the letter book.
related: [git status, git reset, rm]
sketch: >
  A long-handled corn broom with a stitched straw head, mid-sweep on the floorboards, pushing a little drift of loose sheets to the left; one sheet tips up on its edge in front of the bristles.
exercise:
  question: "You started letters/to-aunt.txt this morning and never ran git add. Hobbs runs git clean -f. What happens to the letter?"
  choices:
    - "Nothing. git clean only removes rubbish."
    - "It is deleted, because the letter book never had a copy of it"
    - "It goes to the wastebasket"
  answer: 1
  explanation: "git clean doesn't judge what matters. Any sheet that was never pressed into the book counts as loose and is swept away, with no copy to bring back. git clean -n would have shown it on the list first."
---

## In one line

`git clean` deletes every file in a project that git has never been asked to keep.

## The picture

You ask the housemaid to tidy the drawers. She holds each sheet against the
letter book, and every sheet with no pressed copy in it, she sweeps away: new
drafts, scraps, the letter to your aunt you began this morning. Sheets the book
knows are left alone. What she sweeps out cannot be found again.

## What really happens

`git clean` deletes untracked files, ones git has never been told about, from
the current directory down. It refuses to run without `-f` (force), `-n` (dry
run) or `-i` (interactive). `-d` also removes untracked directories, `-x` also
removes files listed in `.gitignore` (the list of sheets the book is told to
overlook), and `-X` removes only those. Git never had a copy, so it cannot
restore them.

## Try it

```console
$ git status --short
?? letters/to-aunt.txt
$ git clean -n
Would remove letters/to-aunt.txt
$ git clean
fatal: clean.requireForce defaults to true and neither -i, -n, nor -f given; refusing to clean
```

## Margin notes

| Write            | It means                                              |
|------------------|-------------------------------------------------------|
| `git clean -n`   | Show me what you'd sweep, and sweep nothing           |
| `git clean -i`   | Ask me sheet by sheet                                 |
| `git clean -f`   | Sweep every loose sheet                               |
| `git clean -fd`  | Sweep loose drawers too                               |
| `git clean -fdx` | Sweep everything, even sheets the book overlooks. The most dangerous form |

## When an agent asks

Agents reach for `git clean` to get back to a clean slate after a failed build,
often together with `git reset --hard`. Ask Hobbs to run `git clean -n` with
the same margin notes first, and read the list. Any work you haven't added yet
is on it. Refuse `-x` unless you know what is ignored: that is where keys and
local settings often live.

## Careful

- Untracked means never pressed, not unimportant. New work you haven't run `git add` on is swept too.
- `-x` sweeps ignored sheets as well: `.env` files holding keys, local settings, downloaded tools.
