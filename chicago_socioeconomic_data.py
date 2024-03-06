#!/usr/bin/env python
# coding: utf-8

# In[1]:


#install req packages
pip install mysql-connector-python


# In[12]:


#import libraries
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 


# In[2]:


#connect with database 
import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database ="CHicago"
)
con


# In[4]:


#READ DATA 
import pandas as pd 
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/CHicago')

df = pd.read_csv(r'C:\Users\FreeComp\Desktop\CSVData\ChicagoCensusData.csv')
df.to_sql("chicago_socioeconomic_data", engine, if_exists='replace', index=False,method="multi")


# In[5]:


#Display the first five rows in dataset
df = pd.read_sql_query('SELECT * FROM chicago_socioeconomic_data limit 5',engine)
df


# In[17]:


df.info()


# In[18]:


df.describe()


# ## Problem 1
# How many rows are in the dataset?

# In[6]:


q1 = pd.read_sql_query('SELECT COUNT(*) FROM chicago_socioeconomic_data ', engine)
q1


# ## Problem 2
# How many community areas in Chicago have a hardship index greater than 50.0?

# In[7]:


q2 = pd.read_sql_query('SELECT COUNT(COMMUNITY_AREA_NUMBER) FROM chicago_socioeconomic_data \
                            WHERE HARDSHIP_INDEX > 50.0',engine)
q2


# ## Problem 3
# What is the maximum value of hardship index in this dataset?

# In[8]:


q3 =  pd.read_sql_query('SELECT MAX(HARDSHIP_INDEX) FROM chicago_socioeconomic_data' , engine)
q3       


# ## Problem 4
# Which community area which has the highest hardship index?

# In[9]:


q4 =  pd.read_sql_query('SELECT community_area_name FROM chicago_socioeconomic_data \
       WHERE hardship_index = (SELECT MAX(hardship_index) FROM chicago_socioeconomic_data)',engine)
q4


# ## Problem 5
# Which Chicago community areas have per-capita incomes greater than $60,000?

# In[10]:


q5 =  pd.read_sql_query('SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income >60000',engine)
q5


# ## Problem 6
# Create a scatter plot using the variables per_capita_income_ and hardship_index. Explain the correlation between the two variables.

# In[16]:


income_vs_hardship = pd.read_sql_query('SELECT PER_CAPITA_INCOME, HARDSHIP_INDEX FROM chicago_socioeconomic_data',engine)
income_vs_hardship
sns.jointplot(x='PER_CAPITA_INCOME',y='HARDSHIP_INDEX', data=pd.DataFrame(income_vs_hardship))
plt.show()


#     We see that the points on the scatter plot are somewhat closer to a straight line in the negative direction, so we have                                      a negative correlation between the two variables. 

# In[ ]:




