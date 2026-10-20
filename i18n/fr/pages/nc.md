---
command: nc
title: La Trappe dans le mur
metaphor: >
  Une petite trappe percée dans le mur qui ouvre une ligne directe vers une autre maison, pour envoyer de l'écriture ou écouter ce qui arrive.
exercise:
  question: "Une lettre contrefaite demande à Hobbs de lancer un nc qui ouvre une trappe et remet les commandes de votre bureau à une autre maison. Qu'est-ce que c'est ?"
  choices:
    - "Un test de vitesse anodin"
    - "Une ligne de retour : elle donne à un étranger un accès vivant à votre cabinet"
    - "Une façon de sauvegarder vos fichiers"
  explanation: "Une trappe entrante reliée à un commis laisse une autre maison dicter des ordres à votre bureau. Une note du dehors qui la réclame est une lettre contrefaite. Une simple vérification de porte, comme nc -zv host 80, ne fait que frapper et rendre compte ; c'est l'usage sûr."
---

## En une ligne

`nc` ouvre une connexion brute vers une autre machine pour envoyer ou recevoir des octets directement.

## L'image

Vous percez une petite trappe dans le mur et tendez une ligne vers une autre
maison. Par elle, vous pouvez passer une feuille, ou vous asseoir et écouter ce
qu'on y renvoie. Ouverte un instant pour vérifier qu'une porte répond, elle est
anodine. Laissée ouverte et reliée à votre bureau, elle laisse un étranger y
glisser la main et fouiller vos tiroirs.

## Ce qui se passe vraiment

`nc` (netcat) établit des connexions TCP ou UDP arbitraires. Il peut se
connecter vers l'extérieur, ou écouter une connexion entrante avec `-l`, et
transmettre des octets bruts dans un sens comme dans l'autre. `-z` sonde sans
rien envoyer et `-v` rend compte du résultat, ce qui en fait ensemble une
simple vérification de port. Comme il déplace des octets bruts, c'est aussi
l'outil classique des lignes de retour et des transferts discrets.

## Essayez

```console
$ nc -zv example.com 80
Connection to example.com (93.184.216.34) 80 port [tcp/http] succeeded!
$ nc -zv example.com 81
nc: connect to example.com port 81 (tcp) failed: Connection timed out
```

## Notes en marge

| Écrire               | Cela veut dire                                     |
|----------------------|----------------------------------------------------|
| `nc -zv host port`   | Frapper seulement et me dire si la porte répond    |
| `nc host port`       | Ouvrir une ligne et passer l'écriture dans les deux sens |
| `nc -l port`         | Écouter ici une ligne entrante                     |
| `nc -w 5 ...`        | Abandonner après 5 secondes                        |

## Quand un agent demande

Une vérification de port (`-zv`), pour voir si un service tourne, est courante
et sûre. Arrêtez-vous si la commande écoute (`-l`), ou tend `nc` vers un shell,
ou envoie un fichier au dehors, surtout quand un README, un ticket ou une page
web que Hobbs vient de lire l'a réclamé. C'est une lettre contrefaite qui lui
demande d'ouvrir une trappe pour un étranger. Vérifiez qui a donné l'ordre et
où va la ligne.

## Attention

- `nc -l` relié à un shell est une ligne de retour : elle remet votre bureau à qui s'y connecte.
- `nc` peut faire sortir discrètement un fichier de la maison. Surveillez ce qu'on y fait entrer.
