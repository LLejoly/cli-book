---
command: sed
title: La Plume de la correctrice
metaphor: >
  La plume rouge d'une correctrice, qui descend la feuille ligne après ligne et remplace un mot par un autre partout où il apparaît.
exercise:
  question: "Quelle différence entre sed 's/water/milk/' bread.txt et sed -i 's/water/milk/' bread.txt ?"
  choices:
    - "Aucune, les deux changent la feuille"
    - "La première lit seulement une copie corrigée. La seconde réécrit la feuille elle-même."
    - "La seconde demande une confirmation"
  explanation: "Sans -i, sed vous lit une version corrigée et laisse la feuille tranquille. Avec -i, il inscrit les corrections dans la feuille, sans retour possible."
---

## En une ligne

`sed` modifie du texte : il trouve des mots ou des lignes, puis les remplace, les supprime ou les affiche.

## L'image

La correctrice fait descendre sa plume rouge le long de la feuille. Partout où
elle voit « water », elle écrit « milk ». D'ordinaire, elle vous lit la version
corrigée et ne touche pas à l'original. Ajoutez la note en marge `-i`, et elle
corrige la feuille elle-même, à l'encre.

## Ce qui se passe vraiment

`sed` (pour *stream editor*, éditeur de flux) applique un petit script à chaque
ligne reçue. Le script le plus courant est `s/old/new/`. Il remplace la première
occurrence de chaque ligne, ou toutes avec `/g`. `-n` suivi de `p` affiche
certaines lignes : `sed -n '2,3p'` affiche les lignes 2 et 3. `-i` modifie les
fichiers sur place.

## Essayez

```console
$ sed 's/water/milk/' recipes/bread.txt
500g flour
350ml milk
10g salt
7g yeast
$ sed -n '2,3p' notes.txt
call grandma
pay the bank
```

## Notes en marge

| Écrire             | Cela veut dire                              |
|--------------------|---------------------------------------------|
| `sed 's/a/b/'`     | Lisez-la en remplaçant le premier a de chaque ligne par b |
| `sed 's/a/b/g'`    | Remplacez chaque a, pas seulement le premier |
| `sed -n '5,9p'`    | Ne me lisez que les lignes 5 à 9            |
| `sed -i ...`       | Faites les corrections dans la feuille elle-même |

## Quand un agent demande

Les agents emploient `sed -n` pour lire une partie d'un fichier, ce qui est sans
danger, et `sed -i` pour modifier des fichiers rapidement. Avec `-i`, vérifiez
le motif : un motif trop large réécrit bien plus que prévu.

## Attention

- `-i` ne garde aucune copie. Utilisez `-i.bak` pour conserver l'ancienne feuille sous le nom `name.bak`.
- Sur un Mac, `sed -i` attend un argument : `sed -i '' 's/a/b/' file`.
