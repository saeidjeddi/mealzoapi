from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('panel-mealzo-admin/', admin.site.urls),
    path('api/v1/google/', include('api.v1.googleapi.urls')),
    path('api/v1/zoho/', include('api.v1.zohoapi.urls')),
    path('api/v1/companies/', include('api.v1.companies.foodhub.urls')),
    path('api/v1/companies/', include('api.v1.companies.foodhuse.urls')),
    path('api/v1/companies/', include('api.v1.companies.ubereats.urls')),
    path('api/v1/companies/', include('api.v1.companies.whatthefork.urls')),
    path('api/v1/companies/', include('api.v1.companies.justeat.urls')),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
