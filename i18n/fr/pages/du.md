---
command: du
title: Le Pèse-lettre
metaphor: >
  Un pèse-lettre en laiton qui pèse un tiroir et tout ce qu'il contient, pour savoir quels tiroirs sont les plus lourds.
exercise:
  question: "Votre disque est plein. Quelle instruction aide à trouver les tiroirs les plus lourds ?"
  choices:
    - "du -sh * | sort -h"
    - "rm -rf *"
    - "ls -a"
  explanation: "du -sh pèse chaque tiroir, et sort -h les range par taille : les plus lourds arrivent en dernier. Ensuite, c'est vous qui décidez quoi retirer."
---

## En une ligne

`du` montre la place que prennent des fichiers et des dossiers sur le disque.

## L'image

Vous posez chaque tiroir sur le pèse-lettre et lisez son poids, contenu
compris. Peser ne change rien. Cela vous dit seulement où se trouve
l'essentiel du poids dans le cabinet, avant que vous décidiez quoi
désencombrer.

## Ce qui se passe vraiment

`du` (de l'anglais « disk usage », occupation du disque) parcourt les
répertoires et indique la place occupée par chacun. `-s` affiche un seul
total par argument, `-h` utilise des unités lisibles, et `--max-depth=1` (ou
`-d 1`) descend d'un seul niveau. Les tailles comptent les blocs de disque
utilisés : même un tout petit fichier compte donc pour au moins 4K.

## Essayez

```console
$ du -sh letters recipes
4.0K	letters
8.0K	recipes
```

## Notes en marge

| Écrire               | Cela veut dire                                  |
|----------------------|-------------------------------------------------|
| `du -sh drawer`      | Peser ce tiroir, en Ko, Mo ou Go                |
| `du -sh * \| sort -h`| Peser chaque tiroir d'ici, du plus léger au plus lourd |
| `du -d 1 -h`         | Peser chaque tiroir un niveau plus bas          |

## Quand un agent demande

Les agents utilisent `du` pour trouver ce qui remplit un disque. `du` ne fait
que lire : c'est sans danger. Ce qui suit souvent, c'est un `rm` du plus gros
tiroir. Lisez donc cette étape avec attention.

## Attention

- Dans un grand cabinet, `du` sur le grand meuble à tiroirs `/` prend beaucoup de temps, et le commis proteste devant les tiroirs fermés à clé.
