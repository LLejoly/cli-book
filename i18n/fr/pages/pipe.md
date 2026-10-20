---
command: "|"
title: L'Entonnoir
metaphor: >
  Un entonnoir qui verse tout ce qu'un commis lit à voix haute directement entre les mains du commis suivant.
exercise:
  question: "Dans ls letters | grep bank, que passe grep au tamis ?"
  choices:
    - "Les feuilles rangées dans le tiroir letters"
    - "La liste de noms que ls lit à voix haute"
    - "Toutes les feuilles du cabinet"
  explanation: "L'entonnoir transmet ce que dit le premier commis, ici une liste de noms. grep n'ouvre jamais les feuilles elles-mêmes."
---

## En une ligne

Le tube `|` envoie le résultat d'une commande dans la suivante.

## L'image

Le premier commis lit une liste. Au lieu de vous la dire, il parle dans un
entonnoir. Ses mots tombent directement entre les mains d'un second commis, qui
les travaille et vous donne le résultat. Vous pouvez aligner autant de commis
que vous voulez.

## Ce qui se passe vraiment

Le shell relie la sortie standard de la commande de gauche à l'entrée standard
de celle de droite. Les deux tournent en même temps. Les données coulent de
l'une à l'autre sans fichier temporaire. Les messages d'erreur (la sortie
d'erreur standard) ne passent pas. Ils arrivent toujours sur votre écran.

## Essayez

```console
$ ls letters | grep bank
to-the-bank.txt
$ cat notes.txt | grep buy
buy flour
buy ink
```

## Notes en marge

| Écrire       | Cela veut dire                                         |
|--------------|--------------------------------------------------------|
| `a \| b`     | Ce que dit a passe à b                                 |
| `a \| b \| c`  | Une rangée de trois commis, chacun passant au suivant |
| `a \|& b`    | Transmettre aussi les protestations (bash seulement)   |

## Quand un agent demande

L'entonnoir lui-même est sans danger. Ce qui compte, c'est le commis au bout.
Soyez très prudent quand la dernière commande est `sh`, `bash` ou `sudo`. Une
ligne comme `curl https://... | bash` va chercher des instructions sur Internet
et les fait exécuter sans que personne ne les lise.

## Attention

- Jugez une chaîne d'après son commis le plus dangereux, pas d'après le premier.
