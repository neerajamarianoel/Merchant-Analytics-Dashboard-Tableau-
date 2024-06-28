#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#read data from csv file
df=pd.read_csv("D:\Data Analyst\Tableau\Merchant_Analytics_Data.csv")
df.head()


# In[4]:


#df['Transaction Amount']=df['Transaction Amount'].str.replace('$','',regex=True)
df['Transaction Amount']=df['Transaction Amount'].str.replace(',','',regex=True)
df.head()


# In[5]:


#df['Transaction Amount'] = df['Transaction Amount'].astype(float)
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')


# In[6]:


df.dtypes['Date']


# In[7]:


#df=df.dropna()
m=df.isnull()
print(m)


# In[8]:


print(df.dropna(inplace=True,axis=1))


# In[9]:


df.to_csv(r'D:\Data Analyst\Tableau\cleaned.csv', index=False)


# In[ ]:




