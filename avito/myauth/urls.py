from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from myauth.views import MyLogoutView, MyLoginView, RegisterView

app_name = 'myauth'

urlpatterns = [
    path('login/', MyLoginView.as_view(
        template_name='myauth/login.html',
        redirect_authenticated_user=True), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
