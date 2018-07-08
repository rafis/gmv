from rest_framework import routers

from .views.item_view_set import ItemViewSet
from .views.set_view_set import SetViewSet


router = routers.SimpleRouter()
router.register(r'items', ItemViewSet)
router.register(r'sets', SetViewSet)
