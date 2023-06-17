from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics
from rest_framework import status
from rest_framework.response import Response

from apps.clients.models import Client
from apps.clients.api.serializers import (
    ClientSerializer, UpdateClientSerializer
)

"""
    Clase generica CreateAPIView para la creación de un objeto del modelo Client
"""       
class ClientsCreateApiView(generics.CreateAPIView):

    serializer_class = ClientSerializer
    
    def post(self, request):
        client_serializer = self.serializer_class(data=request.data)        
        if client_serializer.is_valid():
            client_serializer.save()
            return Response({'message': 'Cliente registrado correctamente.'}, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': client_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

"""
    Clase generica GenericViewSet, cuenta con los metodos para listar, editar y eliminar clientes.
"""    

class ClientViewSet(viewsets.GenericViewSet):

    model = Client
    serializer_class = ClientSerializer
    queryset = None

    def get_object(self, pk=None):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self, pk=None):
        """Obtiene el objeto del modelo Client consultado

        Args.
            pk (id, optional): Id del cliente en la base de datos. Defaults to None.

        Returns.
            object: Ojeto del modelo cliente correspondiente al pk ingresado, si no hay pk se retornan todos los que tengan is_active = True
        """        
        model = self.get_serializer().Meta.model
        if pk == None:
            return (
                model.objects.filter(is_active=True).order_by('-date_joined')
            )
        else:
            return (
                model.objects.filter(is_active=True)
                .filter(id=pk)
                .first()
            )
    
    '''
        Función para listar clientes
    '''
    def list(self, request):
       
        client_serializer = self.serializer_class(self.get_queryset(), many=True)
        data = {
            "clients": client_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)
    
    '''
        Función para ver detalles de un cliente
    '''
    def retrieve(self, request, pk=None):
        client = self.get_object(pk)
        client_serializer = self.serializer_class(client)
        return Response(client_serializer.data)
    
    '''
        Función para actualizar clientes
    '''
    def update(self, request, pk=None):
        client = self.get_object(pk)
        client_serializer = UpdateClientSerializer(client, data=request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response({
                'message': 'Cliente actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': client_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    '''
        Función para realizar el eliminado lógico de clientes
    '''
    def destroy(self, request, pk=None):
        client_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if client_destroy == 1:
            return Response({
                'message': 'Cliente eliminado correctamente'
            })
        return Response({
            'message': 'No existe el cliente que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)