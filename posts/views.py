from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

from .forms import NewPostForm, EditPostForm
from .models import Post

def PostDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post.html', {'post': post})

@login_required
def NewPost(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been added')
            return redirect('posts:postdetail', pk=post.pk)
        else:
            print("Form errors:", form.errors)
            messages.warning(request, f'There are errors in form. \n{form.errors}')
    else:
        form = NewPostForm()
        
    return render(request, 'posts/createpost.html', {'form': form})

@login_required
def DeletePost(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    post.delete()

    return redirect('core:homepage')


@login_required
def EditPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been added')
            return redirect('posts:postdetail', pk=post.pk)
        else:
            messages.warning(request, f'There are errors in form. \n{form.errors}')
    else:
        form = EditPostForm(instance=post)
        
    return render(request, 'posts/editpost.html', {'form': form, 'post': post})
