from django.urls import path
from . import views



app_name = 'cuisine'

urlpatterns = [
    path('cuisine/', views.CuisineApiView.as_view(), name='cuisines'),
]