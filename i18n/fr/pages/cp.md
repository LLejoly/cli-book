---
command: cp
title: Le Papier carbone
metaphor: >
  Une feuille de papier carbone glissée sous une feuille : vous obtenez l'original et une copie exacte.
exercise:
  question: "notes-copy.txt existe déjà. Que fait cp notes.txt notes-copy.txt ?"
  choices:
    - "Vous demande d'abord"
    - "Écrit par-dessus notes-copy.txt sans un mot"
    - "Crée plutôt notes-copy-2.txt"
  explanation: "cp remplace sans bruit une feuille du même nom. Ajoutez -i pour qu'il demande, ou -n pour qu'il refuse."
---

## En une ligne

`cp` fait une copie d'un fichier ou d'un dossier.

## L'image

Vous glissez un papier carbone sous une feuille, vous repassez une fois sur
les mots, et vous voilà avec deux feuilles identiques. L'original reste à sa
place. Si une feuille portait déjà le nouveau nom, la copie se pose dessus et
les anciens mots sont perdus.

## Ce qui se passe vraiment

`cp` copie un fichier source vers un chemin de destination, ou plusieurs
sources dans un répertoire de destination. Un fichier de destination qui
existe déjà est écrasé sans avertissement. Les répertoires demandent `-r`.
`-a` conserve les dates et les permissions : c'est ce qu'il vous faut pour une
sauvegarde.

## Essayez

```console
$ cp notes.txt notes-copy.txt
$ cp -r letters letters-backup
$ ls
letters  letters-backup  notes-copy.txt  notes.txt  recipes
```

## Notes en marge

| Écrire         | Cela veut dire                                            |
|----------------|-----------------------------------------------------------|
| `cp -i a b`    | Me demander avant d'écrire par-dessus une feuille existante |
| `cp -n a b`    | Ne jamais écrire par-dessus une feuille existante         |
| `cp -r a b`    | Copier tout un tiroir et tout ce qu'il contient           |
| `cp -a a b`    | Copier un tiroir à l'identique, dates et serrures comprises |

## Quand un agent demande

Les agents copient des fichiers pour faire une sauvegarde avant une
modification, ou pour partir d'un modèle. Ce sont deux bonnes habitudes.
Vérifiez la destination : si ce nom est déjà pris, l'ancienne feuille sera
remplacée.

## Attention

- L'écrasement se fait en silence. Copier sur le mauvais nom détruit cette feuille.
- `cp -r` sur un grand tiroir peut remplir votre cabinet. Vérifiez d'abord sa taille.
