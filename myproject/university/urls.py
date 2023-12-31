from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('navbar/', views.navbar, name='navbar'),
]
