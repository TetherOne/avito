from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AdDetailsView, AdsListView, AdCreateView, AdUpdateView, AdDeleteView, profile, your_profile

app_name = 'avitoapp'


urlpatterns = [
    path('', login_required(AdsListView.as_view()), name='main-page'),
    path('create/', login_required(AdCreateView.as_view()), name='create-ad'),
    path('profile/<int:pk>/', login_required(your_profile), name='your-profile'),
    path('details/<int:pk>/', login_required(AdDetailsView.as_view()), name='details-ad'),
    path('details/<int:pk>/profile/<int:user_id>/', login_required(profile), name='profile'),
    path('details/<int:pk>/update/', login_required(AdUpdateView.as_view()), name='update'),
    path('profile/<int:pk>/delete/', login_required(AdDeleteView.as_view()), name='delete-ad'),
    path('profile/<int:pk>/update/', login_required(your_profile), name='your-profile'),

]
