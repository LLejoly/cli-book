---
command: cat
title: Le Lutrin
metaphor: >
  Un lutrin où le commis vous lit une feuille à voix haute, de la première ligne à la dernière.
exercise:
  question: "Que fait cat notes.txt letters/to-grandma.txt ?"
  choices:
    - "Colle les deux feuilles ensemble pour de bon"
    - "Lit les deux feuilles à voix haute, l'une après l'autre"
    - "Ne lit que la première feuille"
  explanation: "cat lit chaque feuille nommée, dans l'ordre, sans en changer aucune. Son nom vient de l'anglais conCATenate : enchaîner."
---

## En une ligne

`cat` vous montre tout ce qui est écrit dans un fichier.

## L'image

Vous tendez une feuille au commis. Il la pose sur le lutrin et vous la lit à
voix haute, chaque ligne, de haut en bas. Donnez-lui deux feuilles : il les lit
l'une après l'autre, sans pause. Les feuilles retournent ensuite dans le
tiroir, exactement comme elles étaient.

## Ce qui se passe vraiment

`cat` lit chaque fichier nommé, dans l'ordre, et écrit ses octets sur la sortie
standard. Son nom vient de l'anglais « concatenate » (enchaîner). Il ne modifie
pas les fichiers. Sur un fichier binaire, comme une image, il affiche des
caractères illisibles. Pour un long fichier, un paginateur comme `less` se lit
plus facilement.

## Essayez

```console
$ cat notes.txt
buy flour
call grandma
pay the bank
buy ink
$ cat -n notes.txt
     1	buy flour
     2	call grandma
     3	pay the bank
     4	buy ink
```

## Notes en marge

| Écrire               | Cela veut dire                                    |
|----------------------|---------------------------------------------------|
| `cat sheet`          | Lire cette feuille à voix haute                   |
| `cat -n sheet`       | La lire avec un numéro devant chaque ligne        |
| `cat a b`            | Lire la feuille a, puis la feuille b              |
| `cat a b > c`        | Recopier les deux, dans l'ordre, sur une nouvelle feuille c |

## Quand un agent demande

Les agents utilisent `cat` pour lire un fichier avant de le modifier. C'est une
bonne pratique, et vous pouvez accepter sans crainte. Souvenez-vous que ce
qu'il lit, l'agent le sait désormais. Réfléchissez à deux fois avant de le
laisser lire des fichiers qui contiennent des mots de passe ou des clés
privées.

## Attention

- `>` ne fait pas partie de `cat`. Il écrit sur une feuille et efface d'abord ce qui s'y trouvait : `cat a > a` vous laisse donc une feuille blanche.
