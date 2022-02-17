import csv, json

f = open("states.csv")
f = f.readlines()

reader = csv.reader(f)

d = {}

for row in reader:
    d[row[0].strip()] = row[1]

jsonfile = json.dumps(d)

with open('test.json', 'w') as t:
    t.write(jsonfile)
    t.close()