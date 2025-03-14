# cors_middleware.py

from django.utils.deprecation import MiddlewareMixin

# Define the allowed origins
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",  
     # Production URL
]

class CORSMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        origin = request.META.get("HTTP_ORIGIN")
        if origin in ALLOWED_ORIGINS:
            response["Access-Control-Allow-Origin"] = origin
            response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
            response["Access-Control-Allow-Credentials"] = "true"  # Optional, if needed

        # Handle preflight OPTIONS requests
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
            response["Access-Control-Max-Age"] = "86400"  # Cache preflight response for 24 hours

        return response
