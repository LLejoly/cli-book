---
command: git fetch
title: Le Plateau d'argent
metaphor: >
  Le plateau d'argent posé sur la table du vestibule, où le courrier du matin attend, encore cacheté, que vous décidiez de le relier dans votre livre.
exercise:
  question: "Hobbs vient de lancer git fetch. Qu'est-ce qui a changé dans votre tiroir ?"
  choices:
    - "Chaque feuille correspond maintenant à celle de l'autre maison"
    - "Rien encore. Les nouvelles attendent dans origin/main jusqu'à ce que vous fassiez un merge ou un pull."
    - "Vos modifications non enregistrées ont été remplacées par les leurs"
  explanation: "fetch ne fait qu'apporter le courrier dans le vestibule. Vos feuilles et vos propres brouillons restent exactement comme ils étaient, jusqu'à un merge, un rebase ou un pull."
---

## En une ligne

`git fetch` télécharge ce que d'autres ont partagé, sans changer aucun de vos fichiers.

## L'image

Le courrier arrive et on le pose sur le plateau d'argent du vestibule. Rien
n'est ouvert, rien n'est relié dans votre livre. Vous pouvez regarder les
enveloppes, voir qui écrit et à quel sujet. Vous déciderez plus tard de les
relier ou non.

## Ce qui se passe vraiment

`git fetch` télécharge les nouveaux commits et les nouvelles branches d'un
dépôt distant (par défaut `origin`) et met à jour les branches de suivi, comme
`origin/main`, qui notent où en sont les brouillons de l'autre maison. Vos
propres branches, l'index et vos fichiers ne sont pas touchés. `git pull` est
un fetch suivi d'un merge ou d'un rebase ; le fetch seul vous laisse regarder
d'abord.

## Essayez

```console
$ git fetch
From github.com:you/study
   2412c63..7f3a9e1  main       -> origin/main
$ git log --oneline main..origin/main
7f3a9e1 Add sugar to the bread
```

## Notes en marge

| Écrire                         | Cela veut dire                                    |
|--------------------------------|---------------------------------------------------|
| `git fetch`                    | Faire entrer le courrier, le laisser cacheté sur le plateau |
| `git fetch --prune`            | Oublier aussi les brouillons que l'autre maison a retirés |
| `git log main..origin/main`    | Montrer les lettres que je n'ai pas encore reliées |
| `git merge origin/main`        | Maintenant, les relier dans mon livre             |

## Quand un agent demande

Les agents font un fetch pour savoir si le livre partagé a bougé, avant de
comparer, de faire un rebase ou un push. Vous pouvez accepter sans crainte :
vos feuilles ne changent pas. Vérifiez l'adresse si ce n'est pas votre
`origin` habituel. Les pages rapportées de la maison d'un inconnu sont des
papiers venus du dehors : lisez-les, ne les exécutez pas.

## Attention

- Après un fetch, `git status` peut dire que votre branche est « en retard » (behind). Vos feuilles n'ont pas encore changé : le courrier est toujours sur le plateau.
