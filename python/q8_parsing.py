# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import pandas

csv_foot = pandas.read_csv('football.csv')

for teams in csv_foot:
	csv_foot['diff'] = abs(csv_foot['Goals'] - csv_foot['Goals Allowed'])

print(csv_foot.Team[(csv_foot['diff'] == min(csv_foot['diff']))])
