from rest_framework import serializers
from apps.clients.models import *

#serializer para listar, crear y detallar clientes
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    
    
    def create(self,validated_data):
        client = Client(**validated_data)
        client.save()
        return client

'''
    Serializer para actualizar un cliente
'''
class UpdateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('fullname','id_number','email','birthdate','is_active')

