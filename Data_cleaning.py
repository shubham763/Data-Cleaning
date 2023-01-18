
# # Data Cleaning with Python and Pandas

# In this project, I discuss various useful techniques to clean a untidy dataset with Python, NumPy and Pandas.

# ## 1. Introduction to Python data cleaning

# ## 2. Tidy data format

# There are three principles of tidy data:
# 
# **•	Columns represent separate variables.**
# 
# **•	Rows represent individual observations.**
# 
# **•	Observational units form tables.**
# 
# 
# Tidy data makes it easier to fix common data problems. So, we need to transform the untidy dataset into tidy data. 
# 
# Before we look into the details of cleaning the dataset, we have to understand what constitutes an untidy data. We need to diagnose our data and find common signs of a messy dataset.
# 

# ## 3. Signs of an untidy dataset
# 
# 
# We have to take a closer look to find common signs of a messy dataset:
# 
# 
# •	**Missing numerical data**
# 
# Missing numerical data needs to be identified and addressed. Either delete or replace with a suitable test statistic.
# 
# 
# •	**Untidy data**
# 
# Untidy dataset can contain multiple problems. They prevent us from transforming the messy dataset into a clean dataset that is suitable for analysis.
# 
# 
# •	**Unexpected data values**
# 
# Mismatched data types of a column and data values can cause potential problems. They need to be investigated and solved.
# 
# 
# •	**Inconsistent column names**
# 
# Column names contain inconsistent capitalizations and bad characters. They need to be addressed properly.
# 
# 
# •	**Outliers** (can also be found using boxplot)
# 
# Outliers need to be detected. They pose potential problems needs to be investigated and removed.
# 
# 
# •	**Duplicate rows and columns** (causes data redundancy)
# 
# Duplicate rows and columns make data redundant. They can bias an analysis. Hence, they needs to be found and dropped.
# 
# 

# ## 4. Python data cleaning - prerequisites
# 
# 
# We need three Python libraries for the data cleansing process – NumPy, Pandas and Matplotlib.
# 
# 
# •	**NumPy** 
# 
# •	**Pandas** 
# 
# •	**Matplotlib**

# ## 5. Import the required Python libraries
# 
# 
# We have seen that we need three Python libraries – NumPy, Pandas and Matplotlib for the data cleaning process. We need to import these libraries, we can import them with their usual shorthand notation:-

# In[1]:

# import the Python libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ## 6. The source dataset
# 
# 
# For this project, I'ce created different type of dataset. It contains all the details (name,last name,etc) of my facebook friends.
# 
# The dataset can be imported as follows:-
# 

# In[2]:


data = "C:/cleaning_data/friends.txt"

df = pd.read_csv(data)

#############

df.shape


# **Interpretation**
# 
# We can see that our data have 10 rows and 10 columns.

# ### df.head() and df.tail() methods
# 
# 
# We can view the top five and bottom five rows of the dataset with **df.head()** and **df.tail()** methods respectively.
# 

# In[4]:


df.head()


# In[5]:


df.tail()



# In[6]:


df.info()


# In[7]:


df.dtypes


# In[8]:


df["height(cm)"] = pd.to_numeric(df["height(cm)"], errors='coerce')


# In[9]:


df["weight(kg)"] = pd.to_numeric(df["weight(kg)"], errors='coerce')


# In[10]:


df["spend_C"] = pd.to_numeric(df["spend_C"], errors='coerce')


# In[11]:


df.dtypes


# In[12]:


df.head()


# In[13]:


df.tail()


# In[14]:


df.describe()


# In[15]:


df.columns





# We can use various types of plots for data visualization purpose.
# 
# 
# •	**Bar plot**
# 
# •	**Histograms**
# 
# •	**Box plot**
# 
# •	**Scatter plot**
# 
# 
# 

# ### Bar plot

# In[16]:


df['age'].plot('bar')

plt.show()


# ### Histograms

# In[17]:


df['height(cm)'].plot('hist')

plt.show()


# In[18]:


df['weight(kg)'].plot('hist')

plt.show()



# ### Box plot

# In[19]:


df.boxplot(column='height(cm)')

plt.show()


# In[20]:


df.boxplot(column='weight(kg)')

plt.show()


# ### Scatter plot

# In[21]:


df.plot(kind='scatter',x='height(cm)', y='weight(kg)', c='DarkBlue')

plt.show()



# In[22]:


df[['age','sex']] = df.age_sex.str.split("_", expand = True)


# In[23]:


df.head()


# We can see that now we have two separate columns for age and sex.
# 
# Now, there is no need for the age_sex column. So, we should drop that column.
# 
# We can drop 'age_sex' column using the **df.drop()** method as follows:-

# In[24]:


df.drop(['age_sex'], axis=1, inplace=True)


# In[25]:


df


# In[26]:


df = df[['fname','lname','age','sex','section','height(cm)','weight(kg)','spend_A','spend_B','spend_C']]


# In[27]:


df



# In[28]:


pd.set_option('mode.chained_assignment', None)


# In[29]:


df['weight(kg)'].replace(-60, 60, inplace=True)


# In[30]:


df


# In[31]:


df['spend_B'].replace(-100,100, inplace=True)


# In[32]:


df



# In[33]:


mean = df['height(cm)'].mean()


# In[34]:


df['height(cm)'].replace(0.0, mean, inplace=True)


# In[35]:


df



# In[36]:


df['weight(kg)'].replace(160.0, 60.0, inplace=True)


# In[37]:


df


# In[38]:


df.isnull().sum()



# In[39]:


mean_height = df['height(cm)'].mean()

df['height(cm)'].fillna(mean_height, inplace=True)


# In[40]:


mean_weight = df['weight(kg)'].mean()

df['weight(kg)'].fillna(mean_weight, inplace=True)


# In[41]:


mean_spend_A = df['spend_A'].mean()

df['spend_A'].fillna(mean_spend_A, inplace=True)


# In[42]:


mean_spend_B = df['spend_B'].mean()

df['spend_B'].fillna(mean_spend_B, inplace=True)


# In[43]:


mean_spend_C = df['spend_C'].mean()

df['spend_C'].fillna(mean_spend_C, inplace=True)



# In[44]:


df.isnull().sum()



# In[45]:


assert pd.notnull(df).all().all()


# In[46]:


assert (df >=0).all().all()


# In[47]:


df



# In[48]:


pd.melt(frame=df, id_vars=['fname','lname','age','sex','section','height(cm)','weight(kg)'],
                    value_vars=['spend_A','spend_B','spend_C'], var_name='expenditure', value_name='amount')


# we can see that there are no missing or negative values. There are no outliers in our data. Our data is in tidy format.

