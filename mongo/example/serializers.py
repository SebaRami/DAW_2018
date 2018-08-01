from example.models import Example
from rest_framework import serializers


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Example
        fields = ('nombre', 'servicio', 'ciudad', 'total_factura', 'fecha')