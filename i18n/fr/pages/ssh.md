---
command: ssh
title: Le Tuyau acoustique
metaphor: >
  Un tuyau acoustique privé qui mène au cabinet de travail d'une autre maison, pour que les commis de là-bas exécutent vos instructions.
exercise:
  question: "Après ssh you@library, vous tapez rm notes.txt. Quel notes.txt est effacé ?"
  choices:
    - "Celui de votre propre cabinet"
    - "Celui du cabinet de la bibliothèque, à l'autre bout du tuyau"
    - "Les deux"
  explanation: "Une fois la liaison établie, chaque instruction descend le tuyau et s'exécute dans l'autre maison, jusqu'à ce que vous tapiez exit."
---

## En une ligne

`ssh` ouvre une liaison sécurisée vers un autre ordinateur et vous permet d'y taper des commandes.

## L'image

Vous soulevez le capuchon du tuyau acoustique et dites qui vous êtes. Si
l'autre maison reconnaît votre voix, ou votre clé, vous pouvez donner des
instructions aux commis de son cabinet. Tout ce que vous dites passe par le
tuyau. Personne, en chemin, ne peut l'entendre.

## Ce qui se passe vraiment

`ssh` (*secure shell*) ouvre une connexion chiffrée vers une machine distante.
Il vérifie la clé de cette machine, vous identifie par clé ou par mot de passe,
puis y lance un shell. Les commandes s'exécutent alors là-bas. `exit` ferme la
liaison. `ssh host cmd` exécute une seule commande. Les clés se trouvent dans
`~/.ssh`.

## Essayez

```console
$ ssh you@library.example.org
you@library.example.org's password:
you@library:~$ hostname
library
you@library:~$ exit
```

## Notes en marge

| Écrire              | Cela veut dire                                   |
|---------------------|--------------------------------------------------|
| `ssh you@house`     | Ouvrez le tuyau vers cette maison, à mon nom     |
| `ssh house cmd`     | Faites exécuter une instruction là-bas, puis refermez |
| `ssh -i key house`  | Prouvez qui je suis avec cette clé               |
| `exit`              | Remettez le capuchon sur le tuyau                |

## Quand un agent demande

Vérifiez à quelle maison il se relie, et pourquoi. Dès lors, ses instructions
agissent sur cette machine, peut-être un serveur en service dont d'autres
personnes dépendent.

## Attention

- Un avertissement indiquant que la clé de la machine a changé peut signifier que quelqu'un se fait passer pour la maison. Ne l'écartez pas d'un geste.
- Ne collez jamais nulle part la clé privée rangée dans `~/.ssh`.
