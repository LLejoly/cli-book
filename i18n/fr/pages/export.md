---
command: export
title: Le Tableau de liège
metaphor: >
  Un tableau de liège près de la porte, où vous épinglez des notes que chaque commis envoyé au travail lira avant de commencer.
exercise:
  question: "Vous lancez export GREETING=\"good morning\", puis vous fermez la fenêtre du terminal. Que devient la note ?"
  choices:
    - "Elle reste épinglée pour toujours"
    - "Elle disparaît avec cette séance au secrétaire"
    - "Elle est écrite dans chaque feuille"
  explanation: "export n'épingle la note que pour cette séance et pour les commis qu'elle envoie. Pour la garder, il faut l'écrire dans une feuille de démarrage comme ~/.bashrc."
---

## En une ligne

`export` définit une valeur nommée que les programmes que vous lancez peuvent lire.

## L'image

Vous épinglez une carte au tableau : GREETING dit « good morning ». Chaque
commis que vous envoyez désormais jette un coup d'œil au tableau avant de
partir. Tous le savent donc. Les commis déjà sortis ne voient pas la carte.
Et le tableau est vidé quand vous quittez le secrétaire.

## Ce qui se passe vraiment

`export NAME=value` crée une variable du shell et la marque pour l'export :
elle est copiée dans l'environnement de chaque processus enfant lancé ensuite.
C'est ainsi que les programmes lisent des réglages comme `PATH`, `HOME` ou
`API_KEY`. Les changements ne durent que le temps de la session du shell, sauf
s'ils sont écrits dans un fichier de démarrage comme `~/.bashrc`.

## Essayez

```console
$ export GREETING="good morning"
$ echo $GREETING
good morning
$ sh -c 'echo "a new clerk hears: $GREETING"'
a new clerk hears: good morning
```

## Notes en marge

| Écrire             | Cela veut dire                                          |
|--------------------|---------------------------------------------------------|
| `export A=b`       | Épinglez la note A qui dit b, pour chaque commis envoyé |
| `echo $A`          | Lisez-moi ce qui est épinglé sous A                     |
| `unset A`          | Retirez la note A du tableau                            |
| `env`              | Lisez-moi toutes les notes du tableau                   |

## Quand un agent demande

Les agents utilisent `export` pour préparer un outil, par exemple pour lui
indiquer un dossier ou lui donner une clé. Vérifiez ce qui est épinglé.
Modifier `PATH` décide quels programmes s'exécutent quand on tape un nom.

## Attention

- Un secret tapé dans `export API_KEY=...` est enregistré dans l'historique du shell. Préférez un fichier protégé.
