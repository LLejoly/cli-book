---
command: git diff
title: Le Papier calque
metaphor: >
  Une feuille de papier calque posée sur la dernière copie pressée, qui montre exactement quels mots ont changé depuis.
exercise:
  question: "Dans git diff, que signifie une ligne qui commence par + ?"
  choices:
    - "Une ligne ajoutée depuis la dernière copie pressée"
    - "Une ligne particulièrement importante"
    - "Une ligne supprimée"
  explanation: "+ marque une ligne nouvelle dans le tiroir. - marque une ligne qui figurait dans la dernière copie pressée et qui a disparu ou changé."
---

## En une ligne

`git diff` montre exactement les lignes que vous avez modifiées depuis la dernière version enregistrée.

## L'image

Vous posez du papier calque sur la dernière copie pressée d'une feuille, et
vous comparez. Les lignes disparues sont marquées d'un moins, les nouvelles
d'un plus. Tout ce qui n'a pas changé reste tel quel. Les changements
ressortent ainsi d'eux-mêmes.

## Ce qui se passe vraiment

`git diff` compare l'arbre de travail avec l'index et affiche un diff unifié.
`--staged` compare l'index avec le dernier commit, c'est-à-dire ce qui sera
enregistré. `git diff main..branch` compare deux branches. `--stat` ne donne
qu'un résumé par fichier. Rien n'est modifié.

## Essayez

```console
$ git diff
diff --git a/notes.txt b/notes.txt
--- a/notes.txt
+++ b/notes.txt
@@ -1,4 +1,4 @@
 buy flour
 call grandma
 pay the bank
-buy ink
+buy blue ink
```

## Notes en marge

| Écrire             | Cela veut dire                                          |
|--------------------|---------------------------------------------------------|
| `git diff`         | Les modifications pas encore dans la corbeille          |
| `git diff --staged`| Les modifications qui attendent dans la corbeille       |
| `git diff --stat`  | Dites-moi seulement combien de lignes ont changé par feuille |
| `git diff a..b`    | Comparez deux classeurs                                 |

## Quand un agent demande

Un agent qui vous montre `git diff` avant un commit vous laisse vérifier son
travail. Cela ne fait que lire. C'est le meilleur moment pour relire ce qu'il
a changé.

## Attention

- Si `git diff` n'affiche rien, les modifications sont peut-être déjà dans la corbeille. Essayez `--staged`.
