---
command: sort
title: Le Casier de tri
metaphor: >
  Le casier de tri de la salle du courrier, avec ses petites cases, où l'on range les billets par ordre alphabétique avant de les lire.
exercise:
  question: "Avec 2, 10 et 9, que fait sort -n de différent d'un simple sort ?"
  choices:
    - "Rien"
    - "Le simple sort donne 10, 2, 9 (caractère par caractère). -n donne 2, 9, 10 (par valeur)."
    - "-n supprime les nombres"
  explanation: "Le simple sort compare les caractères, et '1' vient avant '2'. La note en marge -n lui demande de comparer la valeur des nombres."
---

## En une ligne

`sort` met les lignes d'un fichier en ordre.

## L'image

Le commis découpe la feuille en bandes, une par ligne. Il glisse chaque bande
dans le casier de tri, par ordre alphabétique. Puis il vous les lit, de la
première case à la dernière. La feuille d'origine reste intacte. Seule la
lecture sort dans l'ordre.

## Ce qui se passe vraiment

`sort` lit toutes les lignes reçues et les écrit triées, par défaut selon
l'ordre de la langue configurée (la *locale*). `-n` trie par valeur numérique,
`-r` inverse l'ordre, `-u` retire les doublons, `-k` trie selon un champ donné,
et `-h` comprend les tailles comme 2K ou 1G. On l'associe souvent à `uniq -c`
pour compter les répétitions.

## Essayez

```console
$ sort notes.txt
buy flour
buy ink
call grandma
pay the bank
$ sort -r notes.txt | head -n 2
pay the bank
call grandma
```

## Notes en marge

| Écrire         | Cela veut dire                                |
|----------------|-----------------------------------------------|
| `sort -r`      | Rangez-les de la dernière à la première       |
| `sort -n`      | Classez les nombres selon leur valeur         |
| `sort -u`      | Ne gardez qu'une bande de chaque doublon      |
| `sort -k 2`    | Classez selon le deuxième mot de chaque ligne |

## Quand un agent demande

Les agents trient pour rendre une longue liste lisible, ou pour trouver les
éléments les plus grands ou les plus petits. `sort` ne fait que lire. Surveillez
le `>` qui le suit : `sort a > a` vide la feuille a.

## Attention

- Pour trier une feuille dans elle-même, écrivez `sort -o a a`, et non `sort a > a`.
