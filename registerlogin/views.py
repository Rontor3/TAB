from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from registerlogin.models import Profile
from website import settings
from django.core.mail import send_mail
import uuid
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
        email = request.POST['email']
        mobile = request.POST['Mobile Number']
        if(Password1 != Password1):
            print("password didnt match")
        else:
            if(User.objects.filter(username=username).exists()):
                messages.info(request, 'Username taken')
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request, 'Email taken')
                return redirect('register')
            elif(Profile.objects.filter(mobile=mobile).exists()):
                messages.info(request, 'Mobile number already exists')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=Password1, email=email)
                user.save()
                auth_token = str(uuid.uuid4())
                profile = Profile.objects.create(user=user, mobile=mobile,auth_token=auth_token)
                profile.save()
                send_mail_after_registration(email, auth_token)
                user.is_active = False
                return redirect('/token')
    else:
        return render(request, 'register.html')


def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username=username, password=Password)
        if(user is not None):
            auth.login(request, user)
            return(redirect('/'))
        elif(not user.isverified):
            message.success(request, 'User is not verified')
            return(redirect('/login'))
        else:
            messages.info('Username/password is wrong')
            return(redirect('login'))
    else:
        return(render(request, 'login.html'))


def logout(request):
    auth.logout(request)
    return redirect('/')


def verify(request, auth_token):
    print(auth_token)
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if(profile_obj):
            if(profile_obj.is_verified):
                messages.success(request, 'Your account has been verified')
                return (redirect('/accounts/login'))
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified')
            return (redirect('/accounts/login'))
        else:
            return redirect('/error')
    except Exception as e:
        print(e)


def error(request):
    return (render(request, 'error.html'))


def token_send(request):
    return render(request, 'token_send.html')


def success(request):
    return render(request, 'success.html')


def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,email_from]
    send_mail(subject, message, email_from, recipient_list)
