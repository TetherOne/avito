from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

from django.views.generic import FormView

from myauth.forms import RegisterForm

from django.urls import reverse_lazy
from django.urls import reverse





class MyLoginView(LoginView):

    def get_success_url(self):
        return reverse('avitoapp:main-page')



class MyLogoutView(LogoutView):

    next_page = reverse_lazy('avitoapp:main-page')



class RegisterView(FormView):

    form_class = RegisterForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:login')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)