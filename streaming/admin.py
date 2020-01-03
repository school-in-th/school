from django.contrib import admin

from .models import Streaming


@admin.register(Streaming)
class StreamingAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'type', 'usage', 'size', 'is_default', 'datetime_create')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['project', 'datetime_create']
        else:
            return []
