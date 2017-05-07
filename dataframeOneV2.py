#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:17:20 2017

@author: missyallan

Learning about Pandas and DataFrames 
"""
import pandas as pd 

#This dictionary represents GDP/CPI data at 10 year intervals form 1990 to 2010

df = pd.DataFrame({"GDP": [5974.7, 10031.0, 14681.1],
                   "CPI": [127.5, 169.3, 217.488],
                   "Year": [1990, 2000, 2010],
                   "Country": ["US", "US", "US"]})
print(df)
print(type(df))

df.shape
print(df.shape)


















