---
command: ln
title: La Carte de réexpédition
metaphor: >
  Une carte laissée dans un tiroir, qui dit « cette feuille est rangée dans le tiroir X », pour que quiconque cherche ici soit envoyé là-bas.
exercise:
  question: "bread est une carte de réexpédition vers recipes/bread.txt. Vous effacez recipes/bread.txt. Qu'arrive-t-il à bread ?"
  choices:
    - "Il garde la recette"
    - "La carte reste, mais elle ne mène plus nulle part"
    - "Il est effacé lui aussi"
  explanation: "Un lien symbolique ne contient qu'une adresse. Quand la vraie feuille a disparu, la carte désigne une place vide."
---

## En une ligne

`ln -s` crée un raccourci : un nom, à un endroit, qui mène à un fichier rangé ailleurs.

## L'image

Au lieu de recopier une feuille, vous laissez une carte de réexpédition dans
un autre tiroir : « la recette du pain est rangée dans le tiroir des
recettes ». Quiconque lit la carte est envoyé tout droit à la vraie feuille. Il
n'existe toujours qu'une seule feuille. Une modification se voit donc des deux
endroits.

## Ce qui se passe vraiment

`ln -s target name` crée un lien symbolique : un petit fichier qui contient un
chemin. La plupart des commandes le suivent sans rien dire. Sans `-s`, `ln`
crée un lien physique : un second nom pour les mêmes données sur le disque.
`ls -l` affiche les liens sous la forme `name -> target`. Supprimer un lien
avec `rm` ne touche pas à sa cible.

## Essayez

```console
$ ln -s recipes/bread.txt bread
$ ls -l bread
lrwxrwxrwx 1 you you 17 Oct 19 09:30 bread -> recipes/bread.txt
$ head -n 1 bread
500g flour
```

## Notes en marge

| Écrire            | Cela veut dire                                   |
|-------------------|--------------------------------------------------|
| `ln -s a b`       | Laisser une carte b qui mène à la feuille a      |
| `ln -sf a b`      | Remplacer la carte b si elle existe déjà         |
| `ln a b`          | Donner un second nom à la même feuille           |
| `readlink b`      | Lisez-moi où mène la carte b                     |

## Quand un agent demande

Les agents se servent des liens pour faire apparaître un outil ou un fichier
de configuration là où un programme l'attend. Vérifiez le sens :
`ln -s target name`. Avec `-f`, un fichier existant nommé `name` est remplacé.

## Attention

- `ln -sf` posé sur une vraie feuille remplace cette feuille par une carte. Son contenu est perdu.
