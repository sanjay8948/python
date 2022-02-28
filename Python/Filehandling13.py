from csv import DictReader
with open('file1.csv','r')as f:
    csv_reader=DictReader(f)
    for row in csv_reader:
        #print(row)
        print(row['name'])


with open('file2.csv','r')as f:
    csv_reader=DictReader(f,delimiter='|')
    for row in csv_reader:
        print(row)
        #print(row['name'])
