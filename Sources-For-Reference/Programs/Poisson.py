# -*- coding: utf-8 -*-
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
import mpld3

#print "Welcome!"
#print "This is a program that can help you plot graphs for poisson distributions"


#Using poisson.pmf to create a list 
#rate = raw_input("Please enter the rate(rate should be an integer), rate = " )
#o = raw_input("Please enter the maximum number of incidents(o should be an integer), o = ")

rate = int(5)
o = int(500)
n = np.arange(0,o+1)
y = poisson.pmf(n, rate)


#Plotting the poisson distribution for users
plt.plot(n,y, 'o-')

plt.title('Poisson: rate=%i' %(rate), fontsize = 20)
plt.xlabel('Number of incidents', fontsize = 15)
plt.ylabel('Probability of happenning', fontsize = 15)


poisim = poisson.rvs(rate, loc = 0, size = 1000)
print ("Mean: %g" % np.mean(poisim))
print ("SD: %g" % np.std(poisim, ddof=1))

#plt.figure()
plt.hist(poisim,bins = 9, normed = True)
plt.xlim(0,10)
plt.xlabel("Number of incidents")
plt.ylabel("density")
plt.show()

#fig = plt.figure(1, figsize=(9, 6))
#fig.savefig('Poisson.png', bbox_inches='tight')

fig = plt.figure(1, figsize=(9, 6))
print(mpld3.fig_to_html(fig))
