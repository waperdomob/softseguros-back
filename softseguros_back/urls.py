from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from rest_framework import permissions

'''
    Se agregan routes y url de la app clients, también se agrega swagger para la documentación desde drf
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.clients.api.routers')),
    path('',include('apps.clients.api.urls')),

]
