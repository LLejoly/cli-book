#!/usr/bin/env python3
"""Bind the pages into the book website.

Reads contents.yml, pages/*.md, chapters/*.md (the tales), sketches/*.svg and the translations in i18n/, and writes:
  dist/index.html      the complete website, open it in any browser
  dist/fragment.html   the same page without <html>/<head>, for hosts that add their own
"""
import html
import json
import re
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
PAGE_NAMES = {"|": "pipe", ">": "redirect", "curl | sh": "curl-pipe-sh"}
EN_SECTIONS = ["In one line", "The picture", "What really happens", "Try it",
               "Margin notes", "When an agent asks", "Careful"]
FENCE = re.compile(r"```(\w*)\n(.*?)```", re.S)


def slug(command):
    return PAGE_NAMES.get(str(command), str(command).replace(" ", "-"))


def console(code):
    """A typewritten slip: typed lines in bold, the clerk's answers plain."""
    lines = []
    for line in code.rstrip("\n").split("\n"):
        if line.startswith("$ "):
            lines.append(f'<span class="typed"><span class="prompt">$</span> {html.escape(line[2:])}</span>')
        else:
            lines.append(f'<span class="said">{html.escape(line)}</span>')
    return '<pre class="slip"><code>' + "\n".join(lines) + "</code></pre>"


def render(text):
    blocks = []

    def keep(m):
        blocks.append(console(m.group(2)) if m.group(1) == "console" else
                      f"<pre class=\"slip\"><code>{html.escape(m.group(2))}</code></pre>")
        return f"\n\n@@BLOCK{len(blocks) - 1}@@\n\n"

    out = markdown.markdown(FENCE.sub(keep, text), extensions=["tables"])
    # In tables a pipe inside code is written \| so it isn't read as a column break.
    out = re.sub(r"<code>[^<]*</code>", lambda m: m.group(0).replace("\\|", "|"), out)
    for i, block in enumerate(blocks):
        out = out.replace(f"<p>@@BLOCK{i}@@</p>", block)
    return out


def split_page(path):
    meta_src, body = re.match(r"^---\n(.*?)\n---\n(.*)$", path.read_text(encoding="utf-8"), re.S).groups()
    sections = []
    for part in re.split(r"^## ", body, flags=re.M)[1:]:
        heading, _, text = part.partition("\n")
        sections.append((heading.strip(), render(text.strip())))
    return yaml.safe_load(meta_src), sections


def load_page(path, keys):
    meta, sections = split_page(path)
    sketch = ROOT / "sketches" / f"{path.stem}.svg"
    return {
        "command": str(meta["command"]),
        "slug": path.stem,
        "title": meta["title"],
        "risk": meta["risk"],
        "metaphor": meta["metaphor"].strip(),
        "related": [str(r) for r in meta.get("related") or []],
        "exercise": meta["exercise"],
        "sketch": sketch.read_text(encoding="utf-8") if sketch.exists() else None,
        "sketchBrief": meta["sketch"].strip(),
        # Sections are keyed by their English heading whatever the language.
        "sections": {keys.get(h, h): html for h, html in sections},
    }


def translate(page, path, ui):
    """Lay a translated page over its English original."""
    meta, sections = split_page(path)
    keys = dict(zip(ui["sections"], EN_SECTIONS))
    ex = {**page["exercise"], **{k: meta["exercise"][k] for k in ("question", "choices", "explanation")}}
    return {**page, "title": meta["title"], "metaphor": meta["metaphor"].strip(), "exercise": ex,
            "sections": {keys.get(h, h): html for h, html in sections}}


def load_tale(number, code):
    """The chapter's tale, in the language if translated, else in English."""
    for path in (ROOT / "i18n" / code / "chapters" / f"{number}.md", ROOT / "chapters" / f"{number}.md"):
        if path.exists():
            meta_src, body = re.match(r"^---\n(.*?)\n---\n(.*)$", path.read_text(encoding="utf-8"), re.S).groups()
            return {"title": yaml.safe_load(meta_src)["title"], "html": render(body.strip())}
    return None


def load_ui(code):
    return yaml.safe_load((ROOT / "i18n" / code / "ui.yml").read_text(encoding="utf-8"))


def main():
    contents = yaml.safe_load((ROOT / "contents.yml").read_text(encoding="utf-8"))
    english = {p.stem: load_page(p, {}) for p in sorted((ROOT / "pages").glob("*.md"))}
    codes = ["en"] + sorted(d.name for d in (ROOT / "i18n").iterdir()
                            if d.is_dir() and d.name != "en" and (d / "ui.yml").exists())
    books = {}
    for code in codes:
        ui = load_ui(code)
        pages = dict(english)
        done = 0
        for path in sorted((ROOT / "i18n" / code / "pages").glob("*.md")) if code != "en" else []:
            if path.stem in english:
                pages[path.stem] = translate(english[path.stem], path, ui)
                done += 1
        if code != "en":
            for stem in english.keys() - {p.stem for p in (ROOT / "i18n" / code / "pages").glob("*.md")}:
                pages[stem] = {**english[stem], "untranslated": True}
        chapters = []
        for ch in contents["chapters"]:
            entries = []
            for command in ch["commands"]:
                page = pages.get(slug(command))
                entries.append(page or {"command": str(command), "slug": slug(command), "missing": True})
            title = (ui.get("chapters") or {}).get(ch["number"], ch["title"])
            chapters.append({"number": ch["number"], "title": title, "pages": entries,
                             "tale": load_tale(ch["number"], code)})
        books[code] = {"name": ui["name"], "ui": ui["ui"], "headings": ui["sections"], "chapters": chapters}
        if code != "en":
            print(f"{ui['name']}: {done} of {len(english)} pages translated")

    data = json.dumps({"languages": codes, "books": books}, ensure_ascii=False).replace("</", "<\\/")
    fragment = (ROOT / "site" / "template.html").read_text(encoding="utf-8").replace("/*BOOK_DATA*/null", data)
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "fragment.html").write_text(fragment, encoding="utf-8")
    (dist / "index.html").write_text(
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + fragment + "\n</body>\n</html>\n",
        encoding="utf-8",
    )
    count = sum(1 for ch in books["en"]["chapters"] for p in ch["pages"] if not p.get("missing"))
    print(f"Bound {count} pages into dist/index.html")


if __name__ == "__main__":
    main()
