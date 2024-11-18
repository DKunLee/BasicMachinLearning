from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SingupForm
from posts.models import Category, Post

def index(request):
    return render(request, 'core/welcome.html')

@login_required
def homepage(request):
    query = request.GET.get('query', '')
    posts = Post.objects.all()
    categories = Category.objects.all()
    if query:
        posts = posts.filter(title__icontains=query)

    return render(request, 'core/homepage.html', {
        'posts': posts,
        'query': query,
        'categories': categories
    })

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SingupForm

    return render(request, 'core/signup.html', {'form': form})
