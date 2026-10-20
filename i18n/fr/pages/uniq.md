---
command: uniq
title: Les Guillemets de répétition
metaphor: >
  Un commis qui recopie une liste écrit des guillemets de répétition au lieu d'une ligne qui répète celle juste au-dessus : seule une répétition placée juste sous sa jumelle est remarquée.
exercise:
  question: "cut -d' ' -f1 notes.txt | uniq affiche encore deux fois buy. Pourquoi ?"
  choices:
    - "uniq ne retire que les répétitions côte à côte, et les deux lignes buy sont éloignées"
    - "uniq ignore le premier mot de chaque ligne"
    - "L'entonnoir perd les notes en marge de uniq"
  explanation: "uniq compare chaque ligne seulement à celle qui la précède. Entre les deux lignes buy, il y a call et pay, donc les deux restent. Placez sort devant, et les répétitions se retrouvent côte à côte."
---

## En une ligne

`uniq` retire une ligne quand elle répète celle qui la précède.

## L'image

Le commis recopie une liste, ligne par ligne. Avant chaque ligne, il ne jette
un œil qu'à celle juste au-dessus. Si elle dit la même chose, il écrit à la
place des guillemets de répétition („). Il ne remonte jamais plus haut sur la
page : une répétition qui vient plus tard, après une ligne différente, est
recopiée en entier. Quand il vous relit la copie, il saute les guillemets.

## Ce qui se passe vraiment

`uniq` lit des lignes dans un fichier ou sur l'entrée standard, et supprime
chaque ligne identique à la précédente. Il ne regarde jamais plus loin en
arrière, c'est pourquoi on l'emploie presque toujours sous la forme
`sort | uniq`. `-c` place un compte devant chaque ligne, `-d` n'affiche que les
lignes répétées, `-u` seulement celles qui ne l'ont pas été, et `-i` ne tient
pas compte des majuscules et des minuscules.

## Essayez

```console
$ cut -d' ' -f1 notes.txt | uniq
buy
call
pay
buy
$ cut -d' ' -f1 notes.txt | sort | uniq -c
      2 buy
      1 call
      1 pay
```

## Notes en marge

| Écrire             | Cela veut dire                                        |
|--------------------|-------------------------------------------------------|
| `sort \| uniq`     | Alignez d'abord les répétitions, puis gardez-en une   |
| `uniq -c`          | Comptez chaque ligne avec ses guillemets de répétition |
| `uniq -d`          | Lisez-moi seulement les lignes suivies de guillemets  |
| `uniq -i`          | Traitez majuscules et minuscules comme une même lettre |

## Quand un agent demande

Les agents emploient `sort | uniq -c | sort -rn` pour compter : les erreurs
les plus fréquentes d'un journal, les mots d'une liste, les auteurs du
copie-lettres. `uniq` ne fait que lire. Vérifiez que `sort` vient avant
`uniq`, sinon les comptes seront faux sans la moindre protestation, et méfiez-vous
d'un second nom de fichier après le premier.

## Attention

- `uniq a b` ne compare pas deux feuilles : il lit `a` et écrit le résultat par-dessus `b`, sans demander.
