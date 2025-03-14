from django.urls import path
from . import views



app_name = 'places'

urlpatterns = [
    path('city/', views.CityApiView.as_view(), name='city'),
    path('region/', views.RegionApiView.as_view(), name='region'),
]