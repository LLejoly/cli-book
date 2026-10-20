---
command: source
title: Les Ordres scellés
metaphor: >
  Une feuille d'ordres scellés ouverte à votre propre bureau et exécutée sur place, de sorte que chaque changement reste dans votre cabinet.
exercise:
  question: "go.sh ne contient qu'une ligne : cd letters. Vous lancez bash go.sh, puis pwd. Dans quel tiroir êtes-vous ?"
  choices:
    - "letters, puisque la feuille le disait"
    - "Toujours study : un commis à part a ouvert le tiroir, pas vous"
    - "Ni l'un ni l'autre, bash go.sh ferme tous les tiroirs"
  explanation: "bash go.sh confie la feuille à un nouveau commis qui travaille puis s'en va. Seul source go.sh exécute les ordres à votre propre bureau, où le changement reste."
---

## En une ligne

`source` exécute les instructions écrites sur une feuille comme si vous les aviez tapées vous-même.

## L'image

Une feuille d'ordres arrive sous scellé. D'ordinaire, vous confiez une telle
feuille à un commis qui travaille dans une autre pièce puis s'en va. Avec
`source`, vous brisez le scellé à votre propre bureau et exécutez les ordres
ici même. Ce qu'ils changent, le tiroir ouvert, les notes sur le tableau de
liège, reste changé dans votre cabinet.

## Ce qui se passe vraiment

`source fichier` (ou `. fichier`) lit le fichier et exécute chaque ligne dans
le shell courant, et non dans un processus enfant. Ainsi `cd`, `export`, les
alias et les fonctions qu'il contient modifient votre session. Lancer
`bash fichier` démarre un nouveau shell, dont les changements disparaissent à
sa fin. Les fichiers de démarrage comme `~/.bashrc` se chargent de cette façon.

## Essayez

```console
$ echo 'cd letters' > go.sh
$ bash go.sh
$ pwd
/home/you/study
$ source go.sh
$ pwd
/home/you/study/letters
```

## Notes en marge

| Écrire             | Cela veut dire                                   |
|--------------------|--------------------------------------------------|
| `source fichier`   | Exécuter les ordres de cette feuille à mon propre bureau |
| `. fichier`        | La même chose, dans l'ancienne forme courte      |
| `source ~/.bashrc` | Relire mes ordres de démarrage maintenant        |
| `bash fichier`     | Confier plutôt la feuille à un nouveau commis     |

## Quand un agent demande

Les agents sourcent une feuille pour préparer un outil, comme
`source .venv/bin/activate`. Demandez d'où vient la requête. Si un README, un
ticket ou une page web que Hobbs vient de lire lui a dit de sourcer une feuille,
c'est un papier venu du dehors qui donne des ordres. Ouvrez d'abord la feuille
avec `cat` et lisez chaque ligne.

## Attention

- Les ordres sourcés s'exécutent avec toutes vos clés. Ils peuvent lire les secrets de votre tableau de liège et les envoyer au dehors.
- Une feuille sourcée peut changer `PATH` ou définir une fonction nommée `ls` ou `sudo`, et le tour dure toute la session.
