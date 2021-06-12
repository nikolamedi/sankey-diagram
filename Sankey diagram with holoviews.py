#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import holoviews as hv
import plotly.graph_objects as go
import plotly.express as pex


# In[2]:


### Based on https://coderzcolumn.com/tutorials/data-science/how-to-plot-sankey-diagram-in-python-jupyter-notebook-holoviews-and-plotly


# In[3]:


hv.extension('bokeh')


# In[4]:


asi_measures = pd.read_csv("final-data.csv")
asi_measures.head()


# In[5]:


### Data cleansing, such as removing entries that are not needed, removing entries without proper name and group dataframe.
### Probably not necessary at all for our data-set.

asi_measures = asi_measures[asi_measures["Category"]!="Net"]
asi_measures = asi_measures[~asi_measures["Indicator"].isin(["Not stated", "All countries"])]
asi_measures_grouped = asi_measures.groupby(by=["Category","ASI"]).sum()[["Count"]]
asi_measures_grouped = asi_measures_grouped.reset_index()
asi_measures_grouped.head()


# In[6]:


### Creating a Sankey diagram:

actions = ["Avoid", "Avoid, Shift","Avoid, Improve","Shift", "Shift, Improve", "Avoid, Shift, Improve", "Improve"]
actions_asi = asi_measures_grouped[asi_measures_grouped.ASI.isin(actions)]
actions_asi


# In[7]:


hv.Sankey(actions_asi)

