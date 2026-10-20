---
command: git push
title: Le Sac postal
metaphor: >
  Le sac postal qui porte vos copies fraîchement pressées jusqu'au copie-lettres partagé, gardé dans une autre maison.
exercise:
  question: "Votre push est refusé avec 'fetch first'. Qu'est-ce que cela veut dire ?"
  choices:
    - "Le livre de l'autre maison contient des copies que vous n'avez pas encore"
    - "Votre mot de passe est faux"
    - "Vos copies sont perdues"
  explanation: "Quelqu'un d'autre a pressé des copies dans le livre partagé. Vous devez d'abord rapporter les siennes chez vous (git pull) avant que votre sac puisse être ajouté."
---

## En une ligne

`git push` envoie vos versions enregistrées vers une copie partagée du projet, ailleurs.

## L'image

Votre copie-lettres est dans votre cabinet. Un second, partagé avec d'autres,
est gardé dans une autre maison. Le sac postal y porte vos copies fraîchement
pressées et les ajoute après la dernière page. Si quelqu'un a ajouté des pages
depuis votre dernier coup d'œil, la maison vous renvoie le sac. Vous devez
d'abord lire les siennes.

## Ce qui se passe vraiment

`git push` envoie les commits d'une branche locale vers un dépôt distant
(souvent `origin`, sur un hébergeur comme GitHub) et fait avancer la branche
distante. Il est refusé si le dépôt distant a des commits que vous n'avez pas.
`--force` écrase quand même la branche distante, et jette les commits que
d'autres y ont mis.

## Essayez

```console
$ git push
To github.com:you/study.git
   244d512..2412c63  main -> main
```

## Notes en marge

| Écrire                    | Cela veut dire                                     |
|---------------------------|----------------------------------------------------|
| `git push`                | Envoyez mes nouvelles copies au livre partagé      |
| `git push -u origin new`  | Envoyez un nouveau classeur et retenez où il va    |
| `git pull`                | Rapportez les copies que d'autres ont ajoutées     |
| `git push --force`        | Remplacez les pages du livre partagé par les miennes |

## Quand un agent demande

Un push rend votre travail visible aux autres : c'est une étape à accepter en
connaissance de cause. Vérifiez le nom de la branche. Refusez `--force` sur une
branche partagée comme `main`, sauf si vous en êtes certain : cela peut effacer
le travail de vos collègues.

## Attention

- Un secret envoyé a quitté la maison. Changez le mot de passe, ne vous contentez pas de supprimer le fichier.
- `--force-with-lease` est le cousin prudent de `--force`.
