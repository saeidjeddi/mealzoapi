from django.urls import path
from . import views



urlpatterns = [

    path('ubereats/', views.UberEatsApiView.as_view()),

    # jwt
]



