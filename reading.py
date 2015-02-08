# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 22:09:41 2015

prend les fichiers pour les transformer en un fichier unique
ne marce que pour cantonales pour l'instant

@author: alexis
"""

import os
import glob
import re
import csv
import pandas as pd

"PRESIDENTIELLES_1965-2012-csv"
"LEGISLATIVES_1958-2012-csv"
"REGIONALES_1986-2010-csv"
"CANTONALES_1988-2011-csv"
folder = "CANTONALES_1988-2011-csv"


if folder in ["REGIONALES_1986-2010-csv", "PRESIDENTIELLES_1965-2012-csv"]:
    index_date_name = 10
if folder in ["LEGISLATIVES_1958-2012-csv", "CANTONALES_1988-2011-csv"]:
    index_date_name = 9    

rename_cols = {
    u'Code du canton': u'Code canton',
    u'Code du département': u'Code département',
    u'Prénom': 'Prenom',
    }

out = pd.DataFrame()
for path in glob.glob('data/' + folder + '/*.csv'):
    path_text = path[:-3] + 'txt'
    texte = open(path_text).read()
#    # test de date: # TODO:
#    match = re.search('(.*?)/(.*?)/(.*?)', texte, re.S)
#    jour, mois, annee = match.group(1)[-2:], match.group(2)
#    print texte

    filename = os.path.split(path)[-1]
    date = filename[index_date_name:(index_date_name + 6)]
    annee = int(date[:4])
    tour = int(date[-1])
    print annee, tour

    tab = pd.read_csv(path, encoding='utf8')
    tab['annee'] = annee
    tab['tour'] = tour
    tab.rename(columns=rename_cols, inplace=True)
    out = out.append(tab)
    print tab.columns

filename_out = 'data/' + folder.split('_')[0] + '.csv'
# TODO: out['Votants'] = out['Votants'].str.replace(' ','')
out.to_csv(filename_out, index=False, sep=';')

list_sub_var = ['NoDepot', 'Nom', u'Prenom', 'Sexe']
cols_to_keep = [col for col in out.columns
                if not any(x in col for x in list_sub_var)]
out = out[cols_to_keep]

for col in out.columns:
    print col
    print out[col].isnull().sum()
