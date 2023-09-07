from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from .models import User
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def profile(request, username):
    User = get_user_model()

    user_info = User.objects.get(username=username)

    context = {
        'user_info': user_info,
    }

    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request,username):
    User = get_user_model()

    me = request.user # 현재 로그인한 사람
    you = User.objects.get(username=username) # 내가 팔로우를 하고 싶은 사람

    # 팔로잉이 이미 되어있는 경우
    if me in you.followers.all():
        me.followings.remove(you) # 팔로우 취소
    # 팔로잉이 아직 안된경우
    else:
        me.followings.add(you) # 팔로우 추가

    return redirect('accounts:profile', username=username)