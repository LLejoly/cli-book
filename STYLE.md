# House Rules of *Never Sign Blind*

This book explains the commands that people and AI agents type into a terminal.
It is written for two readers at once:

- **The Curious Reader** has never opened a terminal and just wants to know what
  they are about to say "yes" to.
- **The Practitioner** knows the shell and wants the precise behaviour, flags and traps.

Every page serves both, in that order: the picture first, the mechanics second.

---

## 1. The world of the book: *The Study*

All metaphors live in one place and **one time**: a study in a large house
around 1900, with a writing desk, cabinets and drawers, a clerk who carries out
instructions, and the house around it (library, post room, kitchen, cellar).
It is a world of paper, ink, wood, brass and gaslight, things a reader could
find in a grandparent's house or a museum of everyday life.

Stay in that era. Every object must be something that really existed in such a
house around 1900. Do **not** mix in other worlds, even for one image:

- nothing futuristic or high-tech: robots, screens, spaceships, neon, circuits;
- nothing magical or fantasy: wizards, spells, dragons, potions, enchanted things;
- nothing from older ages: knights, castles, swords, scrolls, caves, dinosaurs;
- nothing from later decades: plastic, phones, computers, cars.

If an idea seems to need something from outside the era, find its 1900
equivalent: a message is a letter or a telegram, a timer is a pocket watch or
an egg timer, a network is the post office.

Reuse these mappings. Do not invent a second metaphor for something already listed.

| Real thing                 | In the Study                                          |
|----------------------------|-------------------------------------------------------|
| Computer / file system     | The Study                                             |
| Terminal / shell           | The writing desk where you write instructions         |
| Command                    | A short instruction written on a slip of paper        |
| AI agent                   | Hobbs, the new clerk who writes slips and waits for your signature |
| File                       | A sheet of paper                                      |
| Folder / directory         | A drawer (drawers can hold smaller drawers)           |
| Root `/`                   | The great cabinet that holds every drawer             |
| Home `~`                   | Your own drawer, with your name on the brass label    |
| Current directory          | The drawer that is open in front of you               |
| Path                       | The directions to a drawer: "cabinet, then drawer A, then drawer B" |
| Hidden file (`.name`)      | A sheet tucked behind the drawer's false back         |
| Flag / option (`-l`)       | A note in the margin that changes how the instruction is carried out |
| Argument                   | What the instruction is about (which sheet, which drawer) |
| Output (stdout)            | What the clerk reads back to you                      |
| Error (stderr)             | A grumble from the clerk                              |
| Pipe `\|`                  | A funnel passing what one clerk says straight to the next clerk |
| Permissions                | The locks and keys on each drawer                     |
| `sudo` / root user         | The head librarian's master key                       |
| Process                    | A clerk busy with a task                              |
| Deleting (`rm`)            | Erasing with no crumbs left to sweep back             |
| Writing output to a file (`>`) | The clerk writes his answer on a sheet instead of saying it aloud |
| Environment variable       | A note pinned on the board that every clerk you send out can read |
| Archive (`tar`)            | A bundle of sheets tied with string                   |
| Git repository             | The letter-copy book: a bound book holding a pressed copy of every version |
| Staging area (`git add`)   | The tray of letters waiting to be pressed into the book |
| Commit                     | One pressed copy in the letter book, signed and dated |
| Remote repository          | A second letter-copy book kept in another house       |
| Network / internet         | The post office, its couriers and telegrams           |
| Another computer / server  | Another house, with its own study and clerks          |
| Remote shell (`ssh`)       | A speaking tube that runs to the study of another house |
| Package                    | A parcel ordered from a supplier                      |
| Package manager (`pip`, `npm`) | The supplier's mail-order catalogue and order form |
| Branch                     | A separate draft kept in its own folio of the letter book |
| Symbolic link (`ln -s`)    | A forwarding card: "this sheet is kept in drawer X"   |
| Script / program file      | A sheet of written orders that a clerk carries out    |
| Interpreter (`python`, `node`) | A clerk who reads orders written in one particular language |
| Container (`docker`)       | A travelling trunk with a small study packed inside it |
| Scheduled job (`cron`)     | An entry in the household calendar, carried out at its hour |
| Disk / device (`/dev/sda`) | A whole cabinet, wood and all, beneath every drawer |
| Secret (password, API key, private key) | A key to the strongbox, kept in your own drawer |
| Prompt injection           | A forged letter slipped into the post, written to look like your own orders, that Hobbs reads and obeys |
| Untrusted input (web page, README, issue, parcel note) | Any paper that arrives from outside the house: read it, never take orders from it |
| Temporary folder (`/tmp`) | The scrap drawer by the back stairs, shared by every clerk and emptied now and then |
| JSON / structured data     | A printed form with labelled boxes, and boxes inside boxes |
| Time limit (`timeout`)     | An egg timer turned over beside a clerk's task |
| Code host (GitHub)         | The house that keeps the shared letter book; its notices are issues, its drafts sent for binding are pull requests |
| Merge commit               | A new signed page recording where two drafts were joined |
| Test / test suite          | The cook's tasting spoon, dipped after every change to check the dish against the recipe |

