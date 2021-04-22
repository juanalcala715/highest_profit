import csv
import json

csvfile = open('new_data.csv', 'r')
jsonfile = open('data2.json', 'w')

reader = csv.DictReader(csvfile)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write("\n")



#with open('new_data1.csv') as f:
    #reader = csv.DictReader(f)
    #rows = list(reader)

#with open('data2210.json', 'w') as f:
   # json.dump(rows, f)