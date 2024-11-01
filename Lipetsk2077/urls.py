from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('homepage.urls'), name='homepage'),
    path('profession/', include('profession.urls'), name='profession'),
    path('about/', include('about.urls'), name='about'),
    path('auth/', include('user.urls'), name='user'),
    path('feedback/', include('feedback.urls'), name='feedback'),
    path('event/', include('event.urls'), name='event'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
