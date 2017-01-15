import pandas
import collections

fac = pandas.read_csv('faculty.csv')

# Q1
degs = dict()
all_degs = []
for x in range(len(fac)):
	degs[x] = fac.degree[x]
# print(degs)

for x in range(len(fac)):
	s = degs[x]
	for word in s.split():
		all_degs.append(word)
# print(all_degs)

for x in range(len(all_degs)):
	all_degs[x] = ''.join(filter(str.isalpha, all_degs[x]))

counter=collections.Counter(all_degs)
print(len(counter)) 
print(counter)
# Length and counter include the empty degree. Wasn't sure if I should leave it in or not. 

# Q2
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
