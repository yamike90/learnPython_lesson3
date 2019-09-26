import json

with open('data-397-2019-08-27.json', 'r') as json_data:
    json_list = json.load(json_data)
    for row in json_list:
        if row["RepairOfEscalators"] != []:
            print(row["NameOfStation"])
