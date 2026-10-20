---
command: tail
title: La Dernière Page
metaphor: >
  Ouvrir un registre directement à la dernière page pour lire les inscriptions les plus récentes.
exercise:
  question: "Un agent lance tail -f server.log et la commande ne semble jamais finir. Pourquoi ?"
  choices:
    - "Elle est bloquée et il faut l'arrêter tout de suite"
    - "-f continue de surveiller la feuille et lit chaque nouvelle ligne au moment où elle s'écrit"
    - "Le fichier est trop gros pour être lu"
  explanation: "-f veut dire suivre (follow). tail garde le registre ouvert à la dernière page et lit les nouvelles inscriptions à mesure qu'elles arrivent, jusqu'à ce que vous l'arrêtiez avec Ctrl+C."
---

## En une ligne

`tail` affiche les dernières lignes d'un fichier, là où se trouvent les inscriptions les plus récentes.

## L'image

Un registre se remplit du début vers la fin. Les inscriptions les plus récentes
sont donc toujours au bout. Vous l'ouvrez directement à la dernière page et
lisez les dernières lignes. Avec une note en marge, vous pouvez même rester à
cette page et regarder les nouvelles inscriptions apparaître sous la plume du
commis.

## Ce qui se passe vraiment

`tail` affiche les 10 dernières lignes de chaque fichier. `-n N` fixe le nombre
de lignes, et `-n +N` affiche de la ligne N jusqu'à la fin. `-f` garde le
fichier ouvert et affiche les nouvelles lignes à mesure qu'elles s'ajoutent.
C'est ainsi qu'on surveille des journaux (*logs*) en direct.

## Essayez

```console
$ tail -n 1 notes.txt
buy ink
$ tail -n 2 recipes/bread.txt
10g salt
7g yeast
```

## Notes en marge

| Écrire         | Cela veut dire                                     |
|----------------|----------------------------------------------------|
| `tail sheet`   | Lisez-moi les 10 dernières lignes                  |
| `tail -n 50`   | Lisez-moi les 50 dernières lignes                  |
| `tail -n +5`   | Lisez de la ligne 5 jusqu'à la fin                 |
| `tail -f`      | Restez à la dernière page et lisez les nouvelles lignes à leur arrivée |

## Quand un agent demande

Les agents utilisent `tail` pour lire la fin d'un journal quand quelque chose a
mal tourné, car l'erreur la plus récente est en bas. `tail` ne fait que lire.
Avec `-f`, il tourne jusqu'à ce qu'on l'arrête : l'agent peut donc sembler
attendre.

## Attention

- Avec `-f`, arrêtez-le avec Ctrl+C. Rien n'est perdu.
