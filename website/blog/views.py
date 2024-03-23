from django.shortcuts import render, get_object_or_404

from .models import Post, Category

def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count / 2 + count % 2
    return {'cats1': all[:half], 'cats2': all[half:]}



def index(request):
    posts = Post.objects.all()
    newPost = Post.objects.get(pk=1)
    context = {"posts": posts, 'newPost': newPost}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def post(request, title=None):
    post = get_object_or_404(Post, title=title)
    context = {"post": post}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)


def about(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/about.html', context)


def contact(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/contact.html', context)

def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {"post": post}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)