---
command: make
title: Le Livre de ménage
metaphor: >
  Un livre de la maison rempli de recettes établies. Chaque tâche y liste ce dont elle a besoin, et l'on ne refait que celles dont les ingrédients ont changé.
exercise:
  question: "Vous lancez make deux fois de suite. Pourquoi la seconde fois dit-elle 'is up to date' ?"
  choices:
    - "make est cassé"
    - "Rien de ce dont la tâche dépend n'a changé depuis la dernière fois, il n'y a donc rien à refaire"
    - "La première fois a échoué"
  explanation: "make compare les dates : si le résultat est plus récent que tout ce qui sert à le faire, la recette n'est pas suivie de nouveau."
---

## En une ligne

`make` exécute les étapes de construction écrites dans le Makefile d'un projet, en ne refaisant que ce qui n'est plus à jour.

## L'image

Le livre de ménage contient des recettes : « la liste de courses se fait à
partir des notes, en recopiant chaque ligne qui contient *buy* ». Quand vous
demandez la liste de courses, la gouvernante vérifie les dates. Si les notes
ont changé depuis que la liste a été faite, elle suit de nouveau la recette.
Sinon, elle vous dit que c'est déjà fait.

## Ce qui se passe vraiment

`make` lit un `Makefile` fait de règles : une cible, les fichiers dont elle
dépend, et les commandes shell qui la construisent. Il compare les dates de
modification et n'exécute que les règles dont la cible manque ou est plus
ancienne que ses dépendances. `make name` construit une cible précise. `-n`
affiche les commandes sans les exécuter.

## Essayez

```console
$ make
grep buy notes.txt > shopping.txt
$ make
make: 'shopping.txt' is up to date.
$ cat shopping.txt
buy flour
buy ink
```

## Notes en marge

| Écrire         | Cela veut dire                                 |
|----------------|------------------------------------------------|
| `make`         | Suivre la première recette du livre            |
| `make test`    | Suivre la recette appelée test                 |
| `make -n`      | Lisez-moi les étapes sans les faire            |
| `make -j4`     | Laisser quatre aides travailler en même temps  |

## Quand un agent demande

`make`, `make build` ou `make test`, dans un projet que vous connaissez, c'est
la routine. Les vrais ordres sont dans le Makefile. Dans un projet inconnu,
lancez d'abord `make -n`, ou lisez-le.

## Attention

- Un Makefile est une liste d'ordres pour le shell. `make install` demande souvent `sudo` et écrit hors du projet.
