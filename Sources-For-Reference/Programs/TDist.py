from scipy.stats import norm
from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt
import mpld3


#print ("Welcome!")
#print ("This is a program that can help you compare Z distribution and T distribution"


mu = 0
sigma = 1
n = np.arange(-5,5,0.1)

#df = raw_input("Please enter the degree of freedom for T distribution (the value should be a integer): ")
df = int(20)

y = norm.pdf(n,0,1)
x = t.ppf(0.1, df)

x = np.linspace(t.ppf(0.01, df),t.ppf(0.99, df), 100)
plt.plot(x, t.pdf(x, df), 'r-', lw=5)
rv = t(df)


#Plotting the distributions for users
plt.plot(n,y)
plt.plot(x, t.pdf(x, df))
plt.title('Z Dist(blue line) & T Dist(red line)' , fontsize = 15)
plt.xlabel('x', fontsize = 15)
plt.ylabel('Probability density', fontsize = 15)

plt.show()

#fig = plt.figure(1, figsize=(9, 6))
#fig.savefig('TDist.png', bbox_inches='tight')
fig = plt.figure(1, figsize=(9, 6))
print(mpld3.fig_to_html(fig))