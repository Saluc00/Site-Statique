# G�n�rateur de site statique

Ceci est un projet propos� � des �tudiants en Python.

## Qu'est-ce qu'un site statique

Un site internet statique est un site compos� uniquement de fichiers pr�sents dans un dossier :

* des fichiers HTML,
* des fichiers CSS,
* des fichiers JavaScript,
* des images,
* des vid�os,
* �

Cela s'oppose aux sites internet dynamiques, o� certains de ces fichiers sont g�n�r�s � la vol�e par du logiciel, � partir par exemple de donn�es dans une base de donn�es.

## H�berger un site statique

H�berger un site dynamique est plus complexe que pour un site statique, il faut en effet installer le logiciel qui va g�n�rer les fichiers � la vol�e. Par contre, h�berger un site statique est relativement simple, il suffit d'avoir un petit serveur web qui met � disposition le dossier contenant les fichiers statiques.

### Github

Github fournit un h�bergement gratuit de site statique. Il suffit de cr�er un d�p�t git avec Github, et de committer dans une branche sp�cifique. Votre site est alors accessible � l'adresse suivante : https://votre_login.github.io/votre_nom_de_depot/

Plus de renseignement sur :

* https://pages.github.com/
* https://www.christopheducamp.com/2013/12/21/demarrer-avec-pages-github/
* https://developer.mozilla.org/fr/docs/Apprendre/Utiliser_les_pages_GitHub
  
### Utiliser un serveur web

Des outils commes Apache ou Nginx permettent de rendre accessible votre site par internet ou intranet :
* https://httpd.apache.org/docs/trunk/fr/getting-started.html
* http://sametmax.com/servir-des-fichiers-statiques-avec-nginx/
* https://doc.ubuntu-fr.org/nginx
* https://nginxconfig.io/

Python vous fournit un serveur web minimaliste, par exemple pour aller sur http://localhost:8080/ et y voir le site statique dont les fichiers sont dans `./dossier_de_mon_site/`.

```
python -m http.server 8080  --directory ./dossier_de_mon_site/
```

## G�nerer un site statique

Les fichiers compris par un navigateur internet sont aux formats HTML/CSS/JavaScript. Vous n'avez peut-�tre pas envie de taper du HTML quand vous �crivez un blog. Il serait pratique de g�n�rer les pages web � partir d'un format textuel simple, comme le markdown (https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf), langage utilis� pour �crire le document que vous lisez actuellement (https://raw.githubusercontent.com/vpoulailleau/site_statique/master/README.md).

Certains outils open-source le font d�j�, dont certains connus et en Python :

* https://blog.getpelican.com/
* https://www.getlektor.com/
* https://www.mkdocs.org/
* https://github.com/eudicots/Cactus
* http://www.sphinx-doc.org/en/master/
* https://www.getnikola.com/

## Projet

Vous allez r�aliser un outil convertissant un dossier de fichiers markdown et d'images en un autre dossier contenant les fichiers d'un site statique. Du HTML sera g�n�r� � partir du markdown, et cet HTML sera m�lang� avec des mod�les de pages web pour g�n�rer des pages toutes conformes au m�me mod�le (par exemple avec le m�me logo, le m�me sommaire de site internet, le m�me fichier CSS r�f�renc�).

Les fichiers markdown peuvent �tre cr��s :

* avec Visual Studio Code
* avec https://github.com/ncornette/Python-Markdown-Editor
* avec https://pandao.github.io/editor.md/en.html
* avec https://dillinger.io/
* �

Pour donner un ordre d'id�e, la version la plus basique du projet peut �tre faite en moins de 100 lignes.

### R�alisation d'une interface en ligne de commande

Vous allez r�aliser un outil en ligne de commande pour g�n�rer les fichiers du site statique. Il prendra au moins comme param�tres :

* `-i ./un_dossier` ou `--input-directory ./un_dossier` : le chemin du dossier de fichiers source (contenant les fichiers markdown)
* `-o ./un_autre_dossier` ou `--output-directory ./un_autre_dossier` : le chemin du dossier o� seront mis les fichiers g�n�r�s pour le site statique
  * si le dossier existe d�j�, libre � vous de soit l'effacer, soit �crire dedans pour faire des mises � jours (cela sera expliqu� dans le mode d'emploi de votre outil)
  * vous pouvez choisir la convention de nommage qui vous pla�t pour les fichiers g�n�r�s, par exemple vous pouvez utiliser comme pr�fixe le nom du fichier markdown correspondant (cela sera aussi expliqu�)
