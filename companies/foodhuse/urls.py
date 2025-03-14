from django.urls import path
from . import views
urlpatterns = [
    path('foodhouse/', views.FoodhouseApiView.as_view()),

]