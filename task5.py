import json
import csv

with open("task1.json", "r") as file:
    data = json.load(file)

new_user = {"id": 4, "name": "Diana", "age": 28}
data["users"].append(new_user)
data["total"] = len(data["users"])

with open("task1.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON updated")

with open("task3.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "age"])
    writer.writerow(new_user)

print("CSV updated")