# kita akan mencoba dictionary

users = {
    "id" : 1,
    "name" : "Amy Sidra",
    "username" : "amysidra",
    "email" : "amysidra@gmail.com",
    "address" : {
        "jalan" : "jati emas",
        "kelurahan" : "dadapsari",
        "kecamatan" : "gunungpati",
        "geo" : {
            "lat" : "-1234",
            "lang" : "1234"
        }
    }
}

print(users)
print(f"Id = {users["id"]}")
print(f"Nama = {users["name"]}")
print(f"Username = {users["username"]}")
print(f"Email = {users["email"]}")
print(f"alamat = jalan {users["address"]["jalan"]}")
print(f"letak = \nlat : {users["address"]["geo"]["lat"]}\nlang : {users["address"]["geo"]["lang"]} ")

print('\nUbah ke format json')

import json

result = json.dumps(users)
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)