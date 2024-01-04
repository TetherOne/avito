from django.urls import path

from myauth.views import MyLogoutView
from myauth.views import MyLoginView
from myauth.views import RegisterView



app_name = 'myauth'



urlpatterns = [
    path('login/', MyLoginView.as_view(
        template_name='myauth/login.html',
        redirect_authenticated_user=True), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