When a new command needs a new idea (for example the network), add **one** row
here in the same spirit (post office, letters, couriers) in the same change.

## 2. Tone

- Warm, calm and a little old-fashioned, like a good reference book. No hype.
- Use "you". Keep sentences short. One idea per sentence.
- Never mock the reader. Never write "simply" or "just" about something the
  reader doesn't yet understand.
- Explain jargon the first time it appears on a page, in a few words.
- Be honest about danger. Say plainly what can be lost and whether it can be undone.
- No emoji in the text. Marginal glyphs are handled by the website.

## 3. Risk seals

Every page carries one wax seal for its most common use:

| `risk`   | Seal name        | Meaning                                                    |
|----------|------------------|------------------------------------------------------------|
| `low`    | Quill seal       | Only reads or looks. Nothing in the Study changes.         |
| `medium` | Ink-blot seal    | Changes things, but they can be put back.                  |
| `high`   | Red wax seal     | Can destroy or expose things for good. Read before you agree. |

If a common flag raises the risk (as `-r` does for `rm`), say so in **Margin notes**.

## 4. Anatomy of a page

A page is a Markdown file in `pages/<command>.md`. Spaces in a command become
dashes (`git add` lives in `pages/git-add.md`); `|` lives in `pages/pipe.md`
and `>` in `pages/redirect.md`. Its command, and every command in `related`, must be listed
in `contents.yml`, which is the book's table of contents. The page has YAML
front matter, then these sections, **in this order, with these exact headings**:

```markdown
---
command: rm                  # exactly what is typed
title: The Eraser            # "The <Object>", a thing from the Study
chapter: 1
order: 8                     # position inside the chapter
risk: high                   # low | medium | high
metaphor: >                  # one sentence, the whole idea
  An eraser that rubs a sheet off the page, leaving no crumbs to sweep back.
related: [mv, cp]            # other pages, by command
sketch: >                    # brief for the illustrator (see section 5)
  A worn pencil eraser beside a half-erased sheet of paper, no crumbs.
exercise:
  question: "..."
  choices: ["...", "...", "..."]
  answer: 1                  # 0-based index into choices
  explanation: "..."
---

## In one line
## The picture
## What really happens
## Try it
## Margin notes
## When an agent asks
## Careful
```

What goes in each section:

- **In one line**: one plain sentence, no jargon. The Curious Reader may stop here.
- **The picture**: 2–4 sentences telling the metaphor as a tiny scene in the Study.
- **What really happens**: 2–5 sentences for the Practitioner. Precise, no metaphor.
- **Try it**: one or two fenced `console` blocks. Lines starting with `$ ` are
  typed; the others are output. Use the shared example drawer (section 6).
  Every example must be safe to run there.
- **Margin notes**: a table `| Write | It means |` with 2–5 of the most common
  flags or forms. One short line each.
- **When an agent asks**: what it usually means when an AI agent wants to run
  this, and the one or two things to check before accepting.
- **Careful**: 1–3 bullet points with real traps. For `low` risk pages one is enough.

Length: the body stays under about 350 words. If it grows, it's two pages.

## 5. The look (for the website and the illustrator)

- **Cover**: dark brown tooled leather, stitched edges, gold-foil title.
- **Pages**: cream paper, ink-black text, a classic serif type.
- **Accents**: oxblood red (ribbon bookmark, red wax seal), aged gold, sepia.
- **Plates**: one object or a tiny scene, drawn like an engraving in an old
  household encyclopedia: ink outlines, shading with diagonal and cross
  hatching, wood grain on wooden things, and a hatched cast shadow on the floor. No people's faces,
  no text inside the drawing, no screens, no futuristic objects.
