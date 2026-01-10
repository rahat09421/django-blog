from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_blogs = Blog.objects.filter(is_featured=True, status='Published').order_by('-created_at')
    blogs = Blog.objects.filter(is_featured=False, status='Published')
    context = {
        'categories': categories,
        'featured_blogs': featured_blogs,
        'blogs': blogs,
    }
    return render(request, 'home.html', context)