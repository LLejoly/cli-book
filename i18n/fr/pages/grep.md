---
command: grep
title: Le Tamis
metaphor: >
  Un tamis de cuisine où passent toutes les lignes, et qui ne retient que celles qui contiennent votre mot.
exercise:
  question: "Qu'affiche grep -v buy notes.txt ?"
  choices:
    - "Seulement les lignes avec buy"
    - "Toutes les lignes sans buy"
    - "Le nombre de fois où buy apparaît"
  explanation: "-v retourne le tamis : il garde toutes les lignes qui ne contiennent pas le mot. -c, lui, compterait."
---

## En une ligne

`grep` trouve les lignes d'un fichier qui contiennent un mot.

## L'image

Vous versez une feuille, ligne par ligne, dans un tamis. Les lignes qui portent
votre mot restent dans les mailles, et on vous les montre. Toutes les autres
passent au travers et sont laissées de côté. La feuille elle-même ne change
jamais. Vous voyez seulement ce que le tamis a retenu.

## Ce qui se passe vraiment

`grep` cherche un motif dans chaque ligne reçue : un simple mot, ou une
expression régulière. Il affiche les lignes qui correspondent. Il lit les
fichiers que vous nommez, ou l'entrée standard si vous n'en nommez aucun. Il
se termine avec le code 0 s'il a trouvé quelque chose, et 1 sinon. Les scripts
s'en servent pour prendre des décisions.

## Essayez

```console
$ grep buy notes.txt
buy flour
buy ink
$ grep -n bank notes.txt
3:pay the bank
$ grep -r grandma .
./notes.txt:call grandma
```

## Notes en marge

| Écrire             | Cela veut dire                              |
|--------------------|---------------------------------------------|
| `grep -i word`     | Ne pas tenir compte des majuscules          |
| `grep -v word`     | Garder les lignes sans le mot               |
| `grep -n word`     | Donner le numéro de chaque ligne retenue    |
| `grep -r word .`   | Tamiser chaque feuille de chaque tiroir à partir d'ici |
| `grep -c word`     | Compter seulement les lignes retenues       |

## Quand un agent demande

Les agents utilisent `grep` sans cesse, pour trouver où une chose est citée
avant de la modifier. La commande ne fait que lire : vous pouvez accepter sans
crainte. Avec `-r` sur un grand tiroir, elle peut prendre du temps, et montrer
à l'agent une bonne partie de vos fichiers.

## Attention

- Certains caractères, comme `.`, `*` et `[`, ont un sens spécial dans un motif. Pour les chercher tels quels, utilisez `grep -F`.
