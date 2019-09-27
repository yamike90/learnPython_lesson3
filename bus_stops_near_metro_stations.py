import csv
import json

from geopy.distance import geodesic

metro_geo_dict = {}
with open('data-397-2019-08-27.json', 'r') as json_data:
    json_list = json.load(json_data)
    for row in json_list:
        metro_geo_dict[row["NameOfStation"]] = (row["Longitude_WGS84"], row['Latitude_WGS84'])

bus_stops_geo_dict = {}
with open('data-398-2019-09-18.csv', 'r', encoding='windows-1251') as bus_stops:
    reader = csv.DictReader(bus_stops, delimiter=';')
    for row in reader:
        bus_stops_geo_dict[row['ID']] = (row["Longitude_WGS84"], row['Latitude_WGS84'])
    bus_stops_geo_dict.pop("ID")

metro_stops_dict = {}
for station in metro_geo_dict:
    geo_station = metro_geo_dict[station]
    metro_stops_count = 0
    for id in bus_stops_geo_dict:
        geo_stop = bus_stops_geo_dict[id]
        if geodesic(geo_station, geo_stop).m < 500:
            metro_stops_count += 1
            # print(station, id, geodesic(geo_station, geo_stop).m)
    metro_stops_dict[station] = metro_stops_count
    # print(metro_stops_dict)

#print(metro_stops_dict)

max_stops_station = 0
for item in metro_stops_dict:
    if metro_stops_dict[item] >= max_stops_station:
        max_stops_station = metro_stops_dict[item]
        that_great_station = item
print(that_great_station)

