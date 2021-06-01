from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'JanR',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 05, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 06, 2021'
    },
]


"""
Create functions that handle what page the user is supposed to see when using any specific link.
For now we just return a simple httpresponse.
"""


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
