from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class JsonResponse404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return JsonResponse({
                'error': 'Not Found',
                'message': 'The requested URL was not found on the server.'
            }, status=404)
        return response