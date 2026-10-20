---
command: pip install
title: The Order Form
chapter: 6
order: 4
risk: high
metaphor: >
  An order form posted to a supplier's catalogue, whose parcel is delivered and unpacked straight into your Study.
related: [npm install, sudo, curl]
sketch: >
  A printed mail-order form half filled in with pen, lying on an open supplier's catalogue full of small engraved product pictures.
exercise:
  question: "You meant pip install requests but typed pip install requestss. Why does it matter?"
  choices:
    - "It doesn't, pip corrects spelling"
    - "Someone may have listed a lookalike parcel under that name, and it's unpacked and run just the same"
    - "pip will refuse a typo"
  answer: 1
  explanation: "Anyone can list a parcel in the catalogue. Lookalike names are a known trick. pip installs what you name, and its code can run during installation."
---

## In one line

`pip install` downloads a Python package from the internet and installs it.

## The picture

You fill in an order form from the supplier's catalogue and post it. A parcel
arrives and is unpacked into your Study, along with anything the parcel itself
says it needs. You don't open each box to inspect it. You trust the supplier
and the name on the form.

## What really happens

`pip` resolves the named package and its dependencies from an index (PyPI by
default), downloads them, and installs them into the active Python
environment. Source packages can run build code during installation. `-r
requirements.txt` installs a whole list. `==` pins a version.

## Try it

```console
$ pip install requests
Collecting requests
...
Successfully installed certifi-2024.8.30 charset-normalizer-3.4.0 idna-3.10 requests-2.32.3 urllib3-2.2.3
```

## Margin notes

| Write                        | It means                                    |
|------------------------------|---------------------------------------------|
| `pip install name`           | Order this parcel and unpack it             |
| `pip install name==2.1`      | Order exactly version 2.1                   |
| `pip install -r list.txt`    | Order everything on this list               |
| `pip uninstall name`         | Pack it up and send it back                 |

## When an agent asks

Read the parcel name letter by letter, and check it's a well-known one.
Prefer installing into a project's own environment (a venv) over the whole
system, and never with `sudo pip`.

## Careful

- Misspelled or lookalike names are a known way to deliver harmful parcels.
- `sudo pip install` lets an unchecked parcel unpack itself into every drawer of the house.
