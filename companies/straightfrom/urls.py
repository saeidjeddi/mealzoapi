from django.urls import path
from . import views



app_name = 'straightfrom'

urlpatterns = [
    path('straightfrom/', views.StraightfromApiView.as_view(), name='straightfrom'),
]