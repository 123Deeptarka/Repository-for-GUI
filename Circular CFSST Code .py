#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_excel("/Users/deeptarkaroy/Desktop/Circular Dataset.xlsx")
x=df.drop(['N_Test'],axis=1)
y=df['N_Test']


# In[3]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


from xgboost import XGBRegressor
model=XGBRegressor(n_estimators=800,learning_rate=0.1)
model.fit(x_train,y_train)


# In[4]:


model.predict(x_test)


# In[5]:


import pickle 


# In[6]:


with open('efgh','wb') as file:
     pickle.dump(model,file)


# In[7]:


with open('efgh','rb') as file:
     mp=pickle.load(file)


# In[8]:


mp.predict(x_test)


# In[ ]:




