# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 12:51:49 2015

@author: Alexis
"""

import pandas as pd
import datetime

## lecture brute
# tab = pd.read_csv('data/hertzien_UTF8.csv', sep=';', parse_dates = [4])
#year = tab.horaireDebut.str[:4]
#month = tab.horaireDebut.str[5:7]
#hour = tab.horaireDebut.str[8:10]
## on parse la date (en jour)


elections = [ 
    [datetime.datetime(2014,3,23), 'municipales', 1],
    [datetime.datetime(2014,3,30), 'municipales', 2],
    [datetime.datetime(2014,5,5), 'européenne', ],
    [datetime.datetime(2012,4,22), 'présidentielle', 1],
    [datetime.datetime(2014,5,6), 'présidentielle', 2],
    [datetime.datetime(2012,6,10), 'législative', 1],
    [datetime.datetime(2012,6,17), 'législative', 2],
     
    [datetime.datetime(2011,3,20), 'canton', 1],
    [datetime.datetime(2011,3,27), 'canton', 2],
    [datetime.datetime(2010,5,5), 'régionales', 1],
    [datetime.datetime(2010,4,22), 'régionales', 2],
    [datetime.datetime(2009,6,7), 'européenne', ],
    [datetime.datetime(2008,3,9), 'municipales', 1],
    [datetime.datetime(2008,3,16), 'municipales', 2],
    [datetime.datetime(2008,3,9), 'canton', 1],
    [datetime.datetime(2008,3,16), 'canton', 2],
     ]

date_elections = pd.DataFrame(elections, columns=['date', 'elections', 'tour'])


         