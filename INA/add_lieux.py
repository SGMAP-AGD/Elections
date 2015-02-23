# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:20:55 2015

@author: Alexis Eidelman
"""

import pandas as pd

from read import tab


def look_city(serie, list_lieux):
    localite = pd.Series('', index = serie.index)
    for lieu in list_lieux:
        cond = serie.str.contains(';' + lieu + ';')
        localite[cond] += lieu + ';'
        cond_deb = serie.str.startswith(lieu + ';')
        localite[cond_deb] += lieu + ';'        
    return localite
    
# deuxieme liste
lieux = pd.read_csv('data/liste-lieux.csv',
                    encoding='utf8', sep=';',
                    quotechar = "\'")
lieux['label'] = lieux['label'].str.replace("\"",'')
list_region = lieux.loc[lieux['type'] == "\"region\"", 'label']
list_region = list_region.tolist()

list_dep = lieux.loc[lieux['type'] == "\"departement\"", 'label']
list_dep = list_dep.tolist()

tags = tab.tags
region = look_city(tags, list_region)
departement = look_city(tags, list_dep)

## régionale 2010, 
## présidentielle
## législative
tags = tab.tags.str.lower()
for el in ['é', 'è', 'ê', 'ë']:
    tags = tags.str.replace(el, 'e')
for el in ['ö', 'ô']:
    tags = tags.str.replace(el, 'o')
for el in ['î', 'ï']:
    tags = tags.str.replace(el, 'i')
tags = tags.str.replace(' ','')
       
# majuscule, sans tiret, avec les accents

f = open('data//commune.txt', 'r')
list_ville = f.read()
list_ville = list_ville.replace('-', '')
list_ville = list_ville.replace(' ', '')
list_ville = list_ville.split('\n')

city = look_city(tags, list_ville)

tab['ville'] = city
tab['region'] = region
tab['dep'] = departement



