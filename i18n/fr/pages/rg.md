---
command: rg
title: Le Tamis rotatif
metaphor: >
  Un tamis à farine à manivelle, cousin plus rapide du Tamis, qui passe tous les tiroirs d'un coup et laisse de côté les feuilles que vous ne voudriez pas voir tamisées.
exercise:
  question: "Vous tapez rg secret dans le cabinet. Rien ne revient de .secret-diary.txt, alors que le mot y est écrit. Pourquoi ?"
  choices:
    - "rg ne sait pas lire les feuilles qui finissent par .txt"
    - "Le journal est derrière le double fond, et rg saute les feuilles cachées sauf si on lui dit --hidden"
    - "Le journal est vide"
  explanation: "rg laisse de côté les feuilles cachées, celles que le copie-lettres ignore et les fichiers binaires illisibles. Le silence de rg ne vaut que pour les feuilles qu'il a regardées."
---

## En une ligne

`rg` (ripgrep) cherche un mot dans tous les fichiers sous un dossier, très vite.

## L'image

Le Tamis prend une feuille à la fois, sauf si on lui dit autre chose. Le tamis
rotatif, lui, a une manivelle : tournez-la, et tous les tiroirs placés sous le
vôtre passent dans les mailles, vite. Il fait aussi le tri. Les feuilles
derrière le double fond, et celles que le copie-lettres doit ignorer, sont
mises de côté sans être tamisées. Ce qui reste dans les mailles vous est lu,
groupé par feuille, chaque ligne avec son numéro.

## Ce qui se passe vraiment

Par défaut, `rg` cherche récursivement à partir du dossier courant, avec des
expressions régulières (des motifs aux caractères spéciaux). Il saute les
fichiers cachés, les fichiers listés dans `.gitignore` et les fichiers
d'exclusion semblables, et les fichiers binaires. Il fouille plusieurs
fichiers en parallèle, si bien que les résultats arrivent dans n'importe quel
ordre. Quand il reçoit ce qui coule de l'entonnoir (`|`) et aucun chemin, il
cherche là-dedans. Comme `grep`, il se termine avec le code 1 quand rien ne
correspond.

## Essayez

```console
$ rg grandma
notes.txt
2:call grandma
$ rg -l flour
notes.txt
order.json
recipes/bread.txt
recipes/bread-grandma.txt
```

## Notes en marge

| Écrire             | Cela veut dire                                   |
|--------------------|--------------------------------------------------|
| `rg -i word`       | Ne tenez pas compte des majuscules               |
| `rg -l word`       | Nommez seulement les feuilles qui le contiennent |
| `rg -F 'a.b'`      | Cherchez exactement ces caractères, sans motif   |
| `rg -g '*.txt' word` | Ne tamisez que les feuilles dont le nom correspond |
| `rg --hidden word` | Tamisez aussi les feuilles derrière le double fond |

## Quand un agent demande

`rg` est la recherche que les agents utilisent le plus ; l'outil de recherche
de Claude lui-même repose dessus. Les agents le lancent pour trouver chaque
endroit où un nom apparaît avant de le changer. La commande ne fait que lire.
Regardez à deux fois `--hidden`, `-u` ou `-uu` : ils passent derrière le
double fond et dans les feuilles ignorées, là où vivent souvent les fichiers
`.env` et les clés, et ce qu'ils trouvent atterrit dans la conversation de
l'agent.

## Attention

- Ici, `-r` ne veut pas dire récursif comme pour `grep`. Il veut dire `--replace`, qui ne change que ce qui vous est lu, jamais la feuille.
- « Aucun résultat » veut dire aucun parmi les feuilles que rg a regardées. Les feuilles ignorées et cachées n'ont jamais été fouillées.
