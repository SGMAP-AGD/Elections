# HackElections

Page de ressources pour l'Open Data Camp Elections organisé le 23 février 2015 par le Centre de données socio-politiques (IEP Paris), le ministère de l'Intérieur et Etalab. 

## Données du hackathon

### Elections présidentielles

* Structure des données :
 * 1965-2012 : Circonscription * Tour * Candidat
 * 1981-2002 : Commune * Tour * Candidat pour les communes de plus de 9 000 habitants

### Elections législatives

* A savoir
 * L'élection législative de 1986 est la seule élection au scrutin proportionnel

* Structure des données : 
  * 1958-1981 : Circonscription * Tour * Tendance
  * 1986 : Circonscription * Tendance
  * 1988-2012 : Circonscription * Tour * Candidat
  * 1988-1997 : Commune * Tour * Tendance pour les communes de plus de 9 000 habitants
  * 2002-2012 : Commune * Tour * Tendance pour toutes les communes

### Elections régionales

* Structure des données
 * 1986-1998 : Commune  * Tendance pour les communes de plus de 9 000 habitants 
 * 2004 : Commune * Tour * Liste pour les communes de plus de 3 500 habitants
 * 1986-1992 : Département * Tendance
 * 1998 : Circonscription * Liste
 * 2004-2010 : Circonscription * Tour * Liste

### Elections cantonales

* Structure des données
 * 1988-1998 :  Canton * Tour * Tendance
 * 2001-2011 : Canton * Tour * Candidat

## Données annexes

### Découpages territoriaux

* [IGN-GeoFla](http://professionnels.ign.fr/geofla#tab-3) Découpage administratif national réalisé par l'IGN. 
 * Contient les Shapefiles des communes, des cantons et des départements de 2011 à 2014  
* [Contour des communes actuelles d'après OpenStreetMap](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/)
* [Contour des départements actuels d'après OpenStreetMap](https://www.data.gouv.fr/fr/datasets/contours-des-departements-francais-issus-d-openstreetmap/)
* Contour des circonscriptions électorales après le redécoupage de 2010 : 
 * [Fichiers de Joel Gombin](http://www.joelgombin.fr/un-fonds-de-carte-vectoriel-pour-les-circonscriptions-legislatives/) en KML et Shapefile.


### Données sociodémographiques des circonscriptions 

* Description sociodémographiques des circonscriptions électorales d'après l'Insee en 2012
 * [page web](http://www.insee.fr/fr/themes/detail.asp?reg_id=0&ref_id=circo_leg-2012)
 * [Fichier xls](http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/circo_leg/circo_leg-2012/tableau/circonscriptions.xls)

### Données électorales

* [Résultats électoraux publiés par le ministère de l'Intérieur](http://www.interieur.gouv.fr/Elections/Les-resultats)

## Outils 

### Cartographie

Voici quelques outils permettant de faire des cartes : 

* R + ggplot : 
 * [carto_departements.R](https://github.com/SGMAP-AGD/Elections/blob/master/R/carto_departements.R)  exemple de scripts R pour tracer le contour des départements à partir d'un Shapefile
* [d3.js](http://bost.ocks.org/mike/map/) : une librairie javascript de visualisation interactive de données développée par Mike Bostock (@mbostock)
* [datamaps](http://datamaps.github.io) : une librairie javascript spécialisée en cartographie qui s'appuie sur d3.js
* [R + leaflet](http://rstudio.github.io/leaflet/) : un package qui permet de faire des cartes en leaflet.js depuis R
 * [leaflet_departements.R](https://github.com/SGMAP-AGD/Elections/blob/master/R/leaflet_departements.R) : exemple de script R permettant de tracer le contour des départements sur une carte leaflet.js 
* [R + rMaps](http://rmaps.github.io/) : un package qui permet de réaliser des cartes en datamaps.js directement depuis R
* [kartograph](http://kartograph.org/), une librairie python et javascript développée par Gregor Aisch (@gka)
* [geojson.io](http://geojson.io/#map=2/20.0/0.0) outil en ligne permettant de faire des conversion entre Shapefile, KML et GeoJSON

### Nettoyage des fichiers

* [LireMinInterieur](https://github.com/joelgombin/LireMinInterieur), un package R développé par @joelgombin pour nettoyer les fichiers électoraux du ministère de l'Intérieur.

### Outils de graphiques

* [RAW](http://raw.densitydesign.org/) : un outil en ligne pour faire des graphiques facilement
* [DataWrapper](https://datawrapper.de/) : un outil en ligne pour faire des graphiques simples
* 
