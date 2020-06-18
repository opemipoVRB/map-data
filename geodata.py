import csv

import pycristoforo as pyc


country = pyc.get_shape("Nigeria")

points = pyc.geoloc_generation(country, 140058, "Nigeria")

with open('geodata.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for point in points:
        print(point["geometry"]["coordinates"][0], point["geometry"]["coordinates"][1])
        employee_writer.writerow(point["geometry"]["coordinates"])



