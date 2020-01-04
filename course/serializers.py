from rest_framework import serializers

from .models import Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'thumb',

            'datetime_publish'
        )
