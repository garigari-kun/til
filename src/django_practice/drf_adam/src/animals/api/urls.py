from rest_framework import routers

from .views import KittenViewSet


router = routers.SimpleRouter()
router.register(r'', KittenViewSet)