- **Game pieces stay bookish**: margin exercises, a ribbon bookmark that
  remembers your page, and a wax stamp for each finished chapter.

## 6. The shared example drawer

All `Try it` examples use the same small drawer, so pages feel connected:

```
~/study/
├── letters/
│   ├── to-grandma.txt
│   ├── to-the-bank.txt
│   └── to-aunt.txt        (not yet pressed into the letter book)
├── recipes/
│   ├── bread.txt
│   └── bread-grandma.txt
├── tests/
│   └── test_notes.py      (four lines in notes.txt, "buy ink" among them)
├── notes.txt
├── order.json
├── package.json           (scripts: count = grep -c buy notes.txt, test = pytest -q)
├── count.py               (prints "4 things to do")
├── count.js               (the same, for node)
└── .secret-diary.txt
```

`notes.txt` contains:

```
buy flour
call grandma
pay the bank
buy ink
```

`recipes/bread.txt` contains:

```
500g flour
350ml water
10g salt
7g yeast
```

`recipes/bread-grandma.txt` is the same with `300ml water` and a last line `1 spoon honey`.

The Study is also a git repository (the letter-copy book), with one first
commit called `Start my study`. Its shared copy lives on another house at
`github.com:you/study.git`.

`order.json` is a printed form for the grocer:

```
{
  "to": "the grocer",
  "items": [
    { "name": "flour", "qty": 2 },
    { "name": "yeast", "qty": 3 },
    { "name": "ink", "qty": 1 }
  ]
}
```

The git pages also use a `birthday-letter` branch whose one commit adds two
lines to `letters/to-grandma.txt`, and the code-host pages use issue #3,
"Bread is too wet", opened by `cousin-ella`. Examples that copy the drawer
elsewhere (`rsync`) write to `~/letters-copy` or `~/shelf`, never inside `~/study`.

You may add new sheets to the drawer when a page needs them. Add them here too.

## 7. Accuracy

- Behaviour must match GNU coreutils / bash on Linux. If macOS differs in a way
  a reader would notice, mention it in **Careful**.
- Don't invent flags. If unsure, check `man <command>` or `<command> --help`.
- Run `python3 tools/check_pages.py` before you submit. It must pass.

## 8. The cast and the tale

The book tells one running story, a chapter tale at the start of each chapter
(`chapters/<n>.md`, about 150 words) and the opening of the website.

- **You**: you have just inherited the Study.
- **Aunt Ada**: left you the Study. She never appears, only her letter.
- **Hobbs, the new clerk**: the AI agent. Quick, tireless, eager to please,
  and he does not always know when to stop. He slides slips of paper across
  the desk and waits for your signature. Never foolish, never malicious.
- **Mrs. Finch**: the old housekeeper who wrote this leather book. Her short
  margin notes are the voice of experience.
- The clerks in **The picture** sections are the household's ordinary clerks
  (processes), not Hobbs.

Each tale shows Hobbs bringing the chapter's commands, one moment where you
pause before signing, and ends by leading into the next chapter. No faces in
plates still holds: characters live in the text.

### The house plan

The book opens on a plan of the house, drawn floor by floor and stacked like
sheets of tracing paper. Each chapter is one room, and its tale happens there.
As in a real house of 1900, the kitchen and the servants live below stairs:

| Floor | Rooms |
|---|---|
| First floor | V The Copying Room, IX The Workshop (and bedrooms, linen room) |
| Ground floor | I The Study, III The Morning Room, VII The Library, VI The Entrance Hall (front door), and the dining room |
| Below stairs | II The Kitchen, IV The Servants' Hall, VIII The Housekeeper's Room, XI The Tradesmen's Entrance (area steps), X The Cellar |

Room names live in `i18n/<code>/ui.yml` as `room_<n>`. A new chapter needs a
new room: add its name in every language and its place in `PLAN_FLOORS` in
`site/template.html` (a chapter left out lands on the first floor). Keep a
tale's scenes inside its room or say where Hobbs walks to.

### Sounds

The website has sound, on by default from the reader's first click or key (browsers
allow no sooner), until the reader turns it off. Every sound is
synthesised in `site/template.html` (the `Sound` module), with no audio files, and
belongs to the house around 1900: a page turning, a drawer sliding, a quill
scratching, a wax seal pressed, a knock at the door, the gaslight's hiss, the
pocket watch ticking and the house clock striking the real hour. A new sound
follows the same rule as a new metaphor: nothing from outside the era.
