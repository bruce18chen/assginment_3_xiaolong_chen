from django.shortcuts import render
from django.db.models import Count
from .models import Topic, Post

def home(request):
    topics = Topic.objects.annotate(num_posts=Count('post')).order_by('-num_posts')[:10]
    return render(request, 'home.html', {'topics': topics})

def about(request):
    return render(request, 'about.html')

def posts(request):
    return render(request, 'posts.html')

def contact(request):
    return render(request, 'contact.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})