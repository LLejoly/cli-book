---
command: rsync
title: Le Panier du messager
metaphor: >
  Un panier d'osier de messager qui voyage entre deux tiroirs ou deux maisons, chargé seulement des feuilles qui manquent de l'autre côté ou dont l'autre côté n'a qu'une copie plus ancienne.
exercise:
  question: "Quelle différence entre rsync -a letters/ ../shelf/ et rsync -a letters ../shelf/ ?"
  choices:
    - "Aucune, la barre n'est qu'une décoration"
    - "La première copie les feuilles contenues dans letters vers shelf ; la seconde met un tiroir letters entier dans shelf"
    - "La seconde efface letters ensuite"
  explanation: "Une barre oblique à la fin de la source veut dire « ce qu'il y a dans ce tiroir ». Sans elle, rsync emporte le tiroir lui-même, et vous obtenez ../shelf/letters/."
---

## En une ligne

`rsync` rend un dossier semblable à un autre en ne copiant que ce qui est nouveau ou modifié, sur cet ordinateur ou vers un autre.

## L'image

Avant le départ du messager, le commis compare les deux tiroirs feuille par
feuille. Seules les feuilles qui manquent de l'autre côté, ou dont l'autre
côté n'a qu'une copie plus ancienne, vont dans le panier. L'autre tiroir finit
par ressembler au vôtre. Ajoutez `--delete`, et le messager jette aussi tout
ce qui s'y trouve et que le vôtre n'a pas.

## Ce qui se passe vraiment

`rsync SRC DEST` copie des fichiers en sautant ceux dont la taille et la date
de modification correspondent déjà. `-a` (archive) descend dans les
sous-dossiers et conserve droits, dates et liens. `-n` ou `--dry-run` énumère
ce qui se passerait sans rien changer. Une destination comme `host:dir/` passe
par `ssh`. `--delete` supprime à la destination les fichiers absents de la
source.

## Essayez

```console
$ rsync -av --dry-run letters/ ../letters-copy/
sending incremental file list
created directory ../letters-copy
./
to-aunt.txt
to-grandma.txt
to-the-bank.txt

sent 155 bytes  received 31 bytes  372.00 bytes/sec
total size is 33  speedup is 0.18 (DRY RUN)
$ rsync -a letters/ ../letters-copy/
$ ls ../letters-copy
to-aunt.txt  to-grandma.txt  to-the-bank.txt
```

## Notes en marge

| Écrire                   | Cela veut dire                                |
|--------------------------|-----------------------------------------------|
| `rsync -av a/ b/`        | Que b contienne ce que contient a, en nommant chaque feuille |
| `rsync -n ...`           | Une répétition seulement : dites ce que vous emporteriez |
| `rsync -a a/ house:a/`   | Envoyer le panier à une autre maison, par le tuyau acoustique |
| `rsync -a --delete a/ b/`| Jeter aussi de b ce que a n'a pas. Cire rouge |

## Quand un agent demande

Les agents utilisent `rsync` pour sauvegarder un dossier, déployer un site sur
un serveur, ou copier un projet vers une autre machine. Demandez d'abord un
`--dry-run` et lisez la liste. Vérifiez quel côté est la source : inversée,
elle écrase votre propre tiroir. Vérifiez chaque barre oblique finale. Avec
`--delete`, une mauvaise destination peut être vidée.

## Attention

- `--delete` fait passer le sceau au rouge : les feuilles qui n'existent qu'à la destination sont effacées, sans corbeille à papier. Même sans lui, les feuilles modifiées là-bas sont écrasées sans demander (`-u` épargne les plus récentes).
- `letters/` emporte ce qu'il y a dans le tiroir ; `letters` emporte le tiroir lui-même.
- macOS fournit un `rsync` plus ancien ou différent : certaines options peuvent y manquer.
