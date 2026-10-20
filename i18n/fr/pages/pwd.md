---
command: pwd
title: La Carte d'adresse
metaphor: >
  Une carte sur laquelle le commis écrit l'adresse complète du tiroir devant lequel vous vous tenez.
exercise:
  question: "pwd répond /home/you/study/letters. Quel tiroir contient letters ?"
  choices:
    - "study"
    - "home"
    - "letters se contient lui-même"
  explanation: "Une adresse se lit depuis le grand meuble à tiroirs vers le bas. Chaque nom contient celui qui le suit, donc study contient letters."
---

## En une ligne

`pwd` vous dit dans quel dossier vous vous trouvez en ce moment.

## L'image

Après quelques allées et venues dans le cabinet, vous ne savez plus où vous
êtes. Vous le demandez au commis. Il vous tend une carte avec l'adresse
complète : le grand meuble à tiroirs, puis le tiroir home, puis le vôtre, puis
celui qui est ouvert devant vous.

## Ce qui se passe vraiment

`pwd` (print working directory, « afficher le répertoire de travail ») affiche
le chemin absolu du répertoire courant du shell, en partant de `/`. Il ne lit
rien sur le disque et ne change rien. Avec `-P`, il suit les liens symboliques
et montre le chemin physique.

## Essayez

```console
$ cd ~/study/letters
$ pwd
/home/you/study/letters
```

## Notes en marge

| Écrire   | Cela veut dire                                        |
|----------|-------------------------------------------------------|
| `pwd`    | Écrivez-moi l'adresse complète de ce tiroir           |
| `pwd -P` | Écrivez la vraie adresse, pas celle d'un raccourci    |

## Quand un agent demande

Les agents lancent `pwd` pour vérifier où ils se trouvent avant d'agir. Vous
pouvez toujours l'accepter. Si la réponse vous surprend, arrêtez l'agent avant
son instruction suivante. Il s'apprête à travailler dans un tiroir que vous
n'attendiez pas.

## Attention

- L'adresse indique où se tient le commis, pas où sont vos fichiers. Une commande lancée après `pwd` agit sur ce tiroir-là.
