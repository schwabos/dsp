import pandas

fac = pandas.read_csv('faculty.csv')

# Q2
import collections
titles = []
for x in range(len(fac)):
 	titles.append(fac.title[x])

counter=collections.Counter(titles)
print(counter)
# Looking at the output, I assume there is a typo and 'is' should be 'of' for 'Assistant Progessor is Biostatistics'. 
# Therefore final count: {'Professor of Biostatistics': 13, 'Associate Professor of Biostatistics': 12, 'Assistant Professor of Biostatistics': 12}

# Q3
emails = []
for x in range(len(fac)):
	emails.append(fac.email[x])
print(emails)

# Q4
domains = []
for x in range(len(fac)): 
	domains.append(emails[x].split("@",1)[1])
counter=collections.Counter(domains)
print(counter)
