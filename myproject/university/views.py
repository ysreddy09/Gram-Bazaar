from datetime import datetime

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def signup(request):
    # Your view logic here
    return render(request, 'signup.html')


def login(request):
    # Your view logic here
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def navbar(request):
    return render(request, 'navbar.html')


def home_page_slider(request):
    return render(request, 'home_page_slider.html')


def products(request):
    return render(request, 'products.html')


def add_to_cart(request):
    return render(request, 'add_to_cart.html')


def profile(request):
    return render(request, 'profile.html')


def footer(request):
    return render(request, 'footer.html')


def about(request):
    return render(request, 'about.html')
