# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import plotly.graph_objects as go
import os
for dirname, _, filenames in os.walk('CSVFiles'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
df.info()
df.describe()
df.nunique()

