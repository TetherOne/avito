from django.contrib.auth.decorators import login_required

from django.urls import path

from .views import AdDetailsView
from .views import AdsListView
from .views import AdCreateView
from .views import AdUpdateView
from .views import AdDeleteView
from .views import profile
from .views import your_profile
from .views import your_profile_error
from .views import ad_form_error



app_name = 'avitoapp'



urlpatterns = [
    path('', AdsListView.as_view(), name='main-page'),
    path('create/', login_required(AdCreateView.as_view()), name='create-ad'),
    path('create/error/', ad_form_error, name='create-ad-error'),
    path('profile/<int:pk>/', your_profile, name='your-profile'),
    path('profile/error/', your_profile_error, name='your-profile-error'),
    path('details/<int:pk>/', AdDetailsView.as_view(), name='details-ad'),
    path('details/<int:pk>/profile/<int:user_id>/', profile, name='profile'),
    path('details/<int:pk>/update/', AdUpdateView.as_view(), name='update'),
    path('profile/<int:pk>/delete/', login_required(AdDeleteView.as_view()), name='delete-ad'),
    path('profile/<int:pk>/update/', your_profile, name='your-profile')
]