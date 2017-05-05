#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:44:31 2017

@author: missyallan
Missy is practicing Python with NYU DataCamp GitBook
"""


a = "some" 
b= "thing" 
c = a + b 
print('c =', c)

#%%
x = 2 
y =3 
z = x/y 
print('z =', z)


4+5 # add 4 and 5
print(4+5)

#%%
f = "I don't believe it"
print(f)


longstring = """

Four score and seven years ago

Our fathers brought forth. """

print(longstring)

#%%
bad_string = "Sarah's code"
print(bad_string)

#%%

s = '12'
i = int(s) 
type(i)

#%%

x = 'abc'
y = list(x)
print(y)



#%%
# convert integer i to list 
i = 1234
istring = str(i)
print(istring)



#%%
#year is a string representing a year. how to construct a string for the FOLLOWING year 
year = '2015'
intyear = int(year)
nextyear = intyear + 1 
print(nextyear)

#%%
numberlist = [1, 5, -3]
numberlist.append(7)
print(numberlist)

#%%
#convert a string with a comma to a float 

z = '12,234.5'
replaced = z.replace(',',' ')
print(replaced)

nospace = replaced.replace(' ', '')
print(nospace)

b = 0.0 

finalfloat = float(nospace) + b
print(finalfloat)
print(type(finalfloat))

#%%  





























