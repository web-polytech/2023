from .models import Visit
from django.core.cache import cache

def log_visit(request):
    user = request.user if request.user.is_authenticated else None
    visit = {
        "user": user,
        "url": request.path,
        "get_params": request.GET,
        "post_params": request.POST,
        "browser": request.META.get('HTTP_USER_AGENT', ''),
    }
    cache.set('visit_log', visit)

def write_visit_log():
    data = cache.get('visit_log')
    if data:
        Visit.objects.create(
            user=data['user'],
            url=data['url'],
            get_params=data['get_params'],
            post_params=data['post_params'],
            browser=data['browser'],
        )
        cache.delete('visit_log')

def get_visits():
    return Visit.objects.all()