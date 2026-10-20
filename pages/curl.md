---
command: curl
title: The Courier
chapter: 6
order: 1
risk: low
metaphor: >
  A courier sent to another house's address, who brings back exactly what was handed to him at the door.
related: [ping, "|", ssh]
sketch: >
  A courier's leather dispatch case with a shoulder strap and brass clasp, a sealed envelope peeking out from under its flap.
exercise:
  question: "What is risky about curl https://example.org/setup.sh | sh?"
  choices:
    - "Nothing, curl only fetches"
    - "Whatever the courier brings back is carried out at once, unread"
    - "It downloads too slowly"
  answer: 1
  explanation: "curl only fetches, but the funnel hands its answer straight to sh, which carries it out. You never see what was in the envelope."
---

## In one line

`curl` fetches something from a web address, or sends something to it.

## The picture

You give the courier an address. He goes to that house, asks at the door, and
brings back exactly what he was handed: a page, a parcel, a short answer. By
default he reads it aloud to you. He can also carry a letter of yours to the
door and bring back the reply.

## What really happens

`curl` transfers data to or from a URL over HTTP, HTTPS and many other
protocols. It prints the response body to standard output. `-o` saves it to a
file, `-I` shows only the headers, `-L` follows redirects. `-X POST` with
`-d` or `--data` sends data, which can change things on the server.

## Try it

```console
$ curl -s https://example.com | head -n 4
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
```

## Margin notes

| Write              | It means                                         |
|--------------------|--------------------------------------------------|
| `curl url`         | Fetch it and read it to me                       |
| `curl -o a url`    | Fetch it and write it onto sheet a               |
| `curl -I url`      | Only tell me what's on the envelope              |
| `curl -X POST -d ...` | Carry my letter there; it may change things   |

## When an agent asks

Fetching a page or calling an API is usually fine. Look for three things: a
`| sh` or `| bash` at the end, data being sent with `-d`, and keys or
passwords written into the instruction.

## Careful

- `curl ... | sh` runs a stranger's instructions unread. Fetch to a sheet, read it, then decide.
- A key written in the instruction ends up in your shell history.
