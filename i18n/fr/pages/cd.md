---
command: cd
title: La Poignée de tiroir
metaphor: >
  Traverser la pièce jusqu'à un autre tiroir et l'ouvrir, pour qu'il devienne celui qui est devant vous.
exercise:
  question: "Vous êtes dans ~/study/letters. Où vous mène cd .. ?"
  choices:
    - "Dans ~/study"
    - "Au grand meuble à tiroirs /"
    - "Nulle part, .. n'est pas un vrai tiroir"
  explanation: ".. désigne toujours le tiroir qui contient celui où vous êtes. Ici, c'est ~/study."
---

## En une ligne

`cd` vous fait entrer dans un autre dossier.

## L'image

Vous refermez le tiroir qui est devant vous, vous traversez le cabinet et vous
en ouvrez un autre. Rien ne change à l'intérieur des tiroirs. Seule votre
place dans la pièce change. Chaque instruction que vous écrivez ensuite est
exécutée dans le nouveau tiroir.

## Ce qui se passe vraiment

`cd` change le répertoire de travail courant du shell. Il est intégré au
shell : ce n'est pas un programme séparé. Un chemin peut être absolu (il
commence à `/`) ou relatif à l'endroit où vous êtes. Sans argument, `cd` vous
ramène à votre répertoire personnel. `cd -` revient au répertoire précédent.

## Essayez

```console
$ cd ~/study/letters
$ ls
to-grandma.txt  to-the-bank.txt
$ cd ..
$ pwd
/home/you/study
```

## Notes en marge

| Écrire   | Cela veut dire                                       |
|----------|------------------------------------------------------|
| `cd ..`  | Reculer d'un cran, vers le tiroir qui contient celui-ci |
| `cd ~`   | Revenir à votre propre tiroir                        |
| `cd -`   | Revenir là où vous étiez juste avant                 |
| `cd /`   | Aller au grand meuble à tiroirs, qui contient tout   |

## Quand un agent demande

Un agent utilise `cd` pour se placer au bon endroit avant de travailler. Cela
ne change rien par soi-même. Ce qui compte, c'est l'instruction **suivante** :
un `rm` après un `cd` dans le mauvais tiroir efface les mauvaises feuilles.
Vérifiez où il va.

## Attention

- Un chemin qui contient des espaces doit être mis entre guillemets : `cd "old letters"`.
