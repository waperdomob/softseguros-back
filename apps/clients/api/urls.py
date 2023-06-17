from django.urls import path
from apps.clients.api.viewsets import  ClientsCreateApiView
urlpatterns = [
    path('client/create/', ClientsCreateApiView.as_view(), name = 'clients-create'),

]