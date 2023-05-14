from rest_framework import serializers
from news.models import News
from quotes.models import Quote
from gallery.models import Gallery



class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields =['photo_gallery']

class NewsSerializer(serializers.ModelSerializer):
    quote = QuoteSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['cover', 'title', 'tagline', 'lid', 'text', 'date', 'duration', 'quote', 'gallery']
