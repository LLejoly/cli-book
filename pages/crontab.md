---
command: crontab
title: The Household Calendar
chapter: 9
order: 4
risk: medium
metaphor: >
  The household calendar on the kitchen wall, whose standing entries are carried out at their hour, every time, until crossed off.
related: [make, python, export]
sketch: >
  A printed wall calendar hanging from a nail beside a mantel clock, several days circled in ink with small notes written in them.
exercise:
  question: "What does the entry 0 9 * * 1 ./tidy.sh mean?"
  choices:
    - "Run tidy.sh once, now"
    - "Run tidy.sh at 9:00 every Monday"
    - "Run tidy.sh 9 times"
  answer: 1
  explanation: "The five fields are minute, hour, day of month, month and day of week. 0 9 * * 1 is 9:00 on day 1 of the week, Monday."
---

## In one line

`crontab` schedules commands to run automatically at set times.

## The picture

The household calendar holds standing entries: "every Monday at nine, tidy
the study". Nobody needs to remember. When the hour strikes, a clerk carries
out the entry, every week, until someone crosses it off.

## What really happens

`cron` is a background service that runs commands on a schedule. Each user
has a crontab, a table where each line has five time fields (minute, hour,
day of month, month, weekday) and a command. `crontab -l` lists it, `crontab
-e` edits it, `crontab -r` deletes the whole table without asking.

## Try it

```console
$ crontab -l
# m h  dom mon dow  command
0 9 * * 1 /home/you/study/tidy.sh
```

## Margin notes

| Write              | It means                                       |
|--------------------|------------------------------------------------|
| `crontab -l`       | Read me the calendar                           |
| `crontab -e`       | Open the calendar to add or change entries     |
| `crontab -r`       | Tear down the whole calendar, no question      |
| `*/15 * * * *`     | Every fifteen minutes                          |

## When an agent asks

An entry keeps running long after the conversation ends, so ask what it does
and how often. Check it on `crontab -l` afterwards. Be wary of entries that
fetch and run things from the internet.

## Careful

- `-r` sits next to `-e` on the keyboard and erases every entry at once.
