from django.urls import path
from . import views



app_name = 'foodhub'

urlpatterns = [
    path('foodhub/', views.FoothubApiView.as_view(), name='foodhub'),
]
