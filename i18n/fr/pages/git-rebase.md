---
command: git rebase
title: Le Pot de colle
metaphor: >
  Des ciseaux et un pot de colle : vos propres pages sont découpées du brouillon et recollées après les pages les plus récentes d'un autre, chacune pressée à nouveau avec une nouvelle date.
exercise:
  question: "Vous avez fait un rebase sur une branche qu'une collègue avait déjà récupérée. Que se passe-t-il ensuite ?"
  choices:
    - "Rien. Un rebase ne touche que votre propre copie."
    - "Votre branche a maintenant d'autres commits que la sienne. Le push demande --force et peut abîmer sa copie."
    - "Git refuse de faire un rebase sur une branche déjà envoyée"
  explanation: "Le rebase remplace des commits par de nouveaux. Quiconque avait bâti sur les anciens tient maintenant des pages que le livre partagé n'a plus. Ne faites un rebase que sur des branches que personne d'autre n'utilise."
---

## En une ligne

`git rebase` déplace votre travail pour qu'il commence après le travail le plus récent d'une autre branche, en réécrivant son histoire.

## L'image

Vous découpez vos propres pages du brouillon et vous les recollez après les
pages les plus récentes de `main`. Chacune est pressée à nouveau en entrant,
avec une nouvelle date et un nouveau numéro. Le brouillon se lit désormais
comme si vous aviez commencé après elles. Les anciennes pages ne sont plus
dans le brouillon.

## Ce qui se passe vraiment

`git rebase main` prend les commits de la branche courante que `main` n'a pas
et les rejoue par-dessus `main`. Chacun devient un nouveau commit, avec un
nouveau hash, et la branche passe sur les nouveaux. Les anciens commits
restent retrouvables un temps dans `git reflog`. En cas de conflit, il
s'arrête : corrigez le fichier, faites `git add`, puis `git rebase --continue`,
ou `--abort` pour tout annuler.

## Essayez

```console
$ git switch birthday-letter
Switched to branch 'birthday-letter'
$ git log --oneline -1
c41d7e9 Write to grandma for her birthday
$ git rebase main
Successfully rebased and updated refs/heads/birthday-letter.
$ git log --oneline -3
e83b1f0 Write to grandma for her birthday
7f3a9e1 Add sugar to the bread
2412c63 Add stamps to the list
```

Même message, nouveau numéro.

## Notes en marge

| Écrire                   | Cela veut dire                                     |
|--------------------------|----------------------------------------------------|
| `git rebase main`        | Recoller mes pages après les plus récentes de `main` |
| `git rebase --continue`  | J'ai tranché le conflit ; continuez                |
| `git rebase --abort`     | Arrêter, et remettre le brouillon comme il était   |
| `git rebase -i main`     | Me laisser réordonner, réunir ou retirer des pages. Plus risqué |
| `git reflog`             | Où l'on retrouve encore les anciennes pages        |

## Quand un agent demande

Les agents font un rebase pour ranger leur branche avant une pull request, ou
pour la mettre à jour sans page de jonction. C'est bien sur une branche que
seul l'agent a utilisée. Vérifiez la branche : jamais de rebase sur `main`, ni
sur une branche que d'autres ont récupérée. Si le billet suivant est
`git push --force`, l'histoire a été réécrite : lisez Les Pages arrachées
avant de signer.

## Attention

- Le rebase réécrit l'histoire. Sur une branche partagée, il laisse tous les autres avec des pages qui n'existent plus.
- `-i` peut retirer des commits pour de bon, une fois que le reflog les a oubliés. Demandez ce que fait chaque ligne du plan.
