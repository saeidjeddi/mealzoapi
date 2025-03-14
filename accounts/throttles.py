from rest_framework.throttling import UserRateThrottle
from .models import User

class CustomUserRateThrottle(UserRateThrottle):
    def allow_request(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return True

        if user.is_limitation:
            self.rate = f"{user.request_limit}/{user.limitation_type}"
            self.num_requests, self.duration = self.parse_rate(self.rate)
        else:
            return True

        return super().allow_request(request, view)
