---
title: laurent-laporte-pro.github.io
description: A Python package to install my personal website.
---

# Curriculum Vitæ de Laurent LAPORTE

## Table des matières

- [Installation](#installation)
- [Génération de la documentation](#generation-de-la-documentation)
- [Licence](#licence)

## Installation

Ce projet Python permet de générer mon site web personnel.

Il utilise le gestionnaire de projet [hatch](https://hatch.pypa.io/latest/) pour gérer les dépendances,
les tâches de construction et de déploiement de la documentation sur [GitHub Pages](https://laurent-laporte-pro.github.io/).

⇨ Consultez la documentation de [hatch](https://hatch.pypa.io/latest/install/) pour installer cette commande
sur votre machine.

> **Remarque**: en général, on installe `hatch` de manière globale et non pas dans un environnement virtuel.

## Génération de la documentation

Pour générer la documentation, nous utilisons [mkdocs](https://www.mkdocs.org/).
Cette bibliothèque permet de générer un site web statique à partir de fichiers Markdown.

Pour construire la documentation, exécutez la commande suivante :

```bash
hatch hatch run mkdocs build
```

Pour visualiser la documentation en local, exécutez la commande suivante :

```bash
hatch hatch run mkdocs serve
```

Pour déployer la documentation sur GitHub Pages, exécutez la commande suivante :

```bash
hatch hatch run mkdocs gh-deploy
```

## Licence

Ce projet est privé et ne peut être utilisé sans l'autorisation de l'auteur.

Consultez le fichier [LICENCE.md](LICENCE.md) pour plus d'informations.
