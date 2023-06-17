from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

'''
    Se agregan routes y url de la app clients, también se agrega swagger para la documentación desde drf
'''

schema_view = get_schema_view(
   openapi.Info(
      title="Softseguros API",
      default_version='v1.0',
      description="Documentación pública de Softseguros",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="wilmerpb30@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   #permission_classes=[permissions.IsAdminUser],

)
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('',include('apps.clients.api.routers')),
    path('',include('apps.clients.api.urls')),

]
