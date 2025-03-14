from django.urls import path
from . import views



app_name = 'foodhub'

urlpatterns = [
    path('foodhub/', views.FoodhubApiView.as_view(), name='foodhub'),
]