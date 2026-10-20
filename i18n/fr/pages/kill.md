---
command: kill
title: La Clochette
metaphor: >
  Une clochette qu'on agite pour un commis désigné par son numéro, afin qu'il pose son ouvrage et s'arrête.
exercise:
  question: "Quelle différence entre kill 4188 et kill -9 4188 ?"
  choices:
    - "Aucune"
    - "La première demande poliment au commis 4188 de s'arrêter. La seconde le renvoie sur-le-champ, sans lui laisser le temps de ranger."
    - "-9 arrête neuf commis"
  explanation: "Un kill tout simple envoie TERM, qu'un commis peut intercepter pour sauver son travail. -9 (KILL) ne peut pas être intercepté. Le commis disparaît au milieu de sa phrase."
---

## En une ligne

`kill` demande à un programme en cours de s'arrêter, en le désignant par son numéro.

## L'image

Vous cherchez le numéro d'un commis sur le tableau de service, et vous
agitez la clochette pour lui. Le tintement habituel veut dire « terminez, je
vous prie, et arrêtez-vous ». Un commis bien élevé range d'abord ses papiers.
Le coup le plus fort, `-9`, le fait sortir de la pièce à l'instant, au milieu
d'une phrase, ses papiers laissés là où ils sont tombés.

## Ce qui se passe vraiment

`kill` envoie un signal à un processus, désigné par son PID. Par défaut, c'est
`TERM` (15) : il demande au programme de se terminer, et le programme peut
l'intercepter pour faire le ménage. `INT` (2) est ce qu'envoie Ctrl+C. `KILL`
(9) ne peut être ni intercepté ni ignoré, et le programme ne peut rien
sauvegarder. Vous ne pouvez viser que vos propres processus, sauf avec `sudo`.

## Essayez

```console
$ sleep 300 &
[1] 4188
$ kill 4188
[1]+  Terminated              sleep 300
```

## Notes en marge

| Écrire           | Cela veut dire                                 |
|------------------|------------------------------------------------|
| `kill 4188`      | Demander au commis 4188 de terminer et de s'arrêter |
| `kill -9 4188`   | Renvoyer le commis 4188 sur-le-champ, sans rangement |
| `pkill name`     | Sonner pour chaque commis dont la tâche porte ce nom |
| `kill -0 4188`   | Vérifier seulement que le commis 4188 est toujours là |

## Quand un agent demande

Les agents utilisent `kill` pour arrêter un serveur ou une tâche bloquée
qu'ils ont lancés. Vérifiez que le numéro est bien celui de cette tâche. Un
mauvais numéro arrête autre chose, peut-être votre éditeur, avec du travail
non enregistré.

## Attention

- `kill -9` perd tout ce que le programme n'avait pas encore enregistré. Essayez d'abord un simple `kill`.
- `pkill` choisit par nom, et peut arrêter plus de commis que prévu.
