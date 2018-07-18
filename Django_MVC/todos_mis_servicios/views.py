from django.shortcuts import render
from django.views.generic.edit import CreateView
from todos_mis_servicios.models import Usuario, Servicio
# Create your views here.

def post_list(request):
	usuarios = Usuario.objects.all()
	servicios = Servicio.objects.all()
	return render(request, 'todos_mis_servicios/index.html', {'usuarios':usuarios, 'servicios':servicios})
