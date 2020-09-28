#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt
import seaborn as sns

# this statement allows the visuals to render within your Jupyter Notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Locations of tech companies:
df_tech_companies = pd.read_csv('company_zip_updated.csv')
df_tech_companies.rename(columns = {'Latitude':'LAT', 'Longitude':'LON'}, inplace=True)

# CSV of stations, total ridership, location data, and other data of interest:
df_alldata = pd.read_csv('total_traffic_lat_long.csv')
df_alldata.rename(columns = {'Latitude':'LAT', 'Longitude':'LON','Entries_Exits':'TOT_IN_OUT'}, inplace=True)

# Recommended Stations:
df_recommeded = pd.DataFrame()
df_recommeded = df_alldata.loc[(df_alldata['STATION']=='23 ST') | 
                           (df_alldata['STATION']=='34 ST-HERALD SQ') | 
                           (df_alldata['STATION']=='34 ST-PENN STA')| 
                           (df_alldata['STATION']=='42 ST-PORT AUTH') | 
                           (df_alldata['STATION']=='14 ST-UNION SQ') | 
                           (df_alldata['STATION']=='14 ST') | 
                           (df_alldata['STATION']=='GRD CNTRL-42 ST') | 
                           (df_alldata['STATION']=='86 ST')]


# In[3]:


# [PPT SLIDE 5]: 2D map view (spatial distribution) of all station locations
fig = px.scatter_mapbox(df_alldata, lat='LAT', lon='LON', zoom=11)
fig.update_traces(marker=dict(size=10))
fig.update_layout(mapbox_style="stamen-toner")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[4]:


# Subset of all stations with more than 500,000 total traffic over the dataset's time range:
df_stations_gt500k = df_alldata.take(df_alldata.loc[df_alldata['TOT_IN_OUT'] >= 500000].index)


# [PPT SLIDE 6]: Map of these stations:
fig = px.scatter_mapbox(df_stations_gt500k, lat="LAT", lon="LON", zoom=11,center=dict(lat=40.77949,lon=-73.95553),
                        color='TOT_IN_OUT', color_continuous_scale=px.colors.sequential.Rainbow)

fig.update_traces(marker=dict(size=14))
fig.update_layout(mapbox_style="stamen-toner")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[5]:


# [PPT SLIDE 7]: Map of stations with high traffic, juxtaposed with nearby tech companies:
fig = px.scatter_mapbox(df_tech_companies, lat="LAT", lon="LON", zoom=11,center=dict(lat=40.77949,lon=-73.95553))
fig.add_trace(px.scatter_mapbox(df_stations_gt500k, lat='LAT', lon='LON', color='TOT_IN_OUT').data[0])

fig.update_traces(marker=dict(size=12))
fig.update_layout(mapbox_style="stamen-toner")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[6]:


# [PPT SLIDE 8]: Visualize recommended stations superimposed on map of tech company locations (in dark green)
fig = px.scatter_mapbox(df_tech_companies, lat='LAT', lon='LON', zoom=11,center=dict(lat=40.77949,lon=-73.95553))
fig.update_traces(marker=dict(color='green'))

# Plot each station of interest onto the map (not sure how to generalize this in plotly express):
fig.add_trace(px.scatter_mapbox(df_recommeded, lat='LAT', lon='LON',color='STATION').data[0])
fig.add_trace(px.scatter_mapbox(df_recommeded, lat='LAT', lon='LON',color='STATION').data[1])
fig.add_trace(px.scatter_mapbox(df_recommeded, lat='LAT', lon='LON',color='STATION').data[2])
fig.add_trace(px.scatter_mapbox(df_recommeded, lat='LAT', lon='LON',color='STATION').data[3])
fig.add_trace(px.scatter_mapbox(df_recommeded, lat='LAT', lon='LON',color='STATION').data[4])
fig.add_trace(px.scatter_mapbox(df_recommeded, lat='LAT', lon='LON',color='STATION').data[5])
fig.add_trace(px.scatter_mapbox(df_recommeded, lat='LAT', lon='LON',color='STATION').data[6])
fig.add_trace(px.scatter_mapbox(df_recommeded, lat='LAT', lon='LON',color='STATION').data[7])

fig.update_traces(marker=dict(size=14))
fig.update_layout(mapbox_style="stamen-toner")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[7]:


# [Not in PPT]: Viewing map of stations, colored by Zip Codes, sized by Population:
fig = px.scatter_mapbox(df_alldata, lat="LAT", lon="LON", color="ZIPCODE", size="POPULATION", zoom=11,center=dict(lat=40.77949,lon=-73.95553),
                  color_continuous_scale=px.colors.sequential.Rainbow, size_max=14)
fig.update_layout(mapbox_style="stamen-toner")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[8]:


# [Not in PPT]: exploring a pairplot of our data for correlations:
df_temp = df_alldata[['STATION', 'TOT_IN_OUT', 'ZIPCODE', 'POPULATION', 'POPULATION_DEN','MEDIAN_INCOME']].copy()
sns_plot = sns.pairplot(df_temp,diag_kind='kde');


# In[ ]:




