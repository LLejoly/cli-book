---
command: tee
title: Le Raccord en T
metaphor: >
  Un raccord en T de laiton, monté sous l'entonnoir, pour que ce qui s'y verse parte de deux côtés à la fois : vers vous, et sur une feuille.
exercise:
  question: "Quelle différence entre sort notes.txt | tee sorted.txt et sort notes.txt > sorted.txt ?"
  choices:
    - "Aucune"
    - "Les deux écrivent sorted.txt, mais tee vous lit aussi la liste triée"
    - "tee ajoute à la fin de sorted.txt au lieu de le remplacer"
  explanation: "tee écrit la feuille et la dit à voix haute. Comme un seul >, il repart d'une feuille neuve. Seul tee -a ajoute à la fin."
---

## En une ligne

`tee` enregistre dans un fichier ce qui passe par lui, et vous le montre en même temps.

## L'image

L'entonnoir porte la réponse d'un commis jusqu'au suivant. Montez un raccord
en T dessous, et le flot se partage en deux. Une branche continue comme
avant, vers vous ou vers le commis suivant. L'autre se déverse sur une
feuille, écrite à mesure que les mots arrivent. Cette feuille repart à neuf,
sauf si vous dites le contraire.

## Ce qui se passe vraiment

`tee` copie son entrée standard sur la sortie standard et dans chaque fichier
nommé. Il vide d'abord chaque fichier, comme `>`, sauf si vous passez `-a`
(*append*, ajouter). Comme c'est un programme à part, il s'exécute avec ses
propres droits. C'est pourquoi `| sudo tee file` peut écrire là où
`sudo cmd > file` ne le peut pas : dans la seconde forme, la redirection est
ouverte par votre propre shell, sans le passe-partout.

## Essayez

```console
$ sort notes.txt | tee sorted.txt
buy flour
buy ink
call grandma
pay the bank
$ echo "buy stamps" | tee -a notes.txt
buy stamps
```

## Notes en marge

| Écrire                 | Cela veut dire                                  |
|------------------------|-------------------------------------------------|
| `cmd \| tee a`         | Montrez-moi la réponse et écrivez-la sur la feuille a, en la remplaçant |
| `cmd \| tee -a a`      | Montrez-la-moi, et ajoutez-la à la fin de la feuille a |
| `cmd \| tee a b`       | Écrivez-la sur deux feuilles à la fois          |
| `cmd \| sudo tee a`    | Écrivez-la avec le passe-partout. La forme la plus risquée |
| `tee a > /dev/null`    | Écrivez la feuille, mais ne me la lisez pas     |

## Quand un agent demande

Les agents utilisent `| tee build.log` pour garder une longue réponse par
écrit tout en la voyant défiler. Lisez le nom qui suit `tee` : cette feuille
est effacée, sauf si `-a` est là. Soyez le plus prudent avec `sudo tee`,
souvent pointé vers un fichier de réglages comme `/etc/hosts`, qu'il écrase
avec le passe-partout.

## Attention

- `tee` sans `-a`, c'est un seul `>` : l'ancienne feuille est perdue, impossible de revenir en arrière.
- Tout ce qui passe est aussi lu à voix haute : `printenv | tee env.txt` montre vos clés et les garde sur une feuille.
