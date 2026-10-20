---
command: cut
title: Le Massicot
metaphor: >
  Un massicot à plateau quadrillé et à lame articulée, réglé une fois puis abaissé, pour que chaque ligne ne garde que la même colonne.
exercise:
  question: "Vous voulez le deuxième mot de chaque ligne de notes.txt. Quel billet est le bon ?"
  choices:
    - "cut -f2 notes.txt"
    - "cut -d' ' -f2 notes.txt"
    - "cut -c2 notes.txt"
  explanation: "Sans -d, cut découpe les lignes aux tabulations, et notes.txt n'en contient aucune : -f2 affiche donc chaque ligne entière. -c2 donne la deuxième lettre, pas le deuxième mot. -d' ' lui indique que les mots sont séparés par des espaces."
---

## En une ligne

`cut` ne garde qu'une partie de chaque ligne, comme le premier mot ou les dix premières lettres.

## L'image

Le commis pose la feuille sur le massicot, règle la butée sur la bonne colonne
et abaisse la lame. Chaque ligne perd la même partie d'un seul coup, et il vous
lit ce qui reste. La feuille du tiroir n'est pas touchée. Seule sa lecture est
rognée.

## Ce qui se passe vraiment

`cut` affiche des parties choisies de chaque ligne reçue. `-f` choisit des
champs, séparés par une tabulation sauf si `-d` désigne un autre caractère,
unique. `-c` choisit des caractères selon leur position. Les intervalles
s'écrivent `2`, `1,3`, `2-` (jusqu'à la fin de la ligne) ou `-4`. Les champs
sortent dans leur ordre d'origine, quel que soit l'ordre dans lequel vous les
demandez.

## Essayez

```console
$ cut -d' ' -f1 notes.txt
buy
call
pay
buy
$ cut -d' ' -f2- notes.txt
flour
grandma
the bank
ink
```

## Notes en marge

| Écrire             | Cela veut dire                                         |
|--------------------|--------------------------------------------------------|
| `cut -d, -f2`      | Les mots sont séparés par des virgules ; gardez le deuxième |
| `cut -f1,3`        | Gardez la première et la troisième colonne (tabulations) |
| `cut -c1-10`       | Gardez les dix premières lettres de chaque ligne       |
| `cut -s`           | Laissez de côté les lignes sans aucun séparateur       |

## Quand un agent demande

Les agents emploient `cut` pour extraire une colonne d'un tableau : des noms
d'une liste, le deuxième champ d'un CSV (une feuille de valeurs séparées par
des virgules), les noms d'utilisateurs de `/etc/passwd`. `cut` ne fait que
lire. Comparez le caractère de `-d` avec celui que la feuille emploie vraiment :
s'il est faux, vous recevez des lignes entières, et l'agent risque d'en tirer
une mauvaise conclusion.

## Attention

- Deux espaces de suite comptent pour deux séparateurs : le champ suivant sort vide. Quand l'espacement varie, `awk '{print $2}'` est plus sûr.
- `cut` coupe un CSV à chaque virgule, même à l'intérieur de guillemets comme `"Smith, Ada"`.
