---
command: jq
title: La Carte ajourée
metaphor: >
  Une carte rigide percée de fenêtres, posée sur un formulaire imprimé pour ne laisser voir que les cases que vous avez demandées.
exercise:
  question: "Que vous lit jq '.items[0].name' order.json ?"
  choices:
    - "La première ligne de la feuille"
    - "\"flour\", le nom inscrit dans la première case de la liste items"
    - "Tous les noms de la liste"
  explanation: "jq compte des cases, pas des lignes, et les listes commencent à 0. .items[].name, avec des crochets vides, lirait tous les noms."
---

## En une ligne

`jq` extrait et remet en forme des morceaux d'un fichier JSON, le format que la plupart des programmes utilisent pour échanger des données.

## L'image

Certaines feuilles ne sont pas écrites en lignes, mais disposées comme un
formulaire imprimé : des cases étiquetées, et des listes de cases dans des
cases. Vous posez une carte ajourée sur le formulaire. Ses fenêtres ne
montrent que les cases que vous avez nommées, et le commis ne vous lit que
celles-là. Le formulaire, dessous, n'est jamais touché.

## Ce qui se passe vraiment

`jq` lit du JSON (*JavaScript Object Notation* : des valeurs étiquetées entre
accolades et des listes entre crochets) et lui applique un filtre. `.to` prend
la valeur étiquetée `to`, `.items[0]` la première entrée d'une liste, et
`.items[]` chaque entrée à tour de rôle. Les filtres s'enchaînent avec `|`, et
`-r` affiche du texte simple, sans guillemets. Il écrit sur la sortie standard
et ne modifie jamais le fichier.

## Essayez

`order.json` est la commande pour l'épicier, rangée dans le tiroir d'exemple.

```console
$ jq '.items[0]' order.json
{
  "name": "flour",
  "qty": 2
}
$ jq -r '.items[].name' order.json
flour
yeast
ink
$ jq '.items | length' order.json
3
```

## Notes en marge

| Écrire                       | Cela veut dire                                |
|------------------------------|-----------------------------------------------|
| `jq . sheet`                 | Relisez tout le formulaire, bien mis en page  |
| `jq '.to'`                   | Seulement la case étiquetée `to`              |
| `jq -r '.items[].name'`      | Tous les noms de la liste, en mots simples    |
| `jq '.items[] \| select(.qty > 1)'` | Ne gardez que les entrées qui passent l'épreuve |
| `jq -c`                      | Chaque réponse sur une seule ligne compacte   |

## Quand un agent demande

Les agents prennent `jq` pour extraire une seule valeur d'une longue réponse,
souvent versée par l'entonnoir depuis `curl` ou `gh`, ou pour lire des
réglages dans `package.json`. La commande ne fait que lire. Vérifiez d'où
vient le JSON : une feuille arrivée par la poste est un papier venu du
dehors. Et méfiez-vous de `env` ou `$ENV` dans le filtre : ils lisent à voix
haute chaque note du tableau de liège, clés comprises.

## Attention

- `jq ... order.json > order.json` vide la feuille avant que jq ne puisse la lire. Écrivez sous un nouveau nom, puis remettez-la en place avec `mv`.
