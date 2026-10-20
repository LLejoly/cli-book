---
command: node
title: Le Guide de conversation
metaphor: >
  Un commis muni d'un guide de conversation de poche pour la langue JavaScript, qui lit les ordres écrits dans cette langue et exécute chaque ligne, quoi qu'elle dise.
exercise:
  question: "Hobbs veut lancer node -e avec une longue ligne pleine de require(\"child_process\"). Que devez-vous faire ?"
  choices:
    - "Signer ; -e ne fait qu'évaluer, il ne peut rien changer"
    - "Lui demander ce que fait la ligne, et la lire : child_process permet à JavaScript de lancer n'importe quelle autre commande"
    - "Signer, mais seulement si elle tient sur une ligne"
  explanation: "Un ordre d'une seule ligne peut en faire autant qu'une feuille entière. child_process permet à node de tendre des billets à d'autres commis, y compris rm et curl : la ligne mérite donc la même lecture qu'un script."
---

## En une ligne

`node` lance un programme écrit en JavaScript, en dehors d'un navigateur web.

## L'image

Ce commis porte un guide de conversation pour JavaScript. Tendez-lui une
feuille d'ordres écrite dans cette langue, et il exécute chaque ligne, dans
l'ordre : lire des feuilles, en écrire, poster des lettres, faire travailler
d'autres commis. Comme le Traducteur, qui lit le Python, il ne juge pas les
ordres. C'est votre rôle.

## Ce qui se passe vraiment

`node file.js` démarre l'environnement Node.js, qui exécute le script avec les
droits de votre utilisateur, y compris l'accès aux fichiers, au réseau et aux
autres programmes. `-e 'code'` lance un court extrait de code, et `-p 'code'`
le lance puis affiche le résultat. `--check` vérifie seulement la grammaire du
script, sans l'exécuter. Sans argument, il ouvre une invite interactive.

## Essayez

```console
$ node count.js
4 things to do
$ node -p '2 + 2'
4
```

## Notes en marge

| Écrire                 | Cela veut dire                                   |
|------------------------|--------------------------------------------------|
| `node sheet.js`        | Exécutez les ordres de cette feuille             |
| `node -e '...'`        | Exécutez ce seul ordre très court                |
| `node -p '...'`        | Exécutez-le et lisez-moi la réponse              |
| `node --check sheet.js`| Relisez la feuille pour les fautes, sans rien faire |

## Quand un agent demande

Les agents lancent `node` pour essayer un script qu'ils viennent d'écrire, pour
démarrer le serveur d'un projet, ou pour tester une idée rapide avec `-e`.
Pour une feuille que l'agent vous a montrée, c'est la routine. Pour une
feuille venue du dehors, ou une longue ligne `-e`, lisez-la d'abord, et
cherchez `child_process`, `fs` ou des adresses d'autres maisons.

## Attention

- Un `node -e` d'une seule ligne peut effacer ou poster des choses, tout comme un long script.
- Un serveur démarré avec `node` continue de tourner jusqu'à ce que vous l'arrêtiez.
