from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpRequest
from django.http import HttpResponse

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView

from avitoapp.forms import AdForm
from avitoapp.forms import AdSearchForm

from avitoapp.models import Ad
from avitoapp.models import AdImage



class AdsListView(ListView):
    """

    Класс для отображения объявлений на главной странице

    """
    queryset = (
        Ad.objects.select_related('user')
    )
    context_object_name = 'ads'


    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search_term')
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = AdSearchForm(
            self.request.GET)
        return context



class AdDetailsView(DetailView):
    """

    Класс для отображения деталей объявления

    """
    queryset = (
        Ad.objects.select_related('user')
    )
    context_object_name = 'ad'



def profile(request: HttpRequest, pk, user_id) -> HttpResponse:
    """

    Функция для отображения чужого профиля

    """
    user = get_object_or_404(User, id=user_id)
    ads = Ad.objects.filter(user=user)

    context = {
        'profile_user': user,
        'ads': ads,
    }
    return render(request, 'avitoapp/user_profile.html', context=context)



def your_profile(request: HttpRequest, pk) -> HttpResponse:
    """

    Функция для отображения профиля пользователя

    """
    user = get_object_or_404(User, id=pk)
    ads = Ad.objects.filter(user=user)

    context = {
        'profile_user': user,
        'ads': ads,
    }

    return render(request, 'avitoapp/your_profile.html', context=context)



def your_profile_error(request: HttpRequest) -> HttpResponse:
    """

    Функция для отрисовки ошибки профиля пользователя не аутентифицированного в системе

    """
    return render(request, 'avitoapp/your_profile_error.html')



class AdCreateView(CreateView):
    """

    Класс для создания объявления

    """
    model = Ad
    fields = 'name', 'description', 'price', 'address', 'preview', 'phone'
    success_url = reverse_lazy('avitoapp:main-page')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



def ad_form_error(request: HttpRequest) -> HttpResponse:
    """

    Функция для отрисовки ошибки при нажатии на кнопку создать объявление

    """
    return render(request, 'avitoapp/ad_form_error.html')




class AdUpdateView(UpdateView):
    """

    Класс для обновления объявления

    """
    model = Ad
    template_name_suffix = '_update_form'
    form_class = AdForm


    def get_success_url(self):
        return reverse_lazy('avitoapp:your-profile', kwargs={'pk': self.request.user.pk})


    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist('images'):
            AdImage.objects.create(
                ad=self.object,
                image=image,
            )

        return response




class AdDeleteView(DeleteView):
    """

    Класс для удаления объявления

    """
    model = Ad
    success_url = reverse_lazy('avitoapp:main-page')
