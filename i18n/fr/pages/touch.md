---
command: touch
title: Le Tampon dateur
metaphor: >
  Un tampon dateur en caoutchouc qu'on appuie sur une feuille pour la marquer « vue aujourd'hui », ou sur une feuille blanche pour en commencer une nouvelle.
exercise:
  question: "postcard.txt n'existe pas. Que fait touch postcard.txt ?"
  choices:
    - "Il proteste parce que la feuille manque"
    - "Il crée une feuille vide appelée postcard.txt"
    - "Il ouvre la feuille pour qu'on y écrive"
  explanation: "Si la feuille n'existe pas, touch en pose une nouvelle, toute blanche, dans le tiroir. Si elle existe, il met seulement sa date à jour."
---

## En une ligne

`touch` crée un fichier vide, ou met à jour la date d'un fichier qui existe.

## L'image

Vous prenez le tampon dateur et l'appuyez sur une feuille. Si la feuille est
déjà dans le tiroir, seule la date dans son coin change. L'écriture reste telle
quelle. S'il n'y avait pas de feuille, vous tamponnez une feuille blanche et la
rangez dans le tiroir.

## Ce qui se passe vraiment

`touch` règle les dates d'accès et de modification d'un fichier sur l'instant
présent. Si le fichier n'existe pas, il le crée, vide. `-c` empêche cette
création. Des outils de construction comme `make` comparent ces dates. Toucher
un fichier peut donc leur faire refaire certains travaux.

## Essayez

```console
$ touch postcard.txt
$ ls -l postcard.txt
-rw-r--r-- 1 you you 0 Oct 19 09:30 postcard.txt
```

## Notes en marge

| Écrire         | Cela veut dire                                   |
|----------------|--------------------------------------------------|
| `touch a`      | Tamponnez la feuille a à la date du jour, ou commencez-la blanche |
| `touch a b c`  | Tamponnez trois feuilles d'un coup               |
| `touch -c a`   | Tamponnez-la seulement si elle existe déjà       |

## Quand un agent demande

Les agents utilisent `touch` pour créer un fichier vide avant de le remplir. Il
n'efface jamais rien de ce qui est écrit : c'est une commande douce. Le seul
changement visible sera une nouvelle feuille blanche ou une date plus récente.

## Attention

- Toucher des fichiers peut tromper les outils qui décident d'après la date ce qu'il faut refaire, et leur faire recommencer un travail.
