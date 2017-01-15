import pandas
import operator
from pprint import pprint

fac = pandas.read_csv('faculty.csv')

profs_split = []
first_name = [] 
last_name = []
faculty_dict = dict()
professor_dict = dict()
prof_dict = dict()

for x in range(len(fac)):
	profs_split.append(fac.name[x].split(' '))
# print(profs_split)

for x in range(len(profs_split)):
	first_name.append(profs_split[x][0])
	last_name.append(profs_split[x][-1])
# print(first_name)
# print(last_name)




#Q6
for x in range(len(profs_split)):
	faculty_dict[last_name[x]] = [fac.degree[x], fac.title[x].split(" of",1)[0], fac.email[x]]
# print(faculty_dict)

# Q7
for x in range(len(profs_split)):
	professor_dict[first_name[x],last_name[x]] = [fac.degree[x], fac.title[x].split(" of",1)[0], fac.email[x]]
# print(professor_dict)

# Q8
for x in range(len(profs_split)):
	prof_dict[last_name[x], first_name[x]] = [fac.degree[x], fac.title[x].split(" of",1)[0], fac.email[x]]
# print(prof_dict)

sorted_prof_dict = sorted(prof_dict.items(), key=operator.itemgetter(0))
# pprint(sorted_prof_dict)
