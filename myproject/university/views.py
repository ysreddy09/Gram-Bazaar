from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def signup(request):
    # Your view logic here
    return render(request, 'signup.html')


def signup1(request):
    # Your view logic here
    return render(request, 'signup1.html')


def login(request):
    # Your view logic here
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def navbar(request):
    return render(request, 'navbar.html')
