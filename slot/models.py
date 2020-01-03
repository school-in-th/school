from django.db import models


class Slot(models.Model):
    project = models.ForeignKey('project.Project', on_delete=models.SET_NULL, null=True, related_name='+')

    parent_content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE, related_name='+')
    parent_content_id = models.IntegerField()

    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE, related_name='+')
    content_id = models.IntegerField()

    name = models.CharField(max_length=255)

    sort = models.SmallIntegerField(default=1, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    datetime_update = models.DateTimeField(auto_now=True, db_index=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort']
        index_together = [
            ('parent_content_type', 'parent_content_id', 'sort', 'is_active')
        ]

    def __str__(self):
        return '%s: %s' % (self.id, self.name)
