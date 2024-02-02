from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "account"

urlpatterns = [

    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    
]