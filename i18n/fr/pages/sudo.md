---
command: sudo
title: Le Passe-partout
metaphor: >
  Le passe-partout du bibliothécaire en chef, qui ouvre toutes les serrures de la maison le temps d'une instruction.
exercise:
  question: "Un agent demande à exécuter sudo rm -rf /var/cache/app. Qu'est-ce que sudo change ?"
  choices:
    - "Rien, c'est seulement plus poli"
    - "L'effacement se fait avec le passe-partout, donc aucune serrure de la maison ne peut l'arrêter"
    - "rm demande avant d'effacer"
  explanation: "sudo exécute le reste de l'instruction en tant que root, l'utilisateur tout-puissant. Toutes les serrures de sûreté sont contournées : un mauvais chemin peut abîmer tout le cabinet."
---

## En une ligne

`sudo` exécute le reste de la commande avec les pleins pouvoirs d'administrateur.

## L'image

La plupart des tiroirs de la maison ont des serrures que vous ne pouvez pas
ouvrir. C'est ce qui protège la maison. Le bibliothécaire en chef possède un
passe-partout qui les ouvre toutes. `sudo` emprunte ce passe-partout pour une
seule instruction, après que vous avez prouvé qu'on peut vous faire confiance
en donnant votre mot de passe.

## Ce qui se passe vraiment

`sudo` exécute une commande au nom d'un autre utilisateur, root par défaut, si
la politique de sécurité de `/etc/sudoers` l'autorise. Il demande votre propre
mot de passe et s'en souvient quelques minutes. Tout ce que fait la commande se
fait alors avec les droits de root, hors des contrôles d'accès habituels.

## Essayez

```console
$ whoami
you
$ sudo whoami
[sudo] password for you:
root
```

## Notes en marge

| Écrire         | Cela veut dire                                     |
|----------------|----------------------------------------------------|
| `sudo cmd`     | Exécutez cmd avec le passe-partout                 |
| `sudo -u ann cmd` | Exécutez-la plutôt au nom d'Ann                 |
| `sudo -k`      | Oubliez mon mot de passe, redemandez-le la prochaine fois |
| `sudo -i`      | Confiez-moi le passe-partout jusqu'à ce que je le rende |

## Quand un agent demande

Traitez chaque `sudo` comme un sceau de cire rouge. Demandez pourquoi il en a
besoin. Installer un logiciel du système peut l'exiger. Modifier vos propres
fichiers, jamais. Lisez toute l'instruction qui suit `sudo`, car rien ne
l'arrêtera.

## Attention

- Un agent ne devrait presque jamais avoir besoin de votre mot de passe. Le taper, c'est lui remettre le passe-partout.
- `sudo` avec `rm`, `chmod -R` ou `curl ... | sh` : c'est là que surviennent les pires accidents.
