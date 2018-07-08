from rest_framework import serializers

from sharded_storage.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        # fields = ('id', 'cached_name', 'cached_description', 'mime_type', 'filesize', 'crc32', 'sha1')
