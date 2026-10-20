---
command: docker run
title: La Malle de voyage
metaphor: >
  Une malle de voyage où tient un petit cabinet de travail complet, que l'on déballe et met au travail sans déranger le reste de la maison.
exercise:
  question: "docker run -v ~/study:/data ... À quoi sert la partie -v ?"
  choices:
    - "Elle agrandit la malle"
    - "Elle permet au cabinet de la malle d'atteindre un vrai tiroir de votre cabinet"
    - "Elle affiche la version"
  explanation: "-v ouvre un passage entre un tiroir de votre maison et la malle. Ce qui s'exécute à l'intérieur peut alors lire, modifier ou effacer ces feuilles."
---

## En une ligne

`docker run` lance un programme dans un conteneur : une copie emballée et
séparée de tout ce dont il a besoin.

## L'image

La malle arrive avec un petit cabinet complet rangé à l'intérieur : ses
propres tiroirs, ses propres commis, ses propres outils. Vous l'ouvrez et la
mettez au travail. Ce qui se passe à l'intérieur reste à l'intérieur, sauf si
vous ouvrez un passage vers l'un de vos tiroirs ou l'une de vos pièces.

## Ce qui se passe vraiment

`docker run image` crée un conteneur à partir d'une image, télécharge l'image
si besoin, et lance sa commande avec un système de fichiers, des processus et
un réseau isolés. `-v` monte des chemins de la machine hôte dans le conteneur,
`-p` publie des ports, `--rm` supprime le conteneur quand il s'arrête, `-it`
donne un terminal interactif. `--privileged` retire l'essentiel de
l'isolation.

## Essayez

```console
$ docker run --rm python:3.12 python -c 'print("hello from the trunk")'
hello from the trunk
```

## Notes en marge

| Écrire                 | Cela veut dire                                  |
|------------------------|-------------------------------------------------|
| `docker run image`     | Déballer cette malle et la mettre au travail    |
| `--rm`                 | Jeter la malle une fois le travail fini         |
| `-v ~/a:/data`         | Ouvrir un passage de mon tiroir a vers la malle |
| `--privileged`         | Retirer les parois de la malle                  |

## Quand un agent demande

Les conteneurs sont un bon moyen de faire tourner des choses à l'écart de vos
fichiers. Vérifiez les passages `-v` (quels tiroirs la malle peut atteindre),
et refusez `--privileged` à moins de savoir pourquoi il en faut.

## Attention

- `-v /:/host` livre toute la maison à ce qui se trouve dans la malle.
- Les images viennent aussi d'inconnus. Préférez les images officielles et bien connues.
