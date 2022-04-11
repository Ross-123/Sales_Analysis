import pandas as pd
import os


# In[3]:


#df = pd.read_csv(r"C:\Users\HP\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\Sales_April_2019.csv")

##Concatenate all csv files data in to one file
files = [file for file in os.listdir(r"C:\Users\HP\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data")]
all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv(r"C:\Users\HP\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\\"+file)
    all_months_data = pd.concat([all_months_data, df])
                     
all_months_data.to_csv("all_data.csv", index=False)


# In[5]:


all_data = pd.read_csv("all_data.csv") ##Create a Data Frame by reading the csv file.
##all_data.head()  (View Data head)


# In[6]:


##Augment data with additional columns
    ##Add Month column  (View Data head)
    
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data.dropna(how ="all", inplace = True)


    
    


# In[7]:


all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
##all_data.head()  (View Data head)


# In[8]:


all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
## all_data.head()  (View Data head)


# In[9]:


##String to float and Integer
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('float')
all_data['Month'] = all_data['Month'].astype('Int32')
## all_data.head()  (View Data head)


# In[10]:


##Get the sales column
all_data['Sales'] = all_data['Quantity Ordered']* all_data['Price Each']
##all_data.head()


# In[11]:


##Get the Total sales for the each month
##all_data.groupby(['Month']).sum()


# In[16]:


##Monthly Sales in to a bar graph using Matplotlib 
import numpy as np
import matplotlib.pyplot as plt

months = range(1,13)
results = all_data.groupby('Month').sum()

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()


# In[ ]:


##Which city has the highest Sales


# In[17]:


all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1])
##all_data.head()


# In[18]:


##Total Sales on City
##all_data.groupby(['City']).sum()


# In[63]:


results = all_data.groupby(['City']).sum()

results.sort_values(by=['Sales','City',], ascending = False)

results


# In[21]:


import numpy as np
import matplotlib.pyplot as plt

Cities = [city for city, df in all_data.groupby('City')]



plt.bar('Cities', results['Sales'],0.2)
plt.xticks(Cities)
plt.xlabel("Months")
plt.ylabel("Sales")
##plt.show()


# In[69]:


## Get the Time
all_data['Time'] = all_data['Order Date'].apply(lambda x: x.split(' ')[1])
all_data.head()


# In[72]:


all_data['Time'] = pd.to_datetime(all_data['Time'])
all_data['Time'] = all_data['Time'].dt.hour
all_data.head()


# In[76]:


Times = [Time for Time, df in all_data.groupby('Time')]
plt.plot(Times, all_data.groupby(['Time']).count())
all_data.groupby(['Time']).count()
plt.xticks(Times)
plt.grid()
plt.show()



# In[80]:


##Which Items sold together - Group by Order No
df = all_data[all_data['Order ID'].duplicated(keep=False)]
df.head(20)

