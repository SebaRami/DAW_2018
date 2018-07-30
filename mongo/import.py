from djongo import models
from example.models import Example
import csv

with open('todosmisservicios.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader[:500]:
        line = line[0].split(";")
        factura = Example()
        factura.nombre = line[0]
        factura.servicio = line[1]
        factura.ciudad = line[2]
        factura.total_factura = float(line[4])
        factura.fecha = line[3]
        factura.save()