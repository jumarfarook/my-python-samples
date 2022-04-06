import csv

try:
    inputVal = int(input('Enter the number:'))
    outputlist = [str(i) for i in range(inputVal,inputVal+6)]

    with open("csv_module.csv","w") as writefile:
        writefile.write(str(outputlist))

    with open("csv_module.csv","r") as readfile:
        reader = readfile.read()
        print (reader.__str__())

except ValueError:
    print ('Not a valid number')
finally:
    pass