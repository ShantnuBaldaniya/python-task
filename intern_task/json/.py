import json
with open('student.json','r') as file:
    data=json.load(file)
    
print(data)
print(type(data))
print(type('studnet.json'))