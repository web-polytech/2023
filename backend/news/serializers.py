from rest_framework import serializers
from news.models import News
from quotes.models import Quote
from gallery.models import Gallery
from django.core.cache import cache


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ["photo_gallery"]


class NewsSerializer(serializers.ModelSerializer):
    quote = QuoteSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = [
            "cover",
            "title",
            "tagline",
            "lid",
            "text",
            "date",
            "duration",
            "quote",
            "gallery",
        ]

    # def to_representation(self, instance):
    #     cache_key = f"news_{instance.id}"

    #     news_data = cache.get(cache_key)

    #     if news_data is None:
    #         # If the serialized news data is not in the cache, serialize it and store it in the cache
    #         news_data = super().to_representation(instance)
    #         cache.set(cache_key, news_data)

    #     return news_data
