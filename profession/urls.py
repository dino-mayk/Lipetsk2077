from django.urls import path

from profession import views

app_name = 'profession'

urlpatterns = [
    path('', views.list, name='list'),
]
