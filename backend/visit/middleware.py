from .services import log_visit

class VisitLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/api/admin0') and not request.path.startswith('/auth'):
          log_visit(request)
        response = self.get_response(request)
        return response
