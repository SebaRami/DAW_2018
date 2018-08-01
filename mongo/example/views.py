from django.shortcuts import render
from django.views.generic.edit import CreateView
from example.models import Example
from rest_framework import viewsets
from example.serializers import ExampleSerializer

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
    print(servicios)
    return render(request, 'example/index.html', {'facturas':facturas, 'servicios':servicios, 'fechas':fechas})

def filtrar(request):
	facturas = Example.objects.filter(servicio=request.GET['servicio'])
	return render(request, 'example/filtrar.html', {'facturas':facturas})

class ExampleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows example to be viewed or edited.
    """
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer