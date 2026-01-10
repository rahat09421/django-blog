from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Blog
# Create your views here.

def blog_by_category(request, category_id):
    blogs = Blog.objects.filter(status='Published', category=category_id)
    
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'blogs': blogs,
        'category': category,
    }
    return render(request, 'blog_by_category.html', context)