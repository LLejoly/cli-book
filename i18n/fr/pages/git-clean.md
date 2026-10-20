---
command: git clean
title: Le Balai de la femme de chambre
metaphor: >
  Le balai de la femme de chambre, qui chasse des tiroirs chaque feuille qui n'a jamais été pressée dans le copie-lettres.
exercise:
  question: "Vous avez commencé letters/to-aunt.txt ce matin et n'avez jamais lancé git add. Hobbs lance git clean -f. Que devient la lettre ?"
  choices:
    - "Rien. git clean n'enlève que les déchets."
    - "Elle est supprimée, parce que le copie-lettres n'en a jamais eu de copie"
    - "Elle va dans la corbeille à papier"
  explanation: "git clean ne juge pas de ce qui compte. Toute feuille jamais pressée dans le livre est considérée comme volante et balayée, sans copie pour la rapporter. git clean -n l'aurait d'abord montrée dans la liste."
---

## En une ligne

`git clean` supprime tous les fichiers d'un projet que git n'a jamais été chargé de garder.

## L'image

Vous demandez à la femme de chambre de ranger les tiroirs. Elle compare chaque
feuille au copie-lettres, et chaque feuille sans copie pressée, elle la balaie :
brouillons neufs, bouts de papier, la lettre à votre tante commencée ce matin.
Les feuilles que le livre connaît restent en place. Ce qu'elle balaie ne se
retrouve plus.

## Ce qui se passe vraiment

`git clean` supprime les fichiers non suivis, ceux dont git n'a jamais entendu
parler, du répertoire courant vers le bas. Il refuse de s'exécuter sans `-f`
(forcer), `-n` (essai à blanc) ou `-i` (interactif). `-d` supprime aussi les
répertoires non suivis, `-x` supprime aussi les fichiers listés dans
`.gitignore` (la liste des feuilles que le livre doit ignorer), et `-X` ne
supprime que ceux-là. Git n'en a jamais eu de copie : il ne peut pas les
restaurer.

## Essayez

```console
$ git status --short
?? letters/to-aunt.txt
$ git clean -n
Would remove letters/to-aunt.txt
$ git clean
fatal: clean.requireForce defaults to true and neither -i, -n, nor -f given; refusing to clean
```

## Notes en marge

| Écrire           | Cela veut dire                                            |
|------------------|-----------------------------------------------------------|
| `git clean -n`   | Montrez-moi ce que vous balaieriez, et ne balayez rien    |
| `git clean -i`   | Demandez-moi feuille par feuille                          |
| `git clean -f`   | Balayez chaque feuille volante                            |
| `git clean -fd`  | Balayez aussi les tiroirs volants                         |
| `git clean -fdx` | Balayez tout, même les feuilles que le livre ignore. La forme la plus dangereuse |

## Quand un agent demande

Les agents prennent `git clean` pour repartir de zéro après une compilation
ratée, souvent avec `git reset --hard`. Demandez d'abord à Hobbs de lancer
`git clean -n` avec les mêmes notes en marge, et lisez la liste. Tout travail
que vous n'avez pas encore ajouté y figure. Refusez `-x` sauf si vous savez ce
qui est ignoré : c'est là que vivent souvent les clés et les réglages locaux.

## Attention

- Non suivi veut dire jamais pressé, pas sans importance. Le travail neuf sur lequel vous n'avez pas lancé `git add` est balayé aussi.
- `-x` balaie aussi les feuilles ignorées : fichiers `.env` qui gardent des clés, réglages locaux, outils téléchargés.
