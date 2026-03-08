import json

api_data = {
     "users": [
        {"id": 1, "name": "Alice", "age": 25},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Charlie", "age": 22}
    ],
    "total": 3
}

with open("task1.json", "w") as file:
    json.dump(api_data, file, indent=4)

print("File saved")