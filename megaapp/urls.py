from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from accounts.views import TokenView

urlpatterns = [
    path('panel-mealzo-admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('api/v1/google/', include('googleapi.urls')),
    path('api/v1/zoho/', include('zohoapi.urls')),
    path('api/v1/companies/', include('companies.foodhub.urls')),
    path('api/v1/companies/', include('companies.foodhuse.urls')),
    path('api/v1/companies/', include('companies.ubereats.urls')),
    path('api/v1/companies/', include('companies.whatthefork.urls')),
    path('api/v1/companies/', include('companies.justeat.urls')),
    path('api/v1/companies/', include('companies.menulist.urls')),
    path('api/v1/companies/', include('companies.scoffable.urls')),
    path('api/v1/companies/', include('companies.places.urls')),
    path('api/v1/companies/', include('companies.deliveroo.urls')),
    path('api/v1/companies/', include('companies.straightfrom.urls')),
    path('api/v1/companies/', include('companies.cuisine.urls')),
    path('api/v1/companies/', include('companies.kuick.urls')),
    path('api/v1/companies/', include('companies.postcodes.urls')),
    path('api/v1/companies/', include('companies.orderyoyo.urls')),


    # path('', include('home.urls')),
]





urlpatterns += [
    path('api/token/', TokenView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)