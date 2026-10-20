---
command: npm run
title: Le Carnet des commissions
metaphor: >
  Un petit carnet de commissions nommées, rangé avec la liste de colisage du projet : vous annoncez un nom, et le commis exécute les ordres écrits dessous, quels qu'ils soient.
exercise:
  question: "Hobbs demande à lancer npm test dans un projet qu'il vient de cloner depuis la maison d'un inconnu. Que savez-vous de ce qu'il va faire ?"
  choices:
    - "Il lance les tests, donc il ne fait que lire"
    - "Rien encore. test n'est qu'un nom ; les ordres qu'il désigne sont écrits dans package.json, par l'auteur du projet"
    - "npm vérifie chaque commission avant de la lancer"
  explanation: "npm run cherche le nom et confie la ligne écrite là à un shell. C'est l'auteur du projet qui a choisi cette ligne. Un simple npm run affiche chaque commission avec ses ordres : vous pouvez lire avant de signer."
---

## En une ligne

`npm run` exécute une tâche nommée qu'un projet JavaScript a notée pour lui-même.

## L'image

La liste de colisage, `package.json`, cache un petit carnet des commissions.
Chaque commission porte un nom court, comme *test* ou *build*, et une ligne
d'ordres en dessous. Vous annoncez le nom, et le commis exécute la ligne, quoi
qu'elle dise. C'est celui qui a emballé le colis qui a écrit le carnet, pas
vous.

## Ce qui se passe vraiment

`npm run <name>` lit la section `scripts` de `package.json` et lance cette
ligne dans un shell, en ajoutant `node_modules/.bin` au `PATH` pour que les
outils installés du projet soient trouvés. S'il existe des scripts nommés
`pre<name>` ou `post<name>`, ils s'exécutent avant et après. Sans nom,
`npm run` affiche chaque script avec sa commande. Les mots placés après `--`
sont transmis au script.

## Essayez

```console
$ npm run
Lifecycle scripts included in study@1.0.0:
  test
    pytest -q
available via `npm run-script`:
  count
    grep -c buy notes.txt
$ npm run count

> study@1.0.0 count
> grep -c buy notes.txt

2
```

## Notes en marge

| Écrire                 | Cela veut dire                                    |
|------------------------|---------------------------------------------------|
| `npm run`              | Lisez-moi chaque commission et ses ordres         |
| `npm run build`        | Exécutez la commission appelée build              |
| `npm test`             | Raccourci de `npm run test`                       |
| `npm run test -- -x`   | Transmettez `-x` aux ordres de la commission      |

## Quand un agent demande

Les agents lancent `npm run build`, `npm run lint` ou `npm test` après chaque
modification, pour voir si le projet fonctionne encore. Dans votre propre
projet, c'est la routine. Dans un projet que vous venez de cloner ou de
déballer, le carnet des commissions est arrivé avec le colis : lancez d'abord
un simple `npm run`, lisez les lignes, et cherchez une commission `pre`.

## Attention

- Le nom ne dit rien. Une commission appelée `test` peut poster vos clés vers une autre maison.
- Un outil cité dans la commission est pris dans `node_modules` : un mauvais colis installé là s'exécute lui aussi.
