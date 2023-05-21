from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.jobs, name='jobs'),
    path('<str:pk>', views.detail, name='detail'),
]