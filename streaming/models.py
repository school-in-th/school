from django.db import models


class Streaming(models.Model):
    TYPE_CHOICES = (
        (1, 'Opencast'),
    )

    project = models.ForeignKey('project.Project', on_delete=models.SET_NULL, null=True, related_name='+')

    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=1)

    url = models.CharField(max_length=255)
    path = models.CharField(max_length=255)

    usage = models.FloatField(default=0.0)
    size = models.FloatField(default=0.0)

    is_default = models.BooleanField(default=False, db_index=True)
    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-datetime_create']
