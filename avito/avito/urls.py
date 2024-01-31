from django.conf.urls.static import static

from django.conf import settings

from django.contrib import admin

from django.urls import include
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('avito/', include('avitoapp.urls')),
    path('myauth/', include('myauth.urls')),
]



if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
