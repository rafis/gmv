from django.contrib import admin

from sharded_storage.models import Item


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'description')
    readonly_fields = ('created_at',)


admin.site.register(ItemAdmin.model, ItemAdmin)
