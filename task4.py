import csv

ages = []
names = []

with open("task3.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        names.append(row["name"])
        ages.append(int(row["age"]))

print(f"Users: {names}")
print(f"Total users: {len(ages)}")
print(f"Average age: {sum(ages) / len(ages):.1f}")
print(f"Oldest age {max(ages)}")
print(f"Youngest age: {min(ages)}")