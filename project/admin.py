from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from .models import Project, User


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    search_fields = ('app_label', 'model')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'group', 'datetime_create')
