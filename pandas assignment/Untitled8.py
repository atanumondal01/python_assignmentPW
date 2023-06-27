#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1


# In[3]:


import pandas


# In[5]:


ser=pd.Series([4, 8, 15, 16, 23,42])
print(ser)


# In[ ]:





# In[ ]:


#Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
#variable print it.


# In[6]:


l1=[i for i in range(1,11)]


# In[7]:


print(l1)


# In[9]:


ser1=pd.Series(l1)
print(ser1)


# In[ ]:





# In[ ]:


Name
Alice
Bob
Claire

Age
25
30
27

Gender
Female
Male
Female


# In[18]:


data={"Name": ['Alice', 'Bob' ,'Claire'],
     "Age":[25,27,32],
     "Gender":["Female","Male","Female"]}


# In[19]:


pd.DataFrame(data)


# In[ ]:





# In[ ]:


#Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.


# In[ ]:


#In pandas, a DataFrame is a two-dimensional data structure that consists of rows and columns, similar to a table in a
#spreadsheet or a SQL database. It is one of the primary data structures provided by the pandas library for data manipulation and analysis.

#Each column in a DataFrame is represented by a pandas Series, which is a one-dimensional labeled array. A Series can 
#be thought of as a single column of data with an associated index. In other words, a DataFrame is a collection of
#Series objects arranged in a tabular format.

#Here's an example to illustrate the difference between a DataFrame and a Series


# In[20]:


import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Jane', 'Alice'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)


# In[21]:


df


# In[ ]:





# In[ ]:


#Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
#you give an example of when you might use one of these functions?


# In[ ]:


Pandas is a powerful library in Python for data manipulation and analysis. It provides various functions to 
manipulate data in a Pandas DataFrame. Here are some common functions:

head() and tail(): These functions allow you to view the first few rows (head()) or the last few rows (tail()) of a
    DataFrame. They are useful for quickly inspecting the data and checking its structure.


# In[ ]:


import pandas as pd

df = pd.read_csv('data.csv')  # Assuming 'data.csv' is the file containing the data
print(df.head())


# In[10]:


import pandas as pd

df = pd.read_csv('data.csv')
df.info()


# In[ ]:


import pandas as pd

df = pd.read_csv('data.csv')
print(df.describe())


# In[ ]:


import pandas as pd

df = pd.read_csv('data.csv')
print(df.shape)


# In[ ]:


import pandas as pd

df = pd.read_csv('data.csv')
# Select rows where the 'age' column is greater than 30
subset = df.loc[df['age'] > 30]
print(subset)


# In[ ]:





# In[ ]:


# Q5. Which of the following is mutable in nature Series, DataFrame, Panel?


# In[ ]:


In Pandas, both Series and DataFrame are mutable .


# In[23]:


import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
s[2] = 10  # Modify the value at index 2
print(s)


# In[ ]:





# In[22]:


import pandas as pd

data = {'Name': ['John', 'Jane', 'Mike'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)
df['City'] = 'Tokyo'  
print(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




