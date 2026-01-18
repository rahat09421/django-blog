from django.shortcuts import render, redirect
from django.contrib import auth
from blogs.models import Category, Blog, About
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True, status='Published').order_by('-created_at')
    blogs = Blog.objects.filter(is_featured=False, status='Published')

    # Fetch the first about object
    try:
        about = About.objects.first()
    except About.DoesNotExist:
        about = None

    context = {
        'categories': categories,
        'featured_blogs': featured_blogs,
        'blogs': blogs,
        'about': about,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            return redirect('login')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')
