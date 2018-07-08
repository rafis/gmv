from django.contrib import admin

from sharded_storage.models import Set


class SetAdmin(admin.ModelAdmin):
    model = Set
    list_display = ('name', 'description')
    readonly_fields = ('created_at',)


admin.site.register(SetAdmin.model, SetAdmin)
