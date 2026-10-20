---
command: less
title: Le Tourne-page
metaphor: >
  Un long tourne-page en os qui vous laisse feuilleter une longue feuille page après page, en avant ou en arrière, sans jamais la marquer.
exercise:
  question: "Hobbs lance less notes.txt, puis reste là à attendre sans rien faire. Pourquoi ?"
  choices:
    - "La feuille est abîmée et less n'arrive pas à la lire jusqu'au bout"
    - "less attend une touche : espace pour tourner la page, q pour fermer"
    - "less recopie discrètement la feuille ailleurs"
  explanation: "less reste ouvert jusqu'à ce que quelqu'un appuie sur q. Pour vous, au secrétaire, c'est très bien. Mais un commis qui ne peut pas appuyer sur les touches attendra indéfiniment."
---

## En une ligne

`less` affiche un long fichier un écran à la fois, pour que vous le lisiez à votre rythme.

## L'image

La feuille est bien trop longue pour être lue d'un coup d'œil. Vous prenez le
tourne-page en os et vous la feuilletez : une page en avant, une page en
arrière, une recherche rapide d'un mot. C'est vous qui donnez le rythme, pas
le commis. Quand vous avez fini, vous refermez, et la feuille est exactement
comme avant.

## Ce qui se passe vraiment

`less` est un paginateur (*pager*), un programme qui montre le texte un écran
à la fois et attend vos touches. Espace descend d'une page et `b` remonte.
`/word` cherche vers l'avant, `n` saute à l'occurrence suivante, `G` va à la
fin et `q` quitte. Il ne modifie jamais le fichier. Des outils comme
`git log`, `git diff` et `man` l'ouvrent pour vous quand leur réponse dépasse
la hauteur de l'écran.

## Essayez

```console
$ less notes.txt
buy flour
call grandma
pay the bank
buy ink
notes.txt (END)
```

Appuyez sur `q` pour le fermer et revenir au secrétaire.

## Notes en marge

| Écrire             | Cela veut dire                                   |
|--------------------|--------------------------------------------------|
| `less -N sheet`    | Numérotez chaque ligne dans la marge             |
| `less -S sheet`    | Coupez les longues lignes au bord au lieu de les replier |
| `/word`, then `n`  | Trouvez un mot, puis le suivant                  |
| `q`                | Refermez la feuille                              |
| `less +F sheet`    | Restez à la fin et montrez les nouvelles lignes, comme `tail -f` |

## Quand un agent demande

Un agent a rarement besoin de `less`. La commande attend que quelqu'un appuie
sur des touches, et un agent n'a pas de doigts : elle reste donc là jusqu'à ce
qu'on l'arrête. Si un agent la demande, il voulait sans doute `cat`, `head` ou
`sed -n`. Quand `git log` ou `git diff` se bloquent de la même façon, le remède
est `git --no-pager log`, ou d'ajouter `| cat`. La commande ne fait que lire :
vous pouvez accepter sans crainte.

## Attention

- Dans `less`, `v` ouvre la feuille dans un éditeur et `!` lance une autre commande. Seules les touches simples comme espace, `b`, `/` et `q` ne font que lire.
