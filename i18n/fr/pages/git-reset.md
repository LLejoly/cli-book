---
command: git reset
title: L'Effaceur d'encre
metaphor: >
  Un flacon d'effaceur d'encre qui ramène l'écriture de votre secrétaire à ce que montrait la dernière copie pressée.
exercise:
  question: "Vous avez modifié notes.txt sans faire de commit, puis lancé git reset --hard. Pouvez-vous retrouver vos modifications ?"
  choices:
    - "Oui, dans la corbeille à papier"
    - "Non. Elles n'ont jamais été pressées dans le copie-lettres, il n'existe donc aucune copie où revenir."
    - "Oui, avec git log"
  explanation: "--hard ramène le tiroir à la dernière copie pressée. Les modifications jamais enregistrées par un commit sont perdues."
---

## En une ligne

`git reset --hard` jette toutes les modifications non enregistrées et remet les fichiers dans leur dernière version enregistrée.

## L'image

Vous passez l'effaceur d'encre sur chaque feuille de votre secrétaire. L'écriture
disparaît, jusqu'à retrouver ce que montre la dernière copie pressée. Tout ce
que vous avez écrit depuis est perdu. Les copies pressées dans le copie-lettres
ne risquent rien. Le travail non pressé, si.

## Ce qui se passe vraiment

`git reset` déplace la branche courante vers un autre commit. `--soft` garde
vos modifications dans la zone de préparation (l'index). Le mode par défaut,
`--mixed`, les garde dans vos fichiers. `--hard` écrase l'index et les fichiers
pour qu'ils correspondent exactement au commit. Les fichiers non suivis restent
en place ; c'est `git clean -fd` qui les supprime.

## Essayez

```console
$ git diff --stat
 notes.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git reset --hard
HEAD is now at 244d512 Start my study
$ tail -n 1 notes.txt
buy ink
```

## Notes en marge

| Écrire                | Cela veut dire                                    |
|-----------------------|---------------------------------------------------|
| `git reset --hard`    | Effacer mon secrétaire jusqu'à la dernière copie pressée |
| `git reset --soft HEAD~1` | Défaire la dernière copie pressée, garder les feuilles dans la corbeille à courrier |
| `git restore a`       | N'effacer que la feuille a                        |
| `git stash`           | Mettre mes modifications de côté au lieu de les effacer |

## Quand un agent demande

C'est un sceau de cire rouge. Un agent peut s'en servir pour « repartir de
zéro » après une erreur. Avant d'accepter, regardez `git status` : tout ce qui
n'a pas fait l'objet d'un commit sera perdu. Proposez plutôt `git stash`, qui
met les modifications de côté sans danger.

## Attention

- `git reset --hard origin/main` jette aussi les commits que vous n'avez jamais envoyés.
- `git clean -fd` juste après efface aussi les nouvelles feuilles. Ensemble, ils vident un secrétaire entièrement.
