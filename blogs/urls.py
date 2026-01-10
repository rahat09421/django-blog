from django.urls import path
from . import views
urlpatterns = [
    path('<int:category_id>/', views.blog_by_category, name='blog_by_category'),
]