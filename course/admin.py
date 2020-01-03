from django.contrib import admin

from .models import Course, Section


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'name', 'duration', 'datetime_update')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['project', 'datetime_update', 'datetime_create']
        else:
            return []


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'sort', 'is_active', 'datetime_update')
    ordering = ('-datetime_update',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['project', 'datetime_update', 'datetime_create']
        else:
            return []
