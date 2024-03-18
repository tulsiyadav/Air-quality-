#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[8]:


import os
import sys
os.__file__
sys.path.append("D:/internship/AQI")

df = pd.read_csv('Air_Quality.csv')
df.head()


# In[9]:


df.columns


# In[10]:


df1 = df.drop(['id','pollutant_id'], axis = 1 )
df1.head()


# In[11]:


df.shape


# In[12]:


len(df.last_update)


# In[13]:


df1.info()


# In[14]:


pollutant_min_mean = df1.pollutant_min.mean()
pollutant_max_mean = df1.pollutant_max.mean()
pollutant_avg_mean = df1.pollutant_avg.mean()


# In[15]:


df1.pollutant_min = df1.pollutant_min.fillna(pollutant_min_mean )
df1.pollutant_max = df1.pollutant_max.fillna(pollutant_max_mean) 
df1.pollutant_avg = df1.pollutant_avg.fillna(pollutant_avg_mean)


# In[16]:


print(f'Lenth of pollutant min : {len(df1.pollutant_min)}')
print(f'Length of pollutant max : {len(df1.pollutant_max)}')
print(f'Length of pollutant avg : {len(df1.pollutant_avg)}')


# In[17]:


df1['last_update'] = pd.to_datetime(df1['last_update'] )
df1.last_update.dtypes


# In[18]:


counter = 0 
for column in df : 
    if df[column].dtypes == 'object'  :
        counter += 1
        print(f'{column} : {df[column].unique()} : {len(df[column].unique())}')
print(f'There are {counter} No of object columns ')


# In[19]:


df1.last_update.dtypes


# In[20]:


df2 = df1 

df2.info()


# In[21]:


plt.figure(figsize = (6,12))
sns.barplot(x ='pollutant_min' , y = 'state' , data = df2 )
plt.title('Pollutant Min vs State Barplot')


# In[22]:


plt.figure(figsize = (6,12))
sns.barplot(x ='pollutant_max' , y = 'state' , data = df2 )
plt.title('Pollutant Max vs State Barplot')


# In[23]:


plt.figure(figsize = (6,12))
sns.barplot(x ='pollutant_avg' , y = 'state' , data = df2 )
plt.title('Pollutant Avg vs State Barplot')


# In[24]:


import plotly.express as px 
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='pollutant_max',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()


# In[25]:


import plotly.express as px 
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='pollutant_min',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()


# In[26]:


import plotly.express as px 
fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='pollutant_avg',
    color_continuous_scale='Reds'
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()


# In[ ]:




