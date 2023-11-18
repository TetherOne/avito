from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseForbidden
from django.urls import reverse, reverse_lazy

from django.views.generic import UpdateView, DetailView, TemplateView, ListView, DetailView, CreateView, DeleteView

from avitoapp.forms import AdForm, AdSearchForm
from avitoapp.models import Ad, AdImage



class AdsListView(ListView):
    queryset = (
        Ad.objects.select_related('user')
    )
    context_object_name = 'ads'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search_term')  # Получаем значение параметра search_term из GET-запроса
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = AdSearchForm(
            self.request.GET)  # Создаем экземпляр формы поиска с данными из GET-запроса
        return context


class AdDetailsView(DetailView):
    queryset = (
        Ad.objects.select_related('user')
    )
    context_object_name = 'ad'


def profile(request, pk, user_id):
    user = get_object_or_404(User, id=user_id)
    ads = Ad.objects.filter(user=user)
    context = {
        'profile_user': user,
        'ads': ads,
    }
    return render(request, 'avitoapp/user_profile.html', context=context)


def your_profile(request, pk):
    user = get_object_or_404(User, id=pk)
    ads = Ad.objects.filter(user=user)
    context = {
        'profile_user': user,
        'ads': ads,
    }
    return render(request, 'avitoapp/your_profile.html', context=context)


class AdCreateView(CreateView):
    model = Ad
    fields = 'name', 'description', 'price', 'address', 'preview', 'phone'
    success_url = reverse_lazy('avitoapp:main-page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdUpdateView(UpdateView):
    model = Ad
    # fields = 'name', 'description', 'price', 'address', 'preview'
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
    model = Ad
    success_url = reverse_lazy('avitoapp:main-page')
