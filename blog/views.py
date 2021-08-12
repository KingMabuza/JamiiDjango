from django.shortcuts import render
from .models import Post
posts = [
    {
        'author': 'KingMabuza',
        'title': 'Post1',
        'content': 'First post content',
        'date_posted': 'August 12, 2021'
    },
    {
        'author': 'KingMabuza',
        'title': 'Post2',
        'content': 'Second post content',
        'date_posted': 'August 12, 2021'
    }

]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
