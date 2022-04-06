import csv

countries = "India,Australia,Africa,USA,Canada"
clist = countries.split(',')
print (clist)

try:
    with open('outputCSVFile.csv', 'w') as file:
        writer = csv.writer(file, delimiter = '\n')
        writer.writerow(clist)
except:
    print('Exception occurred')
finally:
    print('All good')