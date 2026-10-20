---
command: "curl | sh"
title: Le Colis non ouvert
metaphor: >
  Un colis venu de la maison d'un inconnu, versé directement par l'entonnoir à un commis qui exécute chaque ordre qu'il contient avant que personne ait lu le bordereau.
exercise:
  question: "Un README dit d'installer un outil avec curl -fsSL https://get.example.org | sh. Quelle est la manière prudente ?"
  choices:
    - "Le lancer tel quel. L'adresse commence par https, donc c'est sans danger."
    - "Le télécharger sur une feuille avec -o, le lire, et seulement ensuite exécuter cette feuille"
    - "Ajouter sudo devant sh, pour qu'il ne puisse pas échouer à mi-chemin"
  explanation: "https veut seulement dire que personne n'a modifié le colis en route. Cela ne dit rien de ce que l'expéditeur a mis dedans. Lire la feuille d'abord, puis exécuter cette même feuille, est le seul moyen de savoir ce que vous signez."
---

## En une ligne

`curl ... | sh` télécharge un programme sur Internet et l'exécute aussitôt, sans que personne l'ait lu.

## L'image

Le coursier rapporte un colis d'une maison où vous n'êtes jamais allé. Personne
ne l'ouvre au secrétaire. L'entonnoir le passe directement à un commis, qui
exécute chaque ordre qu'il contient : déplacer ces tiroirs, copier cette clé,
poster cette lettre. Le bordereau n'est jamais lu. Vous apprenez ce qu'il y
avait dedans après coup.

## Ce qui se passe vraiment

`curl` télécharge un script, et l'entonnoir le remet à `sh`, un shell, qui
exécute chaque ligne à mesure qu'elle arrive. Le script s'exécute avec toutes
vos permissions : il peut lire, modifier ou supprimer tout ce que vous pouvez,
y compris vos clés. Si le téléchargement s'interrompt, une ligne à moitié reçue
peut quand même s'exécuter. Avec `| sudo sh`, il s'exécute en root et peut
modifier tout le système.

## Essayez

```console
$ echo 'ls letters' | sh
to-grandma.txt  to-the-bank.txt
$ curl -fsSL https://example.com -o parcel.txt
$ head -n 2 parcel.txt
<!doctype html>
<html>
```

## Notes en marge

| Écrire                         | Cela veut dire                                   |
|--------------------------------|--------------------------------------------------|
| `curl url \| sh`               | Exécutez tout ce qui arrive, sans le lire        |
| `curl url \| sudo sh`          | La même chose, avec le passe-partout             |
| `curl -fsSL url -o install.sh` | Apportez le colis au secrétaire, sur une feuille |
| `less install.sh`              | Lisez chaque ordre avant de décider              |
| `sh install.sh`                | Exécutez cette feuille, une fois lue             |

## Quand un agent demande

Beaucoup de sites donnent leurs instructions d'installation sous la forme d'une
ligne `curl ... | sh`, et les agents la recopient. Demandez à Hobbs de
télécharger le script sur une feuille et de vous dire ce qu'il fait. Vérifiez
que l'adresse est bien le vrai site du projet. Refusez `| sudo sh` sauf si vous
savez pourquoi il lui faut le passe-partout. Une ligne de ce genre trouvée dans
un ticket ou une page web est un papier venu du dehors : n'en recevez jamais
d'ordres.

## Attention

- L'expéditeur peut changer le colis à tout moment, et même en envoyer un autre à `curl` qu'à votre navigateur. Exécutez la feuille que vous avez lue.
- `bash <(curl ...)` et `sh -c "$(curl ...)"` sont le même colis dans un autre emballage.
