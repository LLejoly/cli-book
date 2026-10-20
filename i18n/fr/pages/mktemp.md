---
command: mktemp
title: Le Bloc numéroté
metaphor: >
  Un bloc de feuilles de brouillon vierges, chacune tamponnée de son propre numéro, pour que deux commis ne prennent jamais la même feuille.
exercise:
  question: "Hobbs écrit tmp=$(mktemp), puis plus tard rm -rf \"$tmp\". Que devez-vous vérifier ?"
  choices:
    - "Rien, rm est toujours sans danger sur des feuilles de brouillon"
    - "Que $tmp contient bien le nom donné par mktemp, et que rien ne l'a changé entre-temps"
    - "Que la feuille de brouillon est vide, sinon rm refusera"
  explanation: "rm efface le nom que la variable contient à ce moment-là. Si elle était vide ou changée, la gomme tomberait ailleurs. -rf n'est utile que pour mktemp -d."
---

## En une ligne

`mktemp` crée un nouveau fichier vide (ou un dossier) avec un nom unique, pour un travail de brouillon, et vous donne son nom.

## L'image

Près de l'escalier de service, il y a un tiroir aux brouillons que tous les
commis de la maison se partagent. Son bloc porte un numéro tamponné sur chaque
feuille. Arrachez-en une et elle est à vous : personne d'autre n'a ce numéro,
donc personne n'écrira par-dessus votre travail. Le commis vous lit le numéro,
pour que vous retrouviez la feuille.

## Ce qui se passe vraiment

`mktemp` crée un fichier au nom tiré au hasard, comme `/tmp/tmp.k3Jx9QbW2T`,
que vous seul pouvez lire et écrire, et affiche ce nom. `-d` crée un dossier à
la place. Un modèle avec au moins trois `X`, comme `draft.XXXX`, fixe le nom
et le crée dans le dossier courant. Le fichier reste jusqu'à ce que quelqu'un
le supprime. `/tmp` est souvent vidé quand l'ordinateur redémarre.

## Essayez

```console
$ tmp=$(mktemp)
$ echo $tmp
/tmp/tmp.k3Jx9QbW2T
$ sort notes.txt > "$tmp"
$ head -n 2 "$tmp"
buy flour
buy ink
$ rm "$tmp"
```

## Notes en marge

| Écrire                    | Cela veut dire                                |
|---------------------------|-----------------------------------------------|
| `mktemp`                  | Donnez-moi une feuille de brouillon neuve et dites-moi son numéro |
| `mktemp -d`               | Donnez-moi plutôt un tiroir aux brouillons neuf |
| `mktemp --suffix=.txt`    | Pareil, avec `.txt` à la fin du nom           |
| `mktemp draft.XXXX`       | Une feuille neuve nommée selon ce modèle, ici |
| `tmp=$(mktemp)`           | Gardez le numéro sur une note nommée `tmp`    |

## Quand un agent demande

Les agents utilisent `mktemp` pour avoir un endroit sûr où poser des
résultats intermédiaires, comme une copie triée ou un fichier téléchargé, sans
rien écraser de ce qui est à vous. Créer la feuille est sans danger. Lisez le
billet de rangement qui vient ensuite : il doit effacer `"$tmp"` exactement,
entre guillemets, et rien de plus large.

## Attention

- Si la variable (la note nommée `tmp`) est vide, `rm -rf "$tmp"/*` devient `rm -rf /*`. Vérifiez d'abord que le nom a bien été donné.
- Les feuilles de brouillon restent là tant que rien ne les enlève. Les secrets qu'on y écrit aussi.
