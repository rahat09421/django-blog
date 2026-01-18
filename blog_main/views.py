from django.shortcuts import render
from blogs.models import Category, Blog, About


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

