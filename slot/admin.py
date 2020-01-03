from django.contrib import admin

from .models import Slot


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'content_type', 'content_id', 'name', 'sort', 'is_active', 'datetime_update')
    autocomplete_fields = ('parent_content_type', 'content_type')
    ordering = ('-datetime_update',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['project', 'parent_content_type', 'content_type', 'datetime_update', 'datetime_create']
        else:
            return []
