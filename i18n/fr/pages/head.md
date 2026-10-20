---
command: head
title: Le Signet
metaphor: >
  Un ruban posé en travers d'une feuille, quelques lignes sous le haut, pour que le commis ne lise que ce qui se trouve au-dessus.
exercise:
  question: "Une feuille de registre compte 10 000 lignes. Que vous montre head ?"
  choices:
    - "Les 10 000 lignes, très vite"
    - "Les 10 premières lignes"
    - "Les 10 lignes les plus importantes"
  explanation: "head lit depuis le haut et s'arrête après 10 lignes, sauf si vous indiquez un autre nombre avec -n. Il ne sait pas ce qui est important."
---

## En une ligne

`head` montre seulement les premières lignes d'un fichier.

## L'image

La feuille est longue, et seul le début vous intéresse. Vous posez un ruban en
travers, quelques lignes plus bas, et vous demandez au commis de lire jusqu'au
ruban. Tout ce qui est dessous reste non lu. La feuille elle-même n'est pas
touchée.

## Ce qui se passe vraiment

`head` affiche les 10 premières lignes de chaque fichier, ou de l'entrée
standard. `-n N` change le nombre de lignes, et `-c N` compte en octets.
Avec le `head` de GNU, `-n -N` affiche tout sauf les N dernières lignes. Il
cesse de lire très tôt, et reste donc rapide, même sur d'énormes fichiers.

## Essayez

```console
$ head -n 2 notes.txt
buy flour
call grandma
```

## Notes en marge

| Écrire           | Cela veut dire                             |
|------------------|--------------------------------------------|
| `head sheet`     | Lisez-moi les 10 premières lignes          |
| `head -n 3`      | Lisez-moi les 3 premières lignes           |
| `head -c 100`    | Lisez-moi les 100 premiers caractères      |
| `... \| head`    | Ne me montrez que le début de la réponse du commis |

## Quand un agent demande

Les agents utilisent `head` pour jeter un œil à un fichier avant de le lire
en entier, ou pour couper court à une longue réponse avec `| head`. La
commande ne fait que lire : vous pouvez accepter sans crainte.

## Attention

- Les premières lignes ne sont pas un résumé. Un problème au milieu de la feuille n'apparaîtra pas.
