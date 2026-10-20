---
command: git clone
title: Le Livre emprunté
metaphor: >
  Emprunter le copie-lettres d'une autre maison et en faire votre propre copie complète, chaque page et chaque brouillon.
exercise:
  question: "Vous clonez le projet d'un inconnu. Qu'est-il arrivé à votre cabinet jusqu'ici ?"
  choices:
    - "Ses ordres ont déjà été exécutés"
    - "Un nouveau tiroir contient une copie de son livre. Rien n'y a encore été exécuté."
    - "Votre propre copie-lettres a été remplacé"
  explanation: "Cloner ne fait que copier des feuilles dans un nouveau tiroir. Le danger vient plus tard, quand vous ou un agent lancez quelque chose trouvé à l'intérieur."
---

## En une ligne

`git clone` télécharge une copie complète d'un projet, avec tout son historique, dans un nouveau dossier.

## L'image

Une autre maison tient un copie-lettres sur lequel vous aimeriez travailler.
Plutôt que de le lire sur place, vous en faites une copie complète : chaque
page pressée, chaque brouillon, chaque note. La copie va dans un nouveau tiroir
de votre cabinet. Elle se souvient de la maison d'où elle vient. Vous pourrez
donc aller chercher des nouvelles plus tard.

## Ce qui se passe vraiment

`git clone` crée un nouveau dossier et télécharge tous les objets du dépôt
distant. Il déclare un dépôt distant nommé `origin` qui pointe vers lui, puis
extrait la branche par défaut. `--depth 1` ne récupère que le dernier commit,
ce qui va plus vite pour les gros projets.

## Essayez

```console
$ git clone git@github.com:you/study.git
Cloning into 'study'...
$ cd study
$ git log --oneline
244d512 Start my study
```

## Notes en marge

| Écrire                    | Cela veut dire                                |
|---------------------------|-----------------------------------------------|
| `git clone address`       | Copiez ce livre dans un nouveau tiroir, ici   |
| `git clone address name`  | Appelez plutôt le nouveau tiroir name         |
| `git clone --depth 1 ...` | Ne copiez que les dernières pages             |

## Quand un agent demande

C'est en clonant qu'un agent va chercher un projet sur lequel travailler. En
général, il n'y a pas de souci. Vérifiez l'adresse. Le risque n'est pas la
copie elle-même. C'est de lancer plus tard ses étapes d'installation ou ses
scripts sans les avoir lus.

## Attention

- Un projet cloné peut contenir des ordres qui s'exécutent quand vous le construisez ou l'installez. Traitez le code d'inconnus comme du courrier non lu.
