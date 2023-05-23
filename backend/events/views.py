from rest_framework.viewsets import ModelViewSet
from events.models import Event
from events.serializers import EventSerializer


class EventViewset(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
