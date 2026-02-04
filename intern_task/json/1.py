# import json
# toy_conditions = {'chew bone': 7, "ball": 3, "sock": -1}

# n=json.dumps(toy_conditions)
# print(n)
# print(type(n))
# import json

# json_data = '{"name": "Amit", "age": 22}'

# python_data = json.loads(json_data)

# print(python_data)
# print(type(python_data))



import json

data = {
    "name": "Amit",
    "age": 21,
    "city": "Surat",
    "is_student": True
}


with open('dataa.py','w') as file:
    json.loads(data,file,indent=4)
    

