from .models import LogVisit
from django.core.cache import cache
import time


def log_visit(request):
    user = request.user if request.user.is_authenticated else None
    visit = {
        "user": user,
        "url": request.path,
        "get_params": request.GET,
        "post_params": request.POST,
        "browser": request.META.get('HTTP_USER_AGENT', ''),
    }
    cache.set('visit_log'+str(time.time()), visit)

def write_visit_log():
    keys = cache.keys('*')
    for key in keys:
      if key.startswith('visit'):
        data = cache.get(key)
        LogVisit.objects.create(
            user=data['user'],
            url=data['url'],
            get_params=data['get_params'],
            post_params=data['post_params'],
            browser=data['browser'],
        )
    for key in keys:
      if key.startswith('visit'):
        cache.delete(key)

def get_visits():
    return LogVisit.objects.all()
