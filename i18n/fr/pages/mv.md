---
command: mv
title: La Sacoche
metaphor: >
  Une sacoche pour porter une feuille jusqu'à un autre tiroir, ou pour la rapporter avec une nouvelle étiquette.
exercise:
  question: "Que fait mv to-grandma.txt to-granny.txt ?"
  choices:
    - "Elle fait une copie nommée to-granny.txt"
    - "Elle renomme la feuille, qui reste dans le même tiroir"
    - "Elle crée un tiroir nommé to-granny.txt"
  explanation: "Déplacer une feuille vers un nouveau nom dans le même tiroir, c'est la renommer. Il ne reste qu'une seule feuille."
---

## En une ligne

`mv` déplace un fichier ailleurs, ou lui donne un nouveau nom.

## L'image

Vous glissez une feuille dans votre sacoche, vous allez jusqu'à un autre tiroir
et vous l'y déposez. Rien n'est copié : la feuille est ailleurs, voilà tout.
Renommer, c'est le même trajet sans quitter le tiroir. Vous sortez la feuille
et la remettez sous une nouvelle étiquette.

## Ce qui se passe vraiment

`mv` renomme ou déplace des fichiers et des répertoires. Sur un même système de
fichiers, il change seulement l'entrée. C'est donc instantané, même pour un
énorme répertoire. D'un disque à l'autre, il copie, puis supprime l'original.
Comme `cp`, il écrase une destination existante sans demander, sauf si vous
ajoutez `-i` ou `-n`.

## Essayez

```console
$ mv notes.txt letters/
$ ls letters
notes.txt  to-grandma.txt  to-the-bank.txt
$ mv letters/to-grandma.txt letters/to-granny.txt
```

## Notes en marge

| Écrire           | Cela veut dire                                 |
|------------------|------------------------------------------------|
| `mv a drawer/`   | Porter la feuille a dans ce tiroir             |
| `mv a b`         | Renommer la feuille a en b                     |
| `mv -i a b`      | Me demander avant de recouvrir une feuille existante |
| `mv -n a b`      | Ne jamais recouvrir une feuille existante      |

## Quand un agent demande

Les agents utilisent `mv` pour renommer ou ranger. Lisez les deux noms : le
premier est ce qui part, le dernier est l'endroit où cela arrive. Si le dernier
nom existe déjà, cette feuille est remplacée et perdue.

## Attention

- `mv a b` remplace b si b est une feuille. Si b est un tiroir, a va dedans. Une seule lettre d'écart, deux résultats.
