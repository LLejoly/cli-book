---
command: git push --force
title: Les Pages arrachées
metaphor: >
  Arracher des pages du copie-lettres partagé, dans une autre maison, et coller les vôtres à leur place, si bien que ce que d'autres y avaient pressé est perdu.
exercise:
  question: "Votre push est refusé parce qu'un collègue a pressé de nouvelles pages dans le livre partagé. Hobbs propose git push --force. Que deviennent les pages de votre collègue ?"
  choices:
    - "Elles sont gardées, et les vôtres sont ajoutées après"
    - "Elles sont arrachées de la branche du livre partagé"
    - "Git demande d'abord l'avis de votre collègue"
  explanation: "--force rend la branche partagée identique à la vôtre. Les pages que seule l'autre maison avait en disparaissent, et personne n'est consulté. Rapportez d'abord leurs pages chez vous, ou utilisez au moins --force-with-lease, qui refuse si quelqu'un a pressé de nouvelles pages depuis votre dernier coup d'œil."
---

## En une ligne

`git push --force` remplace la copie partagée d'un projet par la vôtre, même si cela jette le travail des autres.

## L'image

Le second copie-lettres, gardé dans une autre maison, vous renvoie votre sac
postal quand quelqu'un y a pressé des pages que vous n'avez pas lues.
`--force` est une note en marge qui dit : arrachez tout ce qui gêne et collez
mes pages. La maison obéit. Les pages de vos collègues sont arrachées, et
personne dans cette maison ne les garde.

## Ce qui se passe vraiment

`git push --force` (`-f`) place la branche distante sur votre commit local,
même si cela jette des commits qui s'y trouvaient. Les commits qui n'étaient
que sur la branche distante en disparaissent ; vos coéquipiers en ont peut-être
encore une copie dans leurs propres clones, mais git ne les prévient pas.
`--force-with-lease` n'écrase que si la branche distante est encore là où
votre dernier fetch l'a vue.

## Essayez

```console
$ git push
To github.com:you/study.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:you/study.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
$ git push --force-with-lease --dry-run
To github.com:you/study.git
 ! [rejected]        main -> main (stale info)
error: failed to push some refs to 'github.com:you/study.git'
$ git push --force --dry-run
To github.com:you/study.git
 + 5b8e0c4...9a1f3d2 main -> main (forced update)
```

## Notes en marge

| Écrire                        | Cela veut dire                                          |
|-------------------------------|---------------------------------------------------------|
| `git push --force`            | Arrachez tout ce qui gêne, collez les miennes           |
| `git push -f`                 | La même chose, en abrégé                                |
| `git push --force-with-lease` | Seulement si personne n'a pressé de pages depuis mon dernier coup d'œil |
| `git push --dry-run`          | Dites-moi ce qui se passerait, sans rien changer        |
| `git pull`                    | Rapportez d'abord leurs pages chez moi                  |

## Quand un agent demande

Les agents le demandent en général après avoir réécrit leurs propres copies,
par exemple avec `git commit --amend`, quand un push ordinaire est refusé. Sur
une branche où l'agent travaille seul, c'est souvent sans problème. Sur `main`,
ou toute branche que d'autres partagent, refusez et demandez plutôt un
`git pull`. Vérifiez le nom de la branche sur le billet, et préférez
`--force-with-lease`.

## Attention

- Les pages arrachées survivent peut-être dans le livre d'un collègue, ou nulle part. Git ne vous dit pas lequel.
- `--force-with-lease` se fie à votre dernier coup d'œil. Si un fetch a eu lieu en arrière-plan depuis, il laisse passer le push sans que vous ayez lu leurs pages.
