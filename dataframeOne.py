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

#access a df's dimensions number of rows and columns using df.shape 
df.shape
print(df.shape)

#%%

#access the column labels directly with df.columns 

df.columns

#row label referred to as index, access with df.index 

df.index

#%%
#convert to a list by using tolist() method 

df.index.tolist()


#Pandas allows every colum typically a variable to have a diff data type, access types with df.dtypes 

df.dtypes

# to rotate the DataFrame exchanging columns and rows  use the transpose method: df.transpose() or  df.T

df.T

#%%
  
data = {'countrycode': ['CHN', 'CHN', 'CHN', 'FRA', 'FRA', 'FRA'],
        'pop': [1124.8, 1246.8, 1318.2, 58.2, 60.8, 64.7],
        'rgdpe': [2.611, 4.951, 11.106, 1.294, 1.753, 2.032],
        'year': [1990, 2000, 2010, 1990, 2000, 2010]}

pwt = pd.DataFrame(data)                                                                                         


#What kind of object is data? 
#Dictionary 

#What are dimensions of pwt 
pwt.shape

#What dtypes are the variables?

pwt.dtypes 

#What does pwt.columns.tolist() do? 
pwt.columns.tolist()

#What about list(pwt)

list(pwt)

#What is list(pwt)[0]
list(pwt)[0]


#%%
#Operating on DataFrames 

#want to refer to only one of the variables write: 
df['GDP']
print(df["GDP"])

#get the type 
print(type(df['GDP']))
#pandas.Series 


#Series are useful bc we can perform basic math operations on them 

print(df["GDP"] + df["GDP"])
print(df["GDP"] - df["GDP"])
print(df["GDP"] / df["CPI"])
print(df["CPI"] * df["CPI"])

#Can also do operations on a series w ints/floats 
print(df["GDP"] / 10000)

#%%

#Construct new variables from old ones 


df['RGDP'] = df['GDP']/df['CPI']
df['GDP_div_1000'] = df['GDP'] / 1000


#first line computes new variable RGDP as ratio of GDP to CPI 

#second line computes GDP_div_1000 as GDP / 1000 

print('\n)', df)
    
#%%

#Rename variables- assign list of new names to df's column labels 

df.columns = ["cpi", "country", "gdp", "year", "rgdp", "gdp_div_1000"]


#change column names to lower case with list comprehension 

df.columns = [var.lower() for var in df.columns]

#name gdp to ngdp 

df = df.rename(columns={'gdp':'ngdp'})

#%%
#EXTRACT VARIABLES 

#can extract variables by name or number if by name, put names in a list

namelist = ['ngdp', 'rgdp']
numlist  = [2, 4]
df_v1 = df[namelist]
df_v2 = df[numlist]

#Drop method 
#if we want to drop the variable CPI 

df.drop(['cpi'], axis = 1)

#%% 
#Exercises 
#Create a variable diff equal to dff of ngdp/rgdp 
df['diff'] = df['ngdp']/df['rgdp']

#Extract variables ngdp and year 
newlist = ['ngdp', 'year']
df_v3 = df[newlist]


#Drop the variable diff

df.drop(['diff'], axis = 1)

#%%

#DataFrame Methods 

#df.to_csv   #saves to csv
#df.to_excel #saves to excel 

#The top and bottom of a dataframe 

#Use df.head(3) to get the first n observations of a large df

#Use df.tail() to get the last 5 and it creates a new df 

#%%
#Setting the Index 

#We can set the index to whatever we want 

df = df.set_index(['year'])

print(df)

#%%
#Reverse resetting the index with reset() method 

df_reset = df.reset_index()
print(df_reset)

#Statistics 

#df.mean(), mean 

#df.std(), standard deviation 
      
      
#df.describe() mean, std deviation, min and max
       
df.mean() 

#%%

#Exercise. Set year as the index and assign the result to the DataFrame dfi. 
#Use the index method to extract it and verify that year is, in fact, the index.

df = df.set_index(['year'])
df.index

dfi = df.reset_index()
print(dfi)

df.plot.bar()





































