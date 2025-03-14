# ip_port_middleware.py
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

ALLOWED_IP_PORTS = [
    ('http://localhost:127.0.0.1', 5173),
    ('http://localhost', 5173),
    ('takeawaytracker.mealzo.co.uk'),
  
]

class IPPortAllowMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        port = request.META.get('SERVER_PORT')
        if not (ip, int(port)) in ALLOWED_IP_PORTS:
            return JsonResponse({'detail': 'Forbidden: IP or Port not allowed'}, status=403)
        return None
