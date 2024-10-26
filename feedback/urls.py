from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('feedback/', views.index, name='index'),
    path('done/', views.done, name='done'),
    path('', views.list, name='list'),
]
