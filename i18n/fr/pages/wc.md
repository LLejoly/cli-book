---
command: wc
title: Le Compteur
metaphor: >
  Un compteur à main en laiton, sur lequel on clique une fois par ligne, par mot ou par lettre d'une feuille.
exercise:
  question: "wc notes.txt répond 4 9 44 notes.txt. Que représente le 9 ?"
  choices:
    - "Le nombre de lignes"
    - "Le nombre de mots"
    - "La taille en kilo-octets"
  explanation: "wc répond toujours dans le même ordre : les lignes, les mots, puis les octets (à peu près les lettres, les espaces et les fins de ligne)."
---

## En une ligne

`wc` compte les lignes, les mots et les caractères d'un fichier.

## L'image

Le commis prend un compteur en laiton et parcourt la feuille. Il clique une
fois par ligne, une fois par mot et une fois par lettre. Puis il vous lit les
trois nombres. Il ne vous lit pas la feuille elle-même.

## Ce qui se passe vraiment

`wc` (*word count*, compte des mots) affiche pour chaque fichier le nombre de
lignes, de mots et d'octets, dans cet ordre, suivi du nom. `-l`, `-w` et `-c`
n'affichent qu'un seul compte. On le place souvent au bout d'un tuyau, comme
dans `grep error log | wc -l`, pour compter les lignes trouvées.

## Essayez

```console
$ wc -l notes.txt
4 notes.txt
$ wc notes.txt
 4  9 44 notes.txt
```

## Notes en marge

| Écrire          | Cela veut dire                            |
|-----------------|-------------------------------------------|
| `wc -l`         | Comptez seulement les lignes              |
| `wc -w`         | Comptez seulement les mots                |
| `wc -c`         | Comptez les octets                        |
| `... \| wc -l`  | Comptez combien de lignes le commis a dites |

## Quand un agent demande

Les agents utilisent `wc -l` pour voir la longueur d'un fichier avant de le
lire, ou pour compter des résultats. `wc` ne fait que lire. Vous pouvez
toujours accepter sans crainte.

## Attention

- Une dernière ligne sans fin de ligne n'est pas comptée par `-l` : le compte peut avoir une unité de moins.
