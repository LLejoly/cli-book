---
command: git merge
title: L'Aiguille du relieur
metaphor: >
  Une aiguille de relieur et son fil, qui cousent les pages d'un brouillon dans un autre, avec une nouvelle page signée qui note où les deux ont été réunis.
exercise:
  question: "git merge s'arrête sur 'CONFLICT (content): Merge conflict in notes.txt'. Quelle est la suite la plus sûre ?"
  choices:
    - "Lancer git reset --hard pour faire disparaître le message"
    - "Ouvrir notes.txt, choisir entre les lignes marquées, puis git add et git commit"
    - "Supprimer notes.txt et refaire le merge"
  explanation: "Un conflit veut dire que les deux brouillons ont changé les mêmes lignes. Git marque les deux versions et attend une personne. Si vous préférez arrêter, git merge --abort remet tout comme avant le merge."
---

## En une ligne

`git merge` réunit le travail d'une autre branche dans celle où vous êtes.

## L'image

Deux brouillons ont grandi dans des classeurs séparés. L'aiguille du relieur
coud les pages de l'un dans l'autre, si bien que les deux lignes de travail
tiennent dans le même livre. Là où les brouillons avaient pris chacun leur
chemin, une nouvelle page est pressée et signée : « ces deux-là ont été
réunis ici ». Si les deux ont changé les mêmes lignes, le relieur s'arrête et
attend que vous choisissiez.

## Ce qui se passe vraiment

`git merge name` fait entrer les commits de cette branche dans la branche
courante. Si la branche courante n'a pas bougé depuis leur séparation, git
fait une avance rapide (fast-forward) : il avance la branche sans nouveau
commit. Sinon il crée un commit de fusion à deux parents, et ouvre un éditeur
pour son message, sauf avec `--no-edit`. Sur des lignes en conflit, il
s'arrête, écrit les marqueurs `<<<<<<<` et `>>>>>>>` dans le fichier, et
attend.

## Essayez

```console
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
$ git merge --no-edit birthday-letter
Merge made by the 'ort' strategy.
 letters/to-grandma.txt | 2 ++
 1 file changed, 2 insertions(+)
$ git log --oneline --graph -4
*   3e6a0b5 Merge branch 'birthday-letter'
|\
| * c41d7e9 Write to grandma for her birthday
* | 7f3a9e1 Add sugar to the bread
|/
* 2412c63 Add stamps to the list
```

## Notes en marge

| Écrire                       | Cela veut dire                                   |
|------------------------------|--------------------------------------------------|
| `git merge name`             | Coudre ce brouillon dans celui de mon secrétaire |
| `git merge --no-edit name`   | Garder le message habituel pour la page de jonction |
| `git merge --abort`          | Arrêter, et tout remettre comme avant            |
| `git merge --ff-only name`   | Seulement si aucune page de jonction n'est nécessaire ; sinon refuser |

## Quand un agent demande

Les agents font un merge pour faire entrer les nouvelles de `main` dans leur
propre branche, ou pour terminer un travail. Vérifiez sur quelle branche vous
êtes, et laquelle arrive : un merge dans `main` change le brouillon partagé.
S'il y a eu un conflit, demandez comment chacun a été tranché, car l'agent a
choisi entre les lignes de deux personnes. Méfiez-vous de `-X ours` ou
`-X theirs`, qui tranchent tous les conflits dans le même sens.

## Attention

- Faites d'abord un commit, ou mettez de côté vos modifications non enregistrées. Un merge sur un secrétaire en désordre peut refuser, ou mêler deux désordres.
- Une fois un merge envoyé, on l'annule avec `git revert -m 1`, pas avec un reset.
