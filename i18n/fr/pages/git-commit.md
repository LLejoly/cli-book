---
command: git commit
title: La Presse à copier
metaphor: >
  La presse à copier en fonte, qui presse les lettres de la corbeille dans le copie-lettres : une copie permanente, signée et datée.
exercise:
  question: "git commit envoie-t-il votre travail à quelqu'un d'autre ?"
  choices:
    - "Oui, tout le monde le voit aussitôt"
    - "Non, il presse la copie dans votre propre copie-lettres, et nulle part ailleurs"
    - "Seulement si le message le dit"
  explanation: "Un commit reste dans votre cabinet. Envoyer vos nouvelles copies au livre partagé d'une autre maison est une étape à part : git push."
---

## En une ligne

`git commit` enregistre les modifications choisies comme une nouvelle version, avec un message qui dit ce qui a changé.

## L'image

Vous tournez le volant de la presse à copier. Tout ce qui se trouve dans la
corbeille est pressé dans le copie-lettres, en une seule copie nouvelle. Elle
est signée de votre nom, datée, et porte une courte note qui dit pourquoi. On
ne presse jamais par-dessus une copie plus ancienne. Chaque nouvelle copie va
sur la page suivante.

## Ce qui se passe vraiment

`git commit` enregistre l'instantané préparé comme un nouveau commit, avec
auteur, date, message et un lien vers son parent. Il y fait ensuite avancer la
branche courante. Le commit reçoit un identifiant unique (une empreinte comme
`2412c63`). `-m` donne le message directement sur la ligne. `-a` prépare
d'abord les fichiers suivis qui ont été modifiés. `--amend` remplace le
dernier commit.

## Essayez

```console
$ git commit -m "Add stamps to the list"
[main 2412c63] Add stamps to the list
 1 file changed, 1 insertion(+)
```

## Notes en marge

| Écrire               | Cela veut dire                                          |
|----------------------|---------------------------------------------------------|
| `git commit -m "..."`| Pressez la corbeille dans le livre, avec cette note     |
| `git commit -a -m`   | Posez chaque feuille connue et modifiée dans la corbeille, puis pressez |
| `git commit --amend` | Refaites le dernier passage sous la presse              |

## Quand un agent demande

Faire des commits est une bonne habitude, car on peut toujours revenir à une
copie pressée. Lisez le message : il doit dire clairement ce qui a changé.
Prudence avec `--amend` sur des copies déjà envoyées à une autre maison.

## Attention

- Un commit est local. Tant que vous n'avez pas fait de push, personne d'autre ne l'a, et un ordinateur portable perdu l'emporte avec lui.
