---
command: rsync
title: The Carrier's Hamper
chapter: 6
order: 6
risk: medium
metaphor: >
  A carrier's hamper that travels between two drawers or two houses, packed only with the sheets the other side is missing or holds an older copy of.
related: [cp, ssh, tar, curl]
sketch: >
  A lidded wicker hamper with two leather straps, a brass catch and a side handle, standing on the floor with its lid open behind a few loose sheets, a blank luggage tag tied to the handle.
exercise:
  question: "What is the difference between rsync -a letters/ ../shelf/ and rsync -a letters ../shelf/?"
  choices:
    - "None, the slash is only decoration"
    - "The first copies the sheets inside letters into shelf; the second puts a whole letters drawer inside shelf"
    - "The second one deletes letters afterwards"
  answer: 1
  explanation: "A trailing slash on the source means 'what is in this drawer'. Without it, rsync carries the drawer itself, so you get ../shelf/letters/."
---

## In one line

`rsync` makes one folder match another, copying only what is new or changed, on this computer or to another one.

## The picture

Before the carrier leaves, the clerk compares the two drawers sheet by sheet.
Only the sheets the other side lacks, or holds an older copy of, go into the
hamper. The other drawer ends up looking like yours. Add `--delete`, and the
carrier also throws away anything there that yours doesn't have.

## What really happens

`rsync SRC DEST` copies files, skipping those whose size and modification
time already match. `-a` (archive) recurses and keeps permissions, times and
links. `-n` or `--dry-run` lists what would happen and changes nothing. A
destination like `host:dir/` goes through `ssh`. `--delete` removes files in
the destination that are not in the source.

## Try it

```console
$ rsync -av --dry-run letters/ ../letters-copy/
sending incremental file list
created directory ../letters-copy
./
to-aunt.txt
to-grandma.txt
to-the-bank.txt

sent 155 bytes  received 31 bytes  372.00 bytes/sec
total size is 33  speedup is 0.18 (DRY RUN)
$ rsync -a letters/ ../letters-copy/
$ ls ../letters-copy
to-aunt.txt  to-grandma.txt  to-the-bank.txt
```

## Margin notes

| Write                    | It means                                      |
|--------------------------|-----------------------------------------------|
| `rsync -av a/ b/`        | Make b hold what a holds, and name each sheet |
| `rsync -n ...`           | Rehearse only: say what you would carry       |
| `rsync -a a/ house:a/`   | Send the hamper to another house, by speaking tube |
| `rsync -a --delete a/ b/`| Also throw out of b what a doesn't have. Red wax |

## When an agent asks

Agents use `rsync` to back up a folder, deploy a site to a server, or copy a
project to another machine. Ask for a `--dry-run` first and read the list.
Check which side is the source: swapped, it overwrites your own drawer. Check
every trailing slash. With `--delete`, a wrong destination can be emptied.

## Careful

- `--delete` turns the seal red: sheets that exist only at the destination are erased, with no wastebasket. Even without it, changed sheets there are overwritten without asking (`-u` skips newer ones).
- `letters/` carries what is inside the drawer; `letters` carries the drawer itself.
- macOS ships an older or different `rsync`, so some flags may be missing there.
