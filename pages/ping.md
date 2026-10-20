---
command: ping
title: The Reply-Paid Card
chapter: 6
order: 2
risk: low
metaphor: >
  A reply-paid postcard sent to another house asking "are you there?", timed by the clock until the answer comes back.
related: [curl, ssh]
sketch: >
  A reply-paid double postcard with a printed stamp, the return half folded back, beside an open pocket watch on its chain.
exercise:
  question: "ping gets no reply from a house. What can you conclude?"
  choices:
    - "The house has burned down"
    - "Either it's unreachable or it chooses not to answer cards"
    - "Your own Study is broken"
  answer: 1
  explanation: "Many houses ignore these cards on purpose. Silence means 'no answer', not necessarily 'not there'."
---

## In one line

`ping` checks whether another computer can be reached, and how long the answer takes.

## The picture

You post a reply-paid card to another house: "Are you there?" You note the time
on your pocket watch. When the card comes back you note the time again. A fast
reply means a short journey. No reply means the post couldn't get there, or
the house simply ignores such cards.

## What really happens

`ping` sends ICMP echo request packets to a host and reports each echo reply
with its round-trip time, then a summary of packet loss. On Linux it runs
until stopped unless you give `-c` with a count. Firewalls often block ICMP,
so a silent host may still be up.

## Try it

```console
$ ping -c 2 example.com
PING example.com (93.184.215.14) 56(84) bytes of data.
64 bytes from 93.184.215.14: icmp_seq=1 ttl=56 time=11.2 ms
64 bytes from 93.184.215.14: icmp_seq=2 ttl=56 time=11.0 ms
```

## Margin notes

| Write              | It means                                   |
|--------------------|--------------------------------------------|
| `ping house`       | Keep sending cards until I say stop        |
| `ping -c 4 house`  | Send four cards, then stop                 |
| `time=11.2 ms`     | The card took 11 thousandths of a second   |

## When an agent asks

Agents ping to check whether the network or a server is reachable when
something fails. It only asks "are you there?" and is safe to accept.

## Careful

- Without `-c` it never stops on Linux. Ctrl+C ends it safely.
