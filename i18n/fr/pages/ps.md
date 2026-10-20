---
command: ps
title: Le Tableau de service
metaphor: >
  Le tableau de service accroché au mur, qui liste chaque commis au travail en ce moment, avec son numéro et sa tâche en cours.
exercise:
  question: "Qu'est-ce que la colonne PID dans ps ?"
  choices:
    - "Le degré d'occupation de chaque commis"
    - "Le numéro propre à chaque commis, qui sert à l'appeler plus tard"
    - "Le prix de la tâche"
  explanation: "PID veut dire identifiant de processus. C'est ainsi qu'on désigne un commis précis, par exemple pour lui dire d'arrêter avec kill."
---

## En une ligne

`ps` liste les programmes qui tournent en ce moment.

## L'image

Chaque tâche confiée au cabinet est prise en charge par un commis. Le tableau
de service, au mur, liste les commis au travail : le numéro de chacun, depuis
combien de temps il est occupé, et ce qu'il fait. Lire le tableau ne dérange
personne.

## Ce qui se passe vraiment

`ps` donne un instantané des processus en cours. Par défaut, il montre ceux de
votre terminal actuel. `ps aux` (style BSD) ou `ps -ef` (style Unix) listent
tous les processus du système, avec leur PID, leur propriétaire, leur usage du
processeur et de la mémoire, et leur ligne de commande. Pour une vue en direct,
`top` se met à jour sans cesse.

## Essayez

```console
$ sleep 300 &
$ ps
  PID TTY          TIME CMD
 4120 pts/0    00:00:00 bash
 4188 pts/0    00:00:00 sleep
 4190 pts/0    00:00:00 ps
```

## Notes en marge

| Écrire             | Cela veut dire                                |
|--------------------|-----------------------------------------------|
| `ps`               | Les commis qui travaillent à mon secrétaire   |
| `ps aux`           | Tous les commis de la maison                  |
| `ps aux \| grep x` | Trouver les commis dont la tâche mentionne x  |
| `top`              | Un tableau qui se met à jour tout seul        |

## Quand un agent demande

Les agents utilisent `ps` pour vérifier si une chose qu'ils ont lancée tourne
encore, ou pour trouver un commis bloqué. La commande ne fait que lire. Elle est
sans danger. Un `kill` la suit souvent, alors regardez ce qui vient ensuite.

## Attention

- `ps aux` montre les lignes de commande complètes. Elles contiennent parfois un mot de passe que quelqu'un a tapé dans une commande.
