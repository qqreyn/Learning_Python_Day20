import json

with open("task1.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data["total"])

for user in loaded_data["users"]:
    print(f"Name: {user['name']}, Age: {user['age']}")