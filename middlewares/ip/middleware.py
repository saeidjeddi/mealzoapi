from django.http import JsonResponse

ALLOWED_IPS = ['198.168.2.85', '148.52.96.8']  
class RestrictIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META.get('REMOTE_ADDR')
        
        if user_ip not in ALLOWED_IPS:
            return JsonResponse({'error': 'Access denied. Invalid IP address.'}, status=403)

        response = self.get_response(request)
        return response