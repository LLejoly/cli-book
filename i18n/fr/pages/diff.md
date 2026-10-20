---
command: diff
title: Les Deux Chandeliers
metaphor: >
  Deux feuilles posées côte à côte sous une paire de chandeliers, comparées ligne à ligne pour repérer ce qui diffère.
exercise:
  question: "diff répond 4a5 > 1 spoon honey. Qu'est-ce que cela veut dire ?"
  choices:
    - "Après la ligne 4 de la première feuille, la seconde feuille ajoute 1 spoon honey"
    - "La ligne 4 a été supprimée"
    - "Les deux feuilles contiennent 1 spoon honey"
  explanation: "a veut dire « added », ajouté. La flèche > désigne une ligne que seule la seconde feuille contient."
---

## En une ligne

`diff` compare deux fichiers et ne montre que les lignes qui diffèrent.

## L'image

Vous posez votre recette de pain à côté de celle de grand-mère, vous allumez
les deux bougies et vous les lisez ensemble, ligne à ligne. Vous ne dites rien
des lignes identiques. Vous montrez seulement les différences : cette ligne a
changé, celle-là a été ajoutée.

## Ce qui se passe vraiment

`diff` affiche les changements qui transformeraient le premier fichier en le
second. Les lignes marquées `<` viennent du premier fichier, celles marquées
`>` du second. Des codes comme `2c2` (changé), `4a5` (ajouté) et `3d2`
(supprimé) donnent les numéros de ligne. `-u` affiche le format « unifié »,
avec `-` et `+`, qu'utilisent les relectures de code. `diff` se termine avec
le code 1 quand les fichiers diffèrent.

## Essayez

```console
$ diff recipes/bread.txt recipes/bread-grandma.txt
2c2
< 350ml water
---
> 300ml water
4a5
> 1 spoon honey
```

## Notes en marge

| Écrire       | Cela veut dire                                        |
|--------------|-------------------------------------------------------|
| `diff a b`   | Ce qui diffère entre les feuilles a et b              |
| `diff -u a b`| Le montrer avec des - et des +, et quelques lignes autour |
| `diff -r a b`| Comparer deux tiroirs entiers                         |
| `diff -q a b`| Me dire seulement s'ils diffèrent                     |

## Quand un agent demande

Les agents utilisent `diff` pour vérifier ce qu'une modification a vraiment
changé. C'est une habitude à encourager. `diff` ne fait que lire : vous pouvez
accepter sans crainte.

## Attention

- L'ordre compte : `diff a b` et `diff b a` montrent les mêmes changements, avec les flèches inversées.
