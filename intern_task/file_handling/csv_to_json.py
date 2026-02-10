import csv
import json

csv_path = "E:\\code\\python-task\\intern_task\\json\\data.csv"
json_path = "E:\\code\\python-task\\intern_task\\json\\data.json"

with open(csv_path, "r", newline="", encoding="utf-8") as c:
    reader = csv.DictReader(c)
    data = list(reader)

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
    

print("csv file convert to json done")


