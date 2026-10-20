---
command: tar
title: La Liasse et la Ficelle
metaphor: >
  Nouer une pile de feuilles en une seule liasse avec de la ficelle, puis la dénouer plus tard pour les étaler de nouveau.
exercise:
  question: "Quelle instruction noue le tiroir letters en une liasse ?"
  choices:
    - "tar -xzf letters.tar.gz"
    - "tar -czf letters.tar.gz letters"
    - "tar -tzf letters"
  explanation: "c veut dire créer une liasse. x en dénoue une (extraire), et t liste son contenu sans la dénouer."
---

## En une ligne

`tar` rassemble de nombreux fichiers dans un seul fichier d'archive, ou en déballe un.

## L'image

Pour envoyer un tiroir à quelqu'un, vous prenez toutes ses feuilles, vous les
empilez et vous les nouez en une seule liasse. Serrer fort la liasse, `z`, la
rend plus petite pour la poste. À l'arrivée, quelqu'un la dénoue, et les
feuilles retournent dans leurs tiroirs, rangées exactement comme avant.

## Ce qui se passe vraiment

`tar` (*tape archive*, archive sur bande) écrit des fichiers et des répertoires
dans une seule archive, et sait les en ressortir. Les premières lettres disent
quoi faire : `c` créer, `x` extraire, `t` lister. `z` ajoute la compression
gzip et `f` nomme le fichier d'archive. L'extraction écrit les fichiers dans le
répertoire courant et écrase ceux qui portent le même nom.

## Essayez

```console
$ tar -czf letters.tar.gz letters
$ tar -tzf letters.tar.gz
letters/
letters/to-the-bank.txt
letters/to-grandma.txt
```

## Notes en marge

| Écrire                | Cela veut dire                            |
|-----------------------|-------------------------------------------|
| `tar -czf b.tar.gz d` | Nouez le tiroir d en une liasse serrée b  |
| `tar -tzf b.tar.gz`   | Dites-moi ce que contient la liasse, sans la dénouer |
| `tar -xzf b.tar.gz`   | Dénouez la liasse ici                     |
| `tar -xzf b -C dir`   | Dénouez-la dans un autre tiroir           |

## Quand un agent demande

Les agents utilisent `tar` pour sauvegarder un dossier ou pour déballer quelque
chose qu'ils ont téléchargé. Avant de dénouer une liasse venue d'ailleurs,
listez-la d'abord avec `-t`. La dénouer peut remplacer des feuilles que vous
avez déjà.

## Attention

- Une liasse venue d'un inconnu peut éparpiller des feuilles partout où elle l'indique. Listez-la avant de l'extraire.
