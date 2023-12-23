from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from myauth.forms import RegisterForm



# модель для входа на сайт
class MyLoginView(LoginView):
    def get_success_url(self):
        return reverse('avitoapp:main-page')



# модель для выхода с сайта
class MyLogoutView(LogoutView):
    next_page = reverse_lazy('avitoapp:main-page')



# модель для регистрации на сайте
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)