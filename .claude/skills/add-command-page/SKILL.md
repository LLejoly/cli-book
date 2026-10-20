---
name: add-command-page
description: Write or revise a page of Never Sign Blind, the book that explains terminal commands with metaphors from an old study. Use when adding a new command, fixing a page, or adding a chapter.
---

# Adding a page to the book

The book explains terminal commands to two readers at once: someone who has
never used a terminal, and someone who uses one every day. Every page tells a
small scene in **the Study** (drawers, sheets of paper, ink, a clerk at a
writing desk) and then gives the precise behaviour. Your page must feel like
it was written by the same hand as the pages already there.

## Before you write

1. Read `STYLE.md` in full. It is the source of truth; this skill only tells you the order of work.
2. Read `pages/ls.md` (a `low` risk page) and `pages/rm.md` (a `high` risk page) to hear the voice.
3. Check `contents.yml`. If the command isn't listed, add it to the chapter where
   a reader would look for it, or propose a new chapter at the end.
4. Check the real behaviour with `man <command>` or `<command> --help`. Never invent a flag.

## Choosing the metaphor

- Look in the mapping table in STYLE.md section 1 first. If the idea is
  already there (a file is a sheet, a folder is a drawer, a pipe is a funnel),
  **use that mapping**. Never create a second metaphor for the same thing.
- The command itself becomes one object from the Study: `ls` is the Lantern,
  `rm` is the Eraser. Pick an everyday, physical, old-fashioned object whose
  action mirrors the command. Ask: would a ten-year-old get it from the sketch alone?
- If the command needs a brand-new idea (networks, processes, time), add one
  row to the mapping table in the same change, in the same world: post office,
  letters, couriers, clerks, clocks.
- Stay in one era: a house around 1900. No futuristic things, no fantasy or
  magic, no medieval or prehistoric things, nothing modern. If you need an idea
  from outside the era, find its 1900 equivalent (see STYLE.md section 1).

## Writing the page

1. Copy the front matter and the seven headings from STYLE.md section 4, in order.
2. Write **The picture** before anything else. If the scene doesn't work,
   change the object, not the facts.
3. Write **What really happens** for the expert: precise, no metaphor, 2 to 5 sentences.
4. Use the shared example drawer `~/study` (STYLE.md section 6) in **Try it**.
   Every example must be safe to run there. Show real output.
5. Pick the risk seal for the most common use. If a common flag raises it, say so.
6. In **When an agent asks**, say why an AI agent typically runs this command
   and what the reader should check before saying yes. This section is the
   reason the book exists, so make it concrete.
7. Write an exercise whose wrong answers are mistakes a beginner would really
   make, and whose explanation teaches something, not just "B is correct".
8. Write the `sketch` brief: one object or tiny scene, pen and ink with sepia
   wash, no faces, no text, no screens.

## Before you finish

- Run `python3 tools/check_pages.py`. It must print that every page follows the house rules.
- Read your page aloud in your head as the Curious Reader. Any word they
  wouldn't know must be explained on the page.
- Re-read **Careful**: is every danger a real one, said plainly?
- Keep the body under 350 words. If it doesn't fit, split it into two pages.
