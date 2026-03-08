import json
import csv

with open("task1.json", "r") as file:
    data = json.load(file)

users = data["users"]

with open("task3.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "age"])
    writer.writeheader()
    writer.writerows(users)

print("CSV saved")