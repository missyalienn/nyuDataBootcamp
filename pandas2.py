#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:26:20 2017

@author: missyallan
"""

import pandas as pd
url1 = 'https://raw.githubusercontent.com/NYUDataBootcamp'
url2 = '/Materials/master/Data/test.csv'
url  = url1 + url2        # location of file
df = pd.read_csv(url)     # read file and assign it to df

#tells the read_csv to read only first 2 rows of file at url                
dfalt = pd.read_csv(url, nrows=2)

print('\n', df)
print('\n', dfalt)

#tells the read_csv that number 1 is missing 
onemissing = pd.read_csv(url, na_values=[1])
print('\n', onemissing)


#%%
url3 = 'https://raw.githubusercontent.com/NYUDataBootcamp'
url4 = '/Materials/master/Data/test0.csv'    # note the added 0
newurl  = url1 + url2
newdf = pd.read_csv(newurl, index_col=0)
print('\n', newdf)


#Exercise treat the numbers 1 and 6 as missing

somemissing = pd.read_csv(url, na_values= [1,6])
print('\n', somemissing)



