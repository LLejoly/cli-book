---
command: ">"
title: Le Bloc de dictée
metaphor: >
  Un bloc de dictée où le commis écrit sa réponse au lieu de la dire, sur une feuille neuve qui remplace l'ancienne.
exercise:
  question: "notes.txt contient votre liste de courses. Que fait echo hello > notes.txt ?"
  choices:
    - "Elle ajoute hello à la fin de la liste"
    - "Elle remplace toute la liste par le seul mot hello"
    - "Elle refuse, car notes.txt existe déjà"
  explanation: "Un seul > repart d'une feuille blanche, donc l'ancienne liste est perdue. Avec >>, hello aurait été ajouté à la fin."
---

## En une ligne

`>` enregistre le résultat d'une commande dans un fichier, en remplaçant ce qui s'y trouvait. `>>` l'ajoute plutôt à la fin.

## L'image

D'habitude, le commis lit sa réponse à voix haute. Avec le bloc de dictée, il
l'écrit à la place. Un seul `>` veut dire « arrachez une feuille neuve » : tout
ce que portait l'ancienne feuille de ce nom est jeté au panier. Deux, `>>`,
veulent dire « continuez d'écrire au bas de la feuille existante ».

## Ce qui se passe vraiment

Le shell ouvre le fichier nommé en écriture avant même que la commande ne
démarre. `>` vide d'abord le fichier. `>>` écrit à la suite. Seule la sortie
standard est redirigée. Les erreurs arrivent toujours à l'écran, sauf si vous
ajoutez `2>`. Le fichier est créé s'il n'existe pas.

## Essayez

```console
$ ls letters > list.txt
$ cat list.txt
to-grandma.txt
to-the-bank.txt
$ echo "buy stamps" >> notes.txt
$ tail -n 2 notes.txt
buy ink
buy stamps
```

## Notes en marge

| Écrire        | Cela veut dire                                    |
|---------------|---------------------------------------------------|
| `cmd > a`     | Écrire la réponse sur la feuille a, en remplaçant ce qui s'y trouvait |
| `cmd >> a`    | Ajouter la réponse à la fin de la feuille a       |
| `cmd 2> a`    | Écrire les protestations sur la feuille a         |
| `cmd > /dev/null` | Jeter la réponse                              |

## Quand un agent demande

Les agents utilisent `>` pour créer des fichiers rapidement. Vérifiez le nom
qui suit la flèche. Si cette feuille existe déjà, son ancien contenu est perdu
pour de bon.

## Attention

- Un `>` au lieu de `>>` efface la feuille. Impossible de revenir en arrière.
- `sort a > a` vide a avant que sort ne puisse le lire. Écrivez d'abord sous un nouveau nom.
