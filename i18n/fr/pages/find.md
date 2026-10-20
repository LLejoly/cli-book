---
command: find
title: Le Fichier de bibliothèque
metaphor: >
  Le fichier de la bibliothèque, dont les fiches vous indiquent le tiroir exact de chaque feuille qui correspond à votre demande.
exercise:
  question: "Où cherche find . -name \"*.txt\" ?"
  choices:
    - "Seulement dans le tiroir où vous êtes"
    - "Dans le tiroir où vous êtes et dans tous les tiroirs qu'il contient"
    - "Dans tous les tiroirs du cabinet"
  explanation: "Le point veut dire « commencer ici ». find fouille ensuite chaque tiroir plus petit en dessous, mais jamais au-dessus."
---

## En une ligne

`find` cherche dans des dossiers, et dans tous les dossiers qu'ils contiennent, les fichiers qui correspondent à une description.

## L'image

Vous ne savez plus où vous avez rangé les recettes. Plutôt que d'ouvrir chaque
tiroir, vous allez au fichier de la bibliothèque. Vous demandez « toutes les
feuilles dont le nom finit par .txt ». Le commis parcourt chaque tiroir situé
sous celui où vous êtes. Il vous tend une fiche avec le chemin complet de
chacune.

## Ce qui se passe vraiment

`find` parcourt une arborescence de dossiers à partir de chaque point de
départ. Il affiche chaque chemin qui passe les tests donnés, comme `-name`,
`-type f` (fichiers) ou `-type d` (dossiers), `-size` et `-mtime`. Il peut
aussi agir sur chaque résultat, avec `-delete` ou `-exec`.

## Essayez

```console
$ find . -name "*.txt"
./.secret-diary.txt
./letters/to-grandma.txt
./letters/to-the-bank.txt
./notes.txt
./recipes/bread-grandma.txt
./recipes/bread.txt
$ find . -type d
.
./letters
./recipes
```

## Notes en marge

| Écrire             | Cela veut dire                                          |
|--------------------|---------------------------------------------------------|
| `find . -name "x*"`| Trouvez les feuilles dont le nom commence par x         |
| `find . -type d`   | Trouvez seulement les tiroirs                           |
| `find . -mtime -1` | Trouvez les feuilles modifiées depuis un jour           |
| `find . -delete`   | Effacez tout ce qui est trouvé. À traiter comme `rm -r` |

## Quand un agent demande

Les agents utilisent `find` pour prendre la mesure d'un projet. Une simple
recherche ne fait que lire. Regardez la fin du billet : `-delete` ou
`-exec rm` change une recherche en gomme.

## Attention

- `find / ...` fouille tout le cabinet et peut valoir bien des protestations du commis devant les tiroirs fermés à clé.
- Lancez toujours la recherche d'abord sans `-delete`, pour voir ce qu'elle effacerait.
