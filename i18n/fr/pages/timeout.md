---
command: timeout
title: Le Sablier
metaphor: >
  Un sablier à œufs retourné à côté de la tâche d'un commis : quand le sable est écoulé, on lui dit de s'arrêter, qu'il ait fini ou non.
exercise:
  question: "timeout 60 pytest s'arrête au bout d'une minute et $? vaut 124. Qu'est-ce que cela veut dire ?"
  choices:
    - "Tous les tests ont réussi"
    - "Le sable s'est écoulé : les tests ont été interrompus avant la fin, vous ne savez donc encore rien"
    - "Exactement 124 tests ont échoué"
  explanation: "124 est le signal propre à timeout pour dire que le temps était écoulé. La tâche a été arrêtée en route : il n'y a pas de verdict sur les tests, seulement qu'ils ont pris trop de temps."
---

## En une ligne

`timeout` exécute une commande et l'arrête si elle dure plus longtemps que vous ne le permettez.

## L'image

Vous donnez un billet à un commis et vous retournez le sablier à côté de lui.
S'il finit le premier, rien de plus ne se passe. Si le dernier grain de sable
tombe alors qu'il travaille encore, la clochette sonne pour lui et il doit
poser sa tâche là où elle en est.

## Ce qui se passe vraiment

`timeout DURATION COMMAND` lance la commande et lui envoie `TERM` si elle
tourne encore après la durée donnée (en secondes par défaut, ou `m`, `h`,
`d`). Si elle a été arrêtée, `timeout` se termine avec le statut 124. Sinon,
il renvoie le statut de la commande elle-même. `-s` choisit un autre signal,
et `-k` envoie `KILL` plus tard si `TERM` a été ignoré.

## Essayez

```console
$ timeout 2 sleep 10
$ echo $?
124
$ timeout 5 cat notes.txt
buy flour
call grandma
pay the bank
buy ink
$ echo $?
0
```

## Notes en marge

| Écrire                 | Cela veut dire                                |
|------------------------|-----------------------------------------------|
| `timeout 30 cmd`       | Arrêter le commis au bout de trente secondes  |
| `timeout 5m cmd`       | Cinq minutes de sable                         |
| `timeout -k 10 60 cmd` | Sonner à une minute, le renvoyer dix secondes plus tard |
| `timeout -s INT 30 cmd`| Sonner comme Ctrl+C au lieu du tintement habituel |

## Quand un agent demande

Les agents enveloppent les tâches longues ou incertaines dans `timeout` pour
ne pas attendre sans fin une série de tests, un serveur ou un appel sur le
réseau. C'est une bonne habitude. Le sceau est celui du billet à l'intérieur :
lisez cette partie comme si elle était seule. `timeout 60 rm -rf build` efface
tout aussi complètement. Vérifiez que le temps laissé suffit pour finir la
tâche.

## Attention

- Une tâche arrêtée à mi-chemin peut laisser derrière elle des feuilles à moitié écrites.
- Le statut 124 veut dire « temps écoulé », ni « échec » ni « réussite ».
