from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import login_view, profile, register

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path(
        'logout/',
        LogoutView.as_view(template_name='user/logout.html'),
        name='logout',
    ),
]
