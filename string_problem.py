####### Better Solution ########
##############################################################################
word = 'bmaunmdbraaiadx'
#word = 'wmourmlbia#i'
#word = 'cmhuemmbbauir#'

#string[start : stop : step size]

place = word[0::2].replace('#','')
city = word[1::2].replace('#','')

print (place + ',' + city)
##############################################################################

# First attempt
##############################################################################
word = 'bmaunmdbraaiadx'
i=0
place = ""
city = ""

while i < len(word):
  place = place + word[i]
  city = city + word[i+1]
  i=i+2

print (place + ',' + city)
##############################################################################

# Second attempt
##############################################################################
word = 'bmaunmdbraaiadx'
i=0
place=''
city =''

while i < len(word):
  place += word[i]
  if (i+1) < len(word):
    city += word[i+1]
  i=i+2

if (len(city) < len(place)):
  city += '#'

print (place + ',' + city)
print (str(len(place)) + ',' + str(len(city)))
##############################################################################