---
command: pytest
title: La Cuillère à goûter
metaphor: >
  La cuillère à goûter de la cuisinière, trempée dans chaque plat après chaque changement, pour vérifier qu'il a toujours le goût que la recette promet.
exercise:
  question: "pytest affiche .F et 1 failed, 1 passed. Qu'est-ce que cela veut dire ?"
  choices:
    - "Le projet est cassé et pytest l'a réparé"
    - "Deux vérifications ont tourné. La première a tenu ; la seconde a trouvé autre chose que ce qu'elle attendait"
    - "pytest lui-même n'a pas pu démarrer"
  explanation: "Chaque point est une vérification réussie, chaque F une vérification échouée. pytest ne fait que rendre compte ; il ne change rien pour réparer l'échec. Lire l'échec vous dit, à vous ou à Hobbs, où regarder."
---

## En une ligne

`pytest` lance les tests d'un projet Python : de petites vérifications que le code fait toujours ce qu'il doit.

## L'image

Après chaque pincée de sel, la cuisinière trempe la cuillère à goûter et
compare le plat à la recette. Chaque goûter est une vérification : juste, ou
pas juste. Elle ne répare rien avec la cuillère. Elle vous dit seulement quel
plat reprendre.

## Ce qui se passe vraiment

`pytest` trouve les fichiers nommés `test_*.py` ou `*_test.py`, rassemble les
fonctions nommées `test_*` qu'ils contiennent, lance chacune, puis affiche un
point pour une réussite et un `F` pour un échec, avec les détails. Lancer des
tests, c'est lancer le code du projet, ainsi que les fichiers `conftest.py`,
avec vos droits. Il se termine avec un code de sortie non nul si quelque chose
échoue : c'est ainsi que les agents et les outils de construction le
remarquent.

## Essayez

```console
$ pytest -q
..                                                                       [100%]
2 passed in 0.01s
$ pytest -q -k ink
.                                                                        [100%]
1 passed, 1 deselected in 0.01s
```

## Notes en marge

| Écrire             | Cela veut dire                                         |
|--------------------|--------------------------------------------------------|
| `pytest -q`        | Goûtez tout, et rendez compte brièvement               |
| `pytest -x`        | Arrêtez-vous au premier plat qui a un mauvais goût     |
| `pytest -k word`   | Ne goûtez que les vérifications dont le nom contient word |
| `pytest --lf`      | Ne regoûtez que ce qui a échoué la dernière fois       |

## Quand un agent demande

Les agents lancent `pytest` après chaque modification, pour voir s'ils ont
cassé quelque chose. C'est le billet le plus ordinaire qu'ils écrivent. Dans
votre propre projet, acceptez. Dans un projet venu du dehors, les tests sont
des ordres comme les autres : jetez d'abord un œil à `conftest.py` et aux
fichiers de test. Surveillez aussi un agent qui modifie un test jusqu'à ce
qu'il passe, au lieu de corriger le code.

## Attention

- Des tests peuvent écrire des feuilles, poster des lettres ou effacer des choses, si c'est ce que quelqu'un y a écrit.
- Une réussite veut seulement dire que les vérifications écrites ont tenu. Un plat que personne n'a goûté peut encore être raté.
