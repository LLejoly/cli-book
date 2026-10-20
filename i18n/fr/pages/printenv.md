---
command: printenv
title: Le Tableau lu à voix haute
metaphor: >
  Un commis qui se plante devant le tableau de liège et lit tout haut chaque note, y compris les clés du coffre-fort qui y sont suspendues.
exercise:
  question: "Hobbs veut vérifier qu'un outil trouve ses réglages et propose printenv. Votre clé d'API est épinglée au tableau. Quel est le meilleur billet ?"
  choices:
    - "printenv, puis effacer la transcription ensuite"
    - "printenv TOOL_HOME, ou printenv | cut -d= -f1 pour ne voir que les noms"
    - "printenv convient, puisqu'il ne fait que lire"
  explanation: "printenv ne fait que lire, mais il lit tout haut : chaque valeur atterrit dans la transcription, et de là dans des journaux que vous ne contrôlez pas. Demander une seule note par son nom, ou les noms seuls, donne la réponse sans prononcer les clés."
---

## En une ligne

`printenv` montre les réglages que chaque programme que vous lancez peut lire, secrets compris.

## L'image

Le tableau de liège porte des notes pour chaque commis que vous envoyez : où
les choses sont rangées, dans quelle langue écrire, et parfois une clé du
coffre-fort, suspendue là pour qu'un commis puisse aller chercher quelque chose.
`printenv` envoie un commis lire tout haut chaque note du tableau. Quiconque est
à portée de voix entend aussi les clés.

## Ce qui se passe vraiment

`printenv` affiche les variables d'environnement du shell courant, sous forme
de lignes `NAME=value`. Si on lui donne des noms, il n'affiche que ces valeurs.
Il ne change rien, mais les clés d'API, les jetons et les mots de passe vivent
souvent dans l'environnement : sa sortie est donc un secret. Quand un agent le
lance, la sortie atterrit dans la conversation, et peut-être dans des journaux
ou les archives d'un fournisseur.

## Essayez

```console
$ printenv HOME
/home/you
$ export GREETING="good morning"
$ printenv GREETING
good morning
```

## Notes en marge

| Écrire                    | Cela veut dire                                       |
|---------------------------|------------------------------------------------------|
| `printenv`                | Lisez tout haut chaque note, clés comprises          |
| `printenv HOME`           | Lisez-moi seulement la note appelée HOME             |
| `printenv \| cut -d= -f1` | Lisez-moi les noms des notes, pas ce qu'elles disent |
| `env`                     | La même chose que `printenv` sans nom                |

## Quand un agent demande

Les agents lancent `printenv` ou `env` pour dépanner un outil qui ne trouve pas
ses réglages. Demandez à Hobbs de nommer la note dont il a besoin, ou de ne
lister que les noms. Refusez un `printenv` ou un `env` tout nu si une clé est
épinglée à votre tableau : elle serait écrite dans la transcription.

## Attention

- Une clé lue tout haut une seule fois a quitté la maison. Considérez-la comme exposée, et changez-la.
- `env`, `set` et `export -p` lisent eux aussi le tableau tout haut.
