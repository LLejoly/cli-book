---
command: ls
title: La Lanterne
metaphor: >
  Une lanterne que vous levez au-dessus d'un tiroir ouvert, pour lire les étiquettes de tout ce qu'il contient.
exercise:
  question: "Vous tapez ls dans votre tiroir du cabinet et vous ne voyez pas .secret-diary.txt. Pourquoi ?"
  choices:
    - "Il a été supprimé."
    - "Il est glissé derrière le double fond du tiroir. ls -a le montrerait."
    - "ls ne montre que les tiroirs, pas les feuilles."
  explanation: "Les noms qui commencent par un point sont cachés. ls les laisse de côté, sauf si vous ajoutez la note en marge -a."
---

## En une ligne

`ls` vous montre ce que contient un dossier.

## L'image

Vous êtes devant un tiroir ouvert, mais il fait sombre. Vous levez une
lanterne et vous lisez les étiquettes : deux tiroirs plus petits, une feuille
de notes. Rien n'est déplacé, rien n'est touché. Vous regardez, c'est tout.

## Ce qui se passe vraiment

`ls` liste le contenu d'un répertoire, par défaut celui où vous êtes. Il lit
le répertoire, mais ne change rien. Les noms qui commencent par `.` sont
cachés, sauf si vous ajoutez `-a`. Avec `-l`, il affiche aussi, pour chaque
entrée, les permissions, le propriétaire, la taille et la date de
modification.

## Essayez

```console
$ ls
letters  notes.txt  recipes
$ ls -a
.  ..  .secret-diary.txt  letters  notes.txt  recipes
$ ls letters
to-grandma.txt  to-the-bank.txt
```

## Notes en marge

| Écrire    | Cela veut dire                                   |
|-----------|--------------------------------------------------|
| `ls -a`   | Montrer aussi les feuilles cachées (noms qui commencent par `.`) |
| `ls -l`   | Liste détaillée : serrures, propriétaire, taille et date |
| `ls -lh`  | Liste détaillée, avec les tailles en Ko, Mo, Go  |
| `ls -R`   | Regarder aussi dans chaque tiroir plus petit     |

## Quand un agent demande

Un agent lance `ls` pour se repérer avant de faire quoi que ce soit. Il ne fait
que regarder : vous pouvez accepter sans crainte. Mais l'agent verra les noms
de vos fichiers. Réfléchissez-y si les noms de vos dossiers sont privés.

## Attention

- `.` veut dire « ce tiroir-ci » et `..` « le tiroir qui contient celui-ci ». Ce ne sont pas de vraies feuilles.
