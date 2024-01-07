from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('navbar/', views.navbar, name='navbar'),
    path('home_page_slider/', views.home_page_slider, name='home_page_slider'),
    path('products/', views.navbar, name='products'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('profile/', views.profile, name='profile'),
    path('footer/', views.footer, name='footer'),
    path('about/', views.about, name='about'),
]
