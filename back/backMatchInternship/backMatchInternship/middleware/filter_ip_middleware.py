from http import HTTPStatus
from django.http import HttpResponse

class FilterIPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request, exception):
        allowed_ips = ['']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise HTTPStatus.FORBIDDEN

        return None