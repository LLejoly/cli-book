---
command: git status
title: La Feuille de pointage
metaphor: >
  La feuille de pointage du commis, qui compare les tiroirs à la dernière copie pressée du copie-lettres : ce qui a changé, ce qui attend dans la corbeille à courrier, ce qui est nouveau.
exercise:
  question: "git status --short affiche ?? letters/to-aunt.txt. Que veut dire ?? ?"
  choices:
    - "La feuille est abîmée"
    - "Le copie-lettres n'a jamais vu cette feuille"
    - "La feuille attend dans la corbeille à courrier"
  explanation: "?? signale une feuille non suivie : elle est dans le tiroir, mais n'a jamais été pressée dans le copie-lettres."
---

## En une ligne

`git status` montre ce qui a changé depuis la dernière version enregistrée.

## L'image

Le cabinet tient un copie-lettres, avec une copie pressée de chaque version.
Le commis compare les tiroirs à la dernière copie du livre et remplit une
feuille de pointage. Ces feuilles-ci ont changé. Celles-là attendent dans la
corbeille à courrier d'être pressées. Et voici les nouvelles, que le livre n'a
jamais vues.

## Ce qui se passe vraiment

`git status` compare les fichiers de travail, l'index (la zone de préparation)
et le dernier commit. Il liste les fichiers préparés, ceux qui sont modifiés
mais pas encore préparés, et ceux qui ne sont pas suivis. Il indique aussi la
branche où vous êtes, et si elle est en avance ou en retard sur sa copie
distante. Il ne change rien.

## Essayez

```console
$ git status --short
 M notes.txt
?? letters/to-aunt.txt
```

## Notes en marge

| Écrire             | Cela veut dire                                |
|--------------------|-----------------------------------------------|
| `git status`       | Remplir toute la feuille de pointage          |
| `git status -s`    | La version courte, une ligne par feuille      |
| ` M` / `M `        | Modifiée, pas encore dans la corbeille / en attente dans la corbeille |
| `??`               | Une feuille que le copie-lettres n'a jamais vue |

## Quand un agent demande

Les agents lancent `git status` avant et après leur travail, pour voir ce
qu'ils ont changé. La commande ne fait que lire, et c'est très bon signe. Un
agent qui vérifie l'état garde la trace de ses propres modifications.

## Attention

- La feuille de pointage ne connaît que les tiroirs du projet tenu dans le copie-lettres, pas le cabinet tout entier.
