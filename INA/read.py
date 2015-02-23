# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:20:55 2015

@author: Alexis Eidelman
"""

import os
import pandas as pd
import datetime

## lecture brute
# tab = pd.read_csv('data/hertzien_UTF8.csv', sep=';', parse_dates = [4])
#year = tab.horaireDebut.str[:4]
#month = tab.horaireDebut.str[5:7]
#hour = tab.horaireDebut.str[8:10]
## on parse la date (en jour)
parse = lambda x:datetime.datetime.strptime(x[:10], '%Y-%m-%d')
tab = pd.read_csv('data/hertzien_UTF8.csv', sep=';', parse_dates = [4], 
            date_parser=parse)


tab['date'] = pd.DatetimeIndex(tab.horaireDebut)