from django.db import connections
from django.db.utils import OperationalError

class DatabaseConnectionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            connections['default'].cursor()
        except OperationalError:
            connections.close_all()
        return self.get_response(request)
