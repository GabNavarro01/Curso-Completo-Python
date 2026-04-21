# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 07:21:28 2022

@author: Luciano
"""

import pandas as pd


df= pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col = ['Time'], parse_dates = True)

df.head()

# df['12-25-2014':].plot()
# df['10-15-2014':'12-15-2014'].plot()

dh = df['12-25-2014':].copy()
delta_t= -1
delta_h = 19.5
pd.DataFrame([dh['H_SF'].shift(delta_t)-delta_h, dh['H_BA']]).T.plot()

