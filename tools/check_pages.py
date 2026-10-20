#!/usr/bin/env python3
"""Check every page in pages/ against the house rules in STYLE.md."""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "pages"
CONTENTS = ROOT / "contents.yml"

SECTIONS = [
    "In one line",
    "The picture",
    "What really happens",
    "Try it",
    "Margin notes",
    "When an agent asks",
    "Careful",
]
REQUIRED = ["command", "title", "chapter", "order", "risk", "metaphor", "related", "sketch", "exercise"]
RISKS = {"low", "medium", "high"}
# Imagery that breaks the world of the Study.
OFF_WORLD = re.compile(
    r"\b("
    r"robot|spaceship|neon|circuit|cyber|futuristic|hologram|laser|smartphone|plastic"  # future
    r"|wizard|witch|magic|magical|dragon|potion|enchanted|elf|elves|fairy|fairies"  # fantasy
    r"|knight|castle|sword|dungeon|scroll|caveman|cavemen|cave|dinosaur|mammoth"  # older ages
    r")s?\b",
    re.I,
)
MAX_WORDS = 350


PAGE_NAMES = {"|": "pipe", ">": "redirect", "curl | sh": "curl-pipe-sh"}  # commands that can't be file names


def page_name(command):
    return PAGE_NAMES.get(str(command), str(command).replace(" ", "-"))


def check(path, commands):
    errors = []
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return ["missing YAML front matter"]
    meta, body = yaml.safe_load(m.group(1)) or {}, m.group(2)

    for key in REQUIRED:
        if key not in meta:
            errors.append(f"front matter: missing '{key}'")
    if meta.get("command") and path.stem != page_name(meta["command"]):
        errors.append(f"file name should be {page_name(meta['command'])}.md")
    if not str(meta.get("title", "")).startswith("The "):
        errors.append("title should read 'The <Object>'")
    if meta.get("risk") not in RISKS:
        errors.append(f"risk must be one of {sorted(RISKS)}")
    if meta.get("command") not in commands:
        errors.append(f"'{meta.get('command')}' is not listed in contents.yml")
    for rel in meta.get("related") or []:
        if rel not in commands:
            errors.append(f"related: '{rel}' is not listed in contents.yml")

    ex = meta.get("exercise") or {}
    choices = ex.get("choices") or []
    if not ex.get("question") or not ex.get("explanation"):
        errors.append("exercise: needs question and explanation")
    if not 2 <= len(choices) <= 4:
        errors.append("exercise: needs 2 to 4 choices")
    if not isinstance(ex.get("answer"), int) or not 0 <= ex["answer"] < len(choices):
        errors.append("exercise: answer must be a valid 0-based index")

    headings = re.findall(r"^## (.+)$", body, re.M)
    if headings != SECTIONS:
        errors.append(f"sections must be exactly, in order: {SECTIONS} (found {headings})")
    if "```console" not in body:
        errors.append("Try it: needs a ```console example")
    if "| Write" not in body:
        errors.append("Margin notes: needs a '| Write | It means |' table")

    words = len(re.sub(r"```.*?```", "", body, flags=re.S).split())
    if words > MAX_WORDS:
        errors.append(f"body is {words} words, keep it under {MAX_WORDS} or split the page")
    for hit in sorted({h.lower() for h in OFF_WORLD.findall(text)}):
        errors.append(f"off-world imagery: '{hit}' (one era only, see STYLE.md section 1)")
    return errors


MAX_WORDS_TRANSLATED = 420  # translations run a little longer than English


def split(path):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", path.read_text(encoding="utf-8"), re.S)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else (None, None)


def typed_lines(body):
    """What the reader types and sees in console blocks; identical in every language."""
    return [b.strip() for b in re.findall(r"```console\n(.*?)```", body, re.S)]


