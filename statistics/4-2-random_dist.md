[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> \#The CDF is approximately a straight line, which means that the distribution is uniform.  
import random  
import thinkstats2  
import numpy as np  
import thinkplot  
\  
\  
rand_1000 = []  
\  
for x in range(1000):   
    rand_1000.extend([random.random()])  
\# print(rand_1000)  
\  
\# finding the PMF: mimicing pg. 32 -   
pmf = thinkstats2.Pmf(rand_1000)  
\  
thinkplot.Pmf(pmf)  
thinkplot.Show(xlabel='rand_1000', ylabel='PMF')  #this plot doesn't feel useful, since every random number is unique therefore plots 1/1000
\  
\  
\# finding the CDF: mimicing pg. 52 -   
cdf = thinkstats2.Cdf(rand_1000)  
\  
thinkplot.Cdf(cdf)  
thinkplot.Show(xlabel='rand_1000', ylabel='CDF')  
