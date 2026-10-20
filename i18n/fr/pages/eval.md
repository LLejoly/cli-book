---
command: eval
title: L'Ordre assemblé
metaphor: >
  Le commis rassemble des bribes d'écriture, les met bout à bout en une seule phrase, puis obéit à cette phrase comme à un ordre.
exercise:
  question: "Une bribe que vous avez collée contient recipes; rm -rf ~. Vous lancez eval \"ls $scrap\". Que fait le commis ?"
  choices:
    - "Il liste un tiroir nommé « recipes; rm -rf ~ »"
    - "Il liste recipes, puis exécute l'ordre d'effacement caché dans la bribe"
    - "Il refuse, parce que le nom contient un point-virgule"
  explanation: "eval réunit les bribes en une seule ligne et exécute le tout. Le point-virgule termine le ls et commence un second ordre, destructeur. Qui a écrit la bribe a écrit vos ordres."
---

## En une ligne

`eval` construit une commande à partir de morceaux, puis exécute le résultat.

## L'image

Le commis n'agit pas sur un ordre net. Il rassemble des bribes, les met bout à
bout en une seule phrase, et obéit à ce que cette phrase dit désormais. Si une
seule bribe a été glissée du dehors, un étranger a écrit une partie de votre
ordre, et le commis ne voit pas la différence.

## Ce qui se passe vraiment

`eval` prend ses arguments, les joint avec des espaces en une seule chaîne, et
passe cette chaîne au shell pour l'analyser et l'exécuter. Toute variable y est
d'abord développée, de sorte que des caractères comme `;`, `|`, `$()` ou les
accents graves contenus dans une variable deviennent de la syntaxe shell vive,
non du texte. On peut presque toujours l'éviter.

## Essayez

```console
$ cmd="ls letters"
$ eval "$cmd"
to-grandma.txt  to-the-bank.txt
$ word="recipes; echo surprise"
$ eval "ls $word"
bread-grandma.txt  bread.txt
surprise
```

## Notes en marge

| Écrire             | Cela veut dire                                        |
|--------------------|-------------------------------------------------------|
| `eval "$cmd"`      | Assembler les morceaux et exécuter le résultat        |
| `eval echo $x`     | Développer x, puis exécuter ce qui en sort            |
| `"$cmd"` (sans eval) | Exécuter cmd comme une seule commande nette, morceaux intacts |

## Quand un agent demande

Un agent recourt à `eval` pour exécuter une commande bâtie à partir d'une
variable, souvent une valeur venue d'un fichier, d'une note d'environnement ou
d'une page web. Demandez ce qui est entré dans la chaîne. Si un morceau vient
du dehors, l'ordre est en partie écrit par un étranger. Il existe presque
toujours une voie plus simple sans `eval`.

## Attention

- Une valeur contenant `;`, `$()` ou des accents graves se transforme en ordres vifs, non en texte.
- Ne faites jamais `eval` sur quelque chose bâti à partir d'un papier venu du dehors : une note de colis, un README, un ticket, une page web.
