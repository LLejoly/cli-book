---
command: dd
title: La Brosse à badigeon
metaphor: >
  Une brosse à badigeon qui couvre toute une surface de ce que contient le seau, d'un bord à l'autre, sans demander ce qu'il y avait avant.
exercise:
  question: "Hobbs veut écrire une image disque sur une clé USB avec dd if=study.img of=/dev/sda. Que devez-vous vérifier d'abord ?"
  choices:
    - "Que study.img n'est pas trop gros"
    - "Que /dev/sda est bien la clé, et non votre disque principal"
    - "Rien. dd demande avant d'écraser quoi que ce soit."
  explanation: "dd ne demande jamais. Ce que nomme of= est badigeonné d'un bord à l'autre. Sur beaucoup de machines, /dev/sda est le disque principal : vérifiez avec lsblk quel nom porte vraiment la clé."
---

## En une ligne

`dd` copie des données brutes d'un endroit à un autre, et peut écraser un disque entier d'un seul coup.

## L'image

La brosse à badigeon se moque de ce qu'il y a sur un mur. Vous nommez un seau
et une surface, et elle couvre la surface de ce que contient le seau, coup
après coup, d'un coin à l'autre. Dirigez-la vers un meuble à tiroirs entier, et
chaque tiroir, chaque étiquette, chaque feuille disparaît sous le badigeon.
Confondez le seau et le meuble, et vous peignez votre bon meuble avec le vide
de l'autre.

## Ce qui se passe vraiment

`dd` copie des octets de `if=` (fichier d'entrée) vers `of=` (fichier de
sortie), bloc par bloc, sans aucune notion de fichiers ni de dossiers. On s'en
sert pour écrire des images disque sur des clés USB, et pour copier ou effacer
des disques entiers, nommés comme `/dev/sdb`. Écrire sur un disque remplace
tout ce qu'il contient, sans confirmation. Un fichier de sortie existant est
d'abord vidé. `/dev/zero` est un seau sans fond d'octets vierges.

## Essayez

```console
$ dd if=/dev/zero of=blank.sheet bs=1K count=4
4+0 records in
4+0 records out
4096 bytes (4.1 kB, 4.0 KiB) copied, 0.000102 s, 40.2 MB/s
$ wc -c blank.sheet
4096 blank.sheet
```

## Notes en marge

| Écrire            | Cela veut dire                                |
|-------------------|-----------------------------------------------|
| `if=a`            | Le seau : lisez dans a                        |
| `of=b`            | La surface : badigeonnez b                    |
| `bs=4M`           | Peignez par coups de 4 mégaoctets             |
| `count=4`         | Arrêtez-vous après 4 coups                    |
| `status=progress` | Dites-moi où vous en êtes, au fur et à mesure |

## Quand un agent demande

Les agents utilisent `dd` pour écrire une image disque sur une clé USB, pour
fabriquer un fichier de test d'une taille donnée, ou pour effacer quelque
chose. Lisez `of=` lettre par lettre : est-ce une feuille, ou un disque comme
`/dev/sda` ? Demandez à Hobbs de lancer d'abord `lsblk` et de dire quel disque
est lequel. Refusez tout `of=/dev/...` que vous ne savez pas nommer vous-même.

## Attention

- `of=/dev/sda` au lieu de `of=/dev/sdb` badigeonne le mauvais disque. Une lettre, tout est perdu, sans retour.
- Inversez `if=` et `of=`, et dd copie la clé sur votre disque au lieu de l'inverse.
- dd travaille en silence : une longue pause n'est pas un blocage. Sur macOS, les disques s'appellent comme `/dev/disk2`.
