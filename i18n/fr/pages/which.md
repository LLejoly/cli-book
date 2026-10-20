---
command: which
title: L'Annuaire de la maison
metaphor: >
  L'annuaire de la maison, accroché dans le vestibule, qui vous dit dans quelle pièce travaille le commis qui porte tel nom.
exercise:
  question: "python3 se comporte bizarrement. En quoi which python3 peut-il aider ?"
  choices:
    - "Il répare python3"
    - "Il montre quel python3 répond, au cas où un autre serait trouvé en premier"
    - "Il affiche la version de python3"
  explanation: "Plusieurs commis peuvent porter le même nom. La maison envoie celui qui apparaît le premier dans la liste PATH. which vous dit lequel."
---

## En une ligne

`which` indique où se trouve le programme qui répond à un nom de commande.

## L'image

Quand vous appelez « python3 », la maison envoie un commis. Mais lequel ?
L'annuaire du vestibule liste les pièces dans l'ordre où la maison les
parcourt. `which` le lit pour vous et nomme la pièce du commis qui répondra.

## Ce qui se passe vraiment

`which` parcourt dans l'ordre les répertoires listés dans la variable
d'environnement `PATH`, et affiche le premier exécutable portant ce nom. `-a`
les affiche tous. Les commandes internes du shell et les alias ne sont pas des
fichiers : dans bash, `type` ou `command -v` donnent une réponse plus complète.

## Essayez

```console
$ which python3 git
/usr/bin/python3
/usr/bin/git
```

## Notes en marge

| Écrire          | Cela veut dire                                   |
|-----------------|--------------------------------------------------|
| `which name`    | Dans quelle pièce travaille le commis appelé name |
| `which -a name` | Toutes les pièces où travaille un commis de ce nom |
| `type name`     | Est-ce un commis, une règle de la maison ou un surnom |

## Quand un agent demande

Les agents utilisent `which` pour vérifier qu'un outil est installé avant de
s'en servir. Il ne fait que lire. Il est sans danger.

## Attention

- Si `which` trouve un programme dans un tiroir inhabituel que vous ne reconnaissez pas, demandez comment il est arrivé là.
