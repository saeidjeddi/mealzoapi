from django.http import JsonResponse
from ipaddress import ip_address, ip_network

ALLOWED_IPS = [
    '20.117.166.56/29', '20.117.166.64/26', '20.117.166.128/25',
    '20.117.167.0/24', '20.117.168.0/21', '20.117.176.0/20',
    '20.117.192.0/24', '20.117.193.0/27', '20.117.193.32/31'
]

class RestrictIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META.get('REMOTE_ADDR')
        
        if not any(ip_address(user_ip) in ip_network(network) for network in ALLOWED_IPS):
            return JsonResponse({'error': 'Access denied. Invalid IP address.'}, status=403)

        response = self.get_response(request)
        return response
