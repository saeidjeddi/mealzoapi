from django.urls import path
from . import views



app_name = 'deliveroo'

urlpatterns = [
    path('deliveroo/', views.DeliverooApiView.as_view(), name='deliveroo'),
]