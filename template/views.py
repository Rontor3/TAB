from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from registerlogin.models import Profile
from website import settings
import random
import http.client
from django.core.mail import EmailMessage

# Create your views here.


def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']
        twitter_handle = request.POST['Twitter ID']
        if(Password1 != Password2):
            print("password didnt match")
        else:
            if(User.objects.filter(username=username).exists()):
                messages.info(request, 'Username taken')
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request, 'Email taken')
                return redirect('register')
            elif(Profile.objects.filter(twitter_handle=twitter_handle).exists()):
                messages.info(request, 'Twitter  handle number already exists')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=Password1, email=email)
                user.save()
                profile = Profile.objects.create(
                    user=user, twitter_handle=twitter_handle)
                profile.save()
                user.is_active = False
                return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if(request.method == 'POST'):
        username = request.POST['Twitter']
        Password = request.POST['password']
        user = auth.authenticate(username=username, password=Password)
        if(user is not None):
            auth.login(request, user)
            return(redirect('/'))
        else:
            messages.info('Username/password is wrong')
            return(redirect('login'))
    else:
        return(render(request, 'login.html'))


def logout(request):
    auth.logout(request)
    return redirect('/')


# Create your views here.
