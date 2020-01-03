from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'name', 'duration', 'status', 'datetime_create')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['project', 'datetime_create']
        else:
            return []
