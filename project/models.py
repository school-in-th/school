from django.db import models


class Project(models.Model):
    code = models.CharField(max_length=120, db_index=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.name

    @staticmethod
    def pull(code=None):
        if code is None:
            project = Project.objects.order_by('id').first()
            if project is None:
                project = Project.objects.create(code='school', name='School')
        else:
            project = Project.objects.filter(code=code).first()
            if project is None:
                project = Project.objects.create(code='school', name='School')
        return project


class User(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    group = models.ForeignKey('auth.Group', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-datetime_create']
