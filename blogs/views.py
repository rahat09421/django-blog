from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Blog
from django.db.models import Q
# Create your views here.

def blog_by_category(request, category_id):
    blogs = Blog.objects.filter(status='Published', category=category_id)
    
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'blogs': blogs,
        'category': category,
    }
    return render(request, 'blog_by_category.html', context)

def blogs(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'blog': blog,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    if keyword:
        blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    else:
        blogs = Blog.objects.none()
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)

