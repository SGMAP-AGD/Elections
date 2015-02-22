# DataElections

Page de ressources pour l'Open Data Camp Elections organisé le 23 février 2015 par le Centre de données socio-politiques (IEP Paris), le ministère de l'Intérieur et Etalab. 

## Sujets

Chacun peut proposer un sujet sur le [pad](https://lite5.framapad.org/p/x7bq6bVyFO) du projet. Soyez brefs et inventifs. Tous les porteurs d'un sujet seront invités à le présenter rapidement lundi matin pour former une équipe.

## Restitutions

N'hésitez pas à publier vos projets, par exemple sur GitHub, et à poster vos réutilisations sur [DataGouv](http://www.data.gouv.fr/).

## Données du hackathon

Note: le signe ' * ' indique le croisement de variable.

### Elections présidentielles

#### Données du CDSP

* [Données du CDSP](https://www.data.gouv.fr/fr/datasets/elections-presidentielles-1965-2012-1/)
 * Structure des données :
  * 1965-2012 : Circonscription * Tour * Candidat
  * 1981-2002 : Commune * Tour * Candidat pour les communes de plus de 9 000 habitants

#### Données du ministère de l'Intérieur

* Structure : canton * tour * candidat : 
	* Note : Les résultats sont aussi agrégés par circonscription législative, département et région  
	* [1995](https://www.data.gouv.fr/fr/datasets/election-presidentielle-1995-resultats-572083/)
	* [2002](https://www.data.gouv.fr/fr/datasets/election-presidentielle-2002-resultats-572114/)
	* [2007](https://www.data.gouv.fr/fr/datasets/election-presidentielle-2007-resultats-572120/) 
	* [2012](https://www.data.gouv.fr/fr/datasets/election-presidentielle-2012-resultats-572124/)
 
* Structure : commune * tour * candidat : 
	* [1995](https://www.data.gouv.fr/fr/datasets/election-presidentielle-1995-resultats-572085/) 
	* 2002 :  [1er tour](https://www.data.gouv.fr/fr/datasets/election-presidentielle-2002-resultats-572116/), [2ème tour](https://www.data.gouv.fr/fr/datasets/election-presidentielle-2002-resultats-572118/)
	* [2007](https://www.data.gouv.fr/fr/datasets/election-presidentielle-2007-resultats-572122/)
	* [2012](https://www.data.gouv.fr/fr/datasets/election-presidentielle-2012-resultats-572126/)

### Elections législatives

#### Contexte

* L'élection législative de 1986 est la seule élection au scrutin proportionnel

#### Données du CDSP 

* [Données du CDSP](https://www.data.gouv.fr/fr/datasets/elections-legislatives-1958-2012/)
 * 1958-1981 : Circonscription * Tour * Tendance
 * 1986 : Circonscription * Tendance
 * 1988-2012 : Circonscription * Tour * Candidat
 * 1988-1997 : Commune * Tour * Tendance pour les communes de plus de 9 000 habitants
 * 2002-2012 : Commune * Tour * Tendance pour toutes les communes

#### Données du ministère de l'intérieur

* Structure : Canton * tour * candidat 
	* Note : Les résultats sont aussi agrégés par circonscription législative, département et région   
	* [1993](https://www.data.gouv.fr/fr/datasets/elections-legislatives-1993-resultats-572057/)
	* [1997](https://www.data.gouv.fr/fr/datasets/elections-legislatives-1997-resultats-572061/)
	* [2002](https://www.data.gouv.fr/fr/datasets/elections-legislatives-2002-resultats-572065/)
	* [2007](https://www.data.gouv.fr/fr/datasets/elections-legislatives-2007-resultats-572071/)
	* [2012](https://www.data.gouv.fr/fr/datasets/elections-legislatives-2012-resultats-572077/)
	* 

* Structure : Commune * tour * candidat 
	* [1993](https://www.data.gouv.fr/fr/datasets/elections-legislatives-1993-resultats-572059/)
	* [1997](https://www.data.gouv.fr/fr/datasets/elections-legislatives-1997-resultats-572063/)
	* 2002 : [tour 1](https://www.data.gouv.fr/fr/datasets/elections-legislatives-2002-resultats-572067/), [tour 2](https://www.data.gouv.fr/fr/datasets/elections-legislatives-2002-resultats-572069/)
	* 2007 : [tour 1](https://www.data.gouv.fr/fr/datasets/elections-legislatives-2007-resultats-572073/), [tour 2](https://www.data.gouv.fr/fr/datasets/elections-legislatives-2007-resultats-572075/)
	* [2012](https://www.data.gouv.fr/fr/datasets/elections-legislatives-2012-resultats-572079/)

### Elections régionales

#### Données du CDSP

* [Données du CDSP](https://www.data.gouv.fr/fr/datasets/elections-regionales-1986-2010/)
* Structure des données
 * 1986-1998 : Commune  * Tendance pour les communes de plus de 9 000 habitants 
 * 2004 : Commune * Tour * Liste pour les communes de plus de 3 500 habitants
 * 1986-1992 : Département * Tendance
 * 1998 : Circonscription * Liste
 * 2004-2010 : Circonscription * Tour * Liste

#### Données du ministère de l'Intérieur 

* Structure : Canton * tour * liste
	* Note : Les résultats sont aussi agrégés par circonscription législative, département et région 	 	
	* [2004](https://www.data.gouv.fr/fr/datasets/elections-regionales-2004-resultats-572139/)
	* [2010](https://www.data.gouv.fr/fr/datasets/elections-regionales-2010-resultats-572146/) 	

* Structure : Département * tour * liste
	* Note : les résultats sont aussi agrégés par région 	
	* [1998](https://www.data.gouv.fr/fr/datasets/elections-regionales-1998-571487/)

* Structure : Commune * tour * liste
	* [2004](https://www.data.gouv.fr/fr/datasets/elections-regionales-2004-resultats-572143/)
	* [2010](https://www.data.gouv.fr/fr/datasets/elections-regionales-2010-resultats-572148/) 	

### Elections cantonales et départementales

#### Contexte 

Depuis la loi du 17 mai 2013, les élections cantonales sont remplacées par des élections départementales. Les premières élections départementales se tiendront les 22 et 29 mai 2015. Le mode de scrutin est désormais un scrutin binomial majoritaire à deux tours et les cantons ont été redéfinis et le nombre de cantons a été divisé par deux. On passe de 4 055 à 2 074 cantons en 2014.

* [En savoir plus](https://fr.wikipedia.org/wiki/%C3%89lections_d%C3%A9partementales_fran%C3%A7aises_de_2015)

#### Données du CDSP

* [Données du CDSP](https://www.data.gouv.fr/fr/datasets/elections-cantonales-1988-2011/)
 * 1988-1998 :  Canton * Tour * Tendance
 * 2001-2011 : Canton * Tour * Candidat


#### Données du ministère de l'Intérieur

* Structure : Canton * Tour * Candidat
	* Note : Les données sont aussi agrégées par circonscription législative, département et région 	
	* [1992](https://www.data.gouv.fr/fr/datasets/elections-cantonales-1992-resultats-572027/)
	* [1994](https://www.data.gouv.fr/fr/datasets/elections-cantonales-1994-resultats-572031/)
	* [1998](https://www.data.gouv.fr/fr/datasets/elections-cantonales-1998-resultats-572036/)
	* [2001](https://www.data.gouv.fr/fr/datasets/elections-cantonales-2001-resultats-572041/)
	* [2004](https://www.data.gouv.fr/fr/datasets/elections-cantonales-2004-resultats-572045/)
	* [2008](https://www.data.gouv.fr/fr/datasets/elections-cantonales-2008-resultats-572049/)
	* [2011](https://www.data.gouv.fr/fr/datasets/elections-cantonales-2011-resultats-572053/) 	

* Structure : Commune * Tour * Candidat
	* [1992](https://www.data.gouv.fr/fr/datasets/elections-cantonales-1992-resultats-572029/)	 
	* [1994](https://www.data.gouv.fr/fr/datasets/elections-cantonales-1994-resultats-572033/)
	* [1998](https://www.data.gouv.fr/fr/datasets/elections-cantonales-1998-resultats-572038/)
	* [2001](https://www.data.gouv.fr/fr/datasets/elections-cantonales-2001-resultats-572043/) 
	* [2004](https://www.data.gouv.fr/fr/datasets/elections-cantonales-2004-resultats-572047/)
	* [2008](https://www.data.gouv.fr/fr/datasets/elections-cantonales-2008-resultats-572051/)
	* [2011](https://www.data.gouv.fr/fr/datasets/elections-cantonales-2011-resultats-572055/)

* [Liste des candidats au élections départementales de 2015](https://www.data.gouv.fr/fr/datasets/elections-departementales-2015-candidatures-1er-tour/) 
  * Structure : Canton * Binome * Candidat 
  * Variables : nom, prénom, sexe, date de naissance, profession et statut de sortant du candidat,  nom, prénom, sexe, date de naissance et statut de sortant du suppléant

### Les métadonnées de l'INA sur les journaux télévisés

Dans le cadre de DataElections, l'Institut national de l'audiovisuel met à la disposition des participants les métadonnées des journaux télévisés pendant les campagnes électorales des 10 dernières années. Chaque sujet de JT est décrit par son titre, la chaîne sur laquelle il passe, la durée, le titre du JT, la date du JT, un ensemble de tags et une description. 

Ces données ne sont pas diffusées en OpenData et ceux qui veulent les utiliser doivent s'engager à supprimer les données à la fin de l'événement et à ne pas réutiliser les résultats sans autorisation de l'INA. 

## Données annexes

### Découpages territoriaux

* [IGN-GeoFla](http://professionnels.ign.fr/geofla#tab-3) Découpage administratif national réalisé par l'IGN. 
 * Contient les Shapefiles des communes, des cantons et des départements de 2011 à 2014  
 * Voir la [note sur les cantons](https://github.com/SGMAP-AGD/Elections/blob/master/notes_sur_les_cantons.md)
* [Contour des communes actuelles d'après OpenStreetMap](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/)
* [Contour des départements actuels d'après OpenStreetMap](https://www.data.gouv.fr/fr/datasets/contours-des-departements-francais-issus-d-openstreetmap/)
* Contour des circonscriptions électorales après le redécoupage de 2010 : 
 * [Fichiers de Joel Gombin](http://www.joelgombin.fr/un-fonds-de-carte-vectoriel-pour-les-circonscriptions-legislatives/) en KML et Shapefile.
 * [Le Fichier de Joel Gombin converti en geoJSON](https://github.com/SGMAP-AGD/Elections/blob/master/circonscriptions2010.geoJSON)
* [Régions, départements et communes métropolitaines françaises au format GeoJSON](https://github.com/gregoiredavid/france-geojson)
* [Contour des cantons 2015](https://www.data.gouv.fr/fr/datasets/contours-des-cantons-electoraux-departementaux-2015/) mis en ligne par le ministère de l'Intérieur pour l'Open Data Camp Elections
* [Table de correspondance des communes et des cantons avec les circonscriptions législatives](https://www.data.gouv.fr/fr/datasets/table-de-correspondance-des-communes-et-des-cantons-avec-les-circonscriptions-legislat-551418)

### Données sociodémographiques des circonscriptions 

* Description sociodémographiques des circonscriptions électorales d'après l'Insee en 2012
 * [page web](http://www.insee.fr/fr/themes/detail.asp?reg_id=0&ref_id=circo_leg-2012)
 * [Fichier xls](http://www.insee.fr/fr/ppp/bases-de-donnees/donnees-detaillees/circo_leg/circo_leg-2012/tableau/circonscriptions.xls)
* Informations sur l'imposition sur le revenu par commune en 2010, 2011, 2012
 * [fichiers xls](https://www.data.gouv.fr/fr/datasets/l-impot-sur-le-revenu-par-collectivite-territoriale/)
 * [script d'aggrégation et conversion en csv](https://github.com/Leobouloc/save_online/blob/master/load_ircom.py)
* Données de criminologie par département en 2013
 * [données de la gendarmerie nationale](https://www.data.gouv.fr/fr/datasets/les-crimes-et-delits-enregistres-par-la-gendarmerie-nationale/)
 * [données de la police nationale](https://www.data.gouv.fr/fr/datasets/crimes-et-delits-constates-par-la-police-nationale-en-2013/)
 * [script d'aggrégation et conversion en csv](https://github.com/Leobouloc/save_online/blob/master/load_crimes.py)

### Données électorales

* [Résultats électoraux publiés par le ministère de l'Intérieur](http://www.interieur.gouv.fr/Elections/Les-resultats)
* [Ensemble des données électorales du ministère de l'Intéireur](https://www.data.gouv.fr/fr/datasets/resultats-de-lintegralite-des-elections-depuis-2001/), format XML

#### Elections européennes

* [Résultat des élections européennes de 2014](https://www.data.gouv.fr/fr/datasets/elections-europeennes-2014-resulta-2/) au niveau de la circonscription électorale européenne, de la région, du département, de la circonscription législative et du canton
* [Résultat des élections européennes de 2014 par commune](https://www.data.gouv.fr/fr/datasets/elections-europeennes-2014-resultats-par-communes/)

#### Elections municipales

* [Thématique consacrée aux élections municipales sur DataGouvFr](https://www.data.gouv.fr/fr/datasets/thematique-elections-municipales/)

#### Données par bureau de vote publiées par Regards Citoyens

 * [Résultats des élections présidentielles de 2002](https://www.data.gouv.fr/fr/datasets/resultats-des-presidentielles-2002-nd/] 
 * [Résultats des élections présidentielles de 2007](https://www.data.gouv.fr/fr/datasets/resultats-des-elections-presidentielles-2007-nd/)
 * [Résultats des élections présidentielles de 2012](https://www.data.gouv.fr/fr/datasets/resultat-des-elections-presidentielles-francaise-de-2012-au-niveau-bureau-de-vote-nd/)
 
#### Comptes de campagne

* [Données des comptes de campagne des élections législatives de 2012](https://www.data.gouv.fr/fr/datasets/tableau-general-des-elections-legislatives-des-10-et-17-juin-2012/)

## Outils 

### Cartographie

Voici quelques outils permettant de faire des cartes : 

* R + ggplot : 
 * [carto_departements.R](https://github.com/SGMAP-AGD/Elections/blob/master/R/carto_departements.R)  exemple de scripts R pour tracer le contour des départements à partir d'un Shapefile
 * [carto_departements_geoJSON.R](https://github.com/SGMAP-AGD/Elections/blob/master/R/carto_departements_geoJSON.R=) exemple de script pour réaliser une carte en R à partir d'un fichier geoJSON
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

