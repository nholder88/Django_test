from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'nigel',
        'title': 'Trying out',
        'content': 'trfsfdfsgdgsdgsgfdgf',
        'date': 'December 25, 2015'
    },
    {
        'author': 'nigel',
        'title': 'Trying out 2',
        'content': 'trfsfddgf',
        'date': 'December 26, 2015'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Passed in'})
