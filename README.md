# HackElections

Documentation pour l'Open Data Camp Elections organisé le 23 février 2015 par le Centre de données socio-politiques (IEP Paris), le ministère de l'Intérieur et Etalab. 

## Données

### Elections présidentielles

### Elections législatives

* A savoir
 * L'élection législative de 1986 est la seule élection au scrutin proportionnel

* Structure des données : 
  * 1958-1981 : Circonscription * Tour * Tendance
  * 1986 : Circonscription * Tendance
  * 1988-2012 : Circonscription * Tour * Candidat
  * 1988-1997 : Communes * Tour * Tendance pour les communes de plus de 9 000 habitants
  * 2002-2012 : Communes * Tour * Tendance pour toutes les communes

### Elections régionales

### Elections cantonales

## Données annexes

### Découpages territoriaux

* [IGN-GeoFla](http://professionnels.ign.fr/geofla#tab-3) Découpage administratif national réalisé par l'IGN. 
 * Contient les Shapefiles des communes, des cantons et des départements de 2011 à 2014  
* [Contour des communes actuelles d'après OpenStreetMap](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/)
* [Contour des départements actuels d'après OpenStreetMap](https://www.data.gouv.fr/fr/datasets/contours-des-departements-francais-issus-d-openstreetmap/)
* Contour des circonscriptions électorales après le redécoupage de 2010 : 
 * [Fichiers de Joel Gombin](http://www.joelgombin.fr/un-fonds-de-carte-vectoriel-pour-les-circonscriptions-legislatives/) en KML et Shapefile.


### Données sociodémographiques des circonscriptions 

* Description sociodémographiques des circonscriptions électorales d'après l'Insee 
 * [page web](http://www.insee.fr/fr/themes/detail.asp?reg_id=0&ref_id=circo_leg-2012)
 * [Fichier xls](http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/circo_leg/circo_leg-2012/tableau/circonscriptions.xls)


## Outils 

### Cartographie

Voici quelques outils permettant de faire des cartes : 

* R + ggplot : 
* [R + leaflet](http://rstudio.github.io/leaflet/) : un package qui permet de faire des cartes en leaflet.js depuis R
* [R + rMaps](http://rmaps.github.io/) : un package qui permet de réaliser des cartes en datamaps.js directement depuis R
* [datamaps](http://datamaps.github.io/)
* [d3.js](http://bost.ocks.org/mike/map/), une librairie javascript développée par Mike Bostock
* [kartograph](http://kartograph.org/), une librairie python et javascript développée par Gregor Aisch (@gka)

### Nettoyage des fichiers

* [LireMinInterieur](https://github.com/joelgombin/LireMinInterieur), un package R développé par @joelgombin pour nettoyer les fichiers électoraux du ministère de l'Intérieur 
