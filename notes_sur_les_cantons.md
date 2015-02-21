 * Attention ! Il faut distinguer deux types de cantons : d'une part, le canton "réel", c'est-à-dire la circonscription électorale ; d'autre part, les cantons-et-villes ou pseudo-cantons, unités fictives constituées soit des communes entières comprises dans un canton "réel", soit d'une commune divisée en plusieurs cantons réels et formant un seul pseudo-canton. Les données diffusées par l'IGN ou l'INSEE sous le nom de canton concernent en réalité les pseudo-cantons, et il n'existe pas de découpage des cantons exhaustif (soit avant, soit après 2015) en libre. OpenStreetMap a numérisé [une partie des découpages cantonaux](http://wiki.openstreetmap.org/wiki/FR:Cantons_in_France), avant et après 2015. On peut accéder aux cantons 2015 via l'API Overpass. Par exemple, on peut entrer la requête suivante dans http://overpass-turbo.eu/ :

````
// gather results
(
// query part for: “political_division=canton”
relation["political_division"="canton"]({{bbox}});
);
// print results
out body;
>;
out skel qt;
````

