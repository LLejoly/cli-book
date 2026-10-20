# Translating the book

English is the source. Each other language lives in `i18n/<code>/`:

```
i18n/fr/
├── ui.yml        interface text, section headings, chapter titles
├── GLOSSARY.md   the Study's vocabulary and every page title in this language
└── pages/rm.md   one file per English page, same file name
```

A page that has no translation yet is shown in English with a short note, so a
language can grow one page at a time.

## A translated page

The front matter carries only what the reader sees. Everything else (chapter,
order, risk, related, sketch, the exercise's answer) comes from the English page.

```markdown
---
command: rm                     # same as English
title: La Gomme                 # from GLOSSARY.md
metaphor: >
  Une gomme qui efface une feuille sans laisser de miettes à balayer.
exercise:
  question: "..."
  choices: ["...", "...", "..."]   # same number and order as English
  explanation: "..."
---

## En une ligne
...
```

The headings are the ones listed under `sections` in `ui.yml`, in the same
order. The margin-notes table starts with the `write_column` header.

## Rules

- Translate the English page section by section. Do not add or drop facts.
- Commands, flags, paths, code spans and `console` blocks stay byte for byte
  identical to English, outputs included.
- Keep the Study of 1900 (STYLE.md section 1) and use GLOSSARY.md for every
  object. Do not invent another word for a thing already listed.
- Body under about 420 words (translations run longer than English).
- Run `python3 tools/check_pages.py`. It checks translations too.

## A new language

Copy `i18n/en/ui.yml` to `i18n/<code>/ui.yml`, translate the values, write a
GLOSSARY.md like the French one, then translate pages. The build picks the
language up on its own.
