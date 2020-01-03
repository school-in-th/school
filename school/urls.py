from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns_api = [

]

schema_view = get_schema_view(
    openapi.Info(
        title="School API",
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=urlpatterns_api
)

urlpatterns = [
    path('api/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0)),

    path('admin/', admin.site.urls),
]

urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
