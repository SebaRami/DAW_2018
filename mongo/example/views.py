from django.shortcuts import render
from django.views.generic.edit import CreateView
from example.models import Example

# Create your views here.

def index(request):
    facturas = Example.objects.all()
    servicios = []
    fechas = []
    for factura in facturas:
        if factura.getServicio() not in servicios:
            servicios.append(factura.getServicio())
        if factura.getFecha() not in fechas:
            fechas.append(factura.getFecha())


    return render(request, 'example/index.html', {'facturas':facturas, 'servicios':servicios, 'fechas':fechas})