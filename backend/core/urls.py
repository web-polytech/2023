from django.contrib import admin
from django.urls import path, include
from core.routers import router

# Import additional modules for Swagger documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # Swagger documentation URLs
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
]
