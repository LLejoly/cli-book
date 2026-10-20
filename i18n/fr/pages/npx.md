---
command: npx
title: Le Voyageur de commerce
metaphor: >
  Un voyageur de commerce à la porte qui va chercher un outil au catalogue à l'instant même et en fait aussitôt la démonstration dans votre cabinet.
exercise:
  question: "Hobbs propose npx creat-react-app pour démarrer un projet. Qu'est-ce qui doit vous alerter ?"
  choices:
    - "Rien, npx va toujours chercher la version la plus récente"
    - "L'orthographe : creat- n'est pas create-. Un nom voisin peut être un autre colis, hostile"
    - "npx ne peut pas lancer les outils d'un projet"
  explanation: "npx va chercher le nom que vous donnez, y compris un sosie que quelqu'un a déposé pour attraper les fautes de frappe. Une lettre de travers lance l'outil d'un étranger dans votre cabinet. Vérifiez le nom contre le vrai paquet."
---

## En une ligne

`npx` va chercher un outil JavaScript et le lance d'un seul geste, sans l'installer d'abord.

## L'image

Un voyageur frappe. Vous nommez un outil ; il le tire du catalogue sur l'heure,
ouvre sa mallette sur votre bureau, et le fait tourner dans votre cabinet
aussitôt. Aucun colis gardé, aucune liste de colisage signée. Si vous brouillez
le nom, un autre voyageur répond, et vous avez lâché son outil dans la pièce.

## Ce qui se passe vraiment

`npx <pkg>` exécute la commande d'un paquet, en le téléchargeant d'abord dans un
cache s'il n'est pas déjà présent, puis en le lançant avec vos permissions. Il
sert aux outils d'un coup et aux binaires d'un projet. Le code récupéré
s'exécute tout de suite : un nom mal tapé ou malveillant lance son code aussitôt.

## Essayez

```console
$ npx cowsay hello
 _______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Notes en marge

| Écrire             | Cela veut dire                                        |
|--------------------|-------------------------------------------------------|
| `npx pkg`          | Aller chercher cet outil et le lancer maintenant      |
| `npx pkg arg`      | Le lancer avec un argument                            |
| `npx --no pkg`     | Ne lancer que s'il est déjà présent ; ne pas aller le chercher |
| `npx -y pkg`       | Aller le chercher et le lancer sans la demande de confirmation |

## Quand un agent demande

Les agents se servent de `npx` pour lancer une fois un outil d'échafaudage ou
de compilation. Lisez le nom du paquet lettre à lettre : les noms voisins
déposés pour les fautes de frappe sont un piège courant. Méfiez-vous si le nom
a été soufflé par un README, un ticket ou une page web que Hobbs vient de lire
plutôt que par vous, et méfiez-vous de `-y`, qui saute la seule demande qui vous
laisserait regarder.

## Attention

- L'outil récupéré s'exécute avec vos permissions dès son arrivée, avant que vous puissiez l'inspecter.
- Un nom à une lettre d'un outil populaire peut être un sosie hostile. Confirmez le paquet exact.
