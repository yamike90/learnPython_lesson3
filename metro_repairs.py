#В этом задании требуется определить, на каких станциях московского метро сейчас идёт ремонт эскалаторов и вывести на экран их названия.
#Файл с данными можно скачать на странице http://data.mos.ru/opendata/624/row/1773539.

import json

with open('data-397-2019-08-27.json', 'r') as json_data:
    json_list = json.load(json_data)
    for row in json_list:
        if row["RepairOfEscalators"] != []:
            print(row["NameOfStation"])
