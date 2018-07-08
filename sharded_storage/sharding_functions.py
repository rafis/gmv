from django_sharding_library.sharding_functions import BaseBucketingStrategy


class DivModBucketingStrategy(BaseBucketingStrategy):
    """
    A shard selection strategy that assigns shards based on the mod of the
    models pk.
    """
    def __init__(self, shard_group, databases, big_shard_count, small_shard_count, small_shard_size):
        super().__init__(shard_group)
        self.shards = self.get_shards(databases)
        self.big_shard_count = big_shard_count
        self.small_shard_count = small_shard_count
        self.small_shard_size = small_shard_size

    def pick_shard(self, model_sharded_by):
        return self.shards[model_sharded_by.pk // self.small_shard_size + model_sharded_by.pk % self.small_shard_count]

    def get_shard(self, model_sharded_by):
        return self.pick_shard(model_sharded_by)