def check_translation(path, ui):
    errors = []
    original = PAGES / path.name
    if not original.exists():
        return [f"no English page pages/{path.name} to translate"]
    meta, body = split(path)
    if meta is None:
        return ["missing YAML front matter"]
    en_meta, en_body = split(original)

    for key in ("command", "title", "metaphor", "exercise"):
        if key not in meta:
            errors.append(f"front matter: missing '{key}'")
    if str(meta.get("command")) != str(en_meta["command"]):
        errors.append(f"command must stay '{en_meta['command']}'")
    if not str(meta.get("title", "")).startswith(tuple(ui["title_prefixes"])):
        errors.append(f"title should start with one of {ui['title_prefixes']}")
    ex = meta.get("exercise") or {}
    if not ex.get("question") or not ex.get("explanation"):
        errors.append("exercise: needs question and explanation")
    if len(ex.get("choices") or []) != len(en_meta["exercise"]["choices"]):
        errors.append("exercise: needs the same number of choices as English, in the same order")

    headings = re.findall(r"^## (.+)$", body, re.M)
    if headings != ui["sections"]:
        errors.append(f"sections must be exactly, in order: {ui['sections']} (found {headings})")
    if typed_lines(body) != typed_lines(en_body):
        errors.append("console blocks must be identical to the English page")
    if ui["write_column"] not in body:
        errors.append(f"margin notes: needs a '{ui['write_column']}' table")
    words = len(re.sub(r"```.*?```", "", body, flags=re.S).split())
    if words > MAX_WORDS_TRANSLATED:
        errors.append(f"body is {words} words, keep it under {MAX_WORDS_TRANSLATED}")
    text = path.read_text(encoding="utf-8")
    words_off = [w.lower() for w in ui.get("off_world") or []]
    hits = {h.lower() for h in OFF_WORLD.findall(text)}
    if words_off:
        hits |= {h.lower() for h in re.findall(r"\b(" + "|".join(map(re.escape, words_off)) + r")s?\b", text, re.I)}
    for hit in sorted(hits):
        errors.append(f"off-world imagery: '{hit}' (one era only, see STYLE.md section 1)")
    return errors


def check_ui(code, ui, en_ui):
    errors = []
    missing = set(en_ui["ui"]) - set(ui.get("ui") or {})
    if missing:
        errors.append(f"ui.yml: missing keys {sorted(missing)}")
    if len(ui.get("sections") or []) != len(SECTIONS):
        errors.append(f"ui.yml: 'sections' needs {len(SECTIONS)} headings")
    return errors


def main():
    pages = sorted(PAGES.glob("*.md"))
    contents = yaml.safe_load(CONTENTS.read_text(encoding="utf-8"))
    commands = {c for ch in contents["chapters"] for c in ch["commands"]}
    failed = 0
    for path in pages:
        errors = check(path, commands)
        if errors:
            failed += 1
            print(f"✗ {path.name}")
            for e in errors:
                print(f"    {e}")
        else:
            print(f"✓ {path.name}")
    print(f"\n{len(pages) - failed}/{len(pages)} pages follow the house rules.")

    # Chapter tales: one per chapter, short, inside the Study (STYLE.md section 8).
    for folder, words_off in [(ROOT / "chapters", [])] + [
            (d / "chapters", yaml.safe_load((d / "ui.yml").read_text(encoding="utf-8")).get("off_world") or [])
            for d in sorted((ROOT / "i18n").iterdir()) if d.is_dir() and d.name != "en" and (d / "chapters").exists()]:
        for ch in contents["chapters"]:
            path = folder / f"{ch['number']}.md"
            if not path.exists():
                if folder == ROOT / "chapters":
                    failed += 1
                    print(f"✗ chapters/{ch['number']}.md is missing (every chapter opens with a tale)")
                continue
            meta, body = split(path)
            problems = [] if meta and meta.get("title") else ["needs front matter with a title"]
            if body and len(body.split()) > 220:
                problems.append(f"tale is {len(body.split())} words, keep it under 220")
            text = path.read_text(encoding="utf-8")
            hits = {h.lower() for h in OFF_WORLD.findall(text)}
            if words_off:
                hits |= {h.lower() for h in re.findall(r"\b(" + "|".join(map(re.escape, words_off)) + r")s?\b", text, re.I)}
            problems += [f"off-world imagery: '{h}'" for h in sorted(hits)]
            if problems:
                failed += 1
                print(f"✗ {path.relative_to(ROOT)}")
                for e in problems:
                    print(f"    {e}")
    print("Chapter tales checked.")

    i18n = ROOT / "i18n"
    en_ui = yaml.safe_load((i18n / "en" / "ui.yml").read_text(encoding="utf-8"))
    for lang in sorted(d for d in i18n.iterdir() if d.is_dir() and d.name != "en"):
        ui = yaml.safe_load((lang / "ui.yml").read_text(encoding="utf-8"))
        problems = check_ui(lang.name, ui, en_ui)
        for e in problems:
            print(f"✗ i18n/{lang.name}: {e}")
        failed += bool(problems)
        translated = sorted((lang / "pages").glob("*.md"))
        bad = 0
        for path in translated:
            errors = check_translation(path, ui)
            if errors:
                bad += 1
                print(f"✗ i18n/{lang.name}/pages/{path.name}")
                for e in errors:
                    print(f"    {e}")
        failed += bad
        print(f"{ui['name']}: {len(translated) - bad}/{len(translated)} translated pages follow the house rules"
              f" ({len(translated)} of {len(pages)} pages translated).")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
