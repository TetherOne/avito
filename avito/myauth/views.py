from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, CreateView

from myauth.forms import RegisterForm


# Create your views here.



class MyLoginView(LoginView):
    def get_success_url(self):
        return reverse('avitoapp:main-page')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('avitoapp:main-page')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('avitoapp:main-page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

































