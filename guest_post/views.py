from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, "index.html", context)
