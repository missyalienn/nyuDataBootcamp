#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:59:14 2017

@author: missyallan
"""

import sys

print('\nWhat version of Python?\n' ,sys.version,  '\n', sep='')

if float(sys.version_info[0]) < 3.0:
    raise Exception('Program halted, old version of Python. \n', 
                    'Sorry you need to install Anaconda again.')
else:
      
      print('Congrats! You have Python 3!')
      