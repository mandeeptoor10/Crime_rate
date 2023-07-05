#!/usr/bin/env python
# coding: utf-8

# # crime reported in Toronto

# In[11]:


import numpy as np
import random 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go


# In[12]:


crime_in_toronto = pd.read_csv('C://Users//mande//OneDrive//Desktop/crime.csv')


# In[13]:


df= pd.DataFrame(crime_in_toronto)
df


# # crime in different locations 

# In 2021, 34,277 recorded cases in Toronto, illustrating the city's.In 2021, there will be 34,277 recorded cases in Toronto

# In[14]:


type1 = df['premises_type'].unique()
type1


# In[15]:


Commercial= df[df['premises_type']== 'Commercial'].count()
House_crime= df[df['premises_type']== 'House'].count()
Outside_crime=df[df['premises_type']== 'Outside'].count()
Transit_crime=df[df['premises_type']== 'Transit'].count()
other_crime=df[df['premises_type']== 'Other'].count()
Educational_crime=df[df['premises_type']== 'Educational'].count()


# In[16]:


# Count premises type
commercial_crime = df[df['premises_type'] == 'Commercial'].count()['event_unique_id']
house_crime = df[df['premises_type'] == 'House'].count()['event_unique_id']
outside_crime = df[df['premises_type'] == 'Outside'].count()['event_unique_id']
transit_crime = df[df['premises_type'] == 'Transit'].count()['event_unique_id']
other_crime = df[df['premises_type'] == 'Other'].count()['event_unique_id']
educational_crime = df[df['premises_type'] == 'Educational'].count()['event_unique_id']

# Create a dataframe
data = {'Premises Type': ['Commercial', 'House', 'Outside', 'Transit', 'Other', 'Educational'],
        'Count': [commercial_crime, house_crime, outside_crime, transit_crime, other_crime, educational_crime]}

# pie chart 
fig = px.pie(data, values='Count', names='Premises Type', title='Crime Distribution by Premises Type')

# Show pie chart
fig.show()
# Create a dataframe for the bar chart
data_bar = {'Premises Type': ['Commercial', 'House', 'Outside', 'Transit', 'Other', 'Educational'],
            'Count': [commercial_crime, house_crime, outside_crime, transit_crime, other_crime, educational_crime]}

# Create the bar chart using Plotly Express
fig_bar = px.bar(data_bar, x='Premises Type', y='Count', title='Crime Distribution by Premises Type')

# Show the bar chart
fig_bar.show()


# According to the data, outdoor places have the largest number of crimes (9402 incidents), 
# need for greater safety measures in publicspaces. Each year, around 6000 crimes occur in commercial 
# and residential sectors, underscoring the significance of security in both commercial and domestic places.
# There are 1156 crimes reported in transit places, compared to around 2000 crimes reported in other undefined areas.
# These findings point to the necessity for specific tactics to combat crime in various situations and assure community 
# safety generally.

# # offence	

# In[17]:


type_offence = df['offence'].unique()


# In[18]:


# Count the occurrences of each offence type
offence_counts = df['offence'].value_counts().reset_index()

# Rename the columns
offence_counts.columns = ['Offence Type', 'Count']

# Sort the offences based on count in descending order
offence_counts = offence_counts.sort_values('Count', ascending=False)

# Calculate the total number of offences
total_offences = len(df)

# Calculate the percentage of each offence type
offence_percentages = (offence_counts['Count'] / total_offences) * 100

# Create a summary list
summary_list = []
for index, row in offence_counts.iterrows():
    offence_type = row['Offence Type']
    count = row['Count']
    percentage = offence_percentages[index]
    summary = f"{offence_type}: {count} cases ({percentage:.2f}%)"
    summary_list.append(summary)
# Print the summary list
for summary in summary_list:
    print(summary)


# Based on the statistics supplied, the distribution of crime in Toronto reveals interesting tendencies. Assault is the most common infraction, accounting for 37.16% of all instances, closely followed by Theft of Motor Vehicle (19.08%). Break and Enter comes third, accounting for 14.14% of all instances. Robbery of various categories, such as Robbery - Mugging, Robbery - Business, and Robbery - Other, account for around 1% of the total. While other acts have lower numbers, they nonetheless reflect the city's range of criminal activity. It is crucial to highlight that this research is only a snapshot and may not represent the entire criminal environment. For a complete understanding of crime patterns in Toronto, additional information such as temporal and geographical elements are required.

