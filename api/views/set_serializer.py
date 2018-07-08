from rest_framework import serializers

from sharded_storage.models import Set


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'
        # fields = ('id', 'cached_name', 'cached_description', 'owner_user_id')
