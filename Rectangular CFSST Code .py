#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_excel("/Users/deeptarkaroy/Desktop/Thesis/Recatngular dataset .xlsx")
x=df.drop(['a'],axis=1)
y=df['a']


# In[3]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


from xgboost import XGBRegressor
model=XGBRegressor(n_estimators=800,learning_rate=0.1)
model.fit(x_train,y_train)


# In[5]:


model.predict(x_test)


# In[4]:


import pickle 


# In[30]:


with open('Rectangular CFSST Columns','wb') as file:
     pickle.dump(model,file)


# In[31]:


with open('Rectangular CFSST Columns','rb') as file:
     mp=pickle.load(file)


# In[33]:


mp.predict(x_test)


# In[ ]:




