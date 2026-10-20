# Contributing

The book only works if every page sounds like the same author and lives in the
same world. So before anything else, read [STYLE.md](STYLE.md).

## Adding a command

1. Add the command to a chapter in `contents.yml`.
2. Write `pages/<command>.md` following STYLE.md section 4.
3. Draw `sketches/<command>.svg` in the style of the existing plates (open
   `sketches/rm.svg` as a model): viewBox `0 0 200 160`, `stroke="currentColor"`,
   shading done with the hatching patterns defined at the top of each file, and
   surfaces that hide what is behind them marked `class="bg"`. Or leave it out
   and describe the drawing in the page's `sketch` field so an illustrator can make it.
4. Run `python3 tools/check_pages.py` and `python3 tools/build_site.py`, then
   open `dist/index.html` and read your page as a beginner would.

## Translating

The book is written in English and translated in `i18n/<language>/`. French
is the first translation. A missing translated page is shown in English with a
short note, so a language can grow one page at a time. See `i18n/README.md`
and `.claude/skills/translate-page/SKILL.md`.

## AI agents

Agents follow `.claude/skills/add-command-page/SKILL.md` (agents that don't
read Claude skills are pointed there by `AGENTS.md`). The same rules apply:
one era, one world, real behaviour only, and the checker must pass.

## What we check in review

- The metaphor reuses the Study's existing mappings and stays around 1900.
- Every example is safe to run in the shared `~/study` drawer and shows real output.
- **When an agent asks** says concretely what to check before accepting.
- The risk seal is honest.
