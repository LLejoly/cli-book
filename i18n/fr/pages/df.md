---
command: df
title: Le Pot gradué
metaphor: >
  Un pot gradué pour chaque meuble, qui montre d'un coup d'œil à quel point il est plein et combien de place il reste.
exercise:
  question: "Quelle est la différence entre du et df ?"
  choices:
    - "Aucune"
    - "du pèse les tiroirs que vous choisissez. df dit à quel point chaque meuble entier (disque) est plein."
    - "df supprime des fichiers"
  explanation: "df regarde les disques entiers et leur espace libre. du additionne ce qu'utilisent certains dossiers précis."
---

## En une ligne

`df` montre à quel point chaque disque est plein et combien de place il reste.

## L'image

Chaque meuble de la maison a un pot gradué posé à côté de lui. Un coup d'œil
vous donne sa taille, la place occupée et la place restante. Vous n'ouvrez
aucun tiroir. Le pot ne donne que les totaux.

## Ce qui se passe vraiment

`df` (de l'anglais « disk free », disque libre) indique, pour chaque système
de fichiers monté, sa taille, l'espace utilisé et disponible, le pourcentage
d'occupation et le point de montage. `-h` affiche des tailles lisibles.
`df -h .` ne montre que le système de fichiers qui contient le répertoire
courant. `-i` compte les inodes, qui peuvent s'épuiser avant l'espace.

## Essayez

```console
$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       250G  120G  130G  48% /
```

## Notes en marge

| Écrire       | Cela veut dire                                        |
|--------------|-------------------------------------------------------|
| `df -h`      | À quel point chaque meuble est plein, en Go           |
| `df -h .`    | À quel point est plein le meuble qui contient ce tiroir |
| `df -i`      | Combien de feuilles il peut encore recevoir           |

## Quand un agent demande

Les agents consultent `df` quand quelque chose échoue avec « No space left on
device ». `df` ne fait que lire : c'est toujours sans danger.

## Attention

- Un meuble plein à 100 % fait échouer toutes sortes d'outils, de façon étrange. Libérez de la place avant toute autre chose.
