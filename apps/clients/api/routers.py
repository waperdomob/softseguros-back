from rest_framework.routers import DefaultRouter

from apps.clients.api.viewsets import *
from apps.clients.api.serializers import *
router = DefaultRouter()

router.register(r'clients',ClientViewSet, basename = 'clients')

urlpatterns = router.urls