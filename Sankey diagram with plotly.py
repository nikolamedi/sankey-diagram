#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json, urllib
import plotly.graph_objects as go
import pandas as pd
import numpy as np


# In[2]:


asi_measures = pd.read_csv('final-data.csv')
asi_measures.head()


# In[4]:


all_nodes = asi_measures.Category.values.tolist() + asi_measures.ASI.values.tolist()
source_indices = [all_nodes.index(Category) for Category in asi_measures.Category]
target_indices = [all_nodes.index(ASI) for ASI in asi_measures.ASI]

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 20,
      thickness = 20,
      line = dict(color = "black", width = 1.0),
      label =  all_nodes,
    ),

    link = dict(
      source =  source_indices,
      target =  target_indices,
      value =  asi_measures.Count,
))])

fig.update_layout(title_text="Transport mitigation actions in the context of Avoid, Shift and Improve",
                  font_size=10)
fig.show()

