from django.shortcuts import render
from django.views.generic.edit import CreateView
from example.models import Example

# Create your views here.

def index(request):
    facturas = Example.objects.all()
    print(facturas)
    servicios = []
    fechas = []
    for factura in facturas:
        if factura.getServicio() not in servicios:
            servicios.append(factura.getServicio())
        if factura.getFecha() not in fechas:
            fechas.append(factura.getFecha())

    print(servicios)
    return render(request, 'example/index.html', {'facturas':facturas, 'servicios':servicios, 'fechas':fechas})

def filtrar(request):
	facturas = Example.objects.filter(servicio=request.GET['servicio'])
	return render(request, 'example/filtrar.html', {'facturas':facturas})