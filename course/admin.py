from django.contrib import admin

from .models import Course, Section


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'name', 'duration', 'datetime_update')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'is_active', 'sort', 'datetime_update')
    ordering = ('-datetime_update',)
