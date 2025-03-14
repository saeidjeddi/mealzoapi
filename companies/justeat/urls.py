from django.urls import path
from . import views




urlpatterns = [

    path('justeat/', views.JusteatApiView.as_view()),


]
