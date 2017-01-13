import pandas

fac = pandas.read_csv('faculty.csv')
fac.email.to_csv('emails.csv')
