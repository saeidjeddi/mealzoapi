from django.urls import path
from . import views




urlpatterns = [

    path('kuick/', views.KuickApiView.as_view()),


]
