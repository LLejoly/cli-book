---
command: git show
title: La Loupe
metaphor: >
  Une loupe tenue au-dessus d'une seule copie pressée du copie-lettres, pour lire cette page en entier et voir ce qui y a changé.
exercise:
  question: "Vous voulez lire notes.txt exactement tel qu'il était dans la première copie, 244d512. Quel billet fait cela ?"
  choices:
    - "git show 244d512"
    - "git show 244d512:notes.txt"
    - "git log notes.txt"
  explanation: "git show 244d512 montre la note de cette copie et ses changements. En ajoutant :notes.txt, on lit la feuille entière telle qu'elle a été pressée ce jour-là, sans toucher à la feuille d'aujourd'hui."
---

## En une ligne

`git show` affiche une version enregistrée : son message et exactement ce qu'elle a changé.

## L'image

Le copie-lettres est ouvert devant vous. Au lieu de feuilleter toutes les
pages, vous tenez la loupe au-dessus d'une seule copie pressée. Vous lisez qui
l'a signée, quand, la note écrite en dessous, et chaque ligne ajoutée ou
rayée. Quand vous relevez la loupe, le livre est tel qu'il était.

## Ce qui se passe vraiment

`git show` affiche le hash d'un commit, son auteur, sa date et son message,
suivis de son diff par rapport à son parent. Sans argument, il montre `HEAD`,
le dernier commit. `git show <commit>:<path>` affiche le contenu entier d'un
fichier tel qu'il était dans ce commit. `--stat` remplace le diff par un
résumé par fichier. Comme `git log`, il s'ouvre dans un paginateur quand la
sortie est longue.

## Essayez

```console
$ git show --oneline
2412c63 Add stamps to the list
diff --git a/notes.txt b/notes.txt
index 7cd3208..3966100 100644
--- a/notes.txt
+++ b/notes.txt
@@ -2,3 +2,4 @@ buy flour
 call grandma
 pay the bank
 buy ink
+buy stamps
$ git show 244d512:notes.txt
buy flour
call grandma
pay the bank
buy ink
```

## Notes en marge

| Écrire                  | Cela veut dire                               |
|-------------------------|----------------------------------------------|
| `git show`              | Lire la dernière copie et ce qu'elle a changé |
| `git show 244d512`      | Lire cette copie-là                          |
| `git show --stat`       | Seulement quelles feuilles ont changé, et de combien |
| `git show HEAD~1:a.txt` | La feuille a.txt telle qu'elle était une copie plus tôt |

## Quand un agent demande

Les agents utilisent `git show` pour lire un commit de près, par exemple pour
comprendre un changement avant de s'appuyer dessus, ou pour retrouver une
ancienne version d'une feuille. Cela ne fait que lire : vous pouvez accepter
sans crainte. Méfiez-vous de `git show ... > file` : le commis écrit alors sa
réponse par-dessus une feuille, et c'est un tout autre billet.

## Attention

- Si l'écran semble figé, la copie est ouverte dans un paginateur. Appuyez sur `q` pour la refermer.
