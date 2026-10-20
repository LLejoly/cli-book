---
command: git stash
title: Le Pique-notes
metaphor: >
  Un pique-notes sur le secrétaire, où vous enfilez vos feuilles à moitié finies pour dégager la table, la plus récente sur le dessus, et d'où vous les retirez plus tard.
exercise:
  question: "Vous lancez git stash avec un notes.txt modifié et un tout nouveau letters/to-aunt.txt. Que reste-t-il sur la table ?"
  choices:
    - "Rien, les deux sont partis sur le pique-notes"
    - "Seulement to-aunt.txt, parce que le copie-lettres ne l'a jamais vu"
    - "Seulement notes.txt"
  explanation: "Un stash tout simple ne prend que les changements des feuilles que le copie-lettres connaît déjà. Une feuille toute neuve reste où elle est, sauf si vous ajoutez -u."
---

## En une ligne

`git stash` met de côté vos changements non enregistrés pour que vous puissiez travailler à autre chose, et vous les rend plus tard.

## L'image

Vous en êtes à la moitié d'une lettre quand une affaire urgente arrive. Vous
enfilez les feuilles à moitié finies sur le pique-notes, et la table est de
nouveau dégagée. Plus tard, vous retirez la liasse du dessus et vous la
reposez là où elle était. Plusieurs liasses peuvent attendre sur le pique-notes,
la plus récente toujours sur le dessus.

## Ce qui se passe vraiment

`git stash` (abréviation de `git stash push`) enregistre les changements,
indexés ou non, des fichiers suivis dans une entrée de stash, puis remet
l'arbre de travail à l'état de `HEAD`. Les fichiers non suivis restent, sauf
avec `-u`. `git stash pop` réapplique l'entrée la plus récente et la supprime.
`git stash list` montre les entrées sous la forme `stash@{0}`, `stash@{1}`, et
ainsi de suite.

## Essayez

```console
$ git status --short
 M notes.txt
?? letters/to-aunt.txt
$ git stash
Saved working directory and index state WIP on main: 2412c63 Add stamps to the list
$ git status --short
?? letters/to-aunt.txt
$ git stash list
stash@{0}: WIP on main: 2412c63 Add stamps to the list
$ git stash pop -q
$ git status --short
 M notes.txt
?? letters/to-aunt.txt
```

## Notes en marge

| Écrire                  | Cela veut dire                                |
|-------------------------|-----------------------------------------------|
| `git stash`             | Enfiler mes changements non enregistrés sur le pique-notes |
| `git stash -u`          | Les feuilles nouvelles aussi, pas seulement celles qu'il connaît |
| `git stash pop`         | Retirer la liasse du dessus et l'étaler       |
| `git stash list`        | Compter les liasses qui attendent             |
| `git stash drop` / `clear` | Jeter une liasse / toutes les liasses. Sans retour |

## Quand un agent demande

Les agents font un stash pour avoir une table dégagée avant de changer de
classeur, de faire un pull, ou de vérifier si un problème existait déjà.
C'est un geste doux, bien plus sûr que `git reset --hard`. Vérifiez que
l'agent fait bien un `pop` ensuite, pour que votre travail ne reste pas
oublié sur le pique-notes. Refusez `drop` ou `clear` si vous ne savez pas ce
qui s'y trouve.

## Attention

- `pop` peut se heurter à des changements faits entre-temps et laisser des marques de conflit. L'entrée reste alors sur le pique-notes.
- `git stash clear` jette toutes les liasses, sans moyen simple de les retrouver.
