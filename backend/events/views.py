from rest_framework.viewsets import ModelViewSet
from events.models import Event
from events.serializers import EventSerializer


class EventViewset(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

from django.shortcuts import render

def default(request): # это максимально тестовая штука которой тут по хорошему быть не должно как и templates
    return render(request, 'index.html')
