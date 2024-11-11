from django.urls import path, re_path
from django.conf.urls import handler404
from . import views

handler404 = views.url_404

urlpatterns = [
    path('', views.url_home_404),  
    re_path(r'^(?!admin).*$', views.url_404),
]