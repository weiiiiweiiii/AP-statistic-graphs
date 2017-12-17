from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
import mpld3

#print ("Welcome!")
#print ("This is a program that can help you plot graphs for binomial distributions")

#Using binom.pmf to get a list which contains the simulated values

#n = raw_input("Please enter the number of experiments denoted as 'n' (n has to be a integer), n = ")
#p = raw_input("Please enter the probability of success denoted as 'p', p = ")

n = int(50)
o = n + 1
p = float(0.3)

a = np.arange(0,o)
binomial = binom.pmf(a, n, p)


#Plotting the binomial distribution for users
plt.plot(a, binomial, 'o-')
plt.title('Binomial: n=%i, p=%.2f' %(n, p), fontsize = 20)
plt.xlabel('Number of successes', fontsize = 15)
plt.ylabel('Probability of successes', fontsize = 15)



binomsim = binom.rvs(n, p, size = 1000000)
print ("Mean: %g" % np.mean(binomsim))
print ("SD: %g" % np.std(binomsim, ddof=1))
plt.hist(binomsim,normed = True)
plt.xlabel("x")
plt.ylabel("density")
plt.show()

#fig = plt.figure(1, figsize=(9, 6))
#fig.savefig('Binomial.png', bbox_inches='tight')

fig = plt.figure(1, figsize=(9, 6))
print(mpld3.fig_to_html(fig))