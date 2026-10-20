---
command: git add
title: La Corbeille à courrier
metaphor: >
  Poser les lettres terminées dans la corbeille à courrier, près de la presse, pour les faire entrer dans la prochaine copie pressée.
exercise:
  question: "Vous avez modifié notes.txt et recipes/bread.txt, puis lancé git add notes.txt. Que contiendra le prochain commit ?"
  choices:
    - "Les deux modifications"
    - "Seulement la modification de notes.txt"
    - "Rien, add doit être suivi d'une liste de fichiers"
  explanation: "Seules les feuilles posées dans la corbeille entrent dans la prochaine copie pressée. bread.txt reste modifiée dans le tiroir, mais elle est laissée de côté."
---

## En une ligne

`git add` choisit les modifications qui entreront dans la prochaine version enregistrée.

## L'image

Avant de presser une copie dans le copie-lettres, vous choisissez les feuilles
qui y entrent. Vous les posez dans la corbeille à courrier, près de la presse.
Ce qui reste sur le secrétaire ne bouge pas : modifié, mais pas enregistré.
Rien n'est encore pressé. La corbeille est un lieu d'attente, et vous pouvez
encore en retirer des feuilles.

## Ce qui se passe vraiment

`git add` copie le contenu actuel des fichiers dans l'index (la zone de
préparation), c'est-à-dire ce que `git commit` enregistrera. Les nouveaux
fichiers deviennent suivis. `git add .` prépare tout ce qui se trouve sous le
dossier courant, et `-p` permet de choisir des parties d'un fichier.
`git restore --staged` retire un fichier de l'index.

## Essayez

```console
$ git add notes.txt
$ git status --short
M  notes.txt
?? letters/to-aunt.txt
```

## Notes en marge

| Écrire                   | Cela veut dire                                          |
|--------------------------|---------------------------------------------------------|
| `git add a`              | Posez la feuille a dans la corbeille                    |
| `git add .`              | Posez dans la corbeille chaque feuille d'ici, modifiée ou nouvelle |
| `git add -p`             | Montrez-moi chaque modification et laissez-moi choisir  |
| `git restore --staged a` | Retirez la feuille a de la corbeille                    |

## Quand un agent demande

Les agents ajoutent les fichiers qu'ils ont modifiés avant de faire un commit.
Méfiez-vous de `git add .` ou `git add -A` : ils peuvent emporter des feuilles
que vous n'avez jamais voulu partager, comme un fichier de mots de passe.

## Attention

- Une fois un secret pressé dans le copie-lettres et envoyé, il est difficile de l'en retirer. Gardez-le hors de la corbeille.
