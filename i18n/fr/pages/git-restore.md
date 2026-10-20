---
command: git restore
title: La Feuille neuve
metaphor: >
  Une feuille neuve recopiée d'après la dernière copie pressée et posée dans le tiroir à la place de celle que vous avez griffonnée, qui part dans le poêle.
exercise:
  question: "Vous avez passé une heure à modifier notes.txt, sans faire de commit. Hobbs propose git restore notes.txt. Que devient cette heure ?"
  choices:
    - "Elle est gardée dans la corbeille à papier, au cas où vous changeriez d'avis"
    - "Elle est perdue. La feuille revient à ce que contient le livre."
    - "Elle est d'abord pressée dans le livre, puis la feuille est restaurée"
  explanation: "Des modifications jamais enregistrées par un commit ni mises de côté n'ont de copie nulle part. restore les écrase avec la version du livre, et git ne peut pas l'annuler."
---

## En une ligne

`git restore` remet un fichier dans sa dernière version enregistrée, en jetant les modifications non enregistrées que vous y aviez faites.

## L'image

Vous avez griffonné partout sur une feuille et voulez retrouver l'ancienne.
Vous ouvrez le copie-lettres à la dernière copie pressée, vous en recopiez une
feuille neuve, et vous la posez dans le tiroir à la place de la feuille
griffonnée. La feuille griffonnée part dans le poêle. Seule cette feuille
change ; le reste du secrétaire n'est pas touché.

## Ce qui se passe vraiment

`git restore file` écrase le fichier de travail avec sa version de l'index,
qui est celle du dernier commit, sauf si vous avez préparé quelque chose.
`--staged` fait autre chose : il retire le fichier de l'index et laisse vos
modifications en place, sans danger. `--source=` restaure depuis n'importe
quel commit. Les fichiers non suivis ne sont pas touchés. C'est la forme plus
récente et plus claire de `git checkout -- file`.

## Essayez

```console
$ git diff --stat
 notes.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git restore notes.txt
$ git status --short
?? letters/to-aunt.txt
```

## Notes en marge

| Écrire                           | Cela veut dire                                  |
|----------------------------------|-------------------------------------------------|
| `git restore a`                  | Remettre la feuille a comme le livre l'a. Modifications perdues |
| `git restore --staged a`         | Retirer la feuille a de la corbeille à courrier ; garder mes modifications |
| `git restore .`                  | Remettre chaque feuille de ce tiroir et des tiroirs plus petits |
| `git restore --source=HEAD~1 a`  | Retrouver la feuille a telle qu'elle était une copie plus tôt |

## Quand un agent demande

Les agents se servent de `restore` pour défaire leurs propres modifications
après une fausse route, ou pour retirer un fichier de la corbeille à
courrier. Avant d'accepter, lancez `git diff` sur le même fichier : si
certaines de ces lignes sont de vous, elles seront perdues. `--staged` seul
est sans danger. `git restore .` balaie autant que `git reset --hard`. Dans le
doute, proposez `git stash`, qui met les modifications de côté.

## Attention

- Il n'y a pas de corbeille à papier. Des modifications jamais enregistrées par un commit ni mises de côté ne peuvent pas être retrouvées par git.
- `git restore a` et `git restore --staged a` se ressemblent mais n'ont pas le même danger. Relisez le billet deux fois.
