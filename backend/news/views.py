from rest_framework.viewsets import ModelViewSet
from news.models import News
from news.serializers import NewsSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response


class NewsViewset(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    CACHE_KEY_PREFIX = "news"

    @method_decorator(cache_page(60 * 2, key_prefix=CACHE_KEY_PREFIX))  # 2 minutes
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = NewsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def delete_cache(self, prefix):
        from django.core.cache import cache

        keys = [key for key in cache.keys() if prefix in key]
        cache.delete_many(keys)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        self.delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        self.delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        self.delete_cache(self.CACHE_KEY_PREFIX)
        return response
