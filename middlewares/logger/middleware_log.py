import logging
from django.utils.timezone import now
from django.http import HttpRequest

logger = logging.getLogger('django')

class UserAccessLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        if not request.path.startswith('/static/'):
            self.log_user_access(request)
            return response

    def log_user_access(self, request: HttpRequest):
        if request.user.is_authenticated:
            ip_address = request.META.get('REMOTE_ADDR')
            accessed_url = request.get_full_path()
            timestamp = now() 
            username = request.user.username
            email = request.user.email
            log_message = (
                f"User: {username}, Email: {email}, Method: {request.method}, "
                f"IP: {ip_address}, URL: {accessed_url}, Time: {timestamp}"
            )
            logger.info(log_message)