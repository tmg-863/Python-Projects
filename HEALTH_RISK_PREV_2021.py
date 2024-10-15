#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This analysis uses the CDC dataset PLACES: Census Tract Data (GIS Friendly Format), 2021 release 
#PLACES is the expansion of the original 500 Cities project and covers the entire United States—50 states, with 
#information about prevalence of health and risk behaviors.
#and the District of Columbia (DC)—at county, place, census tract, and ZIP Code Tabulation Area (ZCTA)
#More information about the dataset can be learned at the below link:
#https://chronicdata.cdc.gov/500-Cities-Places/PLACES-Census-Tract-Data-GIS-Friendly-Format-2021-/yjkw-uj5s 


# In[57]:


# -*- coding: utf-8 -*-

import import_ipynb
import libpysal
import numpy as np
#from esda.moran import Moran
from libpysal.weights import Queen, KNN
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#load data and make the 'TractFIPS' column the index or ID column
df1 = pd.read_csv('C:/Users/TMG863/Downloads/CRUDE_PREV_2021.csv', index_col=4)

#Dropping extraneous columns; all we really need for this is the TractFIPS and prevalence variables; total population
#is already considered in the prevalence calculation.
df= df1.drop(columns=['TotalPopulation','StateAbbr','StateDesc','CountyName','CountyFIPS','Geolocation']) 
df.head()
#The data below is saying that the prevalence of ACCESS2_CrudePrev is 11.9 per the TotalPopulation of 5789 people. 
#This measurement has already divided the total number of cases by the total number of persons in the population, 
#giving the rate/crude prevalence.


# In[60]:


#The dataset is organized by "TractFIPS" aka the FIPS code for each Census Tract. 
#Each record is information about an individual census tract.

#A summary of the dataset is below, giving data types and column names.


# In[61]:


df.info()
#This dataset has 30 columns and 72,337 rows, with each row being 1 census tract 
#and each column being the health variables info for each census tract. Joy!
#First thing is to find out which communities/census tracts are most similar to each other; 
#for this I will do a 5-cluster and a 10-cluster analysis to see if changing the number of clusters reveals
#anything interesting


# In[62]:


df.describe()


# In[63]:


sns.jointplot(x='SLEEP_CrudePrev',y='DEPRESSION_CrudePrev',data=df,kind='hex')


# In[41]:


#With the hexagonal graph, we can clearly visualize the relationship between <7 hours of sleep and depression;
#the distribution is skewed toward the left; depression, at a rather steep incline.
#But we need to establish clusters of places based on their prevalence of disease, and find which communities
#have similar prevalences of social health risks/behaviors/diseases.

#Later, we will bring in another dataset at the census tract level, to explore the sociodemographic factors 
#contributing to the clusters.AKA why places have the problems they have. 
#From there, we may be able to predict WHERE each kind of prevalence is most/least likely to occur.

#These variables capture different aspects of the socioeconomic reality of each community and, 
#as a nation, provide a comprehensive view into our problems and where they occur. 
#We will be exploring "why" things occur where they do and how much each factor is contributing to each variable.


# In[64]:


pp=df
sns.pairplot(pp)
#Pairplot showing relationships between variables; each dot is a census tract


# In[65]:


sns.pairplot(df, kind="kde")


# In[ ]:




