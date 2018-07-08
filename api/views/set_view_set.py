from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin

from sharded_storage.models import Set
from .set_serializer import SetSerializer


class SetViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = SetSerializer
    queryset = Set.objects.all()
