from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('example/', views.index, name='index'),
    path('filtrar/', views.filtrar, name='filtrar'),
    path(r'modelos/', views.ExampleViewSet.as_view({'get':'list'})),
]