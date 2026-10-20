---
command: mkdir
title: Le Tiroir vide
metaphor: >
  Un menuisier qui ajuste dans le meuble un tiroir neuf et vide, avec une étiquette de laiton toute neuve.
exercise:
  question: "recipes/cakes n'existe pas encore. Que fait mkdir -p recipes/cakes/sponge ?"
  choices:
    - "Il proteste que cakes n'existe pas"
    - "Il crée cakes, puis sponge à l'intérieur"
    - "Il crée un seul tiroir nommé cakes/sponge"
  explanation: "La note en marge -p construit chaque tiroir manquant en chemin. Sans elle, mkdir refuse."
---

## En une ligne

`mkdir` crée un nouveau dossier, vide.

## L'image

Il vous faut un endroit pour ranger vos poèmes. Le menuisier ajuste un tiroir
neuf dans le meuble, vide, avec votre étiquette sur le devant. Rien d'autre
dans le cabinet n'est touché. Si un tiroir porte déjà cette étiquette, il
refuse.

## Ce qui se passe vraiment

`mkdir` (make directory, « créer un répertoire ») crée un ou plusieurs
répertoires. Il échoue si le nom existe déjà ou si le répertoire parent
manque. `-p` crée les parents manquants et ne proteste pas si le répertoire
existe déjà. Un nouveau répertoire peut être supprimé avec `rmdir` tant qu'il
est vide.

## Essayez

```console
$ mkdir poems
$ ls
letters  notes.txt  poems  recipes
$ mkdir recipes/cakes/sponge
mkdir: cannot create directory 'recipes/cakes/sponge': No such file or directory
$ mkdir -p recipes/cakes/sponge
```

## Notes en marge

| Écrire           | Cela veut dire                                |
|------------------|-----------------------------------------------|
| `mkdir name`     | Ajuster ici un tiroir neuf                    |
| `mkdir -p a/b/c` | Ajuster chaque tiroir manquant en chemin      |
| `mkdir a b`      | Ajuster deux tiroirs à la fois                |

## Quand un agent demande

Les agents créent des tiroirs pour y ranger le travail qu'ils vont faire.
C'est sans danger et facile à défaire. Regardez seulement où : un tiroir neuf
dans votre tiroir personnel, ou dans un endroit inattendu, vous dit où l'agent
compte écrire ensuite.

## Attention

- Les noms avec des espaces demandent des guillemets : `mkdir "old letters"`. Sinon, vous obtenez deux tiroirs, `old` et `letters`.
