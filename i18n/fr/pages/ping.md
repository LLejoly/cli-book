---
command: ping
title: La Carte-réponse
metaphor: >
  Une carte-réponse envoyée à une autre maison pour demander « êtes-vous là ? », chronométrée jusqu'au retour de la réponse.
exercise:
  question: "ping ne reçoit aucune réponse d'une maison. Que pouvez-vous en conclure ?"
  choices:
    - "La maison a brûlé"
    - "Soit on ne peut pas la joindre, soit elle choisit de ne pas répondre aux cartes"
    - "Votre propre cabinet est en panne"
  explanation: "Beaucoup de maisons ignorent ces cartes exprès. Le silence veut dire « pas de réponse », pas forcément « personne »."
---

## En une ligne

`ping` vérifie qu'on peut joindre un autre ordinateur, et combien de temps met la réponse.

## L'image

Vous postez une carte-réponse à une autre maison : « Êtes-vous là ? » Vous notez
l'heure à votre montre de gousset. Quand la carte revient, vous notez l'heure à
nouveau. Une réponse rapide veut dire un court trajet. Pas de réponse : la poste
n'a pas pu passer, ou la maison ignore ce genre de cartes.

## Ce qui se passe vraiment

`ping` envoie des paquets ICMP « echo request » à un hôte. Il affiche chaque
réponse avec son temps d'aller-retour, puis un bilan des paquets perdus. Sous
Linux, il continue jusqu'à ce qu'on l'arrête, sauf si vous donnez `-c` avec un
nombre. Les pare-feu bloquent souvent l'ICMP. Un hôte muet peut donc être bien
en marche.

## Essayez

```console
$ ping -c 2 example.com
PING example.com (93.184.215.14) 56(84) bytes of data.
64 bytes from 93.184.215.14: icmp_seq=1 ttl=56 time=11.2 ms
64 bytes from 93.184.215.14: icmp_seq=2 ttl=56 time=11.0 ms
```

## Notes en marge

| Écrire             | Cela veut dire                             |
|--------------------|--------------------------------------------|
| `ping house`       | Envoyer des cartes jusqu'à ce que je dise stop |
| `ping -c 4 house`  | Envoyer quatre cartes, puis s'arrêter      |
| `time=11.2 ms`     | La carte a mis 11 millièmes de seconde     |

## Quand un agent demande

Quand quelque chose échoue, les agents lancent `ping` pour voir si le réseau ou
un serveur répond. La commande demande seulement « êtes-vous là ? ». Vous pouvez
l'accepter sans crainte.

## Attention

- Sans `-c`, elle ne s'arrête jamais sous Linux. Ctrl+C l'arrête sans danger.
