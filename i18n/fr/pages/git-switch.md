---
command: git switch
title: Les Onglets du classeur
metaphor: >
  Des onglets de couleur qui marquent des brouillons séparés dans le copie-lettres, pour passer à un autre brouillon et poser ses feuilles sur le secrétaire.
exercise:
  question: "Que fait git switch -c birthday-letter ?"
  choices:
    - "Il supprime le brouillon birthday-letter"
    - "Il commence un nouveau brouillon appelé birthday-letter à partir de l'endroit où vous êtes, et l'ouvre"
    - "Il envoie le brouillon dans une autre maison"
  explanation: "-c veut dire créer. Le nouveau brouillon part d'une copie du brouillon actuel, et vous pouvez y travailler sans toucher à main."
---

## En une ligne

`git switch` vous fait passer sur une autre branche : une ligne de travail séparée, dans le même projet.

## L'image

Le copie-lettres peut contenir plusieurs brouillons à la fois, chacun dans son
classeur, marqué de son propre onglet. Quand vous ouvrez un autre onglet, les
feuilles de ce brouillon remplacent les autres sur votre secrétaire. L'autre
brouillon reste à l'abri dans le livre, intact. Il attend votre retour.

## Ce qui se passe vraiment

`git switch` place `HEAD` sur une autre branche et met les fichiers de travail
à jour pour qu'ils correspondent. `-c name` crée d'abord la branche. Si des
modifications non enregistrées risquent d'être écrasées, la commande refuse.
L'ancienne commande `git checkout name` fait la même chose. Mais `checkout`
sait aussi restaurer des fichiers, et on se trompe donc plus facilement.

## Essayez

```console
$ git switch -c birthday-letter
Switched to a new branch 'birthday-letter'
$ git branch
* birthday-letter
  main
```

## Notes en marge

| Écrire                 | Cela veut dire                                |
|------------------------|-----------------------------------------------|
| `git switch name`      | Ouvrir le brouillon qui porte cet onglet      |
| `git switch -c name`   | Commencer ici un nouveau brouillon et l'ouvrir |
| `git branch`           | Lister tous les onglets ; * marque celui qui est ouvert |
| `git switch -`         | Revenir au brouillon où j'étais avant         |

## Quand un agent demande

Les agents créent souvent leur propre branche, pour que leur travail reste à
part de `main` jusqu'à ce que vous l'approuviez. C'est une bonne habitude.
Méfiez-vous de `git checkout -- .`, qui ne change pas du tout de branche : il
jette vos modifications non enregistrées.

## Attention

- `git checkout -- file` restaure une feuille depuis le livre et efface les modifications que vous n'aviez pas enregistrées.
