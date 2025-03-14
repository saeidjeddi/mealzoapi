from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path('scoffable/', views.ScoffableApiView.as_view()),
]