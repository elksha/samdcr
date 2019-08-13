from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, UserForm
from .models import Post, Comment
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all()
    totalCnt = Post.objects.filter(author=request.user).count()
    return render(request, 'home.html', { 'posts' : posts, 'totalCnt' : totalCnt } )

@login_required(login_url='/accounts/login/')
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user.get_username()
        post.save()
        return redirect('detail', post_pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'new.html', { 'form' : form })
    
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        comment = form.save(commit=False)
        comment.author = request.user.get_username()
        comment.post = post
        comment.save()

        return redirect('detail', post.pk)
    else:
        form = CommentForm()
        return render(request, 'detail.html', { 'post' : post, 'form': form })

@login_required(login_url='/accounts/login/')
def edit(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        post = form.save(commit = False)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'edit.html', { 'form' : form })

def delete(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
        else:
            form = UserForm()
            error = "아이디가 이미 존재합니다"
            return render(request, 'registration/signup.html', {'form':form, 'error':error})
    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form': form})