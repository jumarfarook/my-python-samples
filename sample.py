s = 'hello world'
listval = s.split(" ")
caplist = [s.capitalize() for s in listval]
output = " ".join(caplist)
print (output)