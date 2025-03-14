from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
        path('user/', views.UserView.as_view(), name='name'),
        path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
        path('update-request-remaining/', views.UpdateRequestRemainingView.as_view(), name='update-request-remaining'),

]