# # occurrencemonth

# In[19]:


# Group the data by month and count 
monthly_counts = df.groupby('occurrencemonth').size().reset_index(name='Count')
monthly_counts


# # mamximum crime can be seen in oct,followed by sept, where as least can we seen april and feb 

# In[27]:


# order of the months
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# In[29]:


# Assuming you have the monthly_counts dataframe
monthly_counts = pd.DataFrame({
    'occurrencemonth': ['April', 'August', 'December', 'February', 'January', 'July', 'June', 'March', 'May',
                        'November', 'October', 'September'],
    'Count': [2378, 3235, 2930, 2226, 2574, 3024, 2931, 2548, 2978, 3019, 3297, 3137]
})

# Sort the months based on the specified order
monthly_counts = monthly_counts.sort_values(by='occurrencemonth', key=lambda x: pd.Categorical(x, categories=month_order))

# Create a line graph
fig = px.line(monthly_counts, x='occurrencemonth', y='Count', title='Occurrences by Month')

# Customize the appearance
fig.update_layout(xaxis_title='Month', yaxis_title='Count')

# Display the line graph
fig.show()


# # occurrencedayofweek	

# In[30]:


occurrencemonth_in_weekdays = df['occurrencedayofweek'].unique()
occurrencemonth_in_weekdays 


# In[24]:


# Group the data by month and count the occurrences
weekly_counts = df.groupby('occurrencedayofweek').size().reset_index(name='Count')
weekly_counts

The most crime is recorded on Fridays, although there is no significant variation between weekdays and weekends; crime is reported every day.
# # Neighbourhood

# In[37]:


Neighbourhood = df['Neighbourhood'].unique()


# In[38]:


crime_n =df.groupby('Neighbourhood').size().reset_index(name='Count')
crime_n


# In[51]:


Neighbourhood1 = df['Neighbourhood']


# In[48]:



# Count the occurrences of each neighbourhood
neighbourhood_counts = df['Neighbourhood'].value_counts().reset_index()
neighbourhood_counts.columns = ['Neighbourhood', 'Count']

# Sort the neighbourhoods by count in descending order
neighbourhood_counts = neighbourhood_counts.sort_values(by='Count', ascending=False)

# Create a bar chart
fig = px.bar(neighbourhood_counts, x='Count', y='Neighbourhood', orientation='h', title='Crime Occurrences by Neighbourhood')

# Customize the appearance
fig.update_layout(xaxis_title='Number of Crimes', yaxis_title='Neighbourhood', yaxis_categoryorder='total ascending',
                  xaxis_tickformat=',d', bargap=0.2)

# Add data labels to the bars
fig.update_traces(textposition='outside', texttemplate='%{x:,}')

# Adjust the figure size for better readability
fig.update_layout(height=800)

# Display the bar chart
fig.show()


# Waterfront Island is the neighbourhood with the greatest crime rate in the dataset, owing to its urban setting and appeal. Beystreet in downtown and Westhill have greater crime rates, which might be attributed to their central positions and higher population concentrations. Woodsteel, Maple Leaf, and Woodbine Lumsden, on the other hand, have lower crime rates, which may be due to their residential character, lower population density, or excellent community policing. This data may help law enforcement and local communities allocate resources, avoid targeted crime, and build safer neighbourhoods via evidence-based solutions and community participation.

# # conclusion 

# In 2021, there were 34,277 reported crimes in Toronto, with outdoor locations having the highest crime rates,
# highlighting the need for greater public safety measures. Significant occurrences occurred in the commercial and
# residential sectors, underscoring the significance of security in these locations. Assault, theft of a motor vehicle,
# and break and enter were the most prevalent offences. Waterfront Island, Beystreet, and Westhill are high-crime areas
# that need targeted enforcement, whereas Woodsteel, Maple Leaf, and Woodbine Lumsden demonstrate excellent community policing.
# This information is valuable for resource allocation and evidence-based community safety programs.
