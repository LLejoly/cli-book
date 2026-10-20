---
command: echo
title: Le Perroquet
metaphor: >
  Le perroquet du cabinet, qui vous répète exactement ce que vous lui dites, après avoir lu les notes épinglées au tableau de liège.
exercise:
  question: "Vous écrivez echo \"My drawer is $HOME\". Que dit le perroquet ?"
  choices:
    - "My drawer is $HOME"
    - "My drawer is /home/you"
    - "Rien, $HOME n'est pas un mot"
  explanation: "Entre guillemets doubles, $HOME est remplacé par la note épinglée sous ce nom avant que le perroquet ne parle. Entre guillemets simples, il dirait $HOME tel quel."
---

## En une ligne

`echo` vous répète le texte que vous lui donnez.

## L'image

Le perroquet, près du secrétaire, répète tout ce que vous dites. Si votre
phrase cite une note du tableau de liège, comme `$HOME`, il lit d'abord la
note. Puis il dit ce qui y est écrit. À lui seul, il ne change rien dans le
cabinet.

## Ce qui se passe vraiment

`echo` écrit ses arguments sur la sortie standard, séparés par des espaces et
suivis d'un retour à la ligne. Le shell remplace les variables comme `$HOME`
et les motifs comme `*` avant que `echo` ne s'exécute. Sa vraie force vient
avec `>` ou `>>`, pour écrire du texte dans un fichier.

## Essayez

```console
$ echo "Hello, Study"
Hello, Study
$ echo "My drawer is $HOME"
My drawer is /home/you
```

## Notes en marge

| Écrire            | Cela veut dire                                   |
|-------------------|--------------------------------------------------|
| `echo text`       | Répétez-moi ceci                                 |
| `echo $NAME`      | Dites ce qui est épinglé au tableau sous NAME    |
| `echo -n text`    | Dites-le sans aller à la ligne                   |
| `echo text > a`   | Écrivez-le plutôt sur la feuille a (voir `>`)    |

## Quand un agent demande

`echo` seul est sans danger. Regardez ce qui suit : `> file` écrit par-dessus
une feuille, et `echo $SECRET` peut afficher un mot de passe dans la
conversation.

## Attention

- `echo $API_KEY` montre votre secret à quiconque voit l'écran ou le journal de l'agent.
