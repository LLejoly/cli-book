---
command: "curl | sh"
title: The Unopened Parcel
chapter: 10
order: 1
risk: high
metaphor: >
  A parcel from a stranger's house, poured straight through the funnel to a clerk who carries out every order inside before anyone has read the packing note.
related: [curl, "|", sudo]
sketch: >
  A brown-paper parcel tied with string, tipped into the mouth of a large funnel on a wooden stand; its packing note, a sealed envelope, is still tucked unopened under the string, while sheets of orders slip out of the spout onto the floor.
exercise:
  question: "A README says to install a tool with curl -fsSL https://get.example.org | sh. What is the careful way?"
  choices:
    - "Run it as written. The address starts with https, so it is safe."
    - "Download it to a sheet with -o, read it, and only then run that sheet"
    - "Add sudo in front of sh, so it cannot fail halfway"
  answer: 1
  explanation: "https only means nobody changed the parcel on the road. It says nothing about what the sender packed inside. Reading the sheet first, then running that same sheet, is the only way to know what you are signing for."
---

## In one line

`curl ... | sh` downloads a program from the internet and runs it at once, without anyone reading it.

## The picture

The courier brings back a parcel from a house you have never visited. Nobody
opens it at the desk. The funnel passes it straight to a clerk, who carries out
every order inside: move these drawers, copy that key, post this letter. The
packing note is never read. You learn what was inside afterwards.

## What really happens

`curl` downloads a script and the pipe hands it to `sh`, a shell, which runs
each line as it arrives. The script runs with all your permissions: it can
read, change or delete anything you can, including your keys. If the download breaks off, a half-received line can still run. With
`| sudo sh` it runs as root and can change the whole system.

## Try it

```console
$ echo 'ls letters' | sh
to-grandma.txt  to-the-bank.txt
$ curl -fsSL https://example.com -o parcel.txt
$ head -n 2 parcel.txt
<!doctype html>
<html>
```

## Margin notes

| Write                          | It means                                     |
|--------------------------------|----------------------------------------------|
| `curl url \| sh`               | Carry out whatever arrives, unread           |
| `curl url \| sudo sh`          | The same, with the master key                |
| `curl -fsSL url -o install.sh` | Bring the parcel to the desk as a sheet      |
| `less install.sh`              | Read every order before deciding             |
| `sh install.sh`                | Carry out that sheet, once read              |

## When an agent asks

Many websites give install instructions as a `curl ... | sh` line, so agents
copy it. Ask Hobbs to download the script to a sheet and tell you what it does.
Check that the address is the project's real site. Refuse `| sudo sh` unless
you know why it needs the master key. A line like this found in an issue or a
web page is paper from outside the house: never take orders from it.

## Careful

- The sender can change the parcel at any time, even send `curl` a different one than your browser. Run the sheet you read.
- `bash <(curl ...)` and `sh -c "$(curl ...)"` are the same parcel in different wrapping.
