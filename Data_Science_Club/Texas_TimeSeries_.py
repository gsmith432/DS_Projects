#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:09:07 2017

@author: gabrielsmith
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

ds = pd.read_csv('Texas_metro_businesscycle_indexes.txt')

## Functions using lambda

test = lambda x: x**2

print('\n')
print(test(5))