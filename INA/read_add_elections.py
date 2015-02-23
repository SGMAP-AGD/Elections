# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:20:55 2015

@author: Alexis Eidelman
"""

import pandas as pd
from read import tab

tags = tab.tags.str.lower()

list_election = [u'législ', u'munici', u'présid', u'canton', u'région']
 
for name in list_election:
    tab[name] = False
    for col in ['titreProgramme', 'tags', 'titreSujet']:
#        print name, col
#        print tab[col].str.contains(u'élect').sum()
        cond = tab[col].str.contains(name)
        tab.loc[cond == True, name] = True
#        print (tab[col].str.contains(u'élect') & tab[col].str.contains(name)).sum()

tab[list_election].sum(axis=1).value_counts()

tab.to_csv('hertzien_with_election.csv', sep=';', encoding='utf8')


