from django.contrib import admin
from django.urls import path, include
from core.routers import router

from django.conf import settings
from django.conf.urls.static import static

# Import additional modules for Swagger documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from events import views

# Create schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API endpoints for the Core project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/admin/", admin.site.urls),
    path(
        "api/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(
        "social-auth/", include("social_django.urls", "social")
    ),  # это обязательные urlы для работы social_auth
    path(
        "auth/", views.default
    ),  # тестовая auth страничка тупо со ссылкой для авторизации через ВК
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
