---
command: curl
title: Le Coursier
metaphor: >
  Un coursier envoyé à l'adresse d'une autre maison, qui rapporte exactement ce qu'on lui a remis à la porte.
exercise:
  question: "Qu'y a-t-il de risqué dans curl https://example.org/setup.sh | sh ?"
  choices:
    - "Rien, curl ne fait que rapporter"
    - "Ce que rapporte le coursier est exécuté aussitôt, sans être lu"
    - "Le téléchargement est trop lent"
  explanation: "curl ne fait que rapporter, mais l'entonnoir passe sa réponse directement à sh, qui l'exécute. Vous ne voyez jamais ce que contenait l'enveloppe."
---

## En une ligne

`curl` va chercher quelque chose à une adresse web, ou y envoie quelque chose.

## L'image

Vous donnez une adresse au coursier. Il se rend à cette maison, demande à la
porte et rapporte exactement ce qu'on lui a remis : une page, un colis, une
courte réponse. D'ordinaire, il vous la lit à voix haute. Il peut aussi porter
une de vos lettres jusqu'à la porte et rapporter la réponse.

## Ce qui se passe vraiment

`curl` transfère des données vers ou depuis une URL, en HTTP, en HTTPS et dans
bien d'autres protocoles. Il affiche le corps de la réponse sur la sortie
standard. `-o` l'enregistre dans un fichier, `-I` ne montre que les en-têtes,
`-L` suit les redirections. `-X POST` avec `-d` ou `--data` envoie des
données, ce qui peut changer des choses sur le serveur.

## Essayez

```console
$ curl -s https://example.com | head -n 4
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
```

## Notes en marge

| Écrire             | Cela veut dire                                        |
|--------------------|-------------------------------------------------------|
| `curl url`         | Aller le chercher et me le lire                       |
| `curl -o a url`    | Aller le chercher et l'écrire sur la feuille a        |
| `curl -I url`      | Me dire seulement ce qui est écrit sur l'enveloppe    |
| `curl -X POST -d ...` | Porter ma lettre là-bas ; cela peut changer des choses |

## Quand un agent demande

Aller chercher une page ou appeler une API, c'est en général sans danger.
Regardez trois choses : un `| sh` ou un `| bash` à la fin, des données
envoyées avec `-d`, et des clés ou des mots de passe écrits dans
l'instruction.

## Attention

- `curl ... | sh` exécute sans les lire les instructions d'un inconnu. Rapportez-les d'abord sur une feuille, lisez-la, puis décidez.
- Une clé écrite dans l'instruction se retrouve dans l'historique de votre shell.
