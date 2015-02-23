# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 14:09:51 2015

@author: Alexis
"""

import pandas as pd


tab = pd.read_csv('data/legislatives2012_final.csv',
                  header = None, encoding='utf8')

tab.columns = ['lieu', 'media', 'date', 'moment', 'heure', 'temps']
tab['year'] = 2012

somme = tab.groupby(['lieu', 'moment', 'year'])['temps'].sum()
compte = tab.groupby(['lieu', 'moment', 'year'])['temps'].count()
tab = pd.DataFrame(somme)
tab['compte'] = compte

#tab.groupby(['lieu', 'moment', 'media'])['temps'].sum().tail(20)

# TODO: mettre l'année
tab.reset_index(inplace=True)
tab.to_csv('legislative2012.csv', index=False)