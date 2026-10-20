---
command: npm install
title: La Liste de colisage
metaphor: >
  Une liste de colisage rangée avec le projet, d'après laquelle on commande et déballe d'un coup tous les colis dont il a besoin.
exercise:
  question: "npm install, sans nom, annonce « added 57 packages ». D'où viennent ces 57 colis ?"
  choices:
    - "npm a choisi des colis populaires"
    - "La liste de colisage nomme quelques colis, et chacun en réclame d'autres"
    - "C'est une erreur"
  explanation: "Chaque colis de la liste peut dépendre d'autres colis, qui dépendent eux-mêmes d'autres encore. Une courte liste devient vite des dizaines de colis."
---

## En une ligne

`npm install` télécharge tous les paquets JavaScript dont un projet dit avoir besoin.

## L'image

Le projet garde une liste de colisage, `package.json`. Vous la remettez au
fournisseur. Il envoie chaque colis de la liste, plus tous les colis que ces
colis réclament à leur tour. On les déballe dans un tiroir appelé
`node_modules`. Certains colis lancent même leur petite routine d'installation
pendant le déballage.

## Ce qui se passe vraiment

Sans argument, `npm install` lit `package.json` et le fichier de verrouillage
(lockfile), puis installe toutes les dépendances dans `node_modules` en
résolvant l'arbre complet. Avec un nom, il ajoute ce paquet et le note dans la
liste. Un paquet peut définir des scripts d'installation qui s'exécutent
d'eux-mêmes, sauf si l'on donne `--ignore-scripts`.

## Essayez

```console
$ npm install
added 57 packages, and audited 58 packages in 3s
found 0 vulnerabilities
```

## Notes en marge

| Écrire                    | Cela veut dire                                 |
|---------------------------|------------------------------------------------|
| `npm install`             | Commander tout ce qui figure sur la liste      |
| `npm install name`        | Commander un colis de plus et l'ajouter à la liste |
| `npm ci`                  | Commander exactement ce que dit le lockfile, rien d'autre |
| `--ignore-scripts`        | Déballer les colis sans lancer leur installation |

## Quand un agent demande

`npm install` dans un projet de confiance est une affaire courante. Soyez plus
prudent quand l'agent ajoute un nouveau colis par son nom. Vérifiez
l'orthographe, et que le colis est bien connu.

## Attention

- Les scripts d'installation s'exécutent avec vos droits. Un mauvais colis peut lire vos feuilles.
- `npm install -g` avec `sudo` déballe les colis dans toute la maison. Évitez-le.
