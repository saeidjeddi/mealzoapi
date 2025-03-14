
from django.urls import path
from . import views


urlpatterns = [
     path('whatthefork/', views.WsApiView.as_view()),
]