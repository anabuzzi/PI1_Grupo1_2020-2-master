import csv

with open('questionandanswers.csv') as csv_file:
  
  csv_reader = csv.reader(csv_file, delimiter=';')

  csv_reader.__next__()

  for row in csv_reader:
    print( row[0] + ';' + row [1])
