---
command: rm
title: La Gomme
metaphor: >
  Une gomme qui efface une feuille de fond en comble, sans laisser de miettes à balayer.
exercise:
  question: "Vous lancez rm notes.txt par erreur. Où pouvez-vous récupérer la feuille ?"
  choices:
    - "Dans la corbeille à papier, comme sur un ordinateur"
    - "Nulle part dans le cabinet. Seule une sauvegarde faite avant peut vous aider."
    - "Tapez rm -undo notes.txt"
  explanation: "rm ne passe pas par la corbeille à papier. Sans sauvegarde faite au préalable, la feuille est perdue."
---

## En une ligne

`rm` supprime des fichiers pour de bon, sans passer par la corbeille à papier.

## L'image

Vous prenez la gomme et vous effacez une feuille. Sur un vrai bureau, il
resterait des miettes, peut-être une trace légère. Ici, il n'y a rien : ni
miettes, ni corbeille, ni trace. Le commis ne demande pas non plus « en
êtes-vous sûr ? ». Il efface, c'est tout.

## Ce qui se passe vraiment

`rm` retire les entrées de répertoire des fichiers que vous nommez. Il ne les
déplace pas dans une corbeille, et les outils ordinaires ne peuvent pas les
restaurer. Il refuse les répertoires, sauf si vous ajoutez `-r` (récursif), qui
supprime le répertoire et tout ce qu'il contient. `-f` (forcer) fait taire les
avertissements et les demandes de confirmation.

## Essayez

```console
$ ls
letters  notes.txt  recipes
$ rm notes.txt
$ ls
letters  recipes
$ rm recipes
rm: cannot remove 'recipes': Is a directory
```

## Notes en marge

| Écrire      | Cela veut dire                                      |
|-------------|-----------------------------------------------------|
| `rm -i`     | Me demander avant d'effacer chaque feuille          |
| `rm -r`     | Effacer un tiroir et tout ce qu'il contient         |
| `rm -f`     | Ne pas me prévenir, ne rien me demander             |
| `rm -rf`    | Effacer tout le tiroir, en silence. La forme la plus dangereuse |

## Quand un agent demande

Les agents lancent souvent `rm` pour ranger des fichiers qu'ils ont créés
eux-mêmes, comme des résultats de compilation ou des fichiers temporaires.
Avant d'accepter, lisez le chemin exact. Méfiez-vous beaucoup de `-rf` associé
à `~`, `/`, `*` ou à un chemin que vous ne reconnaissez pas.

## Attention

- `rm -rf` sur le mauvais tiroir peut effacer des années de travail en une seconde.
- Une espace égarée compte : `rm -rf ./build` efface un tiroir, `rm -rf . /build` efface celui où vous êtes.
- `*` désigne toutes les feuilles du tiroir. Lancez d'abord `ls` avec le même motif pour voir ce qui serait effacé.
