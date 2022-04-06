import os

print (os.getcwd())
os.chdir('..')
lst = os.listdir(os.getcwd())
lst.sort()
print (lst)