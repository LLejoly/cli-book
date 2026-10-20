# Never Sign Blind

*Mrs. Finch's guide to the slips your new clerk will bring you.* A leather-bound manual of the command line, told as a tale.

Source: <https://github.com/LLejoly/cli-book>

A book about the terminal commands that AI agents ask you to run, written for
people who have never opened a terminal and for people who use one every day.

Every command gets a page with:

- **a picture**: the command as an object in an old study around 1900
  (`ls` is a lantern, `rm` is an eraser, the pipe `|` is a funnel);
- **what really happens**, precisely, for the practitioner;
- **a real example** you can run;
- **what to check when an agent asks** to run it;
- **a risk seal** and a **margin exercise** that earns a stamp.

The website shows the book as a leather-bound volume with an ink-drawn
contents tree, a ribbon bookmark and a wax stamp for each finished chapter.

## Build the website

```sh
python3 -m pip install -r requirements.txt
python3 tools/check_pages.py   # every page must follow the house rules
python3 tools/build_site.py    # writes dist/index.html
```

Open `dist/index.html` in a browser. Nothing else is needed: no server, no build tools.

## Publish on GitHub Pages

`.github/workflows/pages.yml` checks every page, binds the book and publishes it
each time `main` changes. Pull requests are checked and built but not published.

Once, in the repository on GitHub: **Settings › Pages › Build and deployment ›
Source: GitHub Actions**. The next push to `main` (or **Actions › Publish the
book › Run workflow**) puts the book at `https://<user>.github.io/<repository>/`.

## How the book is organised

| Path                     | What it holds                                              |
|--------------------------|------------------------------------------------------------|
| `contents.yml`           | The table of contents: chapters and their commands          |
| `pages/<command>.md`     | One page per command (the pipe lives in `pages/pipe.md`)    |
| `sketches/<command>.svg` | The ink sketch for each page                                |
| `STYLE.md`               | The house rules: the world of the Study, tone, page anatomy |
| `site/template.html`     | The look of the book                                        |
| `tools/`                 | The page checker and the site builder                       |
| `.claude/skills/add-command-page/` | The skill AI agents follow to add a page          |

## Languages

English and French. Readers switch language on the cover or above the
contents; the book also opens in the browser's language when it has it.
Translations live in `i18n/`, see `i18n/README.md`.

## Contributing

New pages are welcome, from people and from AI agents. Read
[CONTRIBUTING.md](CONTRIBUTING.md) first.
