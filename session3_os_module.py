import os

input_str = input('Enter your input:')

with open ("filename.txt", "w") as writefile:
    writefile.write(input_str)

with open ("filename.txt", "r") as readfile:
    reader = readfile.read()

print (reader.__str__())
