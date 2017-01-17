[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

    import scipy
    from scipy.stats import norm

    # height is in cm in brfss.py from pg 66, convert in to cm, male between 5’10” and 6’1” 

    cm_low = (5*12+10)*2.54
    cm_high = round((6*12+1)*2.54,2) #Strange that this outputs 185.42000000000002 before rounding
    print(cm_low)
    print(cm_high)

    # µ = 178 cm and σ = 7.7 cm for men

    low_range = scipy.stats.norm(178, 7.7).cdf(cm_low)
    high_range = scipy.stats.norm(178, 7.7).cdf(cm_high)
    total_range = high_range - low_range
    print(total_range*100)
    
    # 34.27% of the U.S. male population is in this range
