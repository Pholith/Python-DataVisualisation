# Aperçu du projet
![capture d'écran du projet](/screenPython.png)

# Guide utilisateur

La version de python recommandé est 3.7, car la librairie dash ne supporte pas encore les versions supérieurs. 
Vous devrez adapter les commandes avec votre version de python installé.

### Commandes d'installation:
```
python3.7 -m pip install pandas
python3.7 -m pip install simpledbf
python3.7 -m pip install numpy==1.19.3
python3.7 -m pip install dash
```
### Commande d'exécution:
```
python3.7 __init__.py
```
Le serveur dash sera lancé sur ce lien http://127.0.0.1:8050/
Le jeu de donnée étant important (80Mo), le lancement du programme et les chargements des données sur la page peuvent prendre quelques minutes.

# Rapport d'analyse

### Source des données

Les données utilisés dans le programme sont téléchargables sur ce ![lien](https://www.data.gouv.fr/fr/datasets/le-marche-du-haut-et-tres-haut-debit-fixe-deploiements/).
Les données sont accessibles dynamiquement via ce lien mais nous avons volontairement choisi de lire ces données depuis un fichier téléchargé pour éviter de retélécharger le fichier de 80Mo à chaque utilisation du programme. 
Le fichier geojson permet d'affiche les polygones des communes, il a aussi été téléchargé sur le site du gouvernement.

### Analyse

On peut observer sur la carte que la région parisienne est la zone où la couverture de fibre semble la plus importante et la plus étendue.
Le nord-est est globalement plus couvert que le sud-ouest. 

La couverture de fibre semble liée à la densité de population de chaque commune. Par exemple, le Nord pas de calais et Paris sont des zones très peuplés et très couvertes, le Limousin et la champagne-ardenne sont peu peuplés et peu couverte par la fibre.

Le département de la Loire qui est complètement couvert par la fibre et sa frontière avec les autres départements est très nette sur la carte, cela 
laisse supposer que la couverture de fibre est influencée par la politique départementale. Cela est aussi visible sur les frontière de la Picardie.

On peut enfin voir que les plus grandes villes de France et leurs périphéries sont bien couvertes par la fibre.

L'histogramme nous montre que la plupart des communes sont soit reliées avec une couverture de plus 80% à la fibre, soit aucunement reliées. 
On peut supposer que cela est lié à la difficulté de se lier au réseau de fibre ou à la politique local. 

# Guide développeur

Le code est découpé en plusieurs parties:
1. On commence par importer les librairies, les plus importantes sont pandas et plotly.express.
2. On définie les fonctions utilisées, il y a ici une seule fonction qui a servi pendant le développement.
3. Dans le programme principal (fonction main), on ouvre les données et on converti le format Dbf5 donné par le gouvernement en format dataframe utilisable.
4. On créer ensuite la carte à l'aide de plotly.express.
5. On effectue quelques opérations sur les données et on créer l'histogramme.
6. Enfin, on utilise dash pour créer un serveur, formater la page et afficher les diagrammes. 
