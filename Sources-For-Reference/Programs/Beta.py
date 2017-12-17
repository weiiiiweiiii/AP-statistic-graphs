# -*- coding: utf-8 -*-
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt
import mpld3

#print "Welcome!"
#print "This is a program that can help you plot graphs for beta distributions"

#Using beta.pdf to get a list
#a =raw_input("Please enter the value of alpha:")
#b =raw_input("Please enter the value of beta:")

a = float(20)
b = float(40)
n = np.arange(0.01,1,0.01)
y = beta.pdf(n, a, b)


plt.plot(n, y)
plt.title('Binomial: a=%i, b=%.2f' %(a, b), fontsize = 20)
plt.xlabel('x', fontsize = 15)
plt.ylabel('Probability density', fontsize = 15)

plt.show()


#fig.savefig('Beta.png', bbox_inches='tight')
fig = plt.figure(1, figsize=(9, 6))
print(mpld3.fig_to_html(fig))