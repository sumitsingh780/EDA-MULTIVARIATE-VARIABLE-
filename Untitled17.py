#!/usr/bin/env python
# coding: utf-8

# # EDA (multivariate analysis)

# In[2]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 


# In[3]:


df = pd.read_csv('penguins.csv')


# In[4]:


df1 =pd.read_csv("train.csv")


# # scatterplot

# # numerical - numerical

# In[15]:


df1


# In[18]:


sns.scatterplot(data=df1, x='Age', y='Fare',hue ='Sex')


# # bar plot 

# In[19]:


sns.barplot(data=df1, x='Pclass', y='Age',hue ='Sex')


# In[20]:


sns.barplot(data=df1, x='Pclass', y='Fare',hue ='Sex')


# # boxplot 

# In[21]:


sns.boxplot(data=df1, x='Sex', y='Age',hue ='Sex')


# # distplot

# In[26]:


sns.histplot(data=df1, x='Age', hue='Sex', multiple='stack')


# In[29]:


# import seaborn as sns
import matplotlib.pyplot as plt

# Filter the data by sex
male_data = df1[df1['Sex'] == 'male']
female_data = df1[df1['Sex'] == 'female']

# Create separate distribution plots for each category of 'Sex'
sns.distplot(male_data['Age'], hist=False, kde=True, label='Male')
sns.distplot(female_data['Age'], hist=False, kde=True, label='Female')

# Set labels and title
plt.xlabel('Age')
plt.ylabel('Density')
plt.title('Distribution of Age by Sex')

# Show legend
plt.legend()

# Show the plot
plt.show()


# # heatmap

# In[30]:


sns.heatmap(pd.crosstab(df1['Pclass'],df1['Survived']))


# # clustermap

# In[31]:


sns.clustermap(pd.crosstab(df1['Pclass'],df1['Survived']))


# In[ ]:





# 

# In[ ]:




