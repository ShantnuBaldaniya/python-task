import json

mock_json='''
[
    {
        "id": 1,
        "name": "Amit Patel",
        "email": "amit@gmail.com",
        "address": {
            "city": "Ahmedabad",
            "pincode": 380001
        }
    },
    {
        "id": 2,
        "name": "Shah",
        "email": "neha@gmail.com",
        "address": {
            "city": "Surat",
            "pincode": 395003
        }
    }
] '''
data=json.loads(mock_json)
print(data)
print(type(data))

for user in data:
        uid = user["id"]
        name = user["name"]
        email = user["email"]
        print(user)
        
user_info = {
            "ID": uid,
            "Name": name,
            "Email": email
        
        }

print(user_info)









