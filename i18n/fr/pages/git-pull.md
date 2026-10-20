---
command: git pull
title: Le Courrier du matin
metaphor: >
  Le courrier du matin, qui apporte les pages que d'autres ont pressées dans le livre partagé, pour les relier ensuite dans votre propre copie.
exercise:
  question: "git pull s'arrête sur 'CONFLICT in notes.txt'. Qu'est-ce que cela veut dire ?"
  choices:
    - "notes.txt a été supprimé"
    - "Vous et quelqu'un d'autre avez modifié les mêmes lignes, et le commis ne devinera pas laquelle l'emporte"
    - "L'autre maison a refusé le courrier"
  explanation: "Quand deux personnes réécrivent les mêmes lignes, git marque les deux versions dans la feuille et attend qu'une personne tranche."
---

## En une ligne

`git pull` fait entrer les modifications que d'autres ont partagées et les fusionne dans votre copie.

## L'image

Chaque matin, le courrier apporte les pages que d'autres ont pressées dans le
livre partagé. Votre commis les relie dans votre copie, après les vôtres. Si
quelqu'un a réécrit les lignes mêmes que vous avez changées, le commis pose les
deux versions côte à côte. Puis il attend que vous choisissiez.

## Ce qui se passe vraiment

`git pull` est un `git fetch` suivi d'une étape d'intégration : une fusion
(merge) par défaut, ou un rebase avec `--rebase`. Il fait une avance rapide
(fast-forward) quand vous n'avez aucun commit local. Si les mêmes lignes ont
changé des deux côtés, il s'arrête sur un conflit. Il écrit alors les
marqueurs `<<<<<<<`, `=======` et `>>>>>>>` dans le fichier.

## Essayez

```console
$ git pull
Updating 2412c63..7f3a9e1
Fast-forward
 recipes/bread.txt | 1 +
 1 file changed, 1 insertion(+)
```

## Notes en marge

| Écrire               | Cela veut dire                                          |
|----------------------|---------------------------------------------------------|
| `git pull`           | Faites entrer le courrier et reliez-le dans mon livre   |
| `git pull --rebase`  | Reliez d'abord le leur, puis pressez à nouveau le mien après |
| `git fetch`          | Ramassez le courrier, sans le relier tout de suite      |

## Quand un agent demande

Faire un pull avant de se mettre au travail est une bonne habitude. Si cela
finit par un conflit, l'agent doit choisir entre les lignes de deux personnes.
Demandez-lui ce qu'il a choisi, et pourquoi.

## Attention

- Avec des modifications non enregistrées dans le tiroir, un pull peut refuser de démarrer. Faites d'abord un commit, ou mettez-les de côté.
