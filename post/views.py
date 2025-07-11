from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from plan.models import Plan

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    for post in posts:
        try:
            post.author_plan = Plan.objects.get(user=post.author)
        except Plan.DoesNotExist:
            post.author_plan = None
    return render(request, 'post/post_list.html', {'posts': posts})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:post_list')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('created_at')
    comment_form = CommentForm()
    return render(request, 'post/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })


@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post:post_detail', pk=pk)
    return redirect('post:post_detail', pk=pk)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('created_at')
    comment_form = CommentForm()

    #이전 글: 현재보다 pk가 작은 것 중 가장 큰 글
    prev_post = Post.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    #다음 글: 현재보다 pk가 큰 것 중 가장 작은 글
    next_post = Post.objects.filter(pk__gt=post.pk).order_by('pk').first()

    return render(request, 'post/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'prev_post': prev_post,
        'next_post': next_post,
    })
