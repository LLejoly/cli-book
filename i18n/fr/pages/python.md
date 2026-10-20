---
command: python
title: Le Traducteur
metaphor: >
  Un commis qui lit des ordres écrits en langage Python et exécute chaque ligne, quoi qu'elle dise.
exercise:
  question: "Un agent demande à lancer python3 cleanup.py. Quel est le risque ?"
  choices:
    - "Aucun, python ne fait que lire"
    - "Autant que ce que dit cleanup.py. Lisez la feuille ou demandez ce qu'elle fait."
    - "C'est toujours dangereux"
  explanation: "python exécute tout ce que dit le script. Le sceau appartient au script, pas à python."
---

## En une ligne

`python` lance un programme écrit en langage Python.

## L'image

Le commis traducteur lit les ordres écrits en Python. Tendez-lui une feuille,
et il exécute chaque ligne, dans l'ordre : lire des feuilles, en écrire,
poster des lettres, et même effacer. Il ne juge pas les ordres. C'est votre
rôle, avant de lui tendre la feuille.

## Ce qui se passe vraiment

`python3 script.py` démarre l'interpréteur, qui compile et exécute le script
avec les droits de votre utilisateur. `-c 'code'` lance un court extrait de
code, `-m module` lance un module installé comme `pytest` ou `http.server`.
Sans argument, il ouvre une invite interactive. Selon le système, `python` peut
désigner la version 2 ou la version 3.

## Essayez

```console
$ python3 count.py
4 things to do
$ python3 -c 'print(2 + 2)'
4
```

## Notes en marge

| Écrire                 | Cela veut dire                                |
|------------------------|-----------------------------------------------|
| `python3 sheet.py`     | Exécuter les ordres de cette feuille          |
| `python3 -c '...'`     | Exécuter ce seul ordre très court             |
| `python3 -m pytest`    | Appeler le commis qui vérifie que tout marche |
| `python3 -m venv .venv`| Installer un atelier séparé pour ce projet    |

## Quand un agent demande

Lancer des tests, ou un script que l'agent vient de vous montrer, est normal.
Pour un script que vous n'avez pas vu, demandez ce qu'il fait. Pour `-c` suivi
d'une longue ligne, lisez la ligne : elle peut tout faire.

## Attention

- Un `python3 -c` d'une seule ligne peut effacer ou poster des choses, tout comme un long script.
