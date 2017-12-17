# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:06:12 2016

@author: Yuliangze
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins

# Define some CSS to control our custom labels
css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""

fig, ax = plt.subplots()
ax.grid(True, alpha=0.3)

N = 50
df = pd.DataFrame(index=range(N))
df['x'] = np.random.randn(N)
df['y'] = np.random.randn(N)

labels = []
for i in range(N):
    label = df.ix[[i], :].T
    label.columns = ['point {0}'.format(i)]
    # .to_html() is unicode; so make leading 'u' go away with str()
    labels.append(str(label.to_html()))

points = ax.scatter(df.x, df.y,c=np.random.random(size=N),
                     s = 1000 * np.random.random(size=N), alpha=.6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('ScatterPlot', size=20)

tooltip = plugins.PointHTMLTooltip(points, labels,
                                   voffset=10, hoffset=10, css=css)
plugins.connect(fig, tooltip)

mpld3.show()
fig = plt.figure(1, figsize=(9, 6))
print(mpld3.fig_to_html(fig))