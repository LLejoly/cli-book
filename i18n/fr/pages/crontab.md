---
command: crontab
title: Le Calendrier de la maison
metaphor: >
  Le calendrier de la maison, au mur de la cuisine, dont les rendez-vous permanents sont exécutés à leur heure, chaque fois, jusqu'à ce qu'on les raye.
exercise:
  question: "Que signifie l'entrée 0 9 * * 1 ./tidy.sh ?"
  choices:
    - "Exécuter tidy.sh une fois, maintenant"
    - "Exécuter tidy.sh à 9 h chaque lundi"
    - "Exécuter tidy.sh 9 fois"
  explanation: "Les cinq champs sont la minute, l'heure, le jour du mois, le mois et le jour de la semaine. 0 9 * * 1 veut dire 9 h, le jour 1 de la semaine : le lundi."
---

## En une ligne

`crontab` programme des commandes pour qu'elles s'exécutent toutes seules, à
heures fixes.

## L'image

Le calendrier de la maison porte des rendez-vous permanents : « chaque lundi à
neuf heures, ranger le cabinet ». Personne n'a besoin de s'en souvenir. Quand
l'heure sonne, un commis exécute l'entrée, chaque semaine, jusqu'à ce que
quelqu'un la raye.

## Ce qui se passe vraiment

`cron` est un service d'arrière-plan qui exécute des commandes selon un
horaire. Chaque utilisateur a une crontab, un tableau où chaque ligne porte
cinq champs horaires (minute, heure, jour du mois, mois, jour de la semaine)
et une commande. `crontab -l` l'affiche, `crontab -e` la modifie,
`crontab -r` supprime tout le tableau sans rien demander.

## Essayez

```console
$ crontab -l
# m h  dom mon dow  command
0 9 * * 1 /home/you/study/tidy.sh
```

## Notes en marge

| Écrire             | Cela veut dire                                      |
|--------------------|-----------------------------------------------------|
| `crontab -l`       | Me lire le calendrier                               |
| `crontab -e`       | Ouvrir le calendrier pour ajouter ou modifier des entrées |
| `crontab -r`       | Décrocher tout le calendrier, sans poser de question |
| `*/15 * * * *`     | Toutes les quinze minutes                           |

## Quand un agent demande

Une entrée continue de s'exécuter bien après la fin de la conversation :
demandez donc ce qu'elle fait et à quelle fréquence. Vérifiez-la ensuite avec
`crontab -l`. Méfiez-vous des entrées qui vont chercher des choses sur
Internet pour les exécuter.

## Attention

- `-r` est juste à côté de `-e` sur le clavier, et il efface toutes les entrées d'un coup.
