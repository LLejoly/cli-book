---
name: translate-page
description: Translate a page of Never Sign Blind into another language, or start a new language, keeping the Study's vocabulary and the page format.
---

# Translate a page

English in `pages/` is the source. Translations live in `i18n/<code>/pages/`
with the same file name. Read `i18n/README.md` once, then for each page:

1. Read `STYLE.md` sections 1 and 2 (the Study around 1900, the tone).
2. Read `i18n/<code>/GLOSSARY.md`. Use its word for every object and its exact
   title for every page, also when a page mentions another one. If you need a
   word for an object that isn't listed, add one row to the glossary in the
   same change, and use it everywhere.
3. Read `i18n/<code>/ui.yml` for the seven section headings and the
   margin-notes header (`write_column`).
4. Translate section by section. Same facts, same order, natural phrasing in
   the target language, the same warmth. Don't add or drop anything.
5. Front matter keeps only `command`, `title`, `metaphor` and `exercise`
   (`question`, `choices` in the same order, `explanation`). The answer index,
   risk, related pages and plate come from the English page.
6. Leave untouched: commands, flags, paths, code spans, `console` blocks
   (outputs included) and the first column of the margin-notes table. The reader
   types the same thing in every language.

## A new language

Copy `i18n/en/ui.yml` to `i18n/<code>/ui.yml` and translate the values, the
`sections`, `write_column`, `title_prefixes` (how titles start, like "The ")
and `chapters`. Add `off_world` words in that language that would break the
1900 Study. Write a `GLOSSARY.md` modelled on `i18n/fr/GLOSSARY.md` before the
first page. The build and the language switch pick the folder up on their own.

## Before you finish

- Run `python3 tools/check_pages.py`. It checks translations against their
  English page and must pass.
- Run `python3 tools/build_site.py`, open `dist/index.html`, switch language on
  the cover, and read your page once as the Curious Reader.
