---
command: xargs
title: Le Contremaître
metaphor: >
  Un contremaître qui prend une liste de noms et confie chacun d'eux à un commis, dans une même instruction.
exercise:
  question: "Que fait find . -name '*.tmp' | xargs rm ?"
  choices:
    - "Il liste les feuilles .tmp"
    - "Il efface chaque feuille .tmp que find nomme"
    - "Rien, rm ne sait pas lire ce qui sort d'un entonnoir"
  explanation: "rm ne lit pas lui-même l'entonnoir, mais xargs transforme chaque nom reçu en argument pour rm. Chaque feuille trouvée est effacée."
---

## En une ligne

`xargs` transforme une liste d'éléments en arguments pour une autre commande.

## L'image

Certains commis, comme celui de la gomme, n'écoutent pas l'entonnoir. Il leur
faut des noms écrits sur leur billet. Le contremaître se tient au bout de
l'entonnoir. Il prend chaque nom qui arrive, l'écrit sur le billet et tend le
billet au commis. Une courte liste devient très vite beaucoup de travail.

## Ce qui se passe vraiment

`xargs` lit des éléments sur l'entrée standard, séparés par des espaces ou des
retours à la ligne. Il lance la commande donnée en ajoutant ces éléments comme
arguments, par lots. `-n 1` passe un élément par exécution, `-I {}` place
chaque élément là où figure `{}`, `-0` lit une entrée séparée par des
caractères NUL (à associer à `find -print0`), et `-P` en lance plusieurs à la
fois.

## Essayez

```console
$ ls letters | xargs -n 1 echo "write to"
write to to-grandma.txt
write to to-the-bank.txt
```

## Notes en marge

| Écrire                | Cela veut dire                                  |
|-----------------------|-------------------------------------------------|
| `... \| xargs cmd`    | Confiez chaque nom à cmd                        |
| `xargs -n 1`          | Un nom par billet                               |
| `xargs -I {} cp {} b/`| Mettez chaque nom à la place de {}              |
| `xargs -p`            | Demandez-moi avant chaque billet                |

## Quand un agent demande

Regardez la commande qui suit `xargs` : c'est ce qui sera fait à chaque
élément. `| xargs rm` ou `| xargs sed -i` peuvent modifier des centaines de
feuilles d'un coup.

## Attention

- Les noms qui contiennent des espaces sont coupés en deux. Utilisez `find ... -print0 | xargs -0`.
- Lancez d'abord la partie gauche seule, pour voir la liste que recevra le contremaître.
