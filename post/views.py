from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from plan.models import Plan

@login_required # 이 뷰가 로그인된 사용자만 접근 가능하도록 할 경우 추가
def post_list(request):
    posts = Post.objects.all().order_by('-created_at') # 게시글 목록 불러오기 (예시)

    my_plan = None
    if request.user.is_authenticated:
        try:
            # 현재 로그인한 사용자의 Plan 객체를 가져옵니다.
            my_plan = request.user.plan
        except Plan.DoesNotExist:
            # Plan 객체가 없는 경우 (아직 생성하지 않은 경우)
            my_plan = None

    context = {
        'posts': posts,
        'my_plan': my_plan, # my_plan 객체를 템플릿 컨텍스트에 추가
    }
    return render(request, 'post/post_list.html', context)

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
