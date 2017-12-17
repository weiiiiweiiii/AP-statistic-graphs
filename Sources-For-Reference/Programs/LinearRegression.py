# -*- coding: utf-8 -*-
"""
Created on Fri May  6 12:33:15 2016

@author: Yuliangze
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import mpld3
import pandas as pd
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

N=500

''' construct the dataset which will be used'''
''' It will help us to randomly choose 500 samples'''
'''arange() first number is beginning,sencond is ending,third is vibration'''

df = pd.DataFrame(index=range(N))
df['x'] = np.arange(0, 1, 0.002)

'''nrom.rvs(mean,sample size,sacle)'''
df['y'] = norm.rvs(0, size=500, scale=0.1)

df.y = df.y + df.x**2

''' calculate MSE'''
def rmse(y_test, y):
    return sp.sqrt(sp.mean((y_test - y) ** 2))

''' the R^2 here to test how well the line fits. the range of it would be (0.1).'''
def R2(y_test, y_true):
    return 1 - ((y_test - y_true)**2).sum() / ((y_true - y_true.mean())**2).sum()


'''the degree of lines'''
plt.scatter(df.x, df.y, s=5)
degree = [1,2]
y_test = []
y_test = np.array(y_test)


'''The coef. for ax^2 bx and c'''
for d in degree:
    clf = Pipeline([('poly', PolynomialFeatures(degree=d)),
                    ('linear', LinearRegression(fit_intercept=False))])
    clf.fit(df.x[:, np.newaxis], df.y)
    y_test = clf.predict(df.x[:, np.newaxis])
    
    print(clf.named_steps['linear'].coef_)
    
    '''print out datasets'''
    print('rmse=%.2f, R2=%.2f, clf.score=%.2f' %
      (rmse(y_test, df.y),
       R2(y_test, df.y),
       clf.score(df.x[:, np.newaxis], df.y))) 
   
    '''plot the lines'''
    plt.plot(df.x, y_test, linewidth=2)
    
    
labels = []
for i in range(N):
    label = df.ix[[i], :].T
    label.columns = ['point {0}'.format(i)]
    # .to_html() is unicode; so make leading 'u' go away with str()
    labels.append(str(label.to_html()))

points = ax.scatter(df.x, df.y,c=np.random.random(size=N), alpha=.6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('LinearRegression', size=20)


tooltip = plugins.PointHTMLTooltip(points, labels,
                                   voffset=10, hoffset=10, css=css)
plugins.connect(fig, tooltip)    
    
    
plt.grid()
'''the box in the upper left,indicate line's degree'''
plt.legend(['1','2'], loc='upper left', title='')
plt.show()

#fig = plt.figure(1, figsize=(9, 6))
#fig.savefig('LinearRegression.png', bbox_inches='tight')
fig = plt.figure(1, figsize=(9, 6))
print(mpld3.fig_to_html(fig))