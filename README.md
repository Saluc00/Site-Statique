# Générateur de site statique

Projet stable et prêt à l'utilisation.

## Sommaire

* [Présentation du projet](#présentation-du-projet)
* [Utilisation](#utilisation)

## Présentation du projet

Réalisation d'un outil convertissant le contenue d'un dossier contenant des fichiers **markdown** en fichiers **HTML** lu par les navigateurs.

## Utilisation

Pour utiliser le générateur de site statique.

Dans un **CLI** *(Invite de commande, exemple : CMD sur Windows)*, il vous faudra être dans le dossier contenant le fichier `main.py` puis appeler ce fichier évoqué précédemment, suivie des différentes commandes d'utilisation du programme.

Plusieurs commandes sont à votre disposition.

* `-i`ou `--input`, est suivie du dossier contenant les fichier *.md*. Soit : `-i [MonDossierMD]` ou `--input [MonDossierMD]`
* `-u` ou `--output`, est suivie du dossier contenant les fichier *.html*. Soit : `-u [MonDossierHTML]` ou `--output [MonDossierHTML]`
* `-h` ou `--help`, Affiche l'aide du programme.

Pour ainsi dire, l'utilisation du générateur de site statique se fais de la sorte :

```
main.py -i [DossierContenantMD] -u [DossierContenantHTML]
```

Ou bien :

```
main.py --input [DossierContenantMD] --output [DossierContenantHTML]
```

*Par USEREAU Lucas*