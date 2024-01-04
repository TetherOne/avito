from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

from django.urls import reverse
from django.urls import reverse_lazy

from django.views.generic import FormView

from myauth.forms import RegisterForm



class MyLoginView(LoginView):
    """

    Класс для входа на сайт

    """
    def get_success_url(self):
        return reverse('avitoapp:main-page')



class MyLogoutView(LogoutView):
    """

    Класс для выхода с сайта

    """
    next_page = reverse_lazy('avitoapp:main-page')



class RegisterView(FormView):
    """

    Класс для регистрации на сайте

    """
    form_class = RegisterForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:login')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)