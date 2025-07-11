from django.shortcuts import render, redirect, get_object_or_404
from .models import CounselPost, CounselComment
from .forms import CounselPostForm, CounselCommentForm
from django.contrib.auth.decorators import login_required
from plan.models import Plan

def counsel_list(request):
    posts = CounselPost.objects.all().order_by('-created_at')
    for post in posts:
        try:
            post.author_plan = Plan.objects.get(user=post.author)
        except Plan.DoesNotExist:
            post.author_plan = None
    return render(request, 'counsel/counsel_list.html', {'posts': posts})


@login_required
def counsel_create(request):
    if request.method == 'POST':
        form = CounselPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('counsel:counsel_list')
    else:
        form = CounselPostForm()
    return render(request, 'counsel/counsel_form.html', {'form': form})


def counsel_detail(request, pk):
    post = get_object_or_404(CounselPost, pk=pk)
    comments = post.comments.all().order_by('created_at')
    comment_form = CounselCommentForm()
    return render(request, 'counsel/counsel_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })


@login_required
def counsel_comment_create(request, pk):
    post = get_object_or_404(CounselPost, pk=pk)
    if request.method == 'POST':
        form = CounselCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('counsel:counsel_detail', pk=pk)
    return redirect('counsel:counsel_detail', pk=pk)


def counsel_detail(request, pk):
    post = get_object_or_404(CounselPost, pk=pk)
    comments = post.comments.all().order_by('created_at')
    comment_form = CounselCommentForm()

    #이전 글: 현재보다 pk가 작은 것 중 가장 큰 글
    prev_post = CounselPost.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    #다음 글: 현재보다 pk가 큰 것 중 가장 작은 글
    next_post = CounselPost.objects.filter(pk__gt=post.pk).order_by('pk').first()

    return render(request, 'counsel/counsel_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'prev_post': prev_post,
        'next_post': next_post,
    })
