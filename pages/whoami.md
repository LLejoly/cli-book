---
command: whoami
title: The Calling Card
chapter: 4
order: 6
risk: low
metaphor: >
  The calling card on the desk's silver tray, showing whose name the clerks are working under right now.
related: [sudo, chmod, ps]
sketch: >
  A footed silver card tray on a turned stem standing on the floor, one blank calling card with a bevelled edge lying flat on it and a second card leaning upright against its rim.
exercise:
  question: "Hobbs runs whoami and the answer is root. What does that tell you?"
  choices:
    - "Nothing important, it is only a name"
    - "Every slip signed now is carried out with the head librarian's master key"
    - "Hobbs has found the great cabinet /"
  answer: 1
  explanation: "root is the house's all-powerful user. Any instruction given under that name passes every lock, so a mistake can reach any drawer in the Study."
---

## In one line

`whoami` tells you which user name the computer is acting as.

## The picture

On the writing desk stands a small silver tray with one calling card on it.
Whatever the clerks do, they do in the name printed on that card, and the
locks of each drawer open or stay shut for that name. Glancing at the card
moves nothing. It only tells you who you are, for now.

## What really happens

`whoami` prints the user name of the current effective user ID. It is the
same as `id -un`. The effective user is the one whose permissions apply, so
under `sudo` it prints `root`. It reads and changes nothing.

## Try it

```console
$ whoami
you
$ id
uid=1000(you) gid=1000(you) groups=1000(you)
```

## Margin notes

| Write          | It means                                         |
|----------------|--------------------------------------------------|
| `whoami`       | Whose card is on the tray?                       |
| `id`           | The name, its number, and every group it belongs to |
| `sudo whoami`  | Show that the master key is in use: prints `root` |
| `echo $HOME`   | Which drawer is this name's own                  |

## When an agent asks

An agent runs `whoami` to learn which user it is working as, often before
installing something or after a permission grumble. It only reads and is safe
to accept. Look at the answer too. If it says `root`, every slip that follows
can open any lock in the house, so read them more slowly. If the agent is
connected to another house through `ssh`, the name is the one used there.

## Careful

- `whoami` names the effective user, not the person at the keyboard. Inside `sudo` it says `root`, even though you typed it.
