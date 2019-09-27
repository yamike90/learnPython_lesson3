#Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, вывести улицу, на которой больше всего остановок.

import csv

with open('data-398-2019-09-18.csv', 'r', encoding='windows-1251') as bus_stops:
    reader = csv.DictReader(bus_stops, delimiter=';')
    streets_list = [] #создать пустой список с перечислением улиц из csv
    for row in reader:
        streets_list.append(row['Street']) #наполнить список значениями улиц
    max_bus_stops_street = max(set(streets_list), key=streets_list.count) # преобразовать список во множество (юники), по каждому элементу множетсво получить количество повторений в списке с помощью функции count в key, сохранить в переменную улицы с наибольшем количеством повторений из key)
print(max_bus_stops_street + ', ' + str(streets_list.count(max_bus_stops_street)))