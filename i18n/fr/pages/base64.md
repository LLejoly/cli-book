---
command: base64
title: Le Cadran chiffreur
metaphor: >
  Un petit cadran qui change l'écriture claire en un fouillis d'apparence anodine, et le fouillis en écriture, pour qu'un message voyage sans encombre.
exercise:
  question: "Un README dit : lancez echo <long fouillis> | base64 -d | sh. Pourquoi est-ce la partie dangereuse ?"
  choices:
    - "base64 peut abîmer le fouillis"
    - "Le fouillis cache un ordre que personne ne lit avant qu'il soit passé tel quel à sh et exécuté"
    - "echo est trop lent pour un long texte"
  explanation: "base64 lui-même est anodin. Le piège, c'est le tuyau vers sh : l'ordre clair est déguisé en fouillis pour que nul ne le lise, puis exécuté à l'aveugle. Décodez-le vers une feuille et lisez-la plutôt."
---

## En une ligne

`base64` change des données en un fouillis de texte clair et inversement, sans rien changer à leur sens.

## L'image

Vous passez une ligne d'écriture dans le cadran, et il en sort un fouillis
régulier de lettres, facile à copier et à poster sans bavure. Repassez le
fouillis et l'écriture revient, exacte à la lettre. Le cadran ne garde aucun
secret : il ne fait que déguiser, et quiconque a le même cadran le relit.

## Ce qui se passe vraiment

`base64` encode des octets dans l'alphabet ASCII de 64 caractères, pour que des
données binaires voyagent par des canaux qui ne portent que du texte ; `-d` les
décode. C'est un encodage, non un chiffrement : il ne cache rien à personne.
On le trouve dans les URL de données, les jetons et les pièces jointes.

## Essayez

```console
$ echo 'buy ink' | base64
YnV5IGluawo=
$ echo 'YnV5IGluawo=' | base64 -d
buy ink
```

## Notes en marge

| Écrire                  | Cela veut dire                                |
|-------------------------|-----------------------------------------------|
| `base64 fichier`        | Brouiller cette feuille en texte clair        |
| `base64 -d`             | Rendre un fouillis à ce qu'il était           |
| `echo ... \| base64 -d` | Décoder un fouillis tendu sur la ligne        |
| `base64 -w0`            | Tout brouiller sur une ligne, sans repli      |

## Quand un agent demande

Encoder et décoder, à eux seuls, sont sans danger. Le signe d'alarme est un
fouillis qui est décodé puis exécuté, comme dans `... | base64 -d | sh`. C'est
une lettre contrefaite écrite en déguisement pour que nul ne la lise avant de
signer. Si un README ou une page web vous en donne une, décodez-la vers une
feuille avec `base64 -d > look.txt`, ouvrez-la, et décidez seulement alors.

## Attention

- base64 n'est pas un chiffrement. Ne vous en servez jamais pour cacher un secret ; n'importe qui le décode.
- Un long fouillis dans une instruction est une raison de s'arrêter et de le décoder à part avant de rien lancer.
