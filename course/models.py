import datetime

from django.db import models


class Course(models.Model):
    project = models.ForeignKey('project.Project', on_delete=models.SET_NULL, null=True, related_name='+')

    name = models.CharField(max_length=255, db_index=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='course/%Y/%m', null=True, blank=True)
    thumb = models.ImageField(upload_to='course/thumb/%Y/%m', null=True, blank=True)

    duration = models.DurationField(default=datetime.timedelta(0))
    is_section = models.BooleanField(default=False)

    datetime_publish = models.DateTimeField(null=True, blank=True, db_index=True)
    datetime_update = models.DateTimeField(auto_now=True, db_index=True)
    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'course.course'
        ordering = ['-datetime_update']


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    duration = models.DurationField(default=datetime.timedelta(0))

    is_active = models.BooleanField(default=True, db_index=True)
    sort = models.IntegerField(default=1, db_index=True)
    datetime_update = models.DateTimeField(auto_now=True, db_index=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'course.section'
        ordering = ['sort']
