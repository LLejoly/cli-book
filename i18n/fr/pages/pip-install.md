---
command: pip install
title: Le Bon de commande
metaphor: >
  Un bon de commande posté au catalogue d'un fournisseur, dont le colis est livré et déballé directement dans votre cabinet.
exercise:
  question: "Vous vouliez taper pip install requests, mais vous avez tapé pip install requestss. Pourquoi est-ce important ?"
  choices:
    - "Ce n'est pas grave, pip corrige l'orthographe"
    - "Quelqu'un a pu inscrire un colis sosie sous ce nom, et il sera déballé et exécuté tout pareil"
    - "pip refusera une faute de frappe"
  explanation: "N'importe qui peut inscrire un colis au catalogue. Les noms sosies sont une ruse connue. pip installe ce que vous nommez, et son code peut s'exécuter pendant l'installation."
---

## En une ligne

`pip install` télécharge un paquet Python depuis Internet et l'installe.

## L'image

Vous remplissez un bon de commande tiré du catalogue de vente par correspondance
du fournisseur, et vous le
postez. Un colis arrive. On le déballe dans votre cabinet, avec tout ce que le
colis dit lui-même réclamer. Vous n'ouvrez pas chaque boîte pour l'inspecter.
Vous faites confiance au fournisseur et au nom inscrit sur le bon.

## Ce qui se passe vraiment

`pip` cherche le paquet nommé et ses dépendances dans un index (PyPI par
défaut), les télécharge, puis les installe dans l'environnement Python actif.
Un paquet livré en sources peut exécuter du code de construction pendant
l'installation. `-r requirements.txt` installe toute une liste. `==` fixe une
version précise.

## Essayez

```console
$ pip install requests
Collecting requests
...
Successfully installed certifi-2024.8.30 charset-normalizer-3.4.0 idna-3.10 requests-2.32.3 urllib3-2.2.3
```

## Notes en marge

| Écrire                       | Cela veut dire                              |
|------------------------------|---------------------------------------------|
| `pip install name`           | Commander ce colis et le déballer           |
| `pip install name==2.1`      | Commander exactement la version 2.1         |
| `pip install -r list.txt`    | Commander tout ce qui est sur cette liste   |
| `pip uninstall name`         | Le remballer et le renvoyer                 |

## Quand un agent demande

Lisez le nom du colis lettre par lettre, et vérifiez qu'il est bien connu.
Installez de préférence dans l'environnement propre au projet (un venv) plutôt
que dans tout le système. Et jamais avec `sudo pip`.

## Attention

- Les noms mal orthographiés ou sosies sont un moyen connu de livrer des colis malveillants.
- `sudo pip install` laisse un colis non vérifié se déballer dans chaque tiroir de la maison.
