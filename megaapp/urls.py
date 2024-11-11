from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from home import views

urlpatterns = [
    path('panel-mealzo-admin/', admin.site.urls),
    path('api/v1/google/', include('api.v1.googleapi.urls')),
    path('api/v1/zoho/', include('api.v1.zohoapi.urls')),

    path('', include('home.urls')),
]
