---
command: whoami
title: La Carte de visite
metaphor: >
  La carte de visite posée sur le porte-cartes d'argent du secrétaire, qui montre au nom de qui les commis travaillent en ce moment.
exercise:
  question: "Hobbs exécute whoami et la réponse est root. Qu'est-ce que cela vous apprend ?"
  choices:
    - "Rien d'important, ce n'est qu'un nom"
    - "Chaque billet signé maintenant sera exécuté avec le passe-partout du bibliothécaire en chef"
    - "Hobbs a trouvé le grand meuble à tiroirs /"
  explanation: "root est l'utilisateur tout-puissant de la maison. Toute instruction donnée sous ce nom passe toutes les serrures : une erreur peut atteindre n'importe quel tiroir du cabinet."
---

## En une ligne

`whoami` vous dit sous quel nom d'utilisateur l'ordinateur agit.

## L'image

Sur le secrétaire se trouve un petit porte-cartes d'argent, avec une carte de
visite posée dessus. Tout ce que font les commis, ils le font au nom imprimé
sur cette carte, et les serrures de chaque tiroir s'ouvrent ou restent
fermées pour ce nom. Jeter un coup d'œil à la carte ne déplace rien. Elle vous
dit seulement qui vous êtes, pour le moment.

## Ce qui se passe vraiment

`whoami` affiche le nom de l'utilisateur effectif courant. C'est la même chose
que `id -un`. L'utilisateur effectif est celui dont les droits s'appliquent :
sous `sudo`, il affiche donc `root`. Il lit et ne change rien.

## Essayez

```console
$ whoami
you
$ id
uid=1000(you) gid=1000(you) groups=1000(you)
```

## Notes en marge

| Écrire         | Cela veut dire                                   |
|----------------|--------------------------------------------------|
| `whoami`       | Quelle carte est sur le porte-cartes ?                |
| `id`           | Le nom, son numéro, et chaque groupe auquel il appartient |
| `sudo whoami`  | Montrer que le passe-partout est en usage : affiche `root` |
| `echo $HOME`   | Quel tiroir est celui de ce nom                  |

## Quand un agent demande

Un agent exécute `whoami` pour savoir sous quel utilisateur il travaille,
souvent avant d'installer quelque chose ou après une protestation au sujet
des droits. Cela ne fait que lire : vous pouvez accepter sans crainte.
Regardez aussi la réponse. Si elle dit `root`, chaque billet qui suit peut
ouvrir n'importe quelle serrure de la maison : lisez-les plus lentement. Si
l'agent est relié à une autre maison par `ssh`, le nom est celui qu'il porte
là-bas.

## Attention

- `whoami` nomme l'utilisateur effectif, pas la personne au clavier. Sous `sudo`, il dit `root`, alors que c'est vous qui avez tapé.
