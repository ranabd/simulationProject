# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import plotly.graph_objects as go
import os
for dirname, _, filenames in os.walk('DataFiles'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('DataFiles/Covid19_Bangladesh.csv')

x = df[df["Confirmed case"] != 0]["Date"]
y = df[df["Confirmed case"] != 0]["Confirmed case"]

fig = go.Figure()

fig.add_trace(go.Bar(x=x,
                     y=y,
                     text=y,
                     textposition="auto"))

fig.update_layout(title=dict(text="Daily confirmed cases",
                             font_size=25
                             ),
                  yaxis=dict(title="Number of cases"),
                  xaxis=dict(title="Date"))
