from django.urls import path
from . import views



urlpatterns = [

    path('orderyoyo/', views.OrderyoyoApiView.as_view()),

]

