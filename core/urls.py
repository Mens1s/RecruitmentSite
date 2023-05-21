from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.logIn, name='login'),
    path('logout/',views.logOut, name='logout'),
    path('profile/<str:pk>/', views.profile, name='profile'),

]