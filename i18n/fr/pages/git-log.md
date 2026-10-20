---
command: git log
title: Le Copie-lettres
metaphor: >
  Feuilleter le copie-lettres à rebours, de la copie la plus récente aux plus anciennes, en lisant qui a pressé chacune, quand et pourquoi.
exercise:
  question: "git log --oneline affiche deux lignes. Quelle copie a été pressée le plus récemment ?"
  choices:
    - "La ligne du haut"
    - "La ligne du bas"
    - "La liste ne permet pas de le savoir"
  explanation: "git log lit le livre de la page la plus récente vers les plus anciennes. Le commit le plus récent vient donc toujours en premier."
---

## En une ligne

`git log` liste les versions enregistrées, la plus récente d'abord, avec qui les a faites et pourquoi.

## L'image

Vous ouvrez le copie-lettres à la dernière page et vous le feuilletez à
rebours. Chaque copie porte un numéro, un nom, une date et la note écrite au
moment où elle a été pressée. Lire le livre n'y change rien.

## Ce qui se passe vraiment

`git log` parcourt l'historique des commits à rebours, depuis le commit
courant. Il montre pour chacun l'empreinte, l'auteur, la date et le message.
`--oneline` réduit chacun à une ligne, `-p` montre le diff, `-n 5` limite le
nombre, et `--graph` dessine les branches. Une longue sortie s'ouvre dans un
paginateur. Appuyez sur `q` pour en sortir.

## Essayez

```console
$ git log --oneline
2412c63 Add stamps to the list
244d512 Start my study
```

## Notes en marge

| Écrire               | Cela veut dire                                          |
|----------------------|---------------------------------------------------------|
| `git log`            | Lisez le livre depuis la dernière page                  |
| `git log --oneline`  | Une ligne par copie                                     |
| `git log -p a`       | Montrez ce qui a changé sur la feuille a dans chaque copie |
| `git log -n 3`       | Seulement les trois dernières copies                    |

## Quand un agent demande

Les agents lisent le journal pour connaître l'histoire d'un projet et la façon
dont ses messages sont rédigés. Cela ne fait que lire : vous pouvez accepter
sans crainte.

## Attention

- Si l'écran semble figé, le livre est ouvert dans un paginateur. Appuyez sur `q` pour le refermer.
