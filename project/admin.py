from django.contrib import admin

from .models import Project, User


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'group', 'datetime_create')
