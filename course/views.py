from rest_framework import viewsets
from rest_framework.response import Response

from .models import Course
from .serializers import CourseListSerializer


class HomeView(viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

    action_serializers = {
        'list': CourseListSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers') and self.action in self.action_serializers:
            return self.action_serializers[self.action]
        else:
            return super().get_serializer_class()

    def get_queryset(self):
        return self.queryset.filter(project=self.request.PROJECT)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        serializer = self.get_serializer(page, many=True)
        return Response(self.get_paginated_response(serializer.data).data)
