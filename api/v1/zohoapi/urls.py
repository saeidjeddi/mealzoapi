from django.urls import path
from . import views



app_name = 'zoho'

urlpatterns = [
        path('mealzo/', views.ZohoMealView.as_view(), name='mealzoho'),

]
