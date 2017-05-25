# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:21:59 2017

@author: o222069
"""

import numpy as np
import pandas as pd
import datetime
import matplotlib.pylab as plt
data=pd.read_csv('Melbourne_housing_extra_data.csv')
data.head()

def val_counts(var):
    print(data[var].value_counts())
    print(data[var].nunique())
    
val_counts('Suburb')
val_counts('Rooms')
val_counts('Type')
val_counts('Method') #can ignore
val_counts('SellerG')#can ignore
val_counts('year')
val_counts('month') # month 3-8 more sales
val_counts('Postcode')
#plot graph for price,distance and date
#building area,year bulit can be used for crosstabulation with other variables

data['date']=pd.to_datetime(data.Date)
data['year']=data.date.dt.year
data['month']=data.date.dt.month
data=data.set_index(['year','month'])
data.sort_index(ascending=True,inplace=True)
ts=data['Price']
ts.head(20)
plt.plot(ts)
pd.crosstab(data.Rooms,data.Type)
pd.crosstab(data.index,data.Rooms)
pd.crosstab(data.index,data.Method)
data.groupby('Postcode')['Price'].mean().astype(int64)

for i in data['Postcode'].unique():
    print(data.Postcode.isnull().values())
data.groupby('Postcode')['Price'].apply(lambda x:x.count())
data.groupby('Postcode')['Price'].isnull.sum()
    
    
df = pd.DataFrame({'Name': pd.Categorical(['John Doe', 'Jane Doe', 'Bob Smith']), 'Score1': np.arange(3), 'Score2': np.arange(3, 6, 1)})
for i in df.Name:
    print(df.loc[df.Name==i,'Score2'])