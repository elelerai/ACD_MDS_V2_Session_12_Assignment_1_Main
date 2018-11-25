# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 05:27:34 2018

@author: Eliud Lelerai
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


df.info()

pd.isna(df)

# Cleaning Airline Column
df['Airline']=df['Airline'].str.replace(r'[^\w\s]+', '')
df['Airline']=df['Airline'].str.replace('\d+', '')
df['Airline']=df['Airline'].str.strip()


# QUESTION 1 Some values in the the FlightNumber column are missing. These numbers are meant 
              # to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in
                # these missing numbers and make the column an integer column (instead of a float column).

 
df.FlightNumber=df['FlightNumber'].interpolate(limit=1)

# QUESTION 2 The From_To column would be better as two separate columns! Split each string on
              # the underscore delimiter _ to give a new temporary DataFrame with the correct values.
                #  Assign the correct column names to this temporary DataFrame.
 
from_to= df['From_To'].str.split('_',expand=True)          
from_to=from_to.rename(columns={0:'Origin',1:'Destination'})

# QUESTION 3 Notice how the capitalisation of the city names is all mixed up in this temporary
             # DataFrame. Standardise the strings so that only the first letter is uppercase (e.g."londON" should become "London".)

from_to.Origin=from_to['Origin'].str.title()
from_to.Destination=from_to['Destination'].str.title()

# QUESTION 4 Delete the From_To column from df and attach the temporary DataFrame from the previous questions.

df=df.drop('From_To',axis=1)
df=pd.concat([df,from_to],axis=1)

# QUESTION 5 In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own
              # column, and so on. If there isn't an Nth value, the value should be NaN. Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,
                # delay_2, etc. and replace the unwanted RecentDelays column in df with delays.

RecentDelays=df['RecentDelays'].apply(pd.Series)

RecentDelays = RecentDelays.rename(columns = lambda x : 'delay_' + str(x))

df=df.drop('RecentDelays',axis=1)  

df=pd.concat([df[:], RecentDelays[:]], axis=1)
            
     






