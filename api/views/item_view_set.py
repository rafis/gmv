from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin

from sharded_storage.models import Item
from .item_serializer import ItemSerializer


class ItemViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
