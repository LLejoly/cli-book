---
command: chmod
title: Le Serrurier
metaphor: >
  Un serrurier qui décide qui peut lire une feuille, qui peut écrire dessus, et qui peut la confier à un commis comme une liste d'ordres.
exercise:
  question: "ls -l affiche -rwxr-xr-x pour tidy.sh. Qui peut changer ce qui est écrit dessus ?"
  choices:
    - "Tout le monde"
    - "Vous seul, le propriétaire"
    - "Personne"
  explanation: "Les lettres vont par trois groupes : le propriétaire, le groupe, tous les autres. Seul le premier groupe a le w (écrire). Les deux autres peuvent la lire et l'exécuter."
---

## En une ligne

`chmod` change qui a le droit de lire, de modifier ou d'exécuter un fichier.

## L'image

Chaque feuille porte trois petites serrures : une pour vous, une pour votre
maisonnée, une pour tous les autres. Chaque serrure peut permettre de lire,
d'écrire ou d'« exécuter comme des ordres ». Le serrurier règle ces serrures.
Une feuille d'instructions ne peut être confiée à un commis comme liste
d'ordres que si sa serrure « exécuter » est ouverte.

## Ce qui se passe vraiment

`chmod` règle les bits de permission pour l'utilisateur, le groupe et les
autres : `r` lecture, `w` écriture, `x` exécution. On peut utiliser des lettres
(`u+x`, `go-w`) ou des nombres octaux, où 4 vaut lecture, 2 écriture et
1 exécution : `755` donne `rwxr-xr-x` et `600` donne `rw-------`. `-R`
applique le changement à toute une arborescence de répertoires.

## Essayez

```console
$ ls -l tidy.sh
-rw-r--r-- 1 you you 20 Oct 19 09:30 tidy.sh
$ chmod +x tidy.sh
$ ./tidy.sh
tidy
$ chmod 600 notes.txt
$ ls -l notes.txt
-rw------- 1 you you 44 Oct 19 09:30 notes.txt
```

## Notes en marge

| Écrire           | Cela veut dire                                          |
|------------------|---------------------------------------------------------|
| `chmod +x a`     | Permettre que la feuille a soit exécutée comme des ordres |
| `chmod 600 a`    | Moi seul peux la lire et l'écrire ; personne d'autre n'y regarde |
| `chmod 755 a`    | Moi, je peux tout faire ; les autres peuvent lire et exécuter |
| `chmod -R ...`   | Changer les serrures de tout un tiroir et de son contenu |

## Quand un agent demande

Les agents lancent souvent `chmod +x` sur un script qu'ils viennent d'écrire,
pour pouvoir l'exécuter. C'est normal. Méfiez-vous de `chmod 777` ou de
`chmod -R` sur de grands tiroirs : ils ouvrent les serrures à tout le monde.

## Attention

- `777` veut dire que n'importe qui peut modifier la feuille. Ce n'est presque jamais la bonne solution.
- `chmod -R` sur votre propre tiroir peut abîmer des clés qui doivent rester privées, comme `~/.ssh`.
