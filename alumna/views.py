from django.shortcuts import render, redirect, get_object_or_404
from .models import AlumnaPost, AlumnaComment
from .forms import AlumnaPostForm, AlumnaCommentForm
from django.contrib.auth.decorators import login_required
from plan.models import Plan

def alumna_list(request):
    posts = AlumnaPost.objects.all().order_by('-created_at')
    for post in posts:
        try:
            post.author_plan = Plan.objects.get(user=post.author)
        except Plan.DoesNotExist:
            post.author_plan = None
    return render(request, 'alumna/alumna_list.html', {'posts': posts})


@login_required
def alumna_create(request):
    if request.method == 'POST':
        form = AlumnaPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('alumna:alumna_list')
    else:
        form = AlumnaPostForm()
    return render(request, 'alumna/alumna_form.html', {'form': form})


def alumna_detail(request, pk):
    post = get_object_or_404(AlumnaPost, pk=pk)
    comments = post.comments.all().order_by('created_at')
    comment_form = AlumnaCommentForm()

    #이전 글: 현재보다 pk가 작은 것 중 가장 큰 글
    prev_post = AlumnaPost.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    #다음 글: 현재보다 pk가 큰 것 중 가장 작은 글
    next_post = AlumnaPost.objects.filter(pk__gt=post.pk).order_by('pk').first()

    return render(request, 'alumna/alumna_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'prev_post': prev_post,
        'next_post': next_post,
    })


@login_required
def alumna_comment_create(request, pk):
    post = get_object_or_404(AlumnaPost, pk=pk)
    if request.method == 'POST':
        form = AlumnaCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('alumna:alumna_detail', pk=pk)
    return redirect('alumna:alumna_detail', pk=pk)
