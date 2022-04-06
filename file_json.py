import json
 
dictionary ={
'name': 'Learner 1',
'experience': 'beginner',
'contact' : [ {
'email': 'xyz@gmail.com',
'from': 'Maharashtra'}], 
'number':'43098090909'
}
object = json.dumps(dictionary, indent = 2)
with open("file_json.json", "w") as outfile:
    outfile.write(object )