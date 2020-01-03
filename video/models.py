import datetime

from django.db import models


class Video(models.Model):
    STATUS_CHOICES = (
        (0, 'init'),
        (1, 'uploading'),
        (2, 'waiting'),
        (3, 'processing'),
        (4, 'completed'),
    )

    project = models.ForeignKey('project.Project', on_delete=models.SET_NULL, null=True, related_name='+')
    streaming = models.ForeignKey('streaming.Streaming', on_delete=models.SET_NULL, null=True, related_name='+')

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='video/%Y/%m', null=True, blank=True)
    thumb = models.ImageField(upload_to='video/thumb/%Y/%m', null=True, blank=True)

    duration = models.DurationField(default=datetime.timedelta(0))
    uuid = models.CharField(max_length=120, db_index=True)
    path = models.CharField(max_length=255, db_index=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)

    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'video.video'
        ordering = ['-datetime_create']