* `-t ./autre_dossier` ou `--template-directory ./autre_dossier` : �ventuellement le dossier contenant des mod�les de pages web � compl�ter
* `-h` ou `--help` : pour afficher de l'aide pour exliquer les param�tres de la commande

Vous pouvez �ventuellement ajouter des param�tres comme :
* ce que vous voulez
* `-k` ou `--kikoo-lol` qui ajoutera dans le texte des � kikoo �, � lol �, � mdr �, � ptdr � ou qui r�p�te des lettres comme dans Hellllo, et autres d�formations du fran�ais (https://fr.wiktionary.org/wiki/kikoolol)
* `-a` ou `--achtung` pour aider les allemands � lire nos blogs fran�ais. Si vous appliquez les r�gles d�crites [ici](https://linuxfr.org/nodes/108129/comments/1642666), zela aidera dafantach no zami alemand dan la prononziation de notr langue et dan la kompr�henzion de no z�kri

Vous pouvez utiliser :

* sys.argv (mais je ne vous le conseille pas, https://docs.python.org/fr/3/library/sys.html#sys.argv)
* argparse (https://docs.python.org/fr/3/howto/argparse.html)
* click (https://click.palletsprojects.com/en/7.x/)

Il se peut donc que votre projet soit utilis� par exemple avec :

```bash
python3.7 generateur.py --input-directory ./dossier_markdown --output-directory ./dossier_resultat/ --achtung -k
```

### Conversion de markdown vers HTML

Vous devez au moins convertir les syntaxes suivantes :

* `#`, un titre de niveau 1 en `<h1>`
* `##`, un titre de niveau 2 en `<h2>`
* `###`, un titre de niveau 3 en `<h3>`
* Convertir les listes non ordon�es en `<ul>` et `<li>`
* Convertir les URL (http://quelquechose.com) en `<a href="http://quelquechose.com">http://quelquechose.com</a>`
* `*un texte*`, un texte important en `<em>un texte</em>`

Vous pouvez faire ces conversions en utilisant au choix :

* les fonctions de base de Python pour les cha�nes de caract�res
* les expressions r�guli�res (https://docs.python.org/fr/3/library/re.html)
* un package de la communaut�
  * https://github.com/Python-Markdown/markdown
  * https://github.com/trentm/python-markdown2

### Qualit� du code

Vous veillerez � respecter :

* la PEP 8 :  https://www.python.org/dev/peps/pep-0008/ (vous pouvez vous aider avec https://github.com/ambv/black et https://github.com/hhatto/autopep8)
* la PEP 20 : https://www.python.org/dev/peps/pep-0020/
* plus de d�tails sur https://vpoulailleau.wordpress.com/2018/12/04/un-code-pythonique/

### Rendu sur Github

Votre projet **personnel** Python sera post� sur Github et un lien vers le d�p�t public sera fourni.

� la racine de votre d�p�t git se trouvera un fichier README.md qui expliquera comment fonctionne votre projet, comment l'utiliser, quel est sa licence�

### Projet open-source

Vous pouvez faire un projet libre et open-source. Beaucoup de projets Python utilisent la license MIT ou BSD 3 clauses, ces licences sont faciles � lire et tr�s permissives. Vous pouvez aussi utiliser une licence plus stricte comme la GPL qui impose que les versions modifi�es de votre projet soient aussi open-source.

Vous pouvez lire la licence BSD 3 clauses du projet https://github.com/vpoulailleau/simplelogging � l'adresse suivante https://github.com/vpoulailleau/simplelogging/blob/master/LICENSE.

Vous pouvez faire en sorte que votre projet soit installable par la communaut� Python en le diffusant sur le Python Package Index (https://pypi.org/), comme par exemple https://pypi.org/project/simplelogging/.

Pour vous aidez dans cette aventure, vous pouvez utiliser https://github.com/audreyr/cookiecutter-pypackage.

### Mises � jour de l'�nonc�

Il se peut que, suite � des questions re�ues, l'�nonc� soit mis � jour. La derni�re version de l'�nonc� est disponible ici : https://github.com/vpoulailleau/site_statique. Vous pouvez voir son historique sur https://github.com/vpoulailleau/site_statique/commits/master.

### Objectifs

Il va de soi que se documenter, copier du code (dans le respect des licences), discuter avec d'autres codeurs est vivement recommand� pour progresser. Regardez comment font les autres, et faites � votre fa�on. Soyez capables d'expliquer ce que vous avez fait.

Pour rappel toutefois, un code sans licence est par d�faut prot�g� par le droit d'auteur, vous n'avez donc pas le droit de le copier, sauf avec un accord de l'auteur.

### �valuation

Le projet est adapt� � tous les niveaux, une version basique est r�alisable, mais le projet peut aller jusqu'� la r�alisation d'un outil open-source rendu disponible � la communaut�.

Les crit�res d'�valuation sont les suivants :

* implication (visible entre autres par l'historique de votre d�p�t git)
* respect de la PEP 8
* respect de la PEP 20
* qualit� du fichier README.md
* r�alisation en conformit� avec les fonctionnalit�s de base de cette �nonc�
* des points bonus si vous allez plus loin

Vous pouvez vous faire une id�e en utilisant le bar�me suivant : https://github.com/vpoulailleau/site_statique/blob/master/checklist.md.

Bon apprentissage, et bon projet.

## Id�es d'algorithme

### Ligne de commande

Commencez par mettre en place la ligne de commande qui acceptera les diff�rents param�tres mentionn�s :

* Affichage du message d'aide (argparse et click savent le g�n�rer en automatique)
* Affichage du nom des dossiers pass�s en param�tres de la ligne de commande

### G�n�ration des fichiers statiques

#### Parcours du dossier de sources

Il va falloir faire un traitement pour chaque fichier markdown pr�sent dans le dossier contenant les fichiers markdown. [Pathlib](https://docs.python.org/fr/3/library/pathlib.html) et sa m�thode [glob](https://docs.python.org/fr/3/library/pathlib.html#pathlib.Path.glob) peuvent aider.

#### Conversion markdown vers HTML

Les fichiers markdown sont des fichiers texte. Il faut les ouvrir, les lire, et g�n�rer le HTML correspondant.

Le r�sultat de chaque conversion est stock� dans un fichier HTML dans le dossier qui contiendra les fichiers statiques (dossier fourni par la ligne de commande).

Les premi�res conversions (les titres) peuvent facilement se r�aliser avec la m�thode [replace](https://docs.python.org/3/library/stdtypes.html#str.replace) des chaines de caract�res.

Il est possible de passer par les [expressions r�guli�res](https://docs.python.org/fr/3/library/re.html), vous pouvez m�me vous faire aider en utilisant cursive_re pr�sent� sur https://vpoulailleau.wordpress.com/2018/11/29/des-expressions-regulieres-lisibles/.

#### M�canisme de template

Le m�canisme de pages mod�les le plus simple est le suivant :

* Vous cr�ez une page HTML par d�faut, et sans contenu, juste le sommaire, le logo, le chargement de CSS�
* � la place du contenu dans la page HTML, vous mettez le texte � REPLACE_ME �
* Quand vous g�n�rez une page HTML, vous ouvrez la page mod�le, et vous remplacer � REPLACE_ME � par l'HTML que vous avez g�n�r� � partir du markdown
* Vous pouvez utiliser https://getbootstrap.com/ pour faire rapidement du HTML plus �volu� (responsive design, menus, listes d�roulantes, slide show�)
* Pour ceux qui veulent faire un m�canisme plus �volu� de pages mod�les, vous pouvez regarder http://jinja.pocoo.org/, https://genshi.edgewall.org/, https://www.makotemplates.org/, https://opensource.com/resources/python/template-libraries
