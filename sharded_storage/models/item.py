from django.db import models
from django.apps import apps
from django_sharding_library.decorators import model_config
from django_sharding_library.fields import TableShardedIDField
from django_sharding_library.models import TableStrategyModel


@model_config(database='default')
class ShardedItemIDs(TableStrategyModel):
    pass


@model_config(shard_group='items_shard_group', sharded_by_field='id')
class Item(models.Model):
    id = TableShardedIDField(primary_key=True, source_table_name='core.ShardedItemIDs')
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_shard(self):
        if self.pk is not None:
            shard_group = getattr(self, 'django_sharding__shard_group')
            django_sharding_app = apps.get_app_config('django_sharding')
            bucketer = django_sharding_app.get_bucketer(shard_group)

            return bucketer.get_shard(self)
        else:
            sharded_by_field = getattr(self, 'django_sharding__sharded_by_field')
            sharded_by_field = self._meta.get_field(sharded_by_field)
            self.pk = sharded_by_field.strategy.get_next_id()
            
            return self.get_shard()

    @staticmethod
    def get_shard_from_id(pk):
        if pk is not None:
            shard_group = getattr(Item, 'django_sharding__shard_group')
            django_sharding_app = apps.get_app_config('django_sharding')
            bucketer = django_sharding_app.get_bucketer(shard_group)
    
            obj = Item()
            obj.pk = pk

            return bucketer.get_shard(obj)
        else:
            sharded_by_field = getattr(Item, 'django_sharding__sharded_by_field')
            
            sharded_by_field = Item._meta.get_field(sharded_by_field)
            pk = sharded_by_field.strategy.get_next_id()
            
            return get_shard_from_id(pk)
