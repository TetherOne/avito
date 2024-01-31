from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

from rest_framework.viewsets import ModelViewSet

from django.shortcuts import get_object_or_404

from avitoapp.serializers import AdSerializer

from django.contrib.auth.models import User

from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView

from avitoapp.forms import AdSearchForm
from avitoapp.forms import AdForm

from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpRequest

from django.urls import reverse_lazy

from avitoapp.models import AdImage
from avitoapp.models import Ad

from django.core.cache import cache



class AdViewSet(ModelViewSet):
    """

    Класс для DRF

    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]

    search_fields = ['name', 'description']
    filterset_fields = [

        'name',

    ]

    ordering_fields = [
        'name',
    ]



class AdsListView(ListView):

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

    Функция для отображения профиля текущего пользователя

    """
    cache_user = cache.get('profile_user')
    cache_ads = cache.get('ads')

    if cache_ads and cache_user:

        context = {
            'profile_user': cache_user,
            'ads': cache_ads,
        }

    else:

        user = get_object_or_404(User, id=pk)
        ads = Ad.objects.filter(user=user)

        cache.set('profile_user', user, 30)
        cache.set('ads', ads, 30)

        context = {
            'profile_user': user,
            'ads': ads,
        }

    return render(request, 'avitoapp/your_profile.html', context=context)



def your_profile_error(request: HttpRequest) -> HttpResponse:

    return render(request, 'avitoapp/your_profile_error.html')



class AdCreateView(CreateView):

    model = Ad
    fields = 'name', 'description', 'price', 'address', 'preview', 'phone'
    success_url = reverse_lazy('avitoapp:main-page')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



def ad_form_error(request: HttpRequest) -> HttpResponse:

    return render(request, 'avitoapp/ad_form_error.html')




class AdUpdateView(UpdateView):

    model = Ad
    template_name_suffix = '_update_form'
    form_class = AdForm


    def get_success_url(self):

        cache.delete('profile_user')
        cache.delete('ads')

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

    model = Ad


    def get_success_url(self):

        cache.delete('profile_user')
        cache.delete('ads')

        return reverse_lazy('avitoapp:main-page')
